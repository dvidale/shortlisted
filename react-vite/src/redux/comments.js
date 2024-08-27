const GET_COMMENTS_BY_REFERRAL = '/comments/GET_COMMENTS_BY_REFERRAL'
const ADD_A_COMMENT = '/comments/ADD_A_COMMENT'
const EDIT_A_COMMENT = '/comments/EDIT_A_COMMENT'
const DELETE_A_COMMENT = '/comments/DELETE_A_COMMENT'


export const getAllCommentsByReferral = (data)=>{
    return {
        type: GET_COMMENTS_BY_REFERRAL,
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

export const deleteAComment = (id) =>{
    return {
        type: DELETE_A_COMMENT,
        payload: id
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

        return data
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
    dispatch(deleteAComment(id))

    return data.message
}







}

/*-----------------
        REDUCER
-------------------*/

const initialState = { comments: {} }

const commentsReducer = (state = initialState, action ) =>{
    switch(action.type){

        case GET_COMMENTS_BY_REFERRAL:{
            const newState = {...state}
            action.payload.forEach(comment =>{
                newState.comments[comment.id] = comment
            })
            return newState
        }
        case ADD_A_COMMENT:{
            const newState = {...state}
            newState.comments[action.payload.id] = action.payload
            return newState
        }
        case EDIT_A_COMMENT:{
            const newState = {...state}
            newState.comments[action.payload.id] = action.payload
            return newState    
        }
        case DELETE_A_COMMENT:{
            const newState = {...state}
            delete newState.comments[action.payload]
            return newState
        }
        default:
            return state

    }

}


export default commentsReducer;
