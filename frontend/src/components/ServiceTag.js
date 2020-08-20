import React from "react";
import "./assets/scss/ServiceTag.scss";

const ServiceTag = (props) => {
  return (
    <div className="tag-container">
      <div className="service-container">{props.service}</div>
    </div>
  );
};

export default ServiceTag;
