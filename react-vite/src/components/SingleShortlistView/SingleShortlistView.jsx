import { useSelector } from "react-redux"
import ShortlistCommentsFeed from '../ShortlistCommentsFeed'
import SearchDetails from "../SearchDetails/SearchDetails"

function SingleShortlistView(){

    const shortlist = useSelector(state => state.shortlists.saved_lists['id'])

    return (
        <>
        <div>Shortlist:</div>

        {shortlist.title}<button>Edit</button>
        <button>Delete</button>

        <div>Search Details</div>
        <SearchDetails params={shortlist}/>
        <ShortlistCommentsFeed/>


        </>
    )
}


export default SingleShortlistView