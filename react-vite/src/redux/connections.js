const CONNECTION_RESULTS = '/connections/CONNECTION_RESULTS'



export const returnConnectionResults = (data,params) => {

    return{
        type: CONNECTION_RESULTS,
        payload:[data, params]
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
        const params = await JSON.parse(formData)
        dispatch(returnConnectionResults(data, params))
        console.log(">>>> parsed form data in thunk:", params);
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
            
            const newState = {...state}
            newState['results'] = action.payload[0]
            newState['parameters'] = action.payload[1]
            return newState
        }
        default:
            return state;




    }

}


export default connectionsReducer;