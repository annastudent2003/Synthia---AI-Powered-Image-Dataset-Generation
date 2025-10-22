import torch, cv2, numpy as np, os
from typing import Dict
from utils import ensure_dir
import imageio.v2 as imageio

def normalize_and_save_depth(depth: np.ndarray, out_png: str):
    """Normalize depth to 16-bit PNG."""
    d = depth.astype(np.float32)
    d = (d - d.min()) / (d.max() - d.min() + 1e-8)
    d16 = (d * 65535.0).astype(np.uint16)
    imageio.imwrite(out_png, d16)

def run_midas_on_image(image_path: str, out_depth_dir: str, model_type: str = "DPT_Large") -> Dict:
    """
    Run MiDaS depth estimation on an image.
    Saves depth PNG and returns stats.
    """
    ensure_dir(out_depth_dir)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load MiDaS
    midas = torch.hub.load("intel-isl/MiDaS", model_type)
    midas.to(device).eval()

    # Load transforms
    transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
    transform = transforms.dpt_transform if "DPT" in model_type else transforms.small_transform

    # Read image
    img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
    input_batch = transform(img).to(device)

    # Inference
    with torch.no_grad():
        prediction = midas(input_batch)
        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=img.shape[:2],
            mode="bicubic",
            align_corners=False,
        ).squeeze()

    depth = prediction.cpu().numpy()
    base = os.path.splitext(os.path.basename(image_path))[0]
    out_png = os.path.join(out_depth_dir, f"{base}_depth.png")
    normalize_and_save_depth(depth, out_png)

    return {"depth_path": out_png, "min": float(depth.min()), "max": float(depth.max())}
