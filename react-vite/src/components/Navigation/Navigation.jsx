

import "./Navigation.css";
import { useModal } from "../../context/Modal";
import { useSelector } from "react-redux";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";

function Navigation() {
  const user = useSelector((store) => store.session.user);
  const { setModalContent } = useModal();

  const handleLogin = () =>{
    setModalContent(
      <LoginFormModal/>
    )
  }
  
  const handleSignUp = () =>{
    setModalContent(
      <SignupFormModal/>
    )
  }
  
  
  return (
 
    <div className="navigation-bar">
     
    <div className="profile-btn">
      { user ? (<>     

       </>):(<>   
       <div className="login-signup-homepage-btns">
       <button className='front-login-signup-btn' onClick={handleLogin}>Login</button>   
       or   
       <button className='front-login-signup-btn' onClick={handleSignUp}>Sign Up</button>
       </div>
           </>)}
      
      

    </div>
    </div>
    
  );
}

export default Navigation;
