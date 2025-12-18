import "./footer.css";
import { FaGithub } from "react-icons/fa";
import { FaLinkedin } from "react-icons/fa";
import HubspotBetaMailingListComponent from "../HubspotForms/HubspotBetaMailingListComponent";

function Footer() {
  return (
    <>
      <div className="footer-wrapper">
        {/* <p className='footer'>Sign up for updates on Shortlisted at <a href="https://deandrevidale.com/shortlisted">DeAndreVidale.com/shortlisted</a>
        </p> */}
        <div className="footer">
          <div >
            Join the Beta Waitlist
            <div id="beta-signup-form">
              <HubspotBetaMailingListComponent
                portalId="44563358"
                formId="83586d74-fd5f-4874-a100-4deaecf185a4"
              />
            </div>
          </div>
          {/* <a href="https://github.com/dvidale">
            Github <FaGithub />
          </a>
          <a href="https://www.linkedin.com/in/deandrevidale">
            LinkedIn <FaLinkedin />
          </a> */}
        </div>
      </div>
    </>
  );
}

export default Footer;
