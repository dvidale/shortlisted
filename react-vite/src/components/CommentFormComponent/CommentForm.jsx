import { useEffect, useState} from "react";
import { useDispatch, useSelector} from "react-redux";
import { useNavigate } from "react-router-dom";
import '../../../src/index.css'

import { addComment, getCommentThreads } from "../../redux/comments";

function CommentForm({ shortlist, referralIdx, user }) {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const [text, setText] = useState(null);
  const [errors, setErrors] = useState({})
  const comments = useSelector( state => state.comments.comments)

  useEffect(()=>{
    let err = {}
if(text){
  if(text.length === 140) err.text = "Comments have a 140 character limit"
}
setErrors(err)
  },[text])

  useEffect(()=>{
    navigate('/')
  },[comments, navigate])
  
  const submitHandler = (e) => {
    e.preventDefault();

    let err = {}
    if(text === null){
        err.text = "Text is required to send this message."
    }else{
      if(text.length === 0) err.text = "Text is required to send this message."
    }
    
    
    setErrors(err)

    if(Object.keys(err).length === 0){

      const commentData = {
        shortlist_id: shortlist.id,
        commenter_id: user.id,
        referral_id: referralIdx,
        text: text,
      };
      
      
      
      dispatch(addComment(JSON.stringify(commentData)))
      .then(setText(''))
      .then(navigate('/'))
      .then(dispatch(getCommentThreads(user.id))
    );
  }
  };


  return (
    <>
      <form onSubmit={submitHandler}>
        <label htmlFor="comment-box"></label>
        <textarea
          id="comment-text"
          placeholder="Send a message"
          maxLength={140}
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        {errors.text && <p className="error">{errors.text}</p>}
        <button id="submit-comment" type="submit">
          Send
        </button>
      </form>
    </>
  );
}

export default CommentForm;
