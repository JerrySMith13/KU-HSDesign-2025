import PIL
path = input("Enter file path: ")
im = PIL.Image.open(path)

im = applyFilters(im)



im = applyText(im)

input("Center text: ")


