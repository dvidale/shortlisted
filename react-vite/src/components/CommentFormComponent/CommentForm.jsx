import { useState} from "react";
import { useDispatch} from "react-redux";

import { addComment, getCommentsByReferral } from "../../redux/comments";

function CommentForm({ shortlist, referralId, user }) {
  const dispatch = useDispatch();


  const [text, setText] = useState("");
  
  
  const submitHandler = (e) => {
    e.preventDefault();

    const commentData = {
      shortlist_id: shortlist.id,
      commenter_id: user.id,
      referral_id: referralId,
      text: text,
    };

    setText('')

    dispatch(addComment(JSON.stringify(commentData))).then(() =>
      dispatch(getCommentsByReferral(referralId))
    );
  };


  return (
    <>
      <form onSubmit={submitHandler}>
        <label htmlFor="comment-box"></label>
        <textarea
          id="comment-text"
          placeholder="Send a message"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <button id="submit-comment" type="submit">
          Send
        </button>
      </form>
    </>
  );
}

export default CommentForm;
