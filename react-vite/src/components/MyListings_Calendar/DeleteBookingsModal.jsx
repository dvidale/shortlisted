import { useModal } from "../../context/Modal"
import { useDispatch, useSelector } from "react-redux"
import { deleteBooking, getMyBookings } from "../../redux/bookings"
import ServerMessageModal from "../ServerMessageModal/ServerMessageModal"



function DeleteBookingsModal({bookingId}){

const { setModalContent, closeModal } = useModal()
const dispatch = useDispatch()

const userId = useSelector(state => state.session.user.id)

const deleteHandler = () => {

    dispatch(deleteBooking(bookingId))
    .then((serverError)=> {
        if(serverError){
            closeModal;
            setModalContent(< ServerMessageModal message={serverError.error}/>)
        }
    })
    .then(closeModal)
    .then(dispatch(getMyBookings(userId)))




}

    return(
        <>
        <div className="delete-booking-modal">
<h2>Are you sure you want to delete this booking?</h2>
<div className="comment-edit-delete-btns btn-hover">
    <button className="modal-delete-btn" onClick={()=> deleteHandler(bookingId)}>Yes (Delete Booking)</button>
    <button onClick={closeModal}>No (Cancel Delete)</button>
</div>
</div>
        </>
    )
}


export default DeleteBookingsModal