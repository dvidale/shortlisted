import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';
import ProfileImageUploadForm from '../components/SignupFormPage/ProfileImgUploadForm.jsx';

import HomeView from '../components/HomeView/HomeView.jsx';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <>
        <HomeView/>
        </>,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "upload",
        element:<ProfileImageUploadForm/>,
      }
    ],
  },
]);