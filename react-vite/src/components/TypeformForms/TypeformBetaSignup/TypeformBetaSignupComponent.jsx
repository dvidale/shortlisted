import { PopupButton } from "@typeform/embed-react";

function TypeformBetaSignupComponent({typeformId}) {
  return (
    <div className="typeform-beta-signup-component">
      <PopupButton
        id={typeformId}
        className="typeform-button"
        style={{ fontSize: 20 }}
        size={60}
      >
        Sign Up for Beta
      </PopupButton>
    </div>
  );
}

export default TypeformBetaSignupComponent;