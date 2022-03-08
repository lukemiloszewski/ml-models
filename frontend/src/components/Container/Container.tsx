import styled from "styled-components";

export const Container = styled.div`
  margin: 60px auto; /* top bottom left right */
  padding: 0;
  display: flex;
  flex-direction: column;
  text-align: center;
  max-width: 270px;
  @media (max-width: 768px) {
    margin: 15px auto 60px; /* top bottom left right */
  }
`;
