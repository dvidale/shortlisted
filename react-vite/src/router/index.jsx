import { createBrowserRouter } from 'react-router-dom';
import Layout from './Layout';


import HomeView from '../components/HomeView/HomeView.jsx';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <>
        <HomeView/>
        </>
      }
    ],
  },
]);