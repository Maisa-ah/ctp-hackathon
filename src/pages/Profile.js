import React from 'react';
import ProfileTag from '../components/ProfileTag.js';
import profilePic from '../components/sampleProfile.svg';
import ClassTag from '../components/ClassTag';
import ServiceTag from '../components/ServiceTag';
import ShortTagContainer from '../components/ShortTagContainer';
import Titling from '../components/Titling';

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
      <Titling title="Services"/>
      <ShortTagContainer>
        <ServiceTag service="Major Advice"/>
        <ServiceTag service="Class Advice"/>
        <ServiceTag service="Friendly Chat"/>
        <ServiceTag service="Activities"/>
        <ServiceTag service="Career Advice"/>
        <ServiceTag service="Collaborate"/>
      </ShortTagContainer>
      <Titling title="Classes"/>
      <ShortTagContainer>
        <ClassTag class="CSCI 335"/>
        <ClassTag class="CSCI 235"/>
        <ClassTag class="CSCI 135"/>
        <ClassTag class="CSCI 260"/>
        <ClassTag class="CSCI 499"/>
        <ClassTag class="CSCI 135"/>
        <ClassTag class="CSCI 260"/>
        <ClassTag class="CSCI 499"/>
      </ShortTagContainer>

    </div>
  );
}

export default ProfilePage;
