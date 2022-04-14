
import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from './Navbar';

const Home = () => (
    <div>
        <Navbar></Navbar>
        <div className='container'>
            <div class='jumbotron mt-5'>
                <h1 class='display-4'>Welcome to Generic Workflows!</h1>
                <p class='lead'>This is an awesome authentication system with production level features!</p>
                <hr class='my-4' />
                <p>Click the Log In button</p>
                <Link class='btn btn-primary btn-lg' to='/login' role='button'>Login</Link>
            </div>
        </div>
    </div>
);

export default Home;