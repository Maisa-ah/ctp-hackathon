import React from 'react';
import ProfileTag from '../components/ProfileTag.js';
import profilePic from '../components/sampleProfile.svg';

function ProfilePage() {
  return (
    <div>
      <ProfileTag
        image={profilePic}
        phone="347-XXX-XXXX"
        email="XXX@gmail.com"
        name="Jane Doe"
        school="Hunter College"
        year="2021"
        bio="Hey guys! I’m Jane. Feel free to reach out."
      />
    </div>
  );
}

export default ProfilePage;
