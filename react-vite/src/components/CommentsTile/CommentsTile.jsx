import '../../../src/index.css'
import { useEffect } from "react"
import { getCommentThreads } from "../../redux/comments"
import { useDispatch, useSelector } from 'react-redux'
import CommentForm from '../CommentFormComponent/CommentForm'
import DeleteCommentModal from '../DeleteCommentModal/DeleteCommentModal'

import { useModal } from '../../context/Modal'
import CommentEditorModal from '../CommentEditorModal/CommentEditorModal'

function CommentsTile({shortlist, referralIdx}){

    const dispatch = useDispatch()

    const current_thread = useSelector(state => state.comments.comment_threads[referralIdx])
    // if(comments) "good";

    const all_threads = useSelector(state => state.comments.comment_threads)

    const user = useSelector(state => state.session.user)

    const {setModalContent} = useModal();

useEffect( ()=>{

dispatch(getCommentThreads(user.id))
 

},[dispatch, all_threads, user])

const commentEditor = (currentComment, commentId) =>{

setModalContent(<CommentEditorModal currentCommentText={currentComment} commentId={commentId}/>) 

}

const deleteCommentModal = (commentId) =>{

    setModalContent(<DeleteCommentModal commentId={commentId}/>)
}


    return (
        <>{current_thread && Object.values(current_thread).length > 0 && Object.values(current_thread).map( comment =>{
            return(
                <div key={comment.id}>
                    <div className="comment_name">
                        {comment.commenter_name}
                    </div>
                    <div className="comment-text">
                       
                        {comment.text}
                    </div>
                    <button onClick={()=> commentEditor(comment.text, comment.id)}>Edit</button>

                    <button onClick={()=> deleteCommentModal(comment.id)} >Delete</button>
                </div>
            )
        })}

       <CommentForm shortlist={shortlist} referralIdx={referralIdx} user={user}/>
       
        </>
    )
}

export default CommentsTile