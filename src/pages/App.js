import React from 'react';
import { Switch, Route, Router } from '../util/router.js';
import HomePage from './Home';
import LoginPage from './Login';
import Form from '../components/Form';
import ProfilePage from './Profile';
import Onboarding from './Onboarding';
import SignUpPage from '../components/Signup';


function App() {
  return (
    <Router>
      <Switch>
      <Route exact path="/onboarding" component={Onboarding} />
        <Route exact path="/" component={HomePage} />
        <Route exact path="/login" component={LoginPage} />
        <Route exact path="/form" component={Form}/>
        <Route exact path="/profile" component={ProfilePage} />
        <Route exact path="/signup" component={SignUpPage} />

      </Switch>
    </Router>
  );
}

export default App;
