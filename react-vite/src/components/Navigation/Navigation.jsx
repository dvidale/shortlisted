// import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  return (
    // <ul>
    //   <li>
    //     <NavLink to="/">Home</NavLink>
    //   </li>
    //   <li>
    <div className="navigation-bar">
     <div>Shortlisted.</div>
    <div className="profile-btn">
      <ProfileButton />

    </div>
    </div>
    
    //   </li>
    // </ul>
  );
}

export default Navigation;
