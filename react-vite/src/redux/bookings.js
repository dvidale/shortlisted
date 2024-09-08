const GET_MY_BOOKINGS = '/bookings/GET_MY_BOOKINGS'

export const getAllMyBookings = (data) =>{

    return {
        type:GET_MY_BOOKINGS,
        payload: data
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
        default:
            return state;


    }
}

export default bookingsReducer;