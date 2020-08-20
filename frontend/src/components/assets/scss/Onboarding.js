import React from 'react';
import './Onboarding.scss';
import {Button} from 'antd';
import 'antd/dist/antd.css';

const Onboarding = (props) =>{
  return(
    <div className="onboarding-contain">
      <div className="title">
        {props.title}
      </div>
      <div className="message">
        {props.message}
      </div>
      <div className="description">
        {props.description}
      </div>
      <img src={props.image} alt="Image of 2 people connecting"></img>
      <div className="button-contain">
        <Button type="primary" onClick={props.buttonOnClick}>Find a Match!</Button>
      </div>
    </div>
  );
}

export default Onboarding;