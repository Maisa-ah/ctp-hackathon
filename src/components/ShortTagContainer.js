import React from 'react';
import './ShortTagContainer.scss';

const ShortTagContainer = (props) =>{
  return(
    <div className="short-contain">
      {props.children}
    </div>
  );
}

export default ShortTagContainer;