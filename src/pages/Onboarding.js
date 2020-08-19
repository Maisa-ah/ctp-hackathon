import React from 'react';
import Onboarding from '../components/Onboarding';
import { useRouter } from '../util/router.js';
import connect from '../components/connection.svg';

function LoginPage() {
  const router = useRouter();
  return (    
    <div>
      <Onboarding
      title="You’re not alone!"
      message="Find students who share your situation."
      description="Get matched with students in your classes or connect with someone who might hold some insight."
      image={connect}
      buttonOnClick={() => {
        router.push('/form');
      }}

      />
    </div>

  );
}

export default LoginPage;
