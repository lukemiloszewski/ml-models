import React, { useState } from "react";

import { Loading, Modal, Spacer, Text } from "@nextui-org/react";
import { Setting } from "react-iconly";

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
  const [visible, setVisible] = React.useState(false);
  const handler = () => setVisible(true);
  const closeHandler = () => {
    setVisible(false);
  };

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
          <Loading color="primary" size="md" type="points" />
        </StyledButton>
      ) : (
        <StyledButton
          flat
          color="primary"
          auto
          onClick={handler}
          iconRight={<Setting set="bold" />}
        ></StyledButton>
      )}
      <Modal
        closeButton
        blur
        animated={false}
        aria-labelledby="modal-title"
        open={visible}
        onClose={closeHandler}
      >
        <Modal.Header>
          <Text id="modal-title" h2>
            ML Models 🤖
          </Text>
        </Modal.Header>
        <Modal.Body>
          <Text size={14}>
            The MNIST database is a collection of 70000 handwritten digits
            commonly used to build machine learning models.
          </Text>
          <Spacer y={0.25} />
          <Text size={14}>
            The model used in this application is a convolutional neural network
            which take's advantage of the spatial nature of the data.
          </Text>
          <Spacer y={0.25} />
          <Text size={14}>
            To view a prediction made by this model, draw any digit between 0
            and 9 within the canvas block.
          </Text>
          <Spacer y={1} />
        </Modal.Body>
      </Modal>
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
