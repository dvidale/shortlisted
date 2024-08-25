import "../../../src/index.css";
import { useSelector} from "react-redux";

import ShortlistCommentsFeed from "../ShortlistCommentsFeed/ShortlistCommentsFeed";
import SearchDetails from "../SearchDetails/SearchDetails";


function SingleShortlistView({shortlistIdx}) {
  
  const shortlist = useSelector((state) => state.shortlists.saved_lists[shortlistIdx]);

  return (
    <>
    <h2>Shortlist:</h2>
      {shortlist ? (
        <>
          

          <h1>{shortlist.title} </h1>
          <button>Edit</button>
          <button>Delete</button>
          <p>{shortlist.description}</p>

          <div>Search Details</div>
          <SearchDetails params={shortlist} />
          <ShortlistCommentsFeed shortlist={shortlist} /> 
        </>
      ) : (
        <></>
      )}
    </>
  );
}

export default SingleShortlistView;
