import os, json, imageio.v2 as imageio
from typing import List, Dict, Any

def build_coco(images: List[Dict[str, Any]], 
               annotations: List[Dict[str, Any]], 
               categories: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {
        "images": images,
        "annotations": annotations,
        "categories": categories
    }

def write_coco(json_path: str, coco_obj: Dict[str, Any]):
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, "w") as f:
        json.dump(coco_obj, f, indent=2)

def get_image_hw(path: str):
    img = imageio.imread(path)
    if img.ndim == 2:
        h, w = img.shape
    else:
        h, w = img.shape[:2]
    return int(h), int(w)
