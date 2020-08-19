import React from 'react';
import Profile from '../components/Profile';
import { useRouter } from '../util/router.js';

function ProfilePage() {
  const router = useRouter();
  return (    
    <div>
      <Profile/>

    </div>

  );
}

export default ProfilePage;
