import SearchConnectionsForm from "../SearchConnectionsForm/SearchConnectionsForm"
import SearchResultsView from "../SearchResultsView/SearchResultsView"


function HomeView(){

    return(
        <>
        <h1>Home View</h1>
        <SearchConnectionsForm/>
        <SearchResultsView/>
        </>
    )
}


export default HomeView