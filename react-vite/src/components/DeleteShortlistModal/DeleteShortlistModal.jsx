import { useDispatch } from "react-redux"
import { deleteShortlist, 
    fetchShortlists
} from "../../redux/shortlists"
import { useModal } from "../../context/Modal"
import { useNavigate } from 'react-router-dom'
import { clearDeletedThreads } from "../../redux/comments"
import ServerMessageModal from "../ServerMessageModal/ServerMessageModal"


function DeleteShortlistModal({ userId,shortlistId }){

const navigate = useNavigate()
const dispatch = useDispatch()
const {setModalContent, closeModal} = useModal();

 


    const deleteHandler= (id) =>{
       
        dispatch(deleteShortlist(id))
        .then((data)=>{ 
            if(data.error){
            setModalContent(<ServerMessageModal message={data.error}/>)
        }else{
            if(data[1].message){
                setModalContent(<ServerMessageModal message={data[1].message}/>)}
                dispatch(clearDeletedThreads(data[0]))
        }
        })
        .then(closeModal)
        .then(()=> dispatch(fetchShortlists(userId)))
        .then(()=> navigate('/'))
      
    // !DO NOT try to trigger the selection of another shortlist from here. It causes the delete to stall
        
    }

return (
<>
<div className="delete-comment-modal"> 
<h2>Are you sure you want to delete this shortlist?</h2>
<div>
    <button className="modal-delete-btn" onClick={()=> deleteHandler(shortlistId)}>Yes (Delete Shortlist)</button>
    <button onClick={closeModal}>No (Cancel Delete)</button>
</div>

</div>
</>

)

}


export default DeleteShortlistModal