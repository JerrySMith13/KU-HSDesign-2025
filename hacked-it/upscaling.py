import cv2
import numpy as np
from PIL import Image, ImageOps
from cv2.dnn_superres import DnnSuperResImpl_create


def pil_to_cv2(img: Image.Image) -> np.ndarray:
    """
    Convert a PIL.Image to an OpenCV BGR (or BGRA/GRAY) ndarray (uint8).
    Handles RGB, RGBA, and L (grayscale). Also respects EXIF orientation.
    """
    # Fix rotation from EXIF if present
    img = ImageOps.exif_transpose(img)

    mode = img.mode
    arr  = np.array(img)

    if mode == "RGB":
        return cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)
    elif mode == "RGBA":
        return cv2.cvtColor(arr, cv2.COLOR_RGBA2BGRA)
    elif mode in ("L", "I;16", "I"):
        # L: 8-bit gray, I;16/I: 16/32-bit integer grayscale
        # OpenCV can take them directly; convert I to 16-bit if needed
        if arr.dtype == np.int32:  # "I" mode often becomes int32
            arr = arr.astype(np.uint16)  # or np.float32 depending on your pipeline
        return arr
    else:
        # Fallback: convert via RGB, then to BGR
        return cv2.cvtColor(np.array(img.convert("RGB")), cv2.COLOR_RGB2BGR)
    

def upscale_and_save(img: Image, filename: str):
    sr = DnnSuperResImpl_create()
    sr.readModel("./FSRCNN-small_x4.pb")  # path to the downloaded model
    sr.setModel("fsrcnn", 4)      # ("edsr"|"espcn"|"fsrcnn"|"lapsrn"), scale: 2/3/4/8

    image = pil_to_cv2(img)
    up = sr.upsample(image)
    cv2.imwrite(f"{filename}.jpg", up)
    
    

if __name__ == "__main__":
    path = "./face.jpg"
    im = Image.open(path)
    upscale_and_save(im, "saved")