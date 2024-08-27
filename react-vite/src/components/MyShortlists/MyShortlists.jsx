
import '../../../src/index.css'

import { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { fetchShortlists } from '../../redux/shortlists'
import SingleShortlistView from '../SingleShortlistView/SingleShortlistView'



function MyShortlists({saved_shortlists}){
 
    const dispatch = useDispatch()

    // const saved_shortlists = useSelector(state => state.shortlists.saved_lists)

    const firstIdx = saved_shortlists && Object.keys(saved_shortlists).length > 0 ? Object.keys(saved_shortlists)[0] : null;

    // console.log(">>> firstIdx assigned:", firstIdx);
    const user = useSelector(state => state.session.user) 
  
    const [shortlistIdx, setShortlistIdx]= useState(firstIdx || null)


    // console.log(">>> firstIdx as default:", firstIdx);
    // console.log(">>>> shortlistIdx from MyShortlists:", shortlistIdx);

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
                            onClick={(e) => setShortlistIdx(e.target.value)}> 
                            {shortlist.title}</button>
                            {/* {console.log(">>>> current shortlist in my-shortlist view:", shortlist)} */}

                            <div>
                                <button>Edit</button>
                                <button>Delete</button>
                            </div>
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