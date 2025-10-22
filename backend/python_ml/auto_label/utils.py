import os, json, cv2, numpy as np
from typing import List, Dict, Tuple

def ensure_dir(d: str):
    os.makedirs(d, exist_ok=True)

def mask_to_polygons(binary_mask: np.ndarray, epsilon_ratio: float = 0.01, min_points: int = 6) -> List[List[float]]:
    """
    Convert binary mask (H,W) → COCO-style polygons.
    """
    mask = (binary_mask.astype(np.uint8) * 255)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    h, w = binary_mask.shape[:2]
    polys: List[List[float]] = []
    for cnt in contours:
        if cv2.contourArea(cnt) < 20:  # skip tiny noise
            continue
        peri = cv2.arcLength(cnt, True)
        epsilon = epsilon_ratio * peri
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        flat = approx.reshape(-1, 2).ravel().astype(float).tolist()
        if len(flat) >= min_points:  
            # clamp inside image
            for i in range(0, len(flat), 2):
                flat[i]   = float(max(0, min(w-1, flat[i])))
                flat[i+1] = float(max(0, min(h-1, flat[i+1])))
            polys.append(flat)
    return polys

def mask_bbox(binary_mask: np.ndarray) -> Tuple[int,int,int,int,int]:
    """Return x,y,w,h,area for a binary mask."""
    ys, xs = np.where(binary_mask > 0)
    if len(xs) == 0 or len(ys) == 0:
        return 0,0,0,0,0
    x_min, x_max = xs.min(), xs.max()
    y_min, y_max = ys.min(), ys.max()
    w = int(x_max - x_min + 1)
    h = int(y_max - y_min + 1)
    area = int((binary_mask>0).sum())
    return int(x_min), int(y_min), w, h, area

def save_mask_png(mask: np.ndarray, out_path: str):
    import imageio.v2 as imageio
    imageio.imwrite(out_path, (mask > 0).astype(np.uint8) * 255)
