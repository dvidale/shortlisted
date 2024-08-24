import { useState } from "react"
import { useSelector } from "react-redux"

function SearchResultsView(){

    const [shortlist_title, setShortlistTitle] = useState('')

    // some state slice of search results
    const searchResults = useSelector(state => state.connections.results)

    const searchParams = useSelector(state => state.connections.parameters)

    // some value that holds the parameters just searched, maybe returned 

    return(
        <>
        <h1>Search Results</h1>
        {/* {Search Parameters Here} */}
       
        <div>{searchParams.industry_area}</div>
        <div>{searchParams.job_title}</div>
        <div>{searchParams.location}</div>
        



        <form>
            <input type='text' 
            name='shortlist-name' 
            value={shortlist_title} 
            onChange={e => setShortlistTitle(e.target.value)}placeholder="Name your list">
            </input>
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