import { useEffect } from "react";


function HubspotBetaMailingListComponent({portalId, formId}) {

  
  useEffect(() => {
    const script = document.createElement("script");
    script.src = "https://js.hsforms.net/forms/embed/v2.js";
    script.async = true;

    script.onload = () => {
      if (window.hbspt) {
        window.hbspt.forms.create({
          region: "na1",
          portalId: portalId,
          formId: formId,
          target: "#hubspot-beta-mailing-list-form",
        });
      }
    };

    document.body.appendChild(script);

    return () => {
      document.body.removeChild(script);
    };
  }, []);


  return <div id="hubspot-beta-mailing-list-form"></div>;
}

export default HubspotBetaMailingListComponent;