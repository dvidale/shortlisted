
import '../../../src/index.css'

import { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { fetchShortlists } from '../../redux/shortlists'
import SingleShortlistView from '../SingleShortlistView/SingleShortlistView'


// !BUG - the shortlists do not load unless I manually force the state to re-render twice
function MyShortlists({saved_shortlists}){
 
    const dispatch = useDispatch()

    // const saved_shortlists = useSelector(state => state.shortlists.saved_lists)

    const firstIdx = Object.keys(saved_shortlists)[0]
    // console.log(">>> firstIdx:", firstIdx);
    const user = useSelector(state => state.session.user) 
 
     
  
    const [shortlistIdx, setShortlistIdx]= useState(firstIdx)

    useEffect(()=>{

        dispatch(fetchShortlists(user.id))

    },[dispatch, user, saved_shortlists])



    return(
        <>
        { Object.keys(saved_shortlists).length > 0 ?  (
            <> 
            <h1>My Shortlists</h1>
   
                {Object.values(saved_shortlists).map( shortlist =>{

                    return(

                        
                            <div key={shortlist.id}>
                            <button value={shortlist.id}
                            onClick={(e) => setShortlistIdx(e.target.value)}> 
                            {shortlist.title}</button>
                      </div>
                       
        
                    )
                })}
                <div id="single-shortlist-view">
        <SingleShortlistView shortlistIdx={shortlistIdx}/>
                     
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