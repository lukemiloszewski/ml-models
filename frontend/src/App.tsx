import React, { useState } from "react";
import CanvasDraw from "react-canvas-draw";

function App() {
  const [state, setState] = useState({
    loadTimeOffset: 0,
    lazyRadius: 10,
    brushRadius: 8,
    brushColor: "red",
    catenaryColor: "blue",
    hideGrid: false,
    canvasWidth: 300,
    canvasHeight: 300,
    hideInterface: false,
    immediateLoading: true,
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

export default App;
