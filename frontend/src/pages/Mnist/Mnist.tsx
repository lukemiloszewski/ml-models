import React, { useState } from "react";

import CanvasDraw from "react-canvas-draw";

import { Container } from "../../components/Container/Container";

export function Mnist() {
  const [state, setState] = useState({
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
    </Container>
  );
}
