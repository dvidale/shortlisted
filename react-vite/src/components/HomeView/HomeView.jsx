import "../../../src/index.css";
import SearchConnectionsForm from "../SearchConnectionsForm/SearchConnectionsForm";
import SearchResultsView from "../SearchResultsView/SearchResultsView";
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import { fetchShortlists } from "../../redux/shortlists";

import MyShortlists from "../MyShortlists/MyShortlists";
import MyListings_Calendar from "../MyListings_Calendar/MyListings_Calendar";
import { getCommentThreads } from "../../redux/comments";
import SingleShortlistView from "../SingleShortlistView/SingleShortlistView";

function HomeView() {
  const dispatch = useDispatch();

  const user = useSelector((state) => state.session.user);

  const saved_shortlists = useSelector((state) => state.shortlists.saved_lists);

  const shortlists_state = useSelector((state) => state.shortlists);

  const firstIdx = saved_shortlists && Object.keys(saved_shortlists).length > 0 ? Object.keys(saved_shortlists)[0] : null;

  // console.log(">>> firstIdx assigned:", firstIdx);

  const [shortlistIdx, setShortlistIdx]= useState(firstIdx || null)

  const [editForm, setEditForm] = useState(false);

  if (shortlists_state) {
    console.log("shortlists state loaded");
  }

  useEffect(() => {
    if (user) {
      dispatch(fetchShortlists(user.id));
    }
  }, [dispatch, user]);

  useEffect(() => {
    if (saved_shortlists) {
      dispatch(getCommentThreads(user.id));
    }
  }, [saved_shortlists, dispatch, user]);

  return (
    <>
      {user ? (
        <>
          <div id="search-and-my-shortlist-container">
            <div id="build-shortlist-form" className="left-panel">
              <SearchConnectionsForm user={user} />
            </div>

            <div id="my-shortlists" className="left-panel visible-panel">
              <MyShortlists shortlistIdx={shortlistIdx} setShortlistIdx={setShortlistIdx} saved_shortlists={saved_shortlists} setEditForm={setEditForm} />
            </div>
          </div>
            <div id="single-shortlist-view" className="center-panel">
              <SingleShortlistView setEditForm={setEditForm} editForm={editForm} shortlistIdx={shortlistIdx} />
            </div>
          <div id="search-results-view" className="center-panel">
            <SearchResultsView user={user} />
          </div>

          <div id="my-listings-calendar-placeholder" className="right-panel">
            <MyListings_Calendar />
          </div>
        </>
      ) : (
        <></>
      )}
    </>
  );
}

export default HomeView;
