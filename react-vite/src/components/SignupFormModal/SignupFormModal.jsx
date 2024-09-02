import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkSignup } from "../../redux/session";
import '../../../src/index.css'
import "./SignupForm.css";

function SignupFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName ] = useState('');
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();

    let err = {}

    
          
    if(firstName.length < 2) err.firstName = "First name must be at least two characters"
    if(lastName.length < 2) err.lastName = "Last name must be at least two characters"
    if(email.length < 6) err.email = "Email must be at least 6 characters"
    if(!email.includes("@")) err.email = "Must be a vaild email address"
    if(username.length < 6) err.username = "Username must be at least six characters"
    if(password.length < 8) err.password = "Password must be at least 8 characters"
    
    if (password !== confirmPassword) err.confirmPassword = "Confirm Password field must be the same as the Password field"

    setErrors(err)

    if(Object.keys(err).length === 0){

      
      const serverResponse = await dispatch(
        thunkSignup({
          first_name: firstName,
          last_name: lastName,
          email,
          username,
          password,
          confirmPassword
        })
      );
      
      if (serverResponse) {
        setErrors(serverResponse);
      } else {
        closeModal();
      }
    }
    
  }
  return (
    <>
    < div className="signup-modal-container">
      <h1>Sign Up</h1>
   
     <p className="error">{errors.server}</p>

      <form onSubmit={handleSubmit}>
    
        <div className='signup-label-field'>   
          <div>First Name</div>

      <label htmlFor="firstName">
       
          <input
          className="field"
            type="text"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            required
          />
        </label>
          </div>
     <p className="two-line-error">{errors.firstName}</p>
      

        <div className='signup-label-field'>  
           <div>Last Name </div>
        <label htmlFor="lastName">
      
          <input
            type="text"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            required
          />
        </label>
       
        </div>
  <p className="two-line-error">{errors.lastName}</p>

<div className="label-field-error">
        <div className='signup-label-field'>    
             <div>Email    </div>
        <label htmlFor="email">
     
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
       
</div>
 <p className="two-line-error">{errors.email}</p>
</div>
<div className='signup-label-field'> 
   <div>Username </div>
        <label htmlFor="username">
        
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </label>
       
        </div>
 <p className="two-line-error">{errors.username}</p>

        <div className='signup-label-field'> <div>Password    </div>
        <label htmlFor="password">
          
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
       

        </div>
 <p className="error">{errors.password}</p>


        <div className='signup-label-field'>   
        <div>Confirm Password </div>
        <label htmlFor="confirm">
       
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
          />
        </label>
    
        </div>
  <p className="error">{errors.confirmPassword}</p>

        <div className='signup-button'>


        <button type="submit">Sign Up</button>
        </div>
      </form>
    </div>
    </>
  );
}

export default SignupFormModal;
