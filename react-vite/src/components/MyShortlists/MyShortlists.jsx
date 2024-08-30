
import '../../../src/index.css'

import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { fetchShortlists } from '../../redux/shortlists'


// import { createContext } from 'react'



function MyShortlists({shortlistIdx, setShortlistIdx, saved_shortlists, setEditForm,setShowSearchResults }){
 
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
                {Object.values(saved_shortlists).reverse().map( shortlist =>{

                    return(

                    
                        <div key={shortlist.id} 
                        
                        className={shortlist.id == shortlistIdx ?'title-and-button-pairs-clicked': 'title-and-button-pairs'}>
                            <div>
                                {/* if current shortlist_id in single view  matches this btn shortlist_id, change the style to .clicked */}
                            <button className={shortlist.id == shortlistIdx ? 'shortlist-btn-clicked' : 'shortlist-btn'} value={shortlist.id}
                            onClick={ e => switchShortlistAndReset(e)    }
                
                            > 
                            {shortlist.title} </button>
                    
                            </div>
                             <div className={shortlist.id != shortlistIdx ?'edit-delete-list-btns': 'edit-delete-list-btns-hidden'}>
                                {/* <button>EDIT</button>
                                <button>DELETE</button> */}
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