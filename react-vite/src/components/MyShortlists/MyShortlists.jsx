
import '../../../src/index.css'

import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { fetchShortlists } from '../../redux/shortlists'


// import { createContext } from 'react'



function MyShortlists({setShortlistIdx, saved_shortlists, setEditForm}){
 
    const dispatch = useDispatch()

    // const saved_shortlists = useSelector(state => state.shortlists.saved_lists)

 
    const user = useSelector(state => state.session.user) 
    
    
    

     
const switchShortlistAndReset = (e)=>{

    setEditForm(false)
    setShortlistIdx(e.target.value)
}
  
    useEffect(()=>{
        
        dispatch(fetchShortlists(user.id))
        

    },[dispatch, user])

    
    
   
    return(
        <>
        { Object.keys(saved_shortlists).length > 0 ?  (
            <> 
            <h1>My Shortlists</h1>
   
                {Object.values(saved_shortlists).map( shortlist =>{

                    return(

                        
                            <div key={shortlist.id}>
                            <button value={shortlist.id}
                            onClick={ e => switchShortlistAndReset(e)    }
                
                            > 
                            {shortlist.title}</button>
                            {/* {console.log(">>>> current shortlist in my-shortlist view:", shortlist)} */}

                            <div>
                                <button>Edit</button>
                                <button>Delete</button>
                            </div>
                      </div>
                       
        
                    )
                })}
                {/* <div id="single-shortlist-view">
        <SingleShortlistView setEditForm={setEditForm} editForm={editForm} shortlistIdx={shortlistIdx}/>
                     
        </div> */}
                 
                </>  
                ):(
                <>
                   <h1>No Shortlists Yet?</h1> 
                   <h1>Create one!</h1>
                   
                </>)
        }
       
         
        
        </>
    )
}


export default MyShortlists