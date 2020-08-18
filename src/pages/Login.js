import React from 'react';
import Field from '../components/Fields';

function LoginPage() {
  return (
    <div>
      <Field title="Email" name="Your email"/>
      <Field title="First Name" name="First Name"/>
      <Field title="Last Name" name="Last Name"/>
      <Field title="Interest" name="Interest"/>
    </div>
  );
}

export default LoginPage;
