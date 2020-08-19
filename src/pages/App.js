import React from 'react';
import { Switch, Route, Router } from '../util/router.js';
import HomePage from './Home';
import LoginPage from './Login';
import ProfilePage from './Profile';
import Onboarding from './Onboarding';

function App() {
  return (
    <Router>
      <Switch>
      <Route exact path="/onboarding" component={Onboarding} />
        <Route exact path="/" component={HomePage} />
        <Route exact path="/login" component={LoginPage} />
        <Route exact path="/profile" component={ProfilePage} />
      </Switch>
    </Router>
  );
}

export default App;
