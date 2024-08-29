
import '../../../src/index.css'

import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { fetchShortlists } from '../../redux/shortlists'


// import { createContext } from 'react'



function MyShortlists({setShortlistIdx, saved_shortlists, setEditForm,setShowSearchResults }){
 
    const dispatch = useDispatch()

    // const saved_shortlists = useSelector(state => state.shortlists.saved_lists)

 
    const user = useSelector(state => state.session.user) 
    
    
    

     
const switchShortlistAndReset = (e)=>{

    setEditForm(false)

    setShortlistIdx(e.target.value)
    setShowSearchResults(false)
}
  
    useEffect(()=>{
        
        dispatch(fetchShortlists(user.id))
        

    },[dispatch, user])

    
    
   
    return(
        <>
        { Object.keys(saved_shortlists).length > 0 ?  (
            <> 
            <h1 className='panel-heading'>My Shortlists</h1>
                <div className='my-shortlists-list'>
                {Object.values(saved_shortlists).map( shortlist =>{

                    return(

                        
                        <div key={shortlist.id} className='title-and-button-pairs'>
                            <div>
                            <button className='shortlist-btn' value={shortlist.id}
                            onClick={ e => switchShortlistAndReset(e)    }
                
                            > 
                            {shortlist.title}</button>
                            {/* {console.log(">>>> current shortlist in my-shortlist view:", shortlist)} */}
                            </div>
                            <div className='edit-delete-list-btns'>
                                <button>EDIT</button>
                                <button>DELETE</button>
                            </div>
                        </div>
                       
        
                    )
                })}
           </div>
                 
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