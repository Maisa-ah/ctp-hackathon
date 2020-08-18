import React from 'react';
import Field from '../components/Fields';

function LoginPage(props) {
  return (
    <div>
      <Field title="Email" name="Your email"/>
      <Field title="First Name" name="First Name"/>
      <Field title="Last Name" name="Last Name"/>
    </div>
  );
}

export default LoginPage;
