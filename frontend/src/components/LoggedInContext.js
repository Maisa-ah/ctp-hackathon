import React, { useState } from "react";
import { useLocalStorage } from "../util/hooks";
import Api from "../util/api";

export const LoggedInContext = React.createContext();

const LoggedInProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loggedIn, setLoggedIn] = useState(false);
  const [token, setToken, removeToken] = useLocalStorage("_token", "");
  const [
    tokenTimestamp,
    setTokenTimestamp,
    removeTokenTimestamp,
  ] = useLocalStorage("_tokenTimestamp", "");

  const login = () => {
    // Automatically Log the user out after 1 hour
    const expire = new Date().getTime() - tokenTimestamp;

    if (expire > 3600000) {
      removeToken();
      removeTokenTimestamp();

      setLoggedIn(false);
      setUser(null);
      return;
    }

    if (token) {
      setLoggedIn(true);

      async function getUser() {
        setUser(await Api.getUser());
      }

      getUser();
    }
  };

  return (
    <LoggedInContext.Provider
      value={{
        user,
        setUser,
        loggedIn,
        setLoggedIn,
        token,
        setToken,
        removeToken,
        login,
        setTokenTimestamp,
        removeTokenTimestamp,
      }}
    >
      {children}
    </LoggedInContext.Provider>
  );
};

export default LoggedInProvider;
