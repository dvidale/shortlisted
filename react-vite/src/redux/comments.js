const GET_COMMENTS_BY_REFERRAL = '/comments/GET_COMMENTS_BY_REFERRAL'

export const getAllCommentsByReferral = (data)=>{
    return {
        type: GET_COMMENTS_BY_REFERRAL,
        payload:data
    }
}



/*-------
THUNKS
-------*/

export const getCommentsByReferral = (id) => async (dispatch) => {

const url = `/api/comments/${id}`

const response = await fetch(url)

if(response.ok){

    const data = await response.json()
    dispatch(getAllCommentsByReferral(data))
    
    return data

}
}


/*-----------------
        REDUCER
-------------------*/

const initialState = { comments: [] }

const commentsReducer = (state = initialState, action ) =>{
    switch(action.type){

        case GET_COMMENTS_BY_REFERRAL:{
            const newState = {...state}
            newState['comments'] = action.payload
            return newState
        }
        default:
            return state

    }

}


export default commentsReducer;
