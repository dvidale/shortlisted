import { useDispatch } from "react-redux"
import {useModal} from '../../context/Modal'
import { useNavigate } from "react-router-dom"
import { deleteReferral } from "../../redux/shortlists"
import { fetchShortlists } from "../../redux/shortlists"

function DeleteReferralModal({idx, fullName, userId}){
    const navigate = useNavigate()
    const dispatch = useDispatch()
    const {closeModal} = useModal();
    
    const deleteHandler = () =>{

        dispatch(deleteReferral(idx))
        .then(closeModal)
        .then(navigate('/'))
        .then(dispatch(fetchShortlists(userId)))
    }


    return(
<>
<h2>Are you sure you want to remove {`"${fullName}"`} from the Shortlist?</h2>
<p>This change cannot be undone.</p>
<div>
    <button onClick={()=> deleteHandler(idx)}>Yes (Remove from Shortlist)</button>
    <button onClick={closeModal}>No (Cancel)</button>
</div>



</>

    )
}

export default DeleteReferralModal