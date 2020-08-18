import React from 'react';
import './Fields.scss';

const Field = (props) =>{
  return(
    <div className="margin">
      {props.title}
      <input className="border" value={props.name}>
      </input>
    </div>
  );
}

export default Field;