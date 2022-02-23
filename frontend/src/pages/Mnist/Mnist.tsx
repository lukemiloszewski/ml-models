import React, { useState } from "react";

import CanvasDraw from "react-canvas-draw";

import { Canvas } from "../../components";
import { Container } from "../../components";

export function Mnist() {
  const [state] = useState({
    loadTimeOffset: 0,
    lazyRadius: 0,
    brushRadius: 5,
    brushColor: "black",
    hideGrid: true,
    canvasWidth: 300,
    canvasHeight: 300,
    hideInterface: true,
  });
  const [saveableCanvas, setSaveableCanvas] = useState<CanvasDraw | null>(null);

  return (
    <Container>
      <div>
        <Canvas
          {...state}
          ref={(canvas: CanvasDraw) => setSaveableCanvas(canvas)}
        />
        <button
          onClick={() => {
            saveableCanvas?.clear();
          }}
        >
          Clear
        </button>
      </div>
    </Container>
  );
}
