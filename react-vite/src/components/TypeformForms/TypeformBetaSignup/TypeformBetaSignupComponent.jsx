import { PopupButton } from "@typeform/embed-react";

function TypeformBetaSignupComponent({typeformId}) {
  return (
    <div className="typeform-beta-signup-component">
      <PopupButton
        id={typeformId}
        className="typeform-button front-login-signup-btn"
        style={{ 
          fontSize: 20, 
          border: "2px solid white",
          boxShadow: "0 0 10px gold, 0 0 20px gold, 0 0 30px gold" }}
        size={60}
      >
        Sign Up for Beta
      </PopupButton>
    </div>
  );
}

export default TypeformBetaSignupComponent;