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

  return (
    <div>
      <CanvasDraw {...state} />
    </div>
  );
}

export default App;
