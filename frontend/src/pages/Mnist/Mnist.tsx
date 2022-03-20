import React, { useState } from "react";

import { Loading } from "@nextui-org/react";

import { StyledButton, ButtonGroup, Canvas, Container } from "../../components";
import { config } from "../../config";
import { MnistResponse } from "../../types/interfaces";
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
  const { data, isFetching } = useRestClient<MnistResponse>(
    ["mnist", imageData],
    config.REACT_APP_MNIST_URL,
    {
      data: imageData,
    },
    enableQuery
  );

  return (
    <Container>
      <h2>MNIST Digit Classification</h2>
      <Canvas {...state} ref={(canvas) => setSaveableCanvas(canvas)} />
      {data && imageData ? (
        <StyledButton flat color="primary" auto clickable={false}>
          {data.result}
        </StyledButton>
      ) : isFetching ? (
        <StyledButton flat color="primary" auto clickable={false}>
          <Loading color="primary" size="sm" type="points" />
        </StyledButton>
      ) : (
        <StyledButton
          flat
          color="primary"
          auto
          clickable={false}
        ></StyledButton>
      )}
      <ButtonGroup>
        <StyledButton
          flat
          color="primary"
          auto
          onClick={() => {
            saveableCanvas.clear();
            setImageData("");
          }}
        >
          Clear
        </StyledButton>
        <StyledButton
          flat
          color="primary"
          auto
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
        </StyledButton>
      </ButtonGroup>
    </Container>
  );
}
