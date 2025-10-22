from PIL import Image, ImageOps, ImageColor

class filter_image:
    """A simple image filter module using Pillow."""

    def grayscale(img:Image):
        """Makes image gray."""
        img.convert("L").convert("RGB")

    def sepia(img: Image):
        """Applies sepia tone to image."""
        grayed = img.convert("L")
        img = ImageOps.colorize(grayed, "#704214", "#C0A080")

    def colorify(img:Image, color, intensity: float = 0):
        """Tints image with a color at given intensity."""
        overlay = Image.new("RGB", img.size, ImageColor.getrgb(color))
        img = Image.blend(img, overlay, intensity)
