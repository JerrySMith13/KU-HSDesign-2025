from PIL import Image, ImageOps, ImageColor

class filter_image:
    """A simple image filter module using Pillow."""
    
    def __init__(self, image_path: str, save_path: str):
        """Define path and save path."""
        self.original = Image.open(image_path).convert("RGB")
        self.image = self.original.copy()
        self.save_path = save_path

    def grayscale(self):
        """Makes image gray."""
        self.image = self.image.convert("L").convert("RGB")
        return self

    def sepia(self):
        """Applies sepia tone to image."""
        grayed = self.image.convert("L")
        self.image = ImageOps.colorize(grayed, "#704214", "#C0A080")
        return self

    def colorify(self, color, intensity: float = None):
        """Tints image with a color at given intensity."""
        overlay = Image.new("RGB", self.image.size, ImageColor.getrgb(color))
        self.image = Image.blend(self.image, overlay, intensity)
        return self

    def reset(self):
        """Resets image to the original."""
        self.image = self.original.copy()
        return self

    def save(self, save_path=None):
        """Saves the filtered image."""
        self.image.save(save_path or self.save_path)
        return self

