import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import "../../../src/index.css";
import '../SingleShortlistView/single-shortlist.css'

import { addComment, getCommentThreads } from "../../redux/comments";

function CommentForm({ shortlist, referralIdx, user }) {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const [text, setText] = useState(null);
  const [errors, setErrors] = useState({});
  const [warnings, setWarnings] = useState({});
  const comments = useSelector((state) => state.comments.comments);

  useEffect(() => {
    setErrors({});
    let warn = {};
    if (text) {
      if (text.length === 140)
        warn.text = "Comments have a 140 character limit";
    }
    setWarnings(warn);
  }, [text]);

  useEffect(() => {
    navigate("/");
  }, [comments, navigate]);

  // * Cancel writing anything
  const cancelComment = () => {
    setText("");
  };

  //* Form Submission

  const submitHandler = (e) => {
    e.preventDefault();

    let err = {};
    if (text === null) {
      err.text = "Text is required to send a message.";
    } else {
      if (text.length === 0) err.text = "Text is required to send a message.";
    }

    setErrors(err);

    if (Object.keys(err).length === 0) {
      const commentData = {
        shortlist_id: shortlist.id,
        commenter_id: user.id,
        referral_id: referralIdx,
        text: text,
      };

      dispatch(addComment(JSON.stringify(commentData))).then((serverError) => {
        if (serverError) {
          setErrors(serverError.error);
          console.log("errors.serverError", errors.serverError);
        } else {
          setText("");
          navigate("/");
          dispatch(getCommentThreads(user.id));
        }
      });
    }
  };

  return (
    <>
     <p>{errors.serverError}</p>
      <form className='comment-form' onSubmit={submitHandler}>
        <div>
        <label htmlFor="comment-box"></label>
        <textarea
          id="comment-textarea"
          placeholder="Send a message"
          maxLength={140}
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
               <p className="warning">{warnings.text}</p>
       <p className="warning">{errors.text}</p>
        {text && (
          <button id="cancel-comment" onClick={cancelComment}>
            Cancel
          </button>
        )}
        </div>
        <div>
        <button id="submit-comment" type="submit">
          Send
        </button>
        </div>
      </form>
    </>
  );
}

export default CommentForm;
