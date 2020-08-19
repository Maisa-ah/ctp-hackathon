import React from 'react';
import './ConnectCard.scss';

const ConnectCard = (props) =>{
  return(
    <div className="card-container" onClick={props.cardOnClick}>
      <div className="info-contain">
        <div className="user-name">
          {props.name}
        </div>
        <div className="user-school">
          {props.school} {props.year}
        </div>
        <div className="user-major">
          {props.major}
        </div>
      </div>
      <div className="user-classes">
        {props.children}
      </div>
    </div>
  );
}

export default ConnectCard;