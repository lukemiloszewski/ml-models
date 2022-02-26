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
  const [saveableCanvas, setSaveableCanvas] = useState<any>(null);
  const [imageData, setImageData] = useState<string | null>(null);
  const [response, setResponse] = useState("Loading...");

  useEffect(() => {
    if (imageData) {
      var base64result = imageData?.split(",")[1];
    } else {
      var base64result = "";
    }
    let imageD = new FormData();
    imageD.append("file", base64result);
    console.log(imageD.get("file"));

    axios
      .post(
        "http://localhost:8000/v1/predict/mnist",

        {
          file: imageD.get("file"),
        },
        {
          headers: {
            Accept: "application/json",
          },
        }
      )
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
            setImageData(saveableCanvas?.getDataURL("png", false, "white"));
          }}
        >
          Predict
        </Button>
      </div>
    </Container>
  );
}
