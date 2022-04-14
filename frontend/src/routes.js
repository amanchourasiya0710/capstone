import { Navigate, useRoutes } from 'react-router-dom';
// layouts
import DashboardLayout from './layouts/dashboard';
import LogoOnlyLayout from './layouts/LogoOnlyLayout';
import Login from './pages/Login';
import Register from './pages/Register';
import Activate from './pages/Activate';
import DashboardApp from './pages/DashboardApp';
import Products from './pages/Products';
import Blog from './pages/Blog';
import User from './pages/User';
import NotFound from './pages/Page404';
import Home from './pages/Home';

// ----------------------------------------------------------------------

export default function Router() {
  return useRoutes([
    {
      path: '/',
      element: <LogoOnlyLayout />,
      children: [
        // { path: '/', element: <Navigate to="/dashboard/app" /> },
        { path: '/', element: <Home /> },
        { path: 'login', element: <Login /> },
        { path: 'register', element: <Register /> },
        // { path: 'reset-password', element: <ResetPassword /> },
        // { path: 'password/reset/confirm/:uid/:token', element: <ResetPasswordConfirm /> },
        { path: 'activate/:uid/:token', element: <Activate /> },
        { path: '404', element: <NotFound /> },
        { path: '*', element: <Navigate to="/404" /> }
      ]
    },
    {
        path: '/dashboard',
        element: <DashboardLayout />,
        children: [
            { path: 'app', element: <DashboardApp /> },
            { path: 'user', element: <User /> },
            { path: 'products', element: <Products /> },
            { path: 'blog', element: <Blog /> }
        ]
    },
    { path: '*', element: <Navigate to="/404" replace /> }
  ]);
}
