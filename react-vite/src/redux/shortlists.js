const BUILD_SHORTLIST = '/shortlists/BUILD_SHORTLIST'
const SAVE_SHORTLIST = '/shortlists/SAVE_SHORTLIST'
const GET_SHORTLISTS = '/shortlists/GET_SHORTLISTS'
const UPDATE_SHORTLIST = '/shortlists/UPDATE_SHORTLIST'
const DELETE_SHORTLIST = '/shortlists/DELETE_SHORTLIST'
const RESET_SHORTLISTS = '/shortlists/RESET_SHORTLISTS'
const CLEAR_SEARCH = '/shortlists/CLEAR_SEARCH'


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

export const clearSearch = () => {
    return {
        type: CLEAR_SEARCH
    }
}

export const resetShortlists = () =>{

    return{
        type: RESET_SHORTLISTS,
        payload: null
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
        
    }else{
        const serverError = await response.json()
        return serverError;  
         //the serverError object: {'location': ["'' is not a valid choice for this field."], 'industry_area': ["'' is not a valid choice for this field."], 'job_title': ["'' is not a valid choice for this field."]}
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

    // TODO: refactor this to only return the referral ids and manually code the success message on the frontend component or something. Basically, no need for the nested array holding both the referral ids and the success message
    return data
    //data response object
    // [ [referrals ids], {success message}]

}else{

    const serverError = await response.json()

    return serverError
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


export const resetShortlistState = () => async (dispatch) =>{

dispatch(resetShortlists())

}

/*-------------------
      REDUCER
---------------------*/

const initialState = { parameters: {}, results_pre_avail: [], saved_lists:{} }

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
        case CLEAR_SEARCH:{
            const newState = {...state, parameters: {}, results_pre_avail: []}
            return newState;
        }
        case RESET_SHORTLISTS:{
            const newState =  { ...state, parameters: {}, results_pre_avail: [], saved_lists:{}}
            return newState
        }
        default:
            return state;




    }

}


export default shortlistsReducer;