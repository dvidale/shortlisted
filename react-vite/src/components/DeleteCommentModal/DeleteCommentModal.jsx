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
<h2>Are you sure you want to delete this comment?</h2>
<div>
    <button onClick={()=> deleteHandler(commentId)}>Yes (Delete Comment)</button>
    <button onClick={closeModal}>No (Cancel Delete)</button>
</div>
</>

    )
}

export default DeleteCommentModal