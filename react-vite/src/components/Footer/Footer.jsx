import { FaGithub } from 'react-icons/fa';
import { FaLinkedin } from 'react-icons/fa';



function Footer(){

    return (
        <>
        <div className='footer-wrapper'>

        <p className='footer'>Sign up for updates on Shortlisted at <a href="https://deandrevidale.com/shortlisted">DeAndreVidale.com/shortlisted</a>
        </p>
        <div className='footer'>

        <a href='https://github.com/dvidale'>

            Github <FaGithub />
        </a>
        <a href='https://www.linkedin.com/in/deandrevidale'>
            LinkedIn <FaLinkedin /> 
        </a>
        </div>
        </div>
        </>
    )
}


export default Footer