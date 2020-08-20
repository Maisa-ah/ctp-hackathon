import React from "react";
import "./assets/scss/ImageField.scss";

const ImageField = (props) => {
  return (
    <div className="img-container">
      <img src={props.image}></img>
      <div className="login-title">{props.description}</div>
    </div>
  );
};

export default ImageField;
