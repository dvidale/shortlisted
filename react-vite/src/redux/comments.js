const GET_ALL_COMMENT_THREADS = '/comments/GET_ALL_COMMENT_THREADS'
const ADD_A_COMMENT = '/comments/ADD_A_COMMENT'
const EDIT_A_COMMENT = '/comments/EDIT_A_COMMENT'
const DELETE_A_COMMENT = '/comments/DELETE_A_COMMENT'


export const getAllCommentThreads = (data)=>{
    return {
        type: GET_ALL_COMMENT_THREADS,
        payload:data
    }
}

export const addAComment = (data) =>{
    return {
        type: ADD_A_COMMENT,
        payload: data
    }
}

export const editAComment = (data) =>{
    return {
        type: EDIT_A_COMMENT,
        payload: data
    }
}

export const deleteAComment = (id, thread) =>{
    return {
        type: DELETE_A_COMMENT,
        payload: [id, thread]
    }
}

/*-------
THUNKS
-------*/

export const getCommentThreads = (id) => async (dispatch) => {

const url = `/api/comments/${id}`

const response = await fetch(url)

if(response.ok){

    const data = await response.json()
    
    dispatch(getAllCommentThreads(data))
    
    return data

}
}

export const addComment = (commentData) => async (dispatch) =>{

    const url = `/api/comments/new`
    const method = 'POST'
    const headers = {'Content-Type' : 'application/json'}
    const body = commentData
    const options = {method, headers, body}
    

    const response = await fetch(url, options)

    if(response.ok){

        const data = await response.json()
        dispatch(addAComment(data))

        // return data
    }else{
        const serverError = await response.json()
        return serverError 
    }
}

export const editComment = (id, commentData) => async (dispatch) => {

    const url = `/api/comments/${id}`
    const method = 'PUT'
    const headers = {'Content-Type' : 'application/json'}
    const body = commentData
    const options = {method, headers, body}
    
    const response = await fetch(url, options)

    if(response.ok){

        const data = await response.json()
        dispatch(editAComment(data))

        return data
    }


}

export const deleteComment = (id) => async (dispatch) =>{

const url = `/api/comments/${id}`
const method = 'DELETE'
const options = {method}

const response = await fetch(url, options)

if(response.ok){

    const data = await response.json()
    dispatch(deleteAComment(id, data['target_thread']))

    return {"message" : "deleted successfully"}
}







}

/*-----------------
        REDUCER
-------------------*/

const initialState = { comment_threads: {} }

const commentsReducer = (state = initialState, action ) =>{
    switch(action.type){

        case GET_ALL_COMMENT_THREADS:{
            const newState = {...state}
            action.payload.forEach(thread =>{
                const referral_id = thread[0]['referral_id']
                newState.comment_threads[referral_id] = {}

                thread.forEach(comment => {

                    newState.comment_threads[referral_id][comment['id']] = comment
                })


            })
            return newState
        }
        case ADD_A_COMMENT:{
            const newState = {...state}
            newState.comment_threads[action.payload['referral_id']] = action.payload['id'] = action.payload
            return newState
        }
        case EDIT_A_COMMENT:{
            const newState = {...state}
            const target_thread = newState.comment_threads[action.payload['referral_id']]
             target_thread[action.payload['id']] = action.payload
            return newState    
        }
        case DELETE_A_COMMENT:{
            const newState = {...state}
            const thread_id = action.payload[1]
            const comment_id = action.payload[0]
            delete newState.comment_threads[thread_id][comment_id]
            return newState
        }
        default:
            return state

    }

}


export default commentsReducer;
