import React from "react";
import { render } from "react-dom";
import App from "./components/App";
import "bootstrap/dist/css/bootstrap.min.css";

const appDiv = document.getElementById("app");
render(<App />, appDiv);
