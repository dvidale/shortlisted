

import "./Navigation.css";
import { useModal } from "../../context/Modal";
import { useSelector } from "react-redux";
import LoginFormModal from "../LoginFormModal";
import TypeformBetaSignupComponent from "../TypeformForms/TypeformBetaSignup/TypeformBetaSignupComponent";
import "../TypeformForms/TypeformBetaSignup/typeform-beta-signup.css";

// import SignupFormModal from "../SignupFormModal";

function Navigation() {
  const user = useSelector((store) => store.session.user);
  const { setModalContent } = useModal();

  const handleLogin = () =>{
    setModalContent(
      <LoginFormModal/>
    )
  }
  
  // const handleSignUp = () =>{
  //   setModalContent(
  //     <SignupFormModal/>
  //   )
  // }
  
  
  return (
 
    <div className="navigation-bar">
    
      { user ? (<>  
      <div className='typeform-button-wrapper'>
<TypeformBetaSignupComponent typeformId="bvWLgIBe" />
        </div>   
       </>):(<>   
       <div className='typeform-button-wrapper'>
<TypeformBetaSignupComponent typeformId="bvWLgIBe" />
        </div>
        <div className='site-title-and-login-signup-btns'>
        <div className="landing-page-site-title">Shortlisted.</div>
       <div className="login-signup-homepage-btns">
       <button className='front-login-signup-btn' onClick={handleLogin}>Demo Login</button>   
          </div>
       {/* or   
       <button className='front-login-signup-btn' onClick={handleSignUp}>Sign Up</button> */}
       </div>
           </>)}

    </div>
    
  );
}

export default Navigation;
