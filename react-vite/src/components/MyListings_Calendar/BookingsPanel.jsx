

function BookingsPanel({user_bookings}){



    return(
        <>
        {user_bookings && Object.keys(user_bookings).length > 0 && Object.values(user_bookings).map( booking => (
        <>
        <div key={booking.id}>{booking.start_date} - {booking.end_date}</div>
        </>
    ))}
        
        </>
    )
}

export default BookingsPanel