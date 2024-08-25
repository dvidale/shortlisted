import "../../../src/index.css";
import { useSelector} from "react-redux";

import ShortlistCommentsFeed from "../ShortlistCommentsFeed/ShortlistCommentsFeed";
import SearchDetails from "../SearchDetails/SearchDetails";


function SingleShortlistView() {
  
  const shortlist = useSelector((state) => state.shortlists.saved_lists[1]);


  return (
    <>
      {shortlist ? (
        <>
          <h2>Shortlist:</h2>

          <h1>{shortlist.title} </h1>
          <button>Edit</button>
          <button>Delete</button>
          <p>{shortlist.description}</p>

          <div>Search Details</div>
          <SearchDetails params={shortlist} />
          <ShortlistCommentsFeed />
        </>
      ) : (
        <></>
      )}
    </>
  );
}

export default SingleShortlistView;
