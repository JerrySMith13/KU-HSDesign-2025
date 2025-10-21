from PIL import Image, ImageOps

def add_border(img: Image, name: str, inset=0):
    border_img = Image.open(f"./borders/{name}")
    border_width = max(1, img.width - 2*inset)
    border_height = max(1, img.height - 2*inset)
    border = ImageOps.contain(border_img, (border_width, border_height), method=Image.LANCZOS)
    x_coord = (img.width - border.width) // 2
    y_coord = (img.height - border.height) // 2
    
    img.paste(border, (x_coord, y_coord), mask=border)
    
    
    
    
    