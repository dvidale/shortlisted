import { useState } from "react"
import { useSelector } from "react-redux"

function SearchResultsView(){

    const [shortlist_title, setShortlistTitle] = useState('')

    // some state slice of search results
    const searchResults = useSelector(state => state.connections.results)

    // some value that holds the parameters just searched, maybe returned 

    return(
        <>
        <h1>Search Results</h1>
        <form>
            <input type='text' 
            name='shortlist-name' 
            value={shortlist_title} 
            onChange={e => setShortlistTitle(e.target.value)}placeholder="Name your list">
            </input>
            <button type='submit'>Save</button>
        </form>


        {/* {Search Parameters Here} */}

        {/*  Array.map of returned results tiles */}
        {searchResults}
        </>
    )
}

export default SearchResultsView