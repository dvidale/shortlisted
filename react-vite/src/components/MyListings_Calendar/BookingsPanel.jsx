import './listings-calendar.css'

function BookingsPanel({user_bookings}){

    const dateDisplay = (date) => {
    return new Intl.DateTimeFormat('en-US',{
        month: 'short',
        day: 'numeric',
        year: 'numeric'
    }).format(new Date(date))


    } 


    return(
        <>
        <h3>Start - End</h3>
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