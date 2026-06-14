"""
=============================================================================
  Synthetic Augmentation Pipeline
  Augments downloaded card images to simulate real-world conditions
=============================================================================
  INSTALLATION:
      pip install pillow numpy opencv-python albumentations tqdm

  USAGE:
      python augment_dataset.py

  This script reads images from  dataset/  and writes augmented copies to
  dataset_augmented/  keeping the same subfolder structure.
=============================================================================
"""

import os
import random
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
from tqdm import tqdm

# ── Optional: albumentations for advanced transforms ─────────────────────
try:
    import albumentations as A
    import cv2
    ALB_AVAILABLE = True
except ImportError:
    ALB_AVAILABLE = False

# ════════════════════════════════════════════════════════════════════════════
#  CONFIGURATION
# ════════════════════════════════════════════════════════════════════════════
INPUT_DIR    = "dataset"
OUTPUT_DIR   = "dataset_augmented"
AUGS_PER_IMG = 5      # how many augmented copies per source image
MAX_SIZE     = 1024   # resize longest edge after augmentation

# ════════════════════════════════════════════════════════════════════════════
#  PURE-PILLOW AUGMENTATIONS  (no OpenCV / albumentations needed)
# ════════════════════════════════════════════════════════════════════════════

def aug_rotate(img: Image.Image) -> Image.Image:
    """Random rotation ±45°, fill with gray."""
    angle = random.uniform(-45, 45)
    return img.rotate(angle, resample=Image.BICUBIC, expand=True,
                      fillcolor=(128, 128, 128))


def aug_brightness(img: Image.Image) -> Image.Image:
    """Random brightness 0.4 – 1.8×."""
    factor = random.uniform(0.4, 1.8)
    return ImageEnhance.Brightness(img).enhance(factor)


def aug_contrast(img: Image.Image) -> Image.Image:
    factor = random.uniform(0.5, 2.0)
    return ImageEnhance.Contrast(img).enhance(factor)


def aug_blur(img: Image.Image) -> Image.Image:
    """Motion or Gaussian blur."""
    if random.random() < 0.5:
        return img.filter(ImageFilter.GaussianBlur(radius=random.uniform(0.5, 2.5)))
    return img.filter(ImageFilter.BoxBlur(radius=random.randint(1, 3)))


def aug_noise(img: Image.Image) -> Image.Image:
    """Add Gaussian noise via numpy."""
    arr  = np.array(img, dtype=np.int16)
    std  = random.uniform(5, 25)
    arr += np.random.normal(0, std, arr.shape).astype(np.int16)
    arr  = np.clip(arr, 0, 255).astype(np.uint8)
    return Image.fromarray(arr)


def aug_flip(img: Image.Image) -> Image.Image:
    """Random horizontal flip."""
    return img.transpose(Image.FLIP_LEFT_RIGHT) if random.random() < 0.5 else img


def aug_crop(img: Image.Image) -> Image.Image:
    """Random crop (simulates partial occlusion / zoom)."""
    w, h = img.size
    margin_x = int(w * random.uniform(0.05, 0.20))
    margin_y = int(h * random.uniform(0.05, 0.20))
    left   = random.randint(0, margin_x)
    top    = random.randint(0, margin_y)
    right  = w - random.randint(0, margin_x)
    bottom = h - random.randint(0, margin_y)
    return img.crop((left, top, right, bottom)).resize((w, h), Image.LANCZOS)


def aug_perspective(img: Image.Image) -> Image.Image:
    """
    Simulate perspective tilt using a simple quad warp.
    Requires numpy; falls back gracefully if not available.
    """
    try:
        arr = np.array(img)
        h, w = arr.shape[:2]

        # Random offsets per corner (pixels)
        def jitter():
            return random.randint(-int(w * 0.15), int(w * 0.15))

        src = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
        dst = np.float32([
            [jitter(), jitter()],
            [w + jitter(), jitter()],
            [w + jitter(), h + jitter()],
            [jitter(), h + jitter()],
        ])
        try:
            import cv2
            M   = cv2.getPerspectiveTransform(src, dst)
            out = cv2.warpPerspective(arr, M, (w, h),
                                      borderValue=(128, 128, 128))
            return Image.fromarray(out)
        except ImportError:
            pass
    except Exception:
        pass
    return img   # fallback — no-op


def aug_shadow(img: Image.Image) -> Image.Image:
    """
    Overlay a semi-transparent dark polygon to simulate shadow.
    """
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    from PIL import ImageDraw
    draw  = ImageDraw.Draw(overlay)
    w, h  = img.size

    # Random dark band across the image
    x0 = random.randint(0, w // 2)
    x1 = random.randint(w // 2, w)
    alpha = random.randint(60, 140)
    draw.polygon([(x0, 0), (x1, 0), (w, h), (0, h)],
                 fill=(0, 0, 0, alpha))

    base = img.convert("RGBA")
    merged = Image.alpha_composite(base, overlay)
    return merged.convert("RGB")


def aug_color_jitter(img: Image.Image) -> Image.Image:
    """Hue / saturation / color jitter via Pillow."""
    img = ImageEnhance.Color(img).enhance(random.uniform(0.3, 1.8))
    img = ImageEnhance.Sharpness(img).enhance(random.uniform(0.5, 2.0))
    return img


# ════════════════════════════════════════════════════════════════════════════
#  ALBUMENTATIONS PIPELINE  (richer, needs cv2 + albumentations)
# ════════════════════════════════════════════════════════════════════════════

def build_alb_pipeline():
    """Build an albumentations augmentation pipeline."""
    if not ALB_AVAILABLE:
        return None
    return A.Compose([
        A.RandomRotate90(p=0.3),
        A.Rotate(limit=45, p=0.6),
        A.HorizontalFlip(p=0.5),
        A.RandomBrightnessContrast(
            brightness_limit=0.4, contrast_limit=0.4, p=0.7),
        A.HueSaturationValue(
            hue_shift_limit=15, sat_shift_limit=40, val_shift_limit=30, p=0.5),
        A.GaussNoise(var_limit=(10, 50), p=0.4),
        A.GaussianBlur(blur_limit=(3, 7), p=0.3),
        A.MotionBlur(blur_limit=7, p=0.2),
        A.RandomShadow(
            shadow_roi=(0, 0, 1, 1),
            num_shadows_lower=1, num_shadows_upper=2,
            shadow_dimension=5, p=0.4),
        A.Perspective(scale=(0.05, 0.15), p=0.5),
        A.CoarseDropout(
            max_holes=4, max_height=60, max_width=60,
            fill_value=128, p=0.3),   # simulate finger occlusion
        A.ImageCompression(quality_lower=50, quality_upper=95, p=0.3),
    ])


ALB_PIPELINE = build_alb_pipeline()

# ════════════════════════════════════════════════════════════════════════════
#  PILLOW-ONLY AUGMENTATION POOL
# ════════════════════════════════════════════════════════════════════════════
PILLOW_AUGS = [
    aug_rotate,
    aug_brightness,
    aug_contrast,
    aug_blur,
    aug_noise,
    aug_flip,
    aug_crop,
    aug_perspective,
    aug_shadow,
    aug_color_jitter,
]


def augment_one(img: Image.Image, use_albumentations: bool = True) -> Image.Image:
    """
    Apply a random combination of augmentations to one image.
    Prefers albumentations pipeline if available.
    """
    if use_albumentations and ALB_PIPELINE is not None:
        import cv2
        arr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out = ALB_PIPELINE(image=arr)["image"]
        img = Image.fromarray(cv2.cvtColor(out, cv2.COLOR_BGR2RGB))
    else:
        # Apply 2–4 random Pillow augmentations
        chosen = random.sample(PILLOW_AUGS, k=random.randint(2, 4))
        for fn in chosen:
            try:
                img = fn(img)
            except Exception:
                pass

    # Ensure correct mode and max size
    img = img.convert("RGB")
    w, h = img.size
    if max(w, h) > MAX_SIZE:
        scale = MAX_SIZE / max(w, h)
        img   = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    return img


# ════════════════════════════════════════════════════════════════════════════
#  MAIN
# ════════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("  Card Dataset Augmentation Pipeline")
    print(f"  Input : {INPUT_DIR}")
    print(f"  Output: {OUTPUT_DIR}")
    print(f"  Augmentations per image: {AUGS_PER_IMG}")
    print(f"  Backend: {'albumentations' if ALB_AVAILABLE else 'Pillow-only'}")
    print("=" * 60)

    if not os.path.isdir(INPUT_DIR):
        print(f"❌  '{INPUT_DIR}' folder not found. Run the downloader first.")
        return

    class_dirs = [
        d for d in sorted(os.listdir(INPUT_DIR))
        if os.path.isdir(os.path.join(INPUT_DIR, d))
    ]

    total_augmented = 0

    for class_name in class_dirs:
        src_folder = os.path.join(INPUT_DIR,  class_name)
        dst_folder = os.path.join(OUTPUT_DIR, class_name)
        os.makedirs(dst_folder, exist_ok=True)

        image_files = [
            f for f in os.listdir(src_folder)
            if f.lower().endswith((".jpg", ".jpeg", ".png"))
        ]

        if not image_files:
            continue

        for fname in tqdm(image_files, desc=f"{class_name:<35}", unit="img"):
            src_path = os.path.join(src_folder, fname)
            try:
                original = Image.open(src_path).convert("RGB")
            except Exception:
                continue

            # Copy original to output folder
            orig_dest = os.path.join(dst_folder, fname)
            original.save(orig_dest, "JPEG", quality=90)

            # Generate augmented copies
            for i in range(AUGS_PER_IMG):
                aug_img  = augment_one(original, use_albumentations=ALB_AVAILABLE)
                aug_name = f"{os.path.splitext(fname)[0]}_aug{i:02d}.jpg"
                aug_path = os.path.join(dst_folder, aug_name)
                aug_img.save(aug_path, "JPEG", quality=88)
                total_augmented += 1

    print(f"\n✅  Augmentation complete!")
    print(f"   Total augmented images created: {total_augmented}")
    print(f"   Output folder: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
