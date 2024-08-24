import SearchConnectionsForm from "../SearchConnectionsForm/SearchConnectionsForm"
import SearchResultsView from "../SearchResultsView/SearchResultsView"
import '../../../src/index.css'
import { useSelector } from "react-redux"


function HomeView(){

const user = useSelector(state => state.session.user)

    return(
        <>
        {user ? (<>
         <div id='build-shortlist-form'>
        <SearchConnectionsForm/>
        </div>
        <div id='search-results-view'>
        <SearchResultsView/>
        </div>
        </>):(<>
        
       
        
        </>)}
       
        </>
    )
}


export default HomeView