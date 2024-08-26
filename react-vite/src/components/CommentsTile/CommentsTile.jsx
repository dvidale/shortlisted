import '../../../src/index.css'
import { useEffect } from "react"
import { getCommentsByReferral } from "../../redux/comments"
import { useDispatch, useSelector } from 'react-redux'

function CommentsTile({id}){

    const dispatch = useDispatch()


    const comments = useSelector(state => state.comments.comments)

    


useEffect( ()=>{

dispatch(getCommentsByReferral(id))


},[dispatch, id])



    return (
        <>{comments.length > 0 && comments.map( comment =>{
            return(
                <div key={comment.id}>
                    <div className="comment_name">
                        {comment.commenter_name}
                    </div>
                    <div className="comment-text">
                        {comment.text}
                    </div>
                </div>
            )
        })}

        
        </>
    )
}

export default CommentsTile