import React from 'react';
import Login from '../components/Login';
import { useRouter } from '../util/router.js';

function LoginPage() {
  const router = useRouter();
  return (    
    <div>
      <Login/>

    </div>

  );
}

export default LoginPage;
