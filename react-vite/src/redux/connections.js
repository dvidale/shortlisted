const CONNECTION_RESULTS = '/connections/CONNECTION_RESULTS'



export const getConnections = (data) => {

    return{
        type: CONNECTION_RESULTS,
        payload:data
    }
}


/*-------------------
       THUNKS
---------------------*/


export const searchConnections = (userId, formData) => async () =>{

    const url = `/api/connections/${userId}`
    const method = 'POST'
    const headers = { 'Content-Type': 'application/json' };
    const body = formData
    console.log(">>>> form_data in thunk:", formData);
    const options = {method, headers, body}

    const response = await fetch(url,options)

    if(response.ok){
        const data = await response.json()
        console.log(">>>> POST route return data in thunk:", data);
        return data
    }
}

/*-------------------
      REDUCER
---------------------*/

const initialState = { results: []}

const connectionsReducer = (state = initialState, action) =>{
    switch(action.type){
        case CONNECTION_RESULTS:
            return {
                ...state, results: action.payload
            };
        default:
            return state;




    }

}


export default connectionsReducer;