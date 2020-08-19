import React from 'react';
import './ProfileTag.scss';
import { useRouter } from '../util/router.js';
import BackButton from './BackButton';
import { ActionVerifiedUser } from 'material-ui/svg-icons';

const ProfileTag = (props) =>{
  const router = useRouter();
  return(
    <div className="profile-container">
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
          <div className="contact">
            <div className="phone">
              {props.phone}
            </div>
            <div>
              {props.email}
            </div>
          </div>
        </div>
        <div className="user-info">
          <div>
            <div className="user-name">
              {props.name}
            </div>
            <div className="user-school">
              {props.school} {props.year}
            </div>
          </div>
          <div className="user-bio">
            {props.bio}
          </div>
        </div>
      </div>
    </div>
  );
}

export default ProfileTag;