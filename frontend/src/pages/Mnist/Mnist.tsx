import React, { useEffect, useState } from "react";

import axios from "axios";
import CanvasDraw from "react-canvas-draw";

import { Button, Canvas, Container } from "../../components";

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
  const [imageData, setImageData] = useState<String | undefined>("");
  const [response, setResponse] = useState("Loading...");

  useEffect(() => {
    axios
      .post("http://127.0.0.1:8000/v1/predict/mnist", { image: imageData })
      .then((res) => {
        setResponse(res.data.image_prediction);
      });
  }, [imageData]);

  return (
    <Container>
      <div>
        <Canvas
          {...state}
          ref={(canvas: CanvasDraw) => setSaveableCanvas(canvas)}
        />
        <Button
          onClick={() => {
            saveableCanvas?.clear();
          }}
        >
          Clear
        </Button>
        <Button
          onClick={() => {
            setImageData(saveableCanvas?.getSaveData());
          }}
        >
          Predict
        </Button>
      </div>
    </Container>
  );
}
