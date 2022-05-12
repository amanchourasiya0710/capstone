import React from "react";
import { Link } from "react-router-dom";
import axios from "axios";

const Check = () => {
  console.log("!!..yaha kab aaoge ??..!!");
  const res = await axios.post(
    `${process.env.REACT_APP_API_URL}/getnames/`,
  );
  return (
    <>
      <div className="container">
        <div className="jumbotron mt-5">
          <h1 className="display-4">Welcome to Generic Workflows!</h1>
          <p className="lead">
            This is an awesome authentication system with production level
            features!
          </p>
          <hr className="my-4" />
          <p>Click the Log In button</p>
          <Link className="btn btn-primary btn-lg" to="/login" role="button">
            Login
          </Link>
        </div>
      </div>
    </>
  );
};

export default Check;
