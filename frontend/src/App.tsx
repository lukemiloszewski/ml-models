import React from "react";

import { GlobalStyle } from "./components/";
import { Mnist } from "./pages/";

export function App() {
  return (
    <React.Fragment>
      <GlobalStyle />
      <Mnist />
    </React.Fragment>
  );
}
