import { useState } from "react";
import { thunkLogin } from "../../redux/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const err ={}

    if(!email.length) err.email ='Email is required'
    if(!password.length) err.password ='Password is required'
    if(password && password.length < 8) err.password = 'Password must be at least 8 characters'

    setErrors(err)

    if(Object.keys(err).length === 0 ){

     const serverResponse = await dispatch(
      thunkLogin({
        email,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
    }
  }

    }
    

  const handleDemoLogin = async (e) => {
    e.preventDefault();

    const serverResponse = await dispatch(
      thunkLogin({
        email: 'aaliyah.walker@example.com',
        password: 'password',
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
    }
  };






  return (
    <>
    <div className="heading-and-form">
      <h1>Log In</h1>

      <form className='login-form' onSubmit={handleSubmit}>
        <div className="login-fields">
          <div className="field-and-error">
        <label>
          Email
          <input className="front-input-field"
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
<div className="error-email">
         <p className="error">{errors.email}</p>
        </div> 
</div>
         <div className="password-and-error">
        <label>
          Password
          <input className="front-input-field"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        <div>
          <p className="error">{errors.password}</p>
        </div>
      </div>
</div>

      <div className="login-buttons">
        <button type="submit">Log In</button>
        
				<button
					className='login-btn'
					onClick={handleDemoLogin}
				>
					Log In Demo User
				</button>
</div>
      </form>
      </div>
    </>
  );
}

export default LoginFormModal;
