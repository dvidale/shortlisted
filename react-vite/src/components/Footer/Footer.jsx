import { FaGithub } from 'react-icons/fa';
import { FaLinkedin } from 'react-icons/fa';



function Footer(){

    return (
        <>
        <p className='footer'>Shortlisted is an application developed by DeAndré Vidale.
        </p>
        <div className='footer'>

        <a href='https://github.com/dvidale/shortlisted'>

            Github <FaGithub />
        </a>
        <a href='https://www.linkedin.com/in/deandrevidale'>
            LinkedIn <FaLinkedin /> 
        </a>
        </div>
        </>
    )
}


export default Footer