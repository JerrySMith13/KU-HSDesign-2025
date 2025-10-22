import { Change } from "./Tool";
import * as photon from '@silvia-odwyer/photon'
class Text extends Change{
    originalImage: photon.PhotonImage;
    text: string;
    fontSize: number;
    pos: {x: number, y: number};
    constructor(originalImage: photon.PhotonImage, text: string, fontSize: number, pos:{x:number, y: number}){
        super()
        this.originalImage = originalImage;
        this.text = text;
        this.fontSize = fontSize;
        this.pos = pos;
    }
    renderText(pos: {x: number, y: number} = this.pos, text: string = this.text, fontSize: number = this.fontSize): photon.PhotonImage{
        let newImg: photon.PhotonImage = new photon.PhotonImage(this.originalImage.get_bytes(), this.originalImage.get_width(), this.originalImage.get_height());
        this.pos = pos;
        this.text = text; 
        this.fontSize = fontSize;
        photon.draw_text(newImg, this.text, pos.x, pos.y, this.fontSize);
        
        return newImg;
    }
    changeCanvas(canvas: photon.PhotonImage): photon.PhotonImage {
        return this.renderText()
    }
    undoChange(canvas: photon.PhotonImage): photon.PhotonImage {
        return this.originalImage;
    }
}

function TextTool(props: any){
    const image: photon.PhotonImage = props.origImage;
    let history: Change[] = props.history;
    const setHistory = props.setHistory;
    const setImg = props.setImg;

    let textChange = new Text(image, "", 10, {x: 0, y: 0});

    <div id="text-tool">
        <input type="range" min={0} max={image.get_width()} id="x-val"
        onChange={(e) => {
            textChange.pos.x = e.target.valueAsNumber;
            setImg(textChange.renderText());
        }}>X Value</input>
        <input type="range" min={0} max={image.get_height()} id="y-val"
        onChange={
            (e) => {
                textChange.pos.y = e.target.valueAsNumber;
                setImg(textChange.renderText());
            }
        }>Y Value</input>
        <input type="text" maxLength={24} id="text-val"
        onChange={
            (e) => {
                textChange.text = e.target.value;
                setImg(textChange.renderText());
            }
        }>Enter text: </input>
        <input type="range" min={10} max={40} id="font-size"
        onChange={
            (e) => {
                textChange.fontSize = e.target.valueAsNumber;
                setImg(textChange.renderText());
            }
        }>Font size</input>
        <button onClick={() => {
            setImg(textChange.changeCanvas(image));
            history.push(textChange);
            setHistory(history);
        }}>Save Change</button>
    </div>
}

export default TextTool;