import "../../../src/index.css";
import "../SingleShortlistView/single-shortlist.css";
// import { useEffect } from "react";
// import { getCommentThreads } from "../../redux/comments";
import { useSelector } from "react-redux";
import CommentForm from "../CommentFormComponent/CommentForm";
import DeleteCommentModal from "../DeleteCommentModal/DeleteCommentModal";
import { VscAccount } from "react-icons/vsc";
import { useModal } from "../../context/Modal";
import CommentEditorModal from "../CommentEditorModal/CommentEditorModal";

function CommentsTile({ shortlist, referralIdx }) {
  const current_thread = useSelector(
    (state) => state.comments.comment_threads[referralIdx]
  );

  const user = useSelector((state) => state.session.user);

  const { setModalContent } = useModal();

  const commentEditor = (currentComment, commentId) => {
    setModalContent(
      <CommentEditorModal
        currentCommentText={currentComment}
        commentId={commentId}
      />
    );
  };

  const deleteCommentModal = (commentId) => {
    setModalContent(<DeleteCommentModal commentId={commentId} />);
  };

  let current_thread_sorted;

  if (current_thread) {
    current_thread_sorted = Object.values(current_thread).sort(
      (comment) => comment["createdAt"]
    );
  }

  return (
    <>
      {current_thread &&
        Object.values(current_thread_sorted).length > 0 &&
        Object.values(current_thread_sorted).map((comment) => {
          return (
            <div key={comment.id} className="comment-bubble-and-avatar">
              <div key={`${comment.id}-name`} className="commenter_name">
                {comment.commenter_name !== user.first_name && (
                  <span key={`${comment.id}-avatar`}>
                    <VscAccount />
                    {comment.commenter_name}
                  </span>
                )}
              </div>

              <div key={`${comment.id}-text`} className="comment-text">
                <span key={`${comment.id}-bubble`} className="message-bubble">{comment.text}</span>
              </div>

              <div key={`${comment.id}-edit-delete`} className="edit-delete-list-btns">
                {comment.commenter_id === user.id && (
                  <button key={`${comment.id}-edit`}
                    onClick={() => commentEditor(comment.text, comment.id)}
                  >
                    Edit
                  </button>
                )}
                {comment.commenter_id === user.id && (
                  <button key={`${comment.id}-delete`} onClick={() => deleteCommentModal(comment.id)}>
                    Delete
                  </button>
                )}
                {comment.commenter_id === user.id && (
                  <div key={`${comment.id}-you-icon`} className="you_icon">
                    <VscAccount />
                    You
                  </div>
                )}
              </div>
            </div>
          );
        })}

      <div className="comment-form-container">
        <CommentForm
          shortlist={shortlist}
          referralIdx={referralIdx}
          user={user}
        />
      </div>
    </>
  );
}

export default CommentsTile;
