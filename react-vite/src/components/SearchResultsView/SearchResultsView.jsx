import { useEffect, useState } from "react"
import { useSelector, useDispatch } from "react-redux"
import SearchDetails from "../SearchDetails/SearchDetails"
import { clearSearch, saveShortlist } from "../../redux/shortlists"
import './search-results.css'
import '../SingleShortlistView/single-shortlist.css'
import SearchResultTile from "./SearchResultTile"
import { useAvailFilter } from "../../hooks/checkBookingAvailability"

function SearchResultsView({user, toggleFormView, setShowShortlists, setIsLoading, setShowSearchResults}){

    const dispatch = useDispatch()

    const [shortlist_title, setShortlistTitle] = useState('')
    const [description, setDescription] = useState('')
    const [errors, setErrors ] = useState({})
            
    const searchParams = useSelector(state => state.shortlists.parameters)

    const avail_filtered_results = useAvailFilter({setShowShortlists, setIsLoading, setShowSearchResults})

    // * Form validations

    useEffect(()=>{
        const err = {}

        if (description.length === 200) err.description = "Descriptions have a 200 character limit"
       
        setErrors(err)

    },[description])

    // *SAVE NEW SHORTLIST
    const submitHandler = async (e)=>{
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

        await dispatch(clearSearch())

        await dispatch(saveShortlist(JSON.stringify(shortlistData))).then( data => {
            if(data.serverError){
                err.server = data.serverError
            setErrors(err)
            }else{
            
                toggleFormView()
                setShortlistTitle('')
                setDescription('')
                // avail_filtered_results = []
                
            }
        }
  
        )
       
        }
    }
 

    return(
        <> 
        <h1 className="search-results-heading">Search Results</h1>
    <p className="error">{errors.server}</p>
        <div className='mobile-results-container'>
        <form method={'POST'} onSubmit={submitHandler}>
            <div className='title-and-save-button'>
            <label htmlFor="shortlist-name"> Like these results? Save them.
            <input type='text' 
            id="shortlist-name"
            name='shortlist-name' className="save-shortlist-title"
            value={shortlist_title} 
            onChange={e => setShortlistTitle(e.target.value)}placeholder="Name your list">
            </input>
</label>


<button id='save-shortlist-btn'className="save-shortlist-btn" type='submit'>Save</button>
</div><p className="error">{errors.title}</p>
            <label htmlFor="description">Add a Description</label>
            <div>
            <textarea id='edit-shortlist-desc' name="description" className="save-shortlist-desc" placeholder="Add any notes about the job." value={description} 
            maxLength={200} onChange={e => setDescription(e.target.value)}/>
     <p className="error">{errors.description}</p>
            </div>
        </form>
        
        <SearchDetails params={searchParams}/>
        
        {avail_filtered_results.length === 0 && <p>Sorry, none of your connections are available for these dates.</p>}
       
       
        {/*  Array.map of returned results tiles */}
        { avail_filtered_results.length > 0 && <p className="result-count">{avail_filtered_results.length} of your peers are available</p>}
        <div className="results-box">
        {avail_filtered_results.length > 0 && avail_filtered_results.map( result =>{
            return (
            
                <div key={result.id}><SearchResultTile resultFirstName={result.first_name} resultLastName={result.last_name}/></div>
            )
        })}
       </div>
       </div>
        
        </>
    )
}

export default SearchResultsView