import "../../../src/index.css";
import SearchConnectionsForm from "../SearchConnectionsForm/SearchConnectionsForm";
import SearchResultsView from "../SearchResultsView/SearchResultsView";
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import { fetchShortlists } from "../../redux/shortlists";
import { FaPlusCircle } from "react-icons/fa";
import { FaMinusCircle } from "react-icons/fa";

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
  const [searchSubmitted, setSearchSubmitted ] = useState(false)

  const resetSearchForm =()=> {
    return true

  }


  const toggleFormView = () => {
    setToggleSymbol(!toggleSymbol);
    setSearchFormView(!searchFormView);
    setShowSearchResults(!showSearchResults)
    setSearchSubmitted(false)
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
    if (saved_shortlists && user) {
      dispatch(getCommentThreads(user.id));
    }
  }, [saved_shortlists, dispatch, user]);


  // const splashImgStyle = {
	// 	width: '100%',
	// 	backgroundImage: `url('https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/splash_page_no_BG.png')`,
	// 	backgroundSize: 'cover',
	// 	backgroundPosition: 'center',
	// 	position: 'relative', // Ensure the overlay is positioned correctly
	// };





  return (
    <>
      {user ? (
        <>
        
          <div id="search-and-my-shortlist-container">
          <div className="shortlisted-title">Shortlisted.</div>
            <button id="new-shortlist-btn" onClick={() => toggleFormView()}>
              <h1>
            
                New Shortlist 
                </h1>
                <h1>
                {toggleSymbol ? <FaPlusCircle /> : <FaMinusCircle />}
             
              </h1>
            </button>

            <div
              id="build-shortlist-form"
              
            >
              <SearchConnectionsForm
                user={user}
                searchFormView={searchFormView}
                setShowSearchResults={setShowSearchResults}
                resetSearchForm={resetSearchForm}
                setSearchSubmitted={setSearchSubmitted}
              
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
            className={`${
              showSearchResults ? "center-panel hide-view" : "center-panel show-view"
            }`}
          >
            <SingleShortlistView
              setEditForm={setEditForm}
              editForm={editForm}
              setShortlistIdx={setShortlistIdx}
              shortlistIdx={shortlistIdx}
              showSearchResults={showSearchResults}
            />
          </div>
          <div
            id="search-results-view"
            className={`${
              showSearchResults ? "center-panel show-view" : "center-panel hide-view"
            }`}
          >
            <SearchResultsView
              user={user}
              setShowSearchResults={setShowSearchResults}
              toggleFormView={toggleFormView}
              setShortlistIdx={setShortlistIdx}
              showSearchResults={showSearchResults}
              searchSubmitted={searchSubmitted}
            />
          </div>

          <div id="my-listings-calendar-placeholder" className="right-panel">
            <MyListings_Calendar />
          </div>
        </>
      ) : (
        <>
       
       {/* <div className="splash-img" style={splashImgStyle}>
 <h1>Recommend peers for jobs, or get referred yourself...</h1>
 <br/>
 <h1>
          with Shortlisted.
        </h1>
        <img alt='splash-img' src='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/splash_page_no_BG.png'/>
       </div> */}
        </>
      )}
    </>
  );
}

export default HomeView;
