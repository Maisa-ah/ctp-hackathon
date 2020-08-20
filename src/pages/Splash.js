import React from 'react';
import splash from '../components/splash.svg';
import Splash from '../components/Splash';
import logo from '../components/graduation.svg';
import { useRouter } from '../util/router.js';

function SplashPage() {
  const router = useRouter();
  return (    
    <div>
      <Splash image={splash} image2={logo} signup="Sign Up" login="Login"
      loginOnClick ={() => {
        router.push('/login');
      }}
      signUpOnClick={() => {
        router.push('/signup');
      }}/>

    </div>

  );
}

export default SplashPage;
