import React, { useState, useContext } from "react";
import { Button } from "antd";
import loginImg from "./assets/img/login.svg";
import ImageField from "./ImageField";
import LoginButton from "./LoginButton";
import { useForm } from "react-hook-form";
import { LoggedInContext } from "../components/LoggedInContext";
import { useHistory } from "react-router-dom";
import Api from "../util/api";

function Login() {
  const history = useHistory();
  const { setToken, loggedIn, setLoggedIn, setTokenTimestamp } = useContext(
    LoggedInContext
  );
  const { register, handleSubmit } = useForm();

  async function loginUser(data) {
    let _token;

    try {
      _token = await Api.login(data);
    } catch (err) {
      return;
    }

    setTokenTimestamp(new Date().getTime());
    setToken(_token);
    setLoggedIn(true);

    history.push("/");
  }

  const onSubmit = data => loginUser(data);

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <ImageField image={loginImg} description="Welcome Back!" />

      <label htmlFor="username">Username</label>
      <input ref={register} name="username" />

      <label htmlFor="password">Password</label>
      <input ref={register} name="password" type="password" />

      <LoginButton />
    </form>
  );
}

export default Login;
