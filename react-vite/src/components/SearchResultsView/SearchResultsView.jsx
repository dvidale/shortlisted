import { useState } from "react"
import { useSelector, useDispatch } from "react-redux"
import SearchDetails from "../SearchDetails/SearchDetails"
import { saveShortlist } from "../../redux/shortlists"



function SearchResultsView({user}){

    const dispatch = useDispatch()

    const [shortlist_title, setShortlistTitle] = useState('')
    const [description, setDescription] = useState('')


    // some state slice of search results
    const searchResults = useSelector(state => state.shortlists.results)

    const searchParams = useSelector(state => state.shortlists.parameters)

    const availCheck = (connection => {
        
        let noConflict = true
        let i = 0

        if (connection['bookings'].length === 0) return noConflict;

        while(noConflict && i < connection['bookings'].length){
            const booking = connection['bookings'][i]
            const [ bookingStart, bookingEnd ] = booking
            const booking_start = new Date(bookingStart)
            const booking_end = new Date(bookingEnd)
            const paramsStart = new Date(searchParams['start_date'])
            
            console.log(">>> connections being checked for avail:", connection.first_name);
            console.log(">>>booking_start", booking_start);
            console.log(">>> booking_end", booking_end);
            console.log(">>>> paramsStart:", paramsStart);

            if(booking_start < paramsStart && paramsStart < booking_end ) noConflict = false

            
            i++
        }

        return noConflict;


       

            
    })
            
    let avail_filtered_results = []

    if(searchResults.length > 0 && (searchResults !== null)){
         avail_filtered_results = searchResults.filter(connection => availCheck(connection))

    }
    

    const submitHandler = (e)=>{
        e.preventDefault()

        const shortlistData ={

            title: shortlist_title,
            description,
            job_title: searchParams.job_title,
            industry_area: searchParams.industry_area,
            genre: searchParams.genre,
            location: searchParams.location,
            start_date: searchParams.start_date,
            end_date: searchParams.end_date,
            created_by:user.id,
            referrals: searchResults
           
        }

        dispatch(saveShortlist(JSON.stringify(shortlistData)))

    }
    
    return(
        <>
        <h1>Search Results</h1>
       <SearchDetails params={searchParams}/>
        
        
        <form method={'POST'} onSubmit={submitHandler}>
            <input type='text' 
            name='shortlist-name' 
            value={shortlist_title} 
            onChange={e => setShortlistTitle(e.target.value)}placeholder="Name your list">
            </input>
            <label htmlFor="description">Description</label>
            <textarea id='description-box' name="description" placeholder="Add any notes about the job." value={description} 
            onChange={e => setDescription(e.target.value)}/>
            <button id='save-shortlist-btn' type='submit'>Save</button>
        </form>


        
        {/*  Array.map of returned results tiles */}
        {avail_filtered_results.length > 0 ? avail_filtered_results.map( result =>{
            return (
            
                <div key={result.id}>{result.first_name}</div>
            )
        }):
        <p>No one matches this search.</p>}
        </>
    )
}

export default SearchResultsView