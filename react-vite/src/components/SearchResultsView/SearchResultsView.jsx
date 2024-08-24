import { useState } from "react"
import { useSelector } from "react-redux"
import SearchDetails from "../SearchDetails/SearchDetails"
function SearchResultsView(){

    const [shortlist_title, setShortlistTitle] = useState('')

    // some state slice of search results
    const searchResults = useSelector(state => state.shortlists.results)

    const searchParams = useSelector(state => state.shortlists.parameters)

    // some value that holds the parameters just searched, maybe returned 

    return(
        <>
        <h1>Search Results</h1>
       <SearchDetails params={searchParams}/>
        
        



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