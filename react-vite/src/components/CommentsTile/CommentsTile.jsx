import '../../../src/index.css'
import { useEffect } from "react"
import { getCommentsByReferral } from "../../redux/comments"
import { useDispatch, useSelector } from 'react-redux'
import CommentForm from '../CommentFormComponent/CommentForm'
import DeleteCommentModal from '../DeleteCommentModal/DeleteCommentModal'

import { useModal } from '../../context/Modal'
import CommentEditorModal from '../CommentEditorModal/CommentEditorModal'

function CommentsTile({shortlist, id}){

    const dispatch = useDispatch()

    const comments = useSelector(state => state.comments.comments)

    const user = useSelector(state => state.session.user)

    const {setModalContent} = useModal();

useEffect( ()=>{

dispatch(getCommentsByReferral(id))
 

},[dispatch, id])

const commentEditor = (currentComment, commentId) =>{

setModalContent(<CommentEditorModal currentCommentText={currentComment} commentId={commentId}/>) 

}

const deleteCommentModal = (commentId) =>{

    setModalContent(<DeleteCommentModal referralId={id}commentId={commentId}/>)
}


    return (
        <>{Object.values(comments).length > 0 && Object.values(comments).map( comment =>{
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

       <CommentForm shortlist={shortlist} referralId={id} user={user}/>
       
        </>
    )
}

export default CommentsTile