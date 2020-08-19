import React from 'react';
import './Splash.scss';
import {Button } from 'antd';
import "antd/dist/antd.css";
import image from 'material-ui/svg-icons/image/image';

const Splash = (props) =>{
  return(
  <div>
    <img src={props.image2}></img>
    <img src={props.image}></img>


  </div>
  );
}

export default Splash;