import React from "react";
import "./assets/scss/ClassTag.scss";

const ClassTag = (props) => {
  return (
    <div className="tag-container">
      <div className="class-container">{props.class}</div>
    </div>
  );
};

export default ClassTag;
