import React from 'react';
import './Splash.scss';
import {Button } from 'antd';
import "antd/dist/antd.css";
import Header from './Header';
import LoginButton from './LoginButton';
import { useRouter } from '../util/router.js';

const Splash = (props) =>{
  const router = useRouter();
  return(
  <div className="splash-container">
    <Header title="CollabU" tagline="Reconnect with your school" image={props.image2}/>
    <div className="splash-image">
      <img src={props.image}></img>
    </div>
    <div className="sign-up">
      <Button type="primary">Sign Up</Button>
    </div>
    <div className="login">
      <Button type="primary"
      buttonOnClick={() => {
        router.push('/login');
      }}
      >Login</Button>
    </div>


  </div>
  );
}

export default Splash;