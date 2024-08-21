const ADD_IMG = 'session/addImage'

const addImg = (data) => ({
    type: ADD_IMG,
    payload: data
  })


// * AWS S3 image upload thunk

export const createImage = (profileImg) => async (dispatch) => {
    const response = await fetch(`/api/images/new`, {
      method: "POST",
    //   headers: {
    //     'Accept': 'application/json',
    //     "Content-Type": "application/json",
    //   },
      body: profileImg
    });
  
    if (response.ok) {
        const {url} = await response.json();
            dispatch(addImg(url));
    } else {
        console.log("There was an error adding your image!")
    }
  };
  

  /*---------
* REDUCER
  ------*/

  const initialState = { img:null }

  function imgReducer(state = initialState, action){
    switch(action.type){
        case ADD_IMG:
            return {...state, img: action.payload};
        default:
            return state;
    }
  }

  export default imgReducer