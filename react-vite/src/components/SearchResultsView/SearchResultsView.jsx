import { useEffect, useState } from "react"
import { useSelector, useDispatch } from "react-redux"
import SearchDetails from "../SearchDetails/SearchDetails"
import { fetchShortlists, saveShortlist } from "../../redux/shortlists"
import './search-results.css'
import '../SingleShortlistView/single-shortlist.css'


function SearchResultsView({user, searchSubmitted, setShowSearchResults, toggleFormView, setShortlistIdx, resetSearchForm}){

    const dispatch = useDispatch()

    const [shortlist_title, setShortlistTitle] = useState('')
    const [description, setDescription] = useState('')
    const [errors, setErrors ] = useState({})


    // some state slice of search results
    const searchResults = useSelector(state => state.shortlists.results_pre_avail)

    const searchParams = useSelector(state => state.shortlists.parameters)

    const saved_shortlists = useSelector(state => state.shortlists.saved_lists)

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
            const paramsEndCheck = searchParams['end_date']
            const paramsEnd = paramsEndCheck ? new Date(paramsEndCheck) : null
            
            // console.log(">>> connections being checked for avail:", connection.first_name);
            // console.log(">>>booking_start", booking_start);
            // console.log(">>> booking_end", booking_end);
            // console.log(">>>> paramsStart:", paramsStart);

            if(booking_start < paramsStart && paramsStart < booking_end ) noConflict = false
            // checks if start date overlaps with a current booking

            if(paramsEnd !== null){
                // console.log(">>> non-null paramsEnd", paramsEnd);
                if(booking_start < paramsEnd && paramsEnd < booking_end ) noConflict = false
                // checks if the job ending overlaps with current booking dates

                if(booking_start < paramsStart && paramsEnd < booking_end) noConflict = false
                // checks for current booking wrapping around job opp

                if(paramsStart < booking_start && booking_end < paramsEnd) noConflict = false
                // checks if job opp wraps around current booking
            }
            
            i++
        }

        return noConflict;

    })
            
    let avail_filtered_results = []

    if(searchResults.length > 0 && (searchResults !== null)){
         avail_filtered_results = searchResults.filter(connection => availCheck(connection))

    }
    
    // * Form validations

    useEffect(()=>{
        const err = {}

      

        if (description.length === 200) err.description = "Descriptions have a 200 character limit"
       
        setErrors(err)

    },[description])

    const submitHandler = (e)=>{
        e.preventDefault()

       
       const err = {}

        if(shortlist_title === '' || shortlist_title.length === 0) err.title = "A title is required to save."

        setErrors(err)

        if(!Object.keys(err).length){


        
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
            referrals: avail_filtered_results
           
        }
      
        
        dispatch(saveShortlist(JSON.stringify(shortlistData))).then( data => {
            if(data){
                err.server = data.error
            setErrors(err)
            }else{
                setShowSearchResults(false)
                toggleFormView()
                setShortlistTitle('')
                setDescription('')
                avail_filtered_results = []
                resetSearchForm()
               
            }
        }
        // TODO: Get the newly saved shortlist to appear in the center panel. Right now it pulls up an older list
        ).then( dispatch(fetchShortlists(user.id)))
        .then( setShortlistIdx(Object.keys(saved_shortlists).length-1) )


        }



    }
    
    return(
        <> 
        <h1 className="search-results-heading">Search Results</h1>
    <p className="error">{errors.server}</p>

        <form method={'POST'} onSubmit={submitHandler}>
            <div className='title-and-save-button'>
            <label htmlFor="shortlist title"> Like these results? Save them.
            <input type='text' 
            name='shortlist-name' className="save-shortlist-title"
            value={shortlist_title} 
            onChange={e => setShortlistTitle(e.target.value)}placeholder="Name your list">
            </input>
</label>


<button id='save-shortlist-btn'className="save-shortlist-btn" type='submit'>Save</button>
</div><p className="error">{errors.title}</p>
            <label htmlFor="description">Add a Description</label>
            <div>
            <textarea id='edit-shortlist-desc' name="description" placeholder="Add any notes about the job." value={description} 
            maxLength={200}onChange={e => setDescription(e.target.value)}/>
     <p className="error">{errors.description}</p>
            </div>
        </form>

        <SearchDetails searchSubmitted={searchSubmitted} params={searchParams}/>
        
        {/*  Array.map of returned results tiles */}
        {searchSubmitted && avail_filtered_results.length > 0 && avail_filtered_results.map( result =>{
            return (
            
                <div key={result.id}>{result.first_name}</div>
            )
        })}
        {searchSubmitted && avail_filtered_results.length === 0 && <p>Sorry, none of your connections match this search.</p>}
        {searchSubmitted === false && <p>Enter job details in the search to see who is available.</p>}
        </>
    )
}

export default SearchResultsView