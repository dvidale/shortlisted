import { useDispatch } from 'react-redux'
import { useModal } from '../../context/Modal'
import { useNavigate } from 'react-router-dom'
import { updateShortlist } from '../../redux/shortlists'

function EditShortlistModal({title, setTitle, description, setDescription, shortlistId}){

    const dispatch = useDispatch()
    // const navigate = useNavigate()
    // const { closeModal } = useModal()


    const submitHandler = (e) =>{
        e.preventDefault()

        const err = {};
    
    if (title === '' || title.length === 0) err.title = "A title is required";



    if (Object.keys(err).length === 0) {
      

      const formData = {
        title,
        description,
      };

      

      dispatch(updateShortlist(shortlistId, JSON.stringify(formData)));
      // TODO: Add server response modal
    }


    }
return (
    <>
    
    <form id="edit-shortlist-modal" onSubmit={submitHandler}>
        <label htmlFor="edit-shortlist-modal-title">
            Title:
            <input id='edit-shortlist-modal-title' type='text'  
            value={title}
            maxLength={40}
            onChange={(e) => setTitle(e.target.value)}
            />
        </label>
        <label htmlFor='edit-shortlist-modal-desc'>
            Description:
            <textarea 
            id='edit-shortlist-modal-desc' 
            type='text'
            value={description}
            onChange={(e)=> setDescription(e.target.value)}
            ></textarea>
        </label>
        <button id='mobile-shortlist-update' type="submit">Update</button>
    </form>
    
    </>
)


}


export default EditShortlistModal