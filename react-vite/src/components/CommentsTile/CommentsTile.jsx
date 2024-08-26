import { useEffect } from "react"
import { getCommentsByReferral } from "../../redux/comments"
import { useDispatch, useSelector } from 'react-redux'

function CommentsTile({id}){

    const dispatch = useDispatch()


    const comments = useSelector(state => state.comments.comments)

    console.log(">>>>comments loading:", comments);


useEffect( ()=>{

dispatch(getCommentsByReferral(id))


},[dispatch, id])



    return (
        <>

        
        </>
    )
}

export default CommentsTile