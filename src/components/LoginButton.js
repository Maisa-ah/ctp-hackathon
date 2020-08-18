import React from 'react';
import './LoginButton.scss';
import {Button } from 'antd';
import "antd/dist/antd.css";

const LoginButton = (props) =>{
  return(
    <div className="button-container">
    <Button type="primary"
    onClick={props.buttonOnClick}
  >
    {props.title}
  </Button>
  </div>
  );
}

export default LoginButton;