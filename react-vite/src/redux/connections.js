const CONNECTION_RESULTS = '/connections/CONNECTION_RESULTS'



export const returnConnectionResults = (data) => {

    return{
        type: CONNECTION_RESULTS,
        payload:data
    }
}


/*-------------------
       THUNKS
---------------------*/


export const searchConnections = (userId, formData) => async (dispatch) =>{

    const url = `/api/connections/${userId}`
    const method = 'POST'
    const headers = { 'Content-Type': 'application/json' };
    const body = formData
    console.log(">>>> form_data in thunk:", formData);
    const options = {method, headers, body}

    const response = await fetch(url,options)

    if(response.ok){
        const data = await response.json()
        
        dispatch(returnConnectionResults(data))
        console.log(">>>> POST route return data in thunk:", data);
        return data
    }
}

/*-------------------
      REDUCER
---------------------*/

const initialState = { parameters: {}, results: []}

const connectionsReducer = (state = initialState, action) =>{
    switch(action.type){
        
        case CONNECTION_RESULTS:{
            // const params = {...action.payload[1] }
            const newState = {...state}
            action.payload.forEach(result => newState.results.push(result))
            return newState
        }
        default:
            return state;




    }

}


export default connectionsReducer;