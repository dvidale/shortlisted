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

    if(Object.keys(errors).length === 0){

      
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
      <h1>Sign Up</h1>
    < div className="signup-modal-container">
    
      {errors.server && <p>{errors.server}</p>}
      <form onSubmit={handleSubmit}>
        <div>  
      <label>
          First Name
          <input
            type="text"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            required
          />
        </label>
        {errors.firstName && <p className="error">{errors.firstName}</p>}
        </div>

        <div>
        <label>
          Last Name
          <input
            type="text"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            required
          />
        </label>
        {errors.lastName && <p className="error">{errors.lastName}</p>}
        </div>

        <div>
        <label>
          Email
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        {errors.email && <p className="error">{errors.email}</p>}
</div>


<div>
        <label>
          Username
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </label>
        {errors.username && <p className="error">{errors.username}</p>}

        </div>

        <div>
        <label>
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        {errors.password && <p className="error">{errors.password}</p>}

        </div>

        <div>
        <label>
          Confirm Password
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
          />
        </label>
        {errors.confirmPassword && <p className="error">{errors.confirmPassword}</p>}
        </div>
        <div>
        <button type="submit">Sign Up</button>
        </div>
      </form>
    </div>
    </>
  );
}

export default SignupFormModal;
