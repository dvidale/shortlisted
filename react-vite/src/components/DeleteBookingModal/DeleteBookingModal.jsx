import { useDispatch, useSelector } from "react-redux"
import { getMyBookings } from "../../redux/bookings"
import { useModal } from "../../context/Modal"




function DeleteBookingModal({id}){

const dispatch = useDispatch();
const { closeModal } = useModal();

const userId = useSelector(state => state.session.user.id)

const deleteHandler = () =>{

    
}

    return(
        <>
        
        </>
    )

}


export default DeleteBookingModal


