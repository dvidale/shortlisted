import { useDispatch } from 'react-redux'
import { useModal } from '../../context/Modal'
import { useNavigate } from 'react-router-dom'

function EditShortlistModal({title, setTitle, description, setDescription, shortlistId}){

    const dispatch = useDispatch()
    const navigate = useNavigate()
    const { closeModal } = useModal()


    const submitHandler = (e) =>{
        e.preventDefault()

        const err = {};
    
    if (title === '' || title.length === 0) err.title = "A title is required";

    setErrors(err);

    if (Object.keys(err).length === 0) {
      editSwitch();

      const formData = {
        title,
        description,
      };

      const shortlistId = shortlist.id;

      dispatch(updateShortlist(shortlistId, JSON.stringify(formData)));
      // TODO: Add server response modal
    }


    }
return (
    <>
    Editor
    <form id="edit-shortlist-modal" onSubmit={submitHandler}>
        <label htmlFor="edit-shortlist-modal-title">
            Title:
            <input id='edit-shortlist-modal-title' type='text'></input>
        </label>
        <label htmlFor='edit-shortlist-modal-desc'>
            Description:
            <input id='edit-shortlist-modal-desc' type='text'></input>
        </label>
        <button id='mobile-shortlist-update' type="submit">Update</button>
    </form>
    
    </>
)


}


export default EditShortlistModal