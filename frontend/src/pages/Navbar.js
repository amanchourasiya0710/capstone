import React, { Fragment, useEffect, useState } from 'react';
import { Link, Navigate } from 'react-router-dom';
import { connect } from 'react-redux';
import { logout } from '../actions/auth';
import { checkAuthenticated, load_user } from '../actions/auth';

const Navbar = ({ logout, isAuthenticated, checkAuthenticated, load_user }) => {
    const [redirect, setRedirect] = useState(false);

    setRedirect(false);
    console.log("aa to gya be iske andar...phir kyu mar raha h!");
    
    useEffect(() => {
        checkAuthenticated();
        load_user();
    }, []);

    const logout_user = () => {
        logout();
        setRedirect(true);
    };

    const guestLinks = () => (
        <Fragment>
            <li className='nav-item'>
                <Link className='nav-link' to='/login'>Login</Link>
            </li>
            <li className='nav-item'>
                <Link className='nav-link' to='/register'>Sign Up</Link>
            </li>
        </Fragment>
    );

    const authLinks = () => (
        <li className='nav-item'>
            <a className='nav-link' href='#!' onClick={logout_user}>Logout</a>
        </li>
    );

    return (
        <Fragment>
            <nav className='navbar navbar-expand-lg navbar-light bg-light'>
                <Link className='navbar-brand' to='/'>Auth System</Link>
                <button 
                    className='navbar-toggler' 
                    type='button' 
                    data-toggle='collapse' 
                    data-target='#navbarNav' 
                    aria-controls='navbarNav' 
                    aria-expanded='false' 
                    aria-label='Toggle navigation'
                >
                    <span className='navbar-toggler-icon'></span>
                </button>
                <div className='collapse navbar-collapse' id='navbarNav'>
                    <ul className='navbar-nav'>
                        <li className='nav-item active'>
                            <Link className='nav-link' to='/'>Home</Link>
                        </li>
                        {isAuthenticated ? authLinks() : guestLinks()}
                    </ul>
                </div>
            </nav>
            {redirect ? <Navigate to='/' /> : <Fragment></Fragment>}
        </Fragment>
    );
};

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});
    
export default connect(mapStateToProps, { logout, checkAuthenticated, load_user})(Navbar);