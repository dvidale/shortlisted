import { useDispatch } from "react-redux"
import { deleteShortlist, 
    fetchShortlists
} from "../../redux/shortlists"
import { useModal } from "../../context/Modal"
import { useNavigate } from 'react-router-dom'


function DeleteShortlistModal({
    userId,shortlistId

}){

const navigate = useNavigate()
const dispatch = useDispatch()
const {closeModal} = useModal();




    const deleteHandler= (id) =>{
       
        dispatch(deleteShortlist(id))
        .then( data => {if(data) console.log("Response to DELETE request:", data)})
        .then(closeModal)
        .then(()=> dispatch(fetchShortlists(userId)))
        .then(()=> navigate('/'))
      
    // !DO NOT try to trigger the selection of another shortlist from here. It causes the delete to stall
        
    }

return (
<>
<h2>Are you sure you want to delete this shortlist?</h2>
<div>
    <button onClick={()=> deleteHandler(shortlistId)}>Yes (Delete Shortlist)</button>
    <button onClick={closeModal}>No (Cancel Delete)</button>
</div>
</>

)

}


export default DeleteShortlistModal