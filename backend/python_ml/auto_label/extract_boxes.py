import imageio.v2 as imageio
import numpy as np
from typing import List, Dict, Any
from utils import mask_bbox

def boxes_from_mask_paths(mask_paths: List[str]) -> List[Dict[str, Any]]:
    """
    Given a list of mask image paths, return bounding box dicts.
    """
    out = []
    for p in mask_paths:
        m = imageio.imread(p)
        if m.ndim == 3:  # handle 3-channel mask
            m = m[...,0]
        x,y,w,h,area = mask_bbox(m > 0)
        out.append({
            "mask_path": p,
            "bbox": [x,y,w,h],
            "area": area
        })
    return out
