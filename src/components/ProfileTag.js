import React from 'react';
import './ProfileTag.scss';
import { useRouter } from '../util/router.js';
import BackButton from './BackButton';
import { ActionVerifiedUser } from 'material-ui/svg-icons';

const ProfileTag = (props) =>{
  const router = useRouter();
  return(
    <div className="tag-container">
      <div className="button-padding">
        <BackButton buttonOnClick={() => {
          router.push('/');
        }}/>
      </div>
      <div className="tag-padding">
        <div className="contact-info">
          <div className="profile-pic">
            <img src={props.image}></img>
          </div>
          <div className="phone">
            {props.phone}
          </div>
          <div>
            {props.email}
          </div>
        </div>
        <div className="user-info">
          <div>
            {props.name}
          </div>
          <div>
            {props.school} {props.year}
          </div>
          <div>
            {props.bio}
          </div>
        </div>
      </div>
    </div>
  );
}

export default ProfileTag;