import { useEffect, useState, useContext } from "react";
import { Outlet } from "react-router-dom";
import { useDispatch } from "react-redux";
import { useMediaQuery } from "react-responsive";
import { ModalProvider, Modal } from "../context/Modal";
import { thunkAuthenticate } from "../redux/session";
import Navigation from "../components/Navigation/Navigation";
import Footer from '../components/Footer/Footer' 
import '../../src/index.css'
import { PanelViews } from "../context/PanelView";




export default function Layout() {

  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(thunkAuthenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  const { defaultLeftPanel, defaultCenterPanel } = useContext(PanelViews)
  
  const [centerPanel, setCenterPanel] = useState(defaultCenterPanel)
  const [leftPanel, setLeftPanel] = useState(defaultLeftPanel)

  const isTabletOrMobile = useMediaQuery({query: '(max-width: 1100px)'})

  return (
    <>
      <PanelViews.Provider value={{centerPanel, setCenterPanel, leftPanel, setLeftPanel}}>
      <ModalProvider>
        <Navigation />
        <div id='app-views-container'>
        {isLoaded && <Outlet />}
        </div>
        {!isTabletOrMobile && 
        <Footer/>
        }
      

        <Modal />

      </ModalProvider>
      </PanelViews.Provider>
    </>
  );
}
