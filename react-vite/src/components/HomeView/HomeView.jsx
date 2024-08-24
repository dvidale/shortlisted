import SearchConnectionsForm from "../SearchConnectionsForm/SearchConnectionsForm"
import SearchResultsView from "../SearchResultsView/SearchResultsView"
import '../../../src/index.css'

function HomeView(){

    return(
        <>
        <h1>Home View</h1>
        <div id='build-shortlist-form'>
        <SearchConnectionsForm/>
        </div>
        <div id='search-results-view'>
        <SearchResultsView/>
        </div>
        </>
    )
}


export default HomeView