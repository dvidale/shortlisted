const BUILD_SHORTLIST = '/shortlists/BUILD_SHORTLIST'
const GET_SHORTLISTS = '/shortlists/GET_SHORTLISTS'


export const buildAShortlist = (data,params) => {

    return{
        type: BUILD_SHORTLIST,
        payload:[data, params]
    }
}

export const getMyShortlists = (data) =>{

    return {
        type: GET_SHORTLISTS,
        payload: data
    }
}


/*-------------------
       THUNKS
---------------------*/


export const buildShortlist = (userId, formData) => async (dispatch) =>{

    const url = `/api/connections/${userId}`
    const method = 'POST'
    const headers = { 'Content-Type': 'application/json' };
    const body = formData
    // console.log(">>>> form_data in thunk:", formData);
    const options = {method, headers, body}

    const response = await fetch(url,options)
   
    if(response.ok){
        const data = await response.json()
        const params = await JSON.parse(formData)
        dispatch(buildAShortlist(data, params))
         // TODO: refactor to pass the form data into Context so we can pass it straight from the component
        // console.log(">>>> parsed form data in thunk:", params);
        return data
    }
}


export const saveShortlist =(shortlistData) => async()=>{


const url = `/api/shortlists/new`
const method = 'POST'
const headers = { 'Content-Type': 'application/json' };
const body = shortlistData
const options = {method, headers, body}

const response = await fetch(url, options)

const data = await response.json()
// console.log(">>>> data returned to save thunk:", data);

return data


}


export const fetchShortlists = (id)=> async (dispatch) =>{

const url = `/api/shortlists/my-shortlists/${id}`

const response = await fetch(url)


if(response.ok){
    // console.log(">>>> response in the fetch shortlists thunk", response);
    const data = await response.json()
    // console.log(">>> data returned from get shortlists route:", data);
    dispatch(getMyShortlists(data))
    return data
}



}

/*-------------------
      REDUCER
---------------------*/
// TODO: consider changing "results" to "search_results" for easier interpretation
const initialState = { parameters: {}, results: [], saved_lists:{}}

const shortlistsReducer = (state = initialState, action) =>{
    switch(action.type){
        
        case BUILD_SHORTLIST:{
            
            const newState = {...state}
            newState['results'] = action.payload[0]
            newState['parameters'] = action.payload[1]
            return newState
        }
        case GET_SHORTLISTS:{
            const newState = {...state}

            action.payload.forEach( shortlist =>{
                newState.saved_lists[shortlist.id] = shortlist
            })
            return newState;
        }
        default:
            return state;




    }

}


export default shortlistsReducer;