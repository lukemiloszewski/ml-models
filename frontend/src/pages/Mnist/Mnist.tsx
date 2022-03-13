import React, { useState } from "react";

import CanvasDraw from "react-canvas-draw";

import {
  Button,
  ButtonGroup,
  Canvas,
  Container,
  Prediction,
} from "../../components";
import { config } from "../../config";
import { MnistType } from "../../types/interfaces";
import { useRestClient } from "../../utils/useRestClient";

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

  const enableQuery = imageData.length > 0;
  const { data } = useRestClient<[MnistType]>(
    ["mnist", imageData],
    config.REACT_APP_MNIST_URL,
    {
      data: imageData,
    },
    enableQuery
  );

  return (
    <Container>
      <h1>MNIST Digit Classification</h1>
      <Canvas
        {...state}
        ref={(canvas: CanvasDraw) => setSaveableCanvas(canvas)}
      />
      {imageData ? (
        <Prediction>{data}</Prediction>
      ) : (
        <Prediction>...</Prediction>
      )}
      <ButtonGroup>
        <Button
          onClick={() => {
            saveableCanvas.clear();
            setImageData("");
          }}
        >
          Clear
        </Button>
        <Button
          onClick={() => {
            const { lines } = JSON.parse(saveableCanvas.getSaveData());
            if (lines.length > 0) {
              setImageData(
                saveableCanvas.getDataURL("png", false, "white").split(",")[1]
              );
            }
          }}
        >
          Predict
        </Button>
      </ButtonGroup>
    </Container>
  );
}
