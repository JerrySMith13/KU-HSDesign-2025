import { useEffect, useRef, useState } from "react";
import { Canvas, FabricImage } from "fabric";


export function RenderCanvas(prop: any){

    const canvasRef = useRef(null);
    const [fabricCanvas, setFabricCanvas] = useState<Canvas | null>(null);
    
    useEffect(() => {
     if (canvasRef.current){
        const newCanvas = new Canvas(canvasRef.current, {
            width: 800,
            height: 600,
            backgroundColor: '#000000',
        });
        setFabricCanvas(newCanvas);
        return () => { newCanvas.dispose() };
     }   
    }, [])

    return (
        <canvas ref={canvasRef} />
    );
}
