import React from "react";
import { useForm } from "react-hook-form";
import './Signup.scss';
import {Button} from 'antd';
import 'antd/dist/antd.css';
import { useRouter } from '../util/router.js';

function SignupPage(){
  const router = useRouter();
  const {register, handleSubmit, errors} = useForm();

  const ButtonOnClick = () => {
    router.push('/onboarding');
  }
  const onSubmit = data => {
    console.log(data);
  }

  return (
    <div className="page-container">
      <div className="heading">Welcome!</div>
      <p className="subtitle">Create Account</p>
        
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="field-container">
          <input className="border" type="tezt" placeholder="Full Name" name="name" ref={register({required: true})}/>
        </div>
        <div className="field-container">
          <input className="border" type="email" placeholder="Your Email" name="email" ref={register({required: true})}/>
        </div>
        <div className="field-container">
          <input className="border" type="text" placeholder="Password" name="password" ref={register({required: true, minlength: 6})}/>
        </div>
        <div className="terms">
          <input type="checkbox" name="terms" className="checkbox"/>
          <label> I read and agree with Terms and Condition</label>
        </div>
        <div className="button-container">
          <Button onClick={ButtonOnClick} type="primary">SIGN UP</Button>
        </div>
          
      </form>
    </div>
  )


    
}
export default SignupPage;