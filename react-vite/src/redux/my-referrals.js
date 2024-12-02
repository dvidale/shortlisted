const GET_MY_REFERRALS = '/referrals/GET_MY_REFERRALS'

export const getMyReferrals = (data) =>{

    return {
        type: GET_MY_REFERRALS,
        payload: data
    }

}

/*-------------------
       THUNKS
---------------------*/

export const getReferrals = (id) => async (dispatch) =>{

    const url = `/api/shortlists/my-referrals/${id}`
    
    const response = await fetch(url);

    if(response.ok){
        const data = await response.json()

        dispatch(getMyReferrals(data['referral_threads']))
    }
    else if(response.status === 404){
        const noMessages = await response.json()

        return noMessages
    }
    else{
        const serverError = await response.json()

        return serverError
    }
    


}

/*-------------------
      REDUCER
---------------------*/

const initialState = { referral_details:{}  }

const myReferralsReducer = (state = initialState, action) =>{
    switch(action.type){
        case GET_MY_REFERRALS:{
            const newState = {...state}
            action.payload.forEach( thread =>{
                newState.referral_details[thread['shortlist_id']] = thread
            })

            return newState;
        }
        default:
            return state;
    }
    
}

export default myReferralsReducer;