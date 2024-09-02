import { useDispatch, useSelector } from "react-redux"
import { deleteComment, getCommentThreads} from "../../redux/comments"
import { useModal } from "../../context/Modal"
import { useNavigate } from "react-router-dom"


function DeleteCommentModal({commentId}){

    const navigate = useNavigate()
    const dispatch = useDispatch()
    const { closeModal } = useModal()

    const userId = useSelector(state => state.session.user.id)
    const deleteHandler = () =>{

        dispatch(deleteComment(commentId))
        .then(closeModal)
        .then(navigate('/'))
        .then(dispatch(getCommentThreads(userId)))

    }

    return (
<>
<div className="delete-comment-modal">
<h2>Are you sure you want to delete this comment?</h2>
<div className="comment-edit-delete-btns btn-hover">
    <button className="modal-delete-btn" onClick={()=> deleteHandler(commentId)}>Yes (Delete Comment)</button>
    <button onClick={closeModal}>No (Cancel Delete)</button>
</div>
</div>

</>

    )
}

export default DeleteCommentModal