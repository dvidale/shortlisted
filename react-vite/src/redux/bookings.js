const GET_MY_BOOKINGS = '/bookings/GET_MY_BOOKINGS'
const CREATE_A_BOOKING = '/bookings/CREATE_A_BOOKING'
const DELETE_A_BOOKING = '/bookings/DELETE_A_BOOKING'

export const getAllMyBookings = (data) =>{

    return {
        type:GET_MY_BOOKINGS,
        payload: data
    }
}

export const createABooking = (data) => {

    return {
        type: CREATE_A_BOOKING,
        payload: data
    }
}

export const deleteABooking = (id) => {

    return {
        type: DELETE_A_BOOKING,
        payload: id
    }
}


/*---------------------------
        THUNKS
----------------------*/

export const getMyBookings = (userId) => async (dispatch) => {

    const url = `/api/bookings/my-bookings/${userId}`
    
    const response = await fetch(url)

    if(response.ok){

        const data = await response.json()
        dispatch(getAllMyBookings(data))
    }else{
        const serverError = await response.json()

        return serverError;
    }
}

export const createBooking = (bookingData) => async (dispatch) => {

    const url = `/api/bookings/new`

    const method = 'POST'

    const headers = {'Content-Type': 'application/json'}
  
    const body = bookingData;

    const options = {method, headers, body}

    const response = await fetch(url, options);



    if(response.ok){

        const data = await response.json()

        dispatch(createABooking(data))

    }else{

        const serverError = await response.json()
        console.log("serverError from new Booking", serverError);
        return serverError;
    }
}

export const deleteBooking = (id) => async(dispatch) =>{

    const url = `/api/bookings/${id}`
    const method = 'DELETE'

    const options = {method}

    const response = await fetch(url, options);

    if(response.ok){

        const data = await response.json()
        dispatch(deleteABooking(data['id']))

    }else{

        const serverError = await response.json()
        console.log("serverError from new Booking", serverError);
        return serverError;
    }




}

/*--------------------------
         REDUCER
------------------------------*/

const intitalState = { user_bookings:{} }

const bookingsReducer = (state = intitalState, action) =>{
    switch(action.type){

        case GET_MY_BOOKINGS:{
            const newState = {...state}
            action.payload.forEach( booking =>{
                newState.user_bookings[booking.id] = booking
            })
            return newState;
        }
        case CREATE_A_BOOKING:{
            const newState = {...state }
            const newBooking = action.payload;
            newState.user_bookings[newBooking.id] = newBooking;
            return newState;
        }
        case DELETE_A_BOOKING:{
            const newState = {...state}
            delete newState.user_bookings[action.payload]
            return newState
        }
        default:
            return state;


    }
}

export default bookingsReducer;