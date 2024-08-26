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
            created_by:user.id
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
            <button type='submit'>Save</button>
        </form>


        
        {/*  Array.map of returned results tiles */}
        {searchResults.map( result =>{
            return (
            
                <div key={result.id}>{result.first_name}</div>
            )
        })}
        </>
    )
}

export default SearchResultsView