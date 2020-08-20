import React from 'react';
import ClassTag from '../components/ClassTag';
import TagContainer from '../components/TagContainer';
import ConnectCard from '../components/ConnectCard';
import { useRouter } from '../util/router.js';
import Titling from '../components/Titling';

function HomePage() {
  const router = useRouter();
  return (
    <div>
      <Titling title2="Your Matches"/>
      <ConnectCard name="Jane Doe" major="Comp Sci" school="Hunter College" year="2021" 
      cardOnClick={() => {
        router.push('/profile');
      }}>
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
