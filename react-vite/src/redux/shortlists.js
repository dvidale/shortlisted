const BUILD_SHORTLIST = '/shortlists/BUILD_SHORTLIST'
const SAVE_SHORTLIST = '/shortlists/SAVE_SHORTLIST'
const GET_SHORTLISTS = '/shortlists/GET_SHORTLISTS'
const UPDATE_SHORTLIST = '/shortlists/UPDATE_SHORTLIST'
const DELETE_SHORTLIST = '/shortlists/DELETE_SHORTLIST'



export const buildAShortlist = (data,params) => {

    return{
        type: BUILD_SHORTLIST,
        payload:[data, params]
    }
}

export const saveAShortlist = (data) =>{

    return{
        type: SAVE_SHORTLIST,
        payload: data
    }


}

export const getMyShortlists = (data) =>{

    return {
        type: GET_SHORTLISTS,
        payload: data
    }
}

export const updateAShortlist = (data) =>{

    return{
        type: UPDATE_SHORTLIST,
        payload: data
    }
}

export const deleteAShortlist = (id) =>{
    return{
        type: DELETE_SHORTLIST,
        payload: id
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
    }else{
        const error = await response.json()
        return error;
    }
}


export const saveShortlist =(shortlistData) => async(dispatch)=>{


const url = `/api/shortlists/new`
const method = 'POST'
const headers = { 'Content-Type': 'application/json' };
const body = shortlistData
const options = {method, headers, body}

const response = await fetch(url, options)

if(response.ok){
    const data = await response.json()
    // console.log(">>>> data returned to save thunk:", data);
    dispatch(saveAShortlist(data))
    return data.id;
}else{
    const error = await response.json()
    console.log("error object", error);
    return error

}


}


export const fetchShortlists = (id)=> async (dispatch) =>{

const url = `/api/shortlists/my-shortlists/${id}`

const response = await fetch(url)


if(response.ok){
    // console.log(">>> Fetch dispatched and returned succesfully");
    // console.log(">>>> response in the fetch shortlists thunk", response);
    const data = await response.json()
    // console.log(">>> data returned from get shortlists route:", data);
    dispatch(getMyShortlists(data))
    return data
}



}


export const updateShortlist = (id, formData) => async (dispatch) => {

    const url = `/api/shortlists/${id}`
    const method = 'PUT'
    const headers = { 'Content-Type': 'application/json' };
    const body = formData;
    const options = {method, headers, body}

    const response = await fetch(url, options)

    if(response.ok){

        const data = await response.json()
        dispatch(updateAShortlist(data))

        return data
    }




}


export const deleteShortlist = (id) => async (dispatch)=> {

const url = `/api/shortlists/${id}`
const method = 'DELETE'
const options = {method}

const response = await fetch(url, options)

if(response.ok){

    const data = await response.json()

    dispatch(deleteAShortlist(id))

    return data

}

}


export const deleteReferral = (id) => async ()=>{

    const url = `/api/shortlists/referrals/${id}`
    const method = 'DELETE'
    const options = {method}

    const response = await fetch(url, options)

    if(response.ok){

        const data = await response.json()
        return data
    }
}

/*-------------------
      REDUCER
---------------------*/
// TODO: consider changing "results" to "search_results" for easier interpretation
const initialState = { parameters: {}, results_pre_avail: [], saved_lists:{}}

const shortlistsReducer = (state = initialState, action) =>{
    switch(action.type){
        
        case BUILD_SHORTLIST:{
            
            const newState = {...state}
            newState['results_pre_avail'] = action.payload[0]
            newState['parameters'] = action.payload[1]
            return newState
        }
        case SAVE_SHORTLIST:{
            const newState = {...state}
            const shortlist = action.payload
            newState.saved_lists[shortlist.id] = shortlist
            return newState;
        }
        case GET_SHORTLISTS:{
            const newState = {...state}

            action.payload.forEach( shortlist =>{
                newState.saved_lists[shortlist.id] = shortlist
            })
            return newState;
        }
        case UPDATE_SHORTLIST:{
            const newState = {...state}
            const shortlist = action.payload
            newState.saved_lists[shortlist.id] = shortlist
            return newState;

        }
        case DELETE_SHORTLIST:{
            const newState ={...state}
            const id = action.payload
            delete newState.saved_lists[id];
            return newState;
        }
        default:
            return state;




    }

}


export default shortlistsReducer;