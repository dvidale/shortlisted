import '../../../src/index.css'
import SearchConnectionsForm from "../SearchConnectionsForm/SearchConnectionsForm"
import SearchResultsView from "../SearchResultsView/SearchResultsView"
import { useSelector, useDispatch } from "react-redux"
import { useEffect } from 'react'
import { fetchShortlists } from '../../redux/shortlists'

import MyShortlists from "../MyShortlists/MyShortlists"
import MyListings_Calendar from '../MyListings_Calendar/MyListings_Calendar'


function HomeView(){
    const dispatch = useDispatch()

const user = useSelector(state => state.session.user)

const saved_shortlists = useSelector(state => state.shortlists.saved_lists)

const shortlists_state = useSelector(state => state.shortlists)

if(shortlists_state){
    console.log("shortlists state loaded");
}
 
    
    useEffect(()=>{
        
        if(user){
            dispatch(fetchShortlists(user.id))
        }
        

    },[dispatch, user])




    return(
        <>
        {user ? (<>
         <div id='build-shortlist-form'>
        <SearchConnectionsForm user={user}/>
        </div>
        <div id='search-results-view'>
        <SearchResultsView user={user}/>
        </div>
        <div id="my-shortlists">
            
            <MyShortlists saved_shortlists={saved_shortlists}/>
        </div>
        <div id="my-listings-calendar-placeholder">
            <MyListings_Calendar/>
        </div>
        
        </>):(<>
        
       
        
        </>)}
       
        </>
    )
}


export default HomeView