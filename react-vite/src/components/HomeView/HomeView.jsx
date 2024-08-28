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

  const firstIdx =
    saved_shortlists && Object.keys(saved_shortlists).length > 0
      ? Object.keys(saved_shortlists)[0]
      : null;

  // console.log(">>> firstIdx assigned:", firstIdx);

  const [shortlistIdx, setShortlistIdx] = useState(firstIdx || null);

  const [editForm, setEditForm] = useState(false);
  const [toggleSymbol, setToggleSymbol] = useState(`+`);
  const [searchFormView, setSearchFormView] = useState(false);
  const [showSearchResults, setShowSearchResults] = useState(false);

  const toggleFormView = () => {
    setToggleSymbol(!toggleSymbol);
    setSearchFormView(!searchFormView);
  };

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
            <button id="new-shortlist-btn" onClick={() => toggleFormView()}>
              <h1>
                {" "}
                New Shortlist{" "}
                <span className="toggle-symbol">
                  {toggleSymbol ? `+` : `-`}
                </span>
              </h1>
            </button>

            <div
              id="build-shortlist-form"
              
            >
              <SearchConnectionsForm
                user={user}
                searchFormView={searchFormView}
                setShowSearchResults={setShowSearchResults}
              />
            </div>

            <div
              id="my-shortlists"
              className={searchFormView ? "hide-view" : "show-view"}
            >
              <MyShortlists
                shortlistIdx={shortlistIdx}
                setShortlistIdx={setShortlistIdx}
                saved_shortlists={saved_shortlists}
                setEditForm={setEditForm}
                searchFormView={searchFormView}
                setShowSearchResults={setShowSearchResults}
              />
            </div>
          </div>
          <div
            id="single-shortlist-view"
            className={`center-panel ${
              showSearchResults ? "hide-view" : "show-view"
            }`}
          >
            <SingleShortlistView
              setEditForm={setEditForm}
              editForm={editForm}
              shortlistIdx={shortlistIdx}
            />
          </div>
          <div
            id="search-results-view"
            className={`center-panel ${
              showSearchResults ? "show-view" : "hide-view"
            }`}
          >
            <SearchResultsView
              user={user}
              setShowSearchResults={setShowSearchResults}
              toggleFormView={toggleFormView}
              setShortlistIdx={setShortlistIdx}
            />
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
