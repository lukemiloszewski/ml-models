import React, { useEffect, useState } from "react";

import axios from "axios";
import CanvasDraw from "react-canvas-draw";

import {
  Button,
  ButtonGroup,
  Canvas,
  Container,
  Prediction,
} from "../../components";
import { config } from "../../config";

export function Mnist() {
  const [state] = useState({
    loadTimeOffset: 0,
    lazyRadius: 0,
    brushRadius: 7,
    brushColor: "black",
    hideGrid: true,
    canvasWidth: 260,
    canvasHeight: 260,
    hideInterface: true,
  });
  const [saveableCanvas, setSaveableCanvas] = useState<any>(null);
  const [imageData, setImageData] = useState<string>("");
  const [response, setResponse] = useState<any>("...");

  useEffect(() => {
    if (imageData.length > 0) {
      var imgStr = imageData.split(",")[1];
      axios
        .post(config.REACT_APP_MNIST_URL, {
          data: imgStr,
        })
        .then((res) => {
          setResponse(res.data.result);
        });
    }
  }, [imageData]);

  return (
    <Container>
      <h1>MNIST Digit Classification</h1>
      <Canvas
        {...state}
        ref={(canvas: CanvasDraw) => setSaveableCanvas(canvas)}
      />
      <Prediction>{response}</Prediction>
      <ButtonGroup>
        <Button
          onClick={() => {
            saveableCanvas.clear();
            setResponse("...");
          }}
        >
          Clear
        </Button>
        <Button
          onClick={() => {
            const { lines } = JSON.parse(saveableCanvas.getSaveData());
            if (lines.length > 0) {
              setImageData(saveableCanvas.getDataURL("png", false, "white"));
            }
          }}
        >
          Predict
        </Button>
      </ButtonGroup>
    </Container>
  );
}
