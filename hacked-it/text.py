from __future__ import annotations

from PIL import Image, ImageFont, ImageDraw, ImageShow

class TextObj:
    def __init__(self, text: str = "", fontSize: int = 32, font: str = "times"):
        self.text = text
        self.fontSize = fontSize
        self.font = font
    
class TextOptions:
    def __init__(
        self,
        topText: TextObj | None = None,
        bottomText: TextObj | None = None,
        centerText: TextObj | None = None,
    ):
        self.topText = topText
        self.bottomText = bottomText
        self.centerText = centerText
    
    topText: TextObj | None
    bottomText: TextObj | None
    centerText: TextObj | None
    
    def renderText(self, img: Image):
        
        width, height = img.size
    
        drawer = ImageDraw.Draw(img)
        
        #render top text
        if self.topText != None:
            font = ImageFont.truetype(f"./fonts/{self.topText.font}")
            
            drawer.text((width //2, 20), self.topText.text, anchor="mm", font=font)
        if self.bottomText != None:
            font = ImageFont.truetype(f"./fonts/{self.bottomText.font}")
            drawer.text((width //2, height - 20), self.bottomText.text, anchor="mm", font=font)
        
        if self.centerText != None:
            font = ImageFont.truetype(f"./fonts/{self.centerText.font}")
            drawer.text((width //2, height //2), self.bottomText.text, anchor="mm", font=font)
            
        
        
if __name__ == "__main__":
    img = Image.open("./obamna.jpg")
    top_text = TextObj("hello w0rld")
    bottom_text = TextObj("bottom text")
    center_text = TextObj("center")
    text = TextOptions(topText=top_text, bottomText=bottom_text, centerText=center_text)
    text.renderText(img)
    
    img.save("helloimg.jpg")
    