import { Change } from "./Tool"
import * as photon from '@silvia-odwyer/photon'

interface Pixel{
    red: number,
    green: number,
    blue: number,
}
class Filter extends Change{
}

class Invert extends Filter{
    pixelEffect(pixel: Pixel): Pixel {
        const red = Math.abs(pixel.red - 255);
        const green = Math.abs(pixel.green - 255);
        const blue = Math.abs(pixel.blue - 255);
        return {red, green, blue}
    }
    changeCanvas(canvas: photon.PhotonImage): photon.PhotonImage {
        photon.invert(canvas);
        return canvas;
    }
    undoChange(canvas: photon.PhotonImage): photon.PhotonImage {
        photon.invert(canvas);
        return canvas;
    }
    
}
class Grayscale extends Filter{
    
}

export default Filter