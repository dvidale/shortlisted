import "./listings-calendar.css";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { useState, useEffect } from "react";
import { getMyBookings, createBooking } from "../../redux/bookings";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import ServerMessageModal from "../ServerMessageModal/ServerMessageModal";
import DeleteBookingsModal from "./DeleteBookingsModal";

function BookingsPanel({ user_bookings }) {
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();

  const {setModalContent} = useModal()

  const dateDisplay = (date) => {
    return new Intl.DateTimeFormat("en-US", {
      month: "short",
      day: "numeric",
      year: "numeric",
    }).format(new Date(date).setHours(0, 0, 0, 0));
  };

  const [bookingStart, setBookingStart] = useState("");
  const [bookingEnd, setBookingEnd] = useState("");
  const [errors, setErrors] = useState({});



  // VALIDATIONS
  useEffect(() => {
    const err = {};

    function pastCheck(bookingDate) {
      const today = new Date().setHours(0, 0, 0, 0);

      if (bookingDate < today) err.booking_date = "Dates cannot be in the past";
    }

    if (bookingStart) {
      pastCheck(bookingStart);
    }
    if (bookingEnd) {
      pastCheck(bookingEnd);
    }

    setErrors(err);
  }, [bookingStart, bookingEnd]);

  const submitHandler = (e) => {
    e.preventDefault();

    const bookingData = {
      user_id: user.id,

      start_date: bookingStart.toISOString(),
      end_date: bookingEnd.toISOString(),
    };

    dispatch(
      createBooking(JSON.stringify(bookingData))
    ).then( serverError => {
if (serverError) {
      setModalContent(<ServerMessageModal message ={serverError.error} />);
    } else {
      setBookingStart("");
      setBookingEnd("");
       dispatch(getMyBookings(user.id));
    }


    } )

  };


  // *DELETE A BOOKING
const handleDeleteBooking = (bookingId) => {

  setModalContent(
    <DeleteBookingsModal bookingId={bookingId}/>
  );
  
  }
  return (
    <div className="bookings-panel">
      <h2 className="booking-title-btn">My Busy Days</h2>

      <h3 className="start-end-title">Start - End</h3>

      <div className="booking-input">
        <form
          id="add-booking-form"
          className={"booking-form"}
          method="POST"
          onSubmit={submitHandler}
        >
          {/* <label htmlFor="booking-start">
                </label> */}
          {errors.booking_date && (
            <div className="booking-error">{errors.booking_date}</div>
          )}
          <div className="booking-inputs">
            <DatePicker
              dateFormat="MMM dd, yyyy"
              id="booking-start"
              selected={bookingStart}
              onChange={(bookingStart) => setBookingStart(bookingStart)}
            />
          </div>
          -
          {/* <label htmlFor="booking-end">
            </label> */}
          <div className="booking-inputs">
            <DatePicker
              dateFormat="MMM dd, yyyy"
              id="booking-end"
              selected={bookingEnd}
              onChange={(bookingEnd) => setBookingEnd(bookingEnd)}
            />
          </div>
          <button id="submit-booking" type="submit">
            {" "}
            ADD{" "}
          </button>
        </form>
      </div>
<div className="bookings-list-container">

      {user_bookings &&
        Object.keys(user_bookings).length > 0 ? ( <>
        
        {
        Object.values(user_bookings).map((booking) => (
            <>
              <div key={booking.id} className="dates-and-buttons">
                {dateDisplay(booking.start_date)} -{" "}
                {dateDisplay(booking.end_date)}
                <div className="edit-delete-list-btns booking-edit-btns">
                 
                  <button type='button' onClick={ ()=> handleDeleteBooking(booking.id)}>Delete</button>
                </div>
              </div>
          </>
        ))
        }
        </> ):(
          
          <div>No dates blocked on your calendar.    
          </div>
        
        )
      
      }
        </div>
    </div>
  );
}

export default BookingsPanel;
