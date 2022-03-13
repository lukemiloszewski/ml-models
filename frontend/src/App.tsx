import { QueryClient, QueryClientProvider } from "react-query";

import React from "react";

import { GlobalStyle } from "./components/";
import { Mnist } from "./pages/";

const queryClient = new QueryClient();

export function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <React.Fragment>
        <GlobalStyle />
        <Mnist />
      </React.Fragment>
    </QueryClientProvider>
  );
}
