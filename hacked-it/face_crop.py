import cv2
from PIL import Image




def crop_face(img_path: str) -> Image:
    face_cascade = cv2.CascadeClassifier("./cascade.xml")
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    x, y, w, h  = faces[0]
    x2 = x + w
    y2 = y + h
    
    img = Image.open(img_path)
    
    # Ensure valid crop box: order and bounds
    x1, y1 = int(x), int(y)
    x2, y2 = int(x2), int(y2)
    if x2 <= x1 or y2 <= y1:
        # Swap/order just in case
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
    w_img, h_img = img.size
    x1 = max(0, min(x1, w_img - 1))
    x2 = max(0, min(x2, w_img))
    y1 = max(0, min(y1, h_img - 1))
    y2 = max(0, min(y2, h_img))
    box = (x1, y1, x2, y2)
    cropped = img.crop(box)
    return cropped
    
if __name__ == "__main__":
     path = input()
     img = crop_face(path)
     img.save("cropped.jpg")
     
