import React from 'react';
import Field from '../components/Fields';
import ClassTag from '../components/ClassTag';
import TagContainer from '../components/TagContainer';
import CardContainer from '../components/ClassTag';
import ConnectCard from '../components/ConnectCard';
import { useRouter } from '../util/router.js';
import ShortTagContainer from '../components/ShortTagContainer';
import ServiceTag from '../components/ServiceTag';

function HomePage() {
  const router = useRouter();
  return (
    <div>
      <ConnectCard name="Jane Doe" major="Comp Sci" school="Hunter College" year="2021" 
      cardOnClick={() => {
        router.push('/profile');
      }}>
      <ShortTagContainer>
        <ServiceTag service="Major Advice"/>
        <ServiceTag service="Class Advice"/>
        <ServiceTag service="Friendly Chat"/>
        <ServiceTag service="Activities"/>
        <ServiceTag service="Career Advice"/>
        <ServiceTag service="Collaborate"/>
      </ShortTagContainer>
      <TagContainer>
        <ClassTag class="CSCI 335"/>
        <ClassTag class="CSCI 235"/>
        <ClassTag class="CSCI 135"/>
        <ClassTag class="CSCI 260"/>
        <ClassTag class="CSCI 499"/>
        <ClassTag class="CSCI 135"/>
        <ClassTag class="CSCI 260"/>
        <ClassTag class="CSCI 499"/>

      </TagContainer>
      </ConnectCard>
      
    </div>
  );
}

export default HomePage;
