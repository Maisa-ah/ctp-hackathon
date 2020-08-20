import React from "react";
import "antd/dist/antd.css";
import { Button } from "antd";
import Back from "./assets/img/back.svg";
import "./assets/scss/BackButton.scss";

const BackButton = (props) => (
  <div className="button-contain">
    <Button
      type="primary"
      shape="circle"
      size="large"
      onClick={props.buttonOnClick}
    >
      <img className="icon-contain" src={Back} alt="Back button" />
    </Button>
  </div>
);

export default BackButton;
