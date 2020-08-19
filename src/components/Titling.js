import React from 'react';
import './Titling.scss';


const Titling = (props) =>{
  return(
  <div>
    <div className="profile-title">
      {props.title}
    </div>
      <div className="home-title">
      {props.title2}
    </div>
  </div>
  );
}

export default Titling;