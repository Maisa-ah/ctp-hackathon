import React from 'react';
import ShortTagContainer from '../components/ShortTagContainer';
import ServiceTag from '../components/ServiceTag';

import './ConnectCard.scss';

const ConnectCard = (props) =>{
  return(
    <div className="card-container" onClick={props.cardOnClick}>
      <div className="info-contain" >
          <div>
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

          <div >
            <ShortTagContainer >
              <ServiceTag service="Major Advice"/>
              <ServiceTag service="Class Advice"/>
              <ServiceTag service="Friendly Chat"/>
              <ServiceTag service="Activities"/>
              <ServiceTag service="Career Advice"/>
              <ServiceTag service="Collaborate"/>
            </ShortTagContainer>
          </div>
       </div>

        <div className="user-classes">
          {props.children}
        </div>
    </div>
  );
}

export default ConnectCard;