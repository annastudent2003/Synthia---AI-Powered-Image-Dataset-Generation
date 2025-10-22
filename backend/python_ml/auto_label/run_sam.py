import os, torch, numpy as np, imageio.v2 as imageio
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator
from PIL import Image
from typing import Dict, Any, List
from utils import ensure_dir, mask_to_polygons, save_mask_png

def run_sam_on_image(
    image_path: str,
    out_mask_dir: str,
    out_poly_dir: str,
    sam_checkpoint_path: str,
    model_type: str = "vit_h"
) -> List[Dict[str, Any]]:
    """
    Runs SAM on an image and saves masks + polygon JSONs.
    Returns list of instance dicts.
    """
    ensure_dir(out_mask_dir); ensure_dir(out_poly_dir)
    device = "cuda" if torch.cuda.is_available() else "cpu"

    sam = sam_model_registry[model_type](checkpoint=sam_checkpoint_path).to(device)
    mask_generator = SamAutomaticMaskGenerator(
    model=sam,
    points_per_side=8,          # lower resolution grid (was 32)
    pred_iou_thresh=0.9,        # only keep good masks
    stability_score_thresh=0.95,
    min_mask_region_area=1000   # ignore tiny specks
)


    image = np.array(Image.open(image_path).convert("RGB"))
    masks = mask_generator.generate(image)

    base = os.path.splitext(os.path.basename(image_path))[0]
    results: List[Dict[str, Any]] = []

    for idx, m in enumerate(masks):
        seg = m["segmentation"].astype(np.uint8)
        polygons = mask_to_polygons(seg)
        if len(polygons) == 0:
            continue

        mask_path = os.path.join(out_mask_dir, f"{base}_mask_{idx:03d}.png")
        save_mask_png(seg, mask_path)

        poly_obj = {
            "image_id": base,
            "instance_id": idx,
            "polygons": polygons,
            "score": float(m.get("predicted_iou", 1.0)),
            "area": int(m.get("area", int(seg.sum())))
        }

        poly_path = os.path.join(out_poly_dir, f"{base}_poly_{idx:03d}.json")
        with open(poly_path, "w") as f: 
            import json; json.dump(poly_obj, f)

        results.append({"mask_path": mask_path, **poly_obj})

    return results
