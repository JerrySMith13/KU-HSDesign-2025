from PIL import Image, ImageDraw

class Sticker:
    name: str
    size: int
    
    def __init__(self, name, size=30):
        self.name = name
        self.size = size

class StickerOptions:
    stickers: list[list[Sticker | None]]
    
    def __init__(self, stickers=None):
        if stickers is None:
            self.stickers = [[None for _ in range(3)] for _ in range(3)]
        else:
            self.stickers = stickers
    
    def renderStickers(self, img: Image):
        width, height = img.size
        draw = ImageDraw.Draw(img)
        cell_w = width / 3
        cell_h = height / 3
        
        for y_pos, x_list in enumerate(self.stickers):
            for x_pos, sticker in enumerate(x_list):
                if sticker is None:
                    continue

                # FIXED: place stickers at cell centers
                x_coord = int((x_pos + 0.5) * cell_w)
                y_coord = int((y_pos + 0.5) * cell_h)
                
                sticker_pil = Image.open(f"./stickers/{sticker.name}.png")
                sticker_width, sticker_height = sticker_pil.size
                watermark_width = int(sticker_width * (sticker.size / 100))
                watermark_height = int(sticker_height * (sticker.size / 100))
                
                sticker_pil.thumbnail((watermark_width, watermark_height))
                
                # Center sticker properly around the target point
                x_paste = x_coord - sticker_pil.width // 2
                y_paste = y_coord - sticker_pil.height // 2
                
                img.paste(sticker_pil, (x_paste, y_paste), sticker_pil)

if __name__ == "__main__":
    sticker1 = Sticker("badge", size=10)
    sticker2 = Sticker("cowboy_hat", size=10)
    
    stickerList = [
        [sticker1, None, sticker2],
        [sticker2, None, None],
        [None, None, sticker1]
    ]
    sticker_opts = StickerOptions(stickerList)
    
    img = Image.open("./obamna.jpg")
    sticker_opts.renderStickers(img)
    img.save("sticker-test.jpg")
