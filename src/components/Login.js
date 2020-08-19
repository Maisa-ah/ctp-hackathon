import React from 'react';
import Field from './Fields';
import login from './login.svg';
import ImageField from './ImageField';
import LoginButton from './LoginButton';
import { useRouter } from '../util/router.js';

function Login() {
  const router = useRouter();
  return (    
    <div className="page-container">
      <ImageField image={login} description="Welcome Back!"/>
      <Field name="Your email"/>
      <Field name="Password"/>
      <LoginButton 
      title="Login" 
      buttonOnClick={() => {
        router.push('/onboarding');
      }}
      />

    </div>

  );
}

export default Login;