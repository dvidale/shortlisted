import { useDispatch } from "react-redux"
import { deleteComment, getCommentsByReferral } from "../../redux/comments"
import { useModal } from "../../context/Modal"
import { useNavigate } from "react-router-dom"


function DeleteCommentModal({commentId, referralId}){

    const navigate = useNavigate()
    const dispatch = useDispatch()
    const { closeModal } = useModal()

    const deleteHandler = () =>{

        dispatch(deleteComment(commentId))
        .then(closeModal)
        .then(navigate('/'))
        .then(dispatch(getCommentsByReferral(referralId)))

    }

    return (
<>
<h2>Are you sure you want to delete this comment?</h2>
<div>
    <button onClick={()=> deleteHandler(commentId)}>Yes (Delete Comment)</button>
    <button onClick={closeModal}>No (Cancel Delete)</button>
</div>
</>

    )
}

export default DeleteCommentModal