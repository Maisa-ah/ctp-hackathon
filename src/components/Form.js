import React from "react";
import { useForm } from "react-hook-form";
import './Form.scss';
import {Button} from 'antd';
import 'antd/dist/antd.css';
import { useRouter } from '../util/router.js';

function Form() {
  const {register, handleSubmit, errors} = useForm();

  const onSubmit = (data) => {
    console.log(data);
    router.push('/3000');
  }

  const router = useRouter();
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div className="field-container">
        <input className="border" type="text" placeholder="First Name" name="firstname" ref={register({required: true})}/>
      </div>
      <div className="field-container">
        <input className="border" type="text" placeholder="Last Name" name="lastname" ref={register({required: true})}/>
      </div>

      <div className="field-container">
        <select className="border" name= "school" ref={register({required: true})}>
          <option value="Queens">Queens College</option>
          <option value="Hunter">Hunter College</option>
          <option selected value="Baruch">Baruch College</option>
          <option value="CCT">New York City College of Technology</option>
          <option value="Brooklyn">Brooklyn College</option>
          <option value="StatenIsland">College of Staten Island</option>
          <option value="Lehman">Lehman College</option>
          <option value="JohnJay">John Jay College of Criminal Justice</option>
          <option value="Medgar">Medgar Evers College</option>
        </select>
      </div>
      <div className="field-container">
        <select className="border" name= "year" ref={register({required: true})}>
          <option value='1'>Freshman</option>
          <option value='2'>Sophmore</option>
          <option selected value='3'>Junior</option>
          <option value="4">Senior</option>
        </select>
      </div>
      <div className="field-container">
        <input className="border" type="text" placeholder="Major" name="major" ref={register({required: true})}/>
      </div>
      <div className="field-container">
        <input className="border" type="text" placeholder="Tell me about yourself!" name='bio' ref={register}></input>
      </div>
      <div className="field-container">
        <input className="border" type="text" placeholder="Can Help With (Optional):" name="help" ref={register}/>
      </div>
      <div className="button-container">
        <Button type="primary">Connect</Button>
      </div>
      
    </form>
  );
}

export default Form;