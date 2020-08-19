import React from 'react';
import './ProfileTag.scss';

const ProfileTag = (props) =>{
  return(
    <div>
      {props.image}
      {props.phone}
      {props.email}
      {props.name}
      {props.school} {props.year}
      {props.bio}
      
    </div>
  );
}

export default ProfileTag;