import React from 'react';
import './Titling.scss';


const Titling = (props) =>{
  return(
  <div className="profile-title">
    {props.title}
  </div>
  );
}

export default Titling;