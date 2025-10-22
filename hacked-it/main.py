from rich.prompt import Prompt, IntPrompt, Confirm, FloatPrompt
import os
from PIL import Image, ImageFont
import text
import sticker
import filters

Vertical = ["top", "middle", "bottom"]
Horizontal = ["left", "center", "right"]

all_files = os.listdir(".")
filtered = [name for name in all_files if name.endswith((".png", ".jpg"))]

fileName = Prompt.ask("Pick an image for a background", choices=filtered)



#crop for face here



img = Image.open(fileName)

#filter options here
all_filters = ["b&w", "sepia", "colorify", ""]
selection = Prompt.ask("Select a filter (enter for none)")

match selection:
    case "":
        pass
    case "b&w":
        filters.filter_image.grayscale(img)        
    case "sepia":
        filters.filter_image.sepia(img)
    case "colorify":
        color = Prompt.ask("Enter color: ")
        intens = FloatPrompt.ask("Enter color intensity")
        filters.filter_image.colorify(img, color, intens)
        

#Select stickers
all_stickers = os.listdir("./stickers")
all_stickers.append("")
sticker_list = [
    [None, None, None],
    [None, None, None],
    [None, None, None]   
]
for i in range(3):
    if Confirm.ask(f"Would you like stickers in the {Vertical[i]} row?"):
        for j in range(3):
            selected = Prompt.ask(f"Select a sticker for the {Vertical[i]} {Horizontal[j]} section", choices=all_stickers, show_choices=True)
            if selected == "":
                selected = None
            else: 
                size = IntPrompt.ask("Size of sticker (%)", default=10)
                sticker_list[i][j] = sticker.Sticker(selected, size)

sticker_opts = sticker.StickerOptions(sticker_list)
sticker_opts.renderStickers(img=img)
            
            
#Text options
topTextObj: text.TextObj | None
bottomTextObj: text.TextObj | None
centerTextObj: text.TextObj | None

topText = Prompt.ask("Top Text (enter for no text)")
if topText.strip() != "":
    textSize = IntPrompt.ask("Enter font size", default=40)
    font = Prompt.ask("Enter font: ", choices=os.listdir("./fonts"))
    topTextObj = text.TextObj(topText, fontSize=textSize, font=font)
else: topTextObj = None
    
centerText = Prompt.ask("Center Text (enter for no text)")
if centerText.strip() != "":
    textSize = IntPrompt.ask("Enter font size", default=40)
    font = Prompt.ask("Enter font", choices=os.listdir("./fonts"))
    centerTextObj = text.TextObj(centerText, fontSize=textSize, font=font)
else: centerTextObj = None
    
bottomText = Prompt.ask("Bottom Text (enter for no text)")
if bottomText.strip() != "":
    textSize = IntPrompt.ask("Enter font size", default=40)
    font = Prompt.ask("Enter font", choices=os.listdir("./fonts"))
    bottomTextObj = text.TextObj(bottomText, fontSize=textSize, font=font)
else: bottomTextObj = None
    
options = text.TextOptions(topText=topTextObj, bottomText=bottomTextObj, centerText=centerTextObj)
options.renderText(img=img)

saveDest = Prompt.ask("Filename to save to")
img.save(f"{saveDest}.png")
