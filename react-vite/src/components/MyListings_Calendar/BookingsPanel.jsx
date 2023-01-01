import './listings-calendar.css'
import { FaPlusCircle } from "react-icons/fa";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { useState } from 'react';

function BookingsPanel({user_bookings}){

    const dateDisplay = (date) => {
    return new Intl.DateTimeFormat('en-US',{
        month: 'short',
        day: 'numeric',
        year: 'numeric'
    }).format(new Date(date))

} 

const [bookingStart, setBookingStart] = useState('')
const [bookingEnd, setBookingEnd] = useState('')

const submitHandler = (e) =>{

    e.preventDefault();

}
    return(
        <>
      
    <h2 className='booking-title-btn'>My Busy Days</h2> 
  
        <h3 className="start-end-title">Start - End</h3>
    <div className='booking-input' > 
    <form id="add-booking-form" className={'show-booking-form'} method='POST' onSubmit={submitHandler}>
        <label htmlFor="booking-start">
            <DatePicker id='booking-start' selected={bookingStart} onChange={ bookingStart => setBookingStart(bookingStart)}/>
            </label>
            <label htmlFor="booking-end">
            <DatePicker id='booking-end' selected={bookingEnd} onChange={ bookingEnd => setBookingEnd(bookingEnd)}  />
            </label>
    <button id="submit-booking" type='submit' ><FaPlusCircle /></button>
    </form>
            </div >
        {user_bookings && Object.keys(user_bookings).length > 0 && Object.values(user_bookings).map( booking => (
        <>
        <div className='cal-box'>
        <div key={booking.id} className="dates-and-buttons">{dateDisplay(booking.start_date) } - {dateDisplay(booking.end_date)}
            <div className="edit-delete-list-btns">


            <button>Edit</button>
            <button>Delete</button>
            </div>
        </div>
        </div>
        </>
    ))}
        
        </>
    )
}

export default BookingsPanel