import React from 'react';
import logo from '../logo.svg';
import './App.css';
import { Switch, Route, Router } from '../util/router.js';
import HomePage from './Home';
import LoginPage from './Login';
import Form from '../components/Form';


function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={HomePage} />
        <Route exact path="/login" component={LoginPage} />
        <Route exact path="/form" component={Form}/>


      </Switch>
    </Router>
  );
}

export default App;
