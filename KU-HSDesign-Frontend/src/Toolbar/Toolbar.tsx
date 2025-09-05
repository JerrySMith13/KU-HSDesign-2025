import { useState } from "react";
import './Toolbar.css'
function Toolbar() {

    const [activeTool, setActiveTool] = useState(-1);
    const tools = ['Filter', 'Crop', 'Text'];

    return (
        <div className="toolbar">
            {tools.map((tool, index) => {
                return (
                    <button
                        key={index}
                        className={`toolbar-button ${activeTool === index ? 'active' : ''}`}
                        onClick={() => {console.log("clicked"); setActiveTool(index)}}
                    >
                        {tool}
                    </button>

                    
                )
            })}
        </div>
    );
}

export default Toolbar