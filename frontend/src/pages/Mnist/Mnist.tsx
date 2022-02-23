import React, { useState } from "react";
import CanvasDraw from "react-canvas-draw";

export function Mnist() {
  const [state, setState] = useState({
    loadTimeOffset: 0,
    lazyRadius: 0,
    brushRadius: 5,
    brushColor: "red",
    catenaryColor: "red",
    hideGrid: false,
    canvasWidth: 300,
    canvasHeight: 300,
    hideInterface: false,
  });
  const [saveableCanvas, setSaveableCanvas] = useState<CanvasDraw | null>(null);

  return (
    <div>
      <CanvasDraw
        {...state}
        ref={(canvasDraw: CanvasDraw) => setSaveableCanvas(canvasDraw)}
      />
      <button
        onClick={() => {
          saveableCanvas?.clear();
        }}
      >
        Clear
      </button>
    </div>
  );
}
