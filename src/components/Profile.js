import React from 'react';
import UserData from './UserData';


import { useRouter } from '../util/router.js';
import Textbox from './Textboxes';
import Dropdown from './Dropdown';

function Profile() {
  const router = useRouter();
  return (    
    <div className="page-container">
      <UserData name="First Name"/>
      <UserData name="Last Name"/>
       <Dropdown name="school"/>
    <Textbox name ="Comment"/>
    </div>
    

  );
}

export default Profile;