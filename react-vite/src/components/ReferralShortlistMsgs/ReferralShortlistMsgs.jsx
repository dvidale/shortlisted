
import { useSelector } from "react-redux";
import CommentEditorModal from "../CommentEditorModal/CommentEditorModal";

import DeleteCommentModal from "../DeleteCommentModal/DeleteCommentModal";
import { useModal } from "../../context/Modal";
import '../SingleShortlistView/single-shortlist.css'

function ReferralShortlistMsgs({referral}){

    const user = useSelector(state => state.session.user)

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




    const referral_thread_sorted = Object.values(referral.comment_thread).sort( message => Math.max(message["createdAt"], message["updatedAt"]) )




    return(
        <>
        
        {
            Object.values(referral_thread_sorted).map(comment => {
                return(
                    <div key={comment.id} className="comment-bubble-and-avatar">
                    <div key={`${comment.id}-name`} className="commenter_name">
                      {comment.commenter_name !== user.first_name && (
                        <span key={`${comment.id}-avatar-span`}>
                          <img className="user-avatar" src={referral.createdby_photo}/>
                          {comment.commenter_name}
                        </span>
                      )}
                    </div>
      
                    <div key={`${comment.id}-text`} className="comment-text">
                      <span key={`${comment.id}-bubble`} className={comment.commenter_id === user.id ? "message-bubble-right" : "message-bubble-left"}>{comment.text}</span>
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
                        <div key={`${comment.id}-you-icon-div`} className="you_icon">
                            <img className="user-avatar" src={user.profile_img_url}/>
                          You
                        </div>
                      )}
                    </div>
                  </div>
                )



            })



        }
        
        
        
        </>



    )


}


export default ReferralShortlistMsgs