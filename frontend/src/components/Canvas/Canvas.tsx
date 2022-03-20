import styled from "styled-components";

import CanvasDraw from "react-canvas-draw";

export const Canvas = styled(CanvasDraw)`
  border: 5px solid rgb(191, 216, 252);
  border-radius: 12px;
  transition: 0.3s;
  :hover {
    cursor: pointer;
    border-color: rgb(142, 186, 248);
    transition: 0.3s;
  }
`;
