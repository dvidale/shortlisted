import { useState } from 'react'
import { useDispatch } from 'react-redux'
import { editComment } from '../../redux/comments'
import { useModal } from '../../context/Modal'
import { useNavigate } from 'react-router-dom'

function CommentEditorModal({currentCommentText, commentId}){

    const [ commentUpdate, setCommentUpdate ] = useState(currentCommentText)

    const dispatch = useDispatch()
    const navigate = useNavigate()
    const { closeModal } = useModal()

    const submitHandler =(e)=>{

        e.preventDefault()

        const commentData = {
            text: commentUpdate
                }
        
            dispatch(editComment(commentId, JSON.stringify(commentData))).then(closeModal).then(navigate('/'))

    }

    return(

        <form id='edit-comment-box' onSubmit={submitHandler}>
        <label htmlFor='edit-comment-form'>Edit Your Comment</label>
        <textarea id='edit-comment-form' value={commentUpdate} 
        onChange={(e)=> setCommentUpdate(e.target.value)}/>
        <button type="submit">Submit</button>
    </form>



    )
}

export default CommentEditorModal