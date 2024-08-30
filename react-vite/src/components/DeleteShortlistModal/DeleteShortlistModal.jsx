import { useDispatch } from "react-redux"
import { deleteShortlist, fetchShortlists} from "../../redux/shortlists"
import { useModal } from "../../context/Modal"
import { useNavigate } from 'react-router-dom'


function DeleteShortlistModal({ userId,shortlist}){

const navigate = useNavigate()
const dispatch = useDispatch()
const {closeModal} = useModal();

// !BUG - get 500 error when you click delete on live site
    const deleteHandler= (id) =>{

        dispatch(deleteShortlist(id))
        .then(closeModal)
        .then(navigate('/'))
        .then(dispatch(fetchShortlists(userId)))
        
    
        
    }

return (
<>
<h2>Are you sure you want to delete this shortlist?</h2>
<div>
    <button onClick={()=> deleteHandler(shortlist.id)}>Yes (Delete Shortlist)</button>
    <button onClick={closeModal}>No (Cancel Delete)</button>
</div>
</>

)

}


export default DeleteShortlistModal