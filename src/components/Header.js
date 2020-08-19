import React from 'react';
import './Header.scss';

const Header = (props) =>{
  return(
    <div className="header-container">
      <div className="logo-container">
        <div className="header-image">
          <img src={props.image}></img>
        </div>
      </div>
    <div className="header-title">
      {props.title}
    </div>
      <div className="header-tagline">
        {props.tagline}
      </div>
  </div>
  );
}

export default Header;