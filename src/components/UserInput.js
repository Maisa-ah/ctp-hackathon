import React from 'react';
import './UserInput.scss';

const UserInput = (props) =>{
  return(
    <div className="margin" >
      {props.title}
      <input className="border" value={props.name}>
      </input>
    </div>
  );
}

export default UserInput;