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
    <div className="profile-btn">
      <ProfileButton />

    </div>
    //   </li>
    // </ul>
  );
}

export default Navigation;
