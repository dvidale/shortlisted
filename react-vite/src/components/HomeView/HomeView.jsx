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
import RecentActivityFeed from "../RecentActivityFeed/RecentActivityFeed";


 
// TODO: Write all labels to match their element ids
function HomeView() {
  const dispatch = useDispatch();

  const user = useSelector((state) => state.session.user);

  const saved_shortlists = useSelector((state) => state.shortlists.saved_lists);

  const shortlists_state = useSelector((state) => state.shortlists);

  const firstIdx =
    saved_shortlists && Object.keys(saved_shortlists).length > 0
      ? Object.keys(saved_shortlists).reverse()[0]['id']
      : null;

      // const lastIdx =  saved_shortlists && Object.keys(saved_shortlists).length > 0
      // ? Object.keys(saved_shortlists)[Object.keys(saved_shortlists).length-1]['id']
      // : null;

  // console.log(">>> firstIdx assigned:", firstIdx);

  const [shortlistIdx, setShortlistIdx] = useState(firstIdx || null);
  const [editForm, setEditForm] = useState(false);
  const [toggleSymbol, setToggleSymbol] = useState(`+`);
  const [searchFormView, setSearchFormView] = useState(false);
  const [showSearchResults, setShowSearchResults] = useState(false);
  const [searchSubmitted, setSearchSubmitted ] = useState(false)
  const [showShortlists, setShowShortlists] = useState(false)
  const [isLoading, setIsLoading] = useState(false)
  const resetSearchForm =()=> {
    return true

  }


  const toggleFormView = () => {
    setToggleSymbol(!toggleSymbol);
    setSearchFormView(!searchFormView);
    setSearchSubmitted(false)

    setShowSearchResults(false)

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


 




  return (
    <>
      {user ? (
        <>
        
          <div id="search-and-my-shortlist-container">
          {/* <div className="shortlisted-title">Shortlisted.</div> */}
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
                setIsLoading={setIsLoading}
                isLoading={isLoading}
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
                setShowShortlists={setShowShortlists}
              />
            </div>
          </div>
          <div
            id="single-shortlist-view"
            className={`${
              showShortlists ? "center-panel show-view" : "center-panel hide-view "
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
              showSearchResults && searchSubmitted ? "center-panel show-view" : "center-panel hide-view"
            }`}
          >
            <SearchResultsView
              user={user}
              setShowSearchResults={setShowSearchResults}
              toggleFormView={toggleFormView}
              setShortlistIdx={setShortlistIdx}
              showSearchResults={showSearchResults}
              searchSubmitted={searchSubmitted}
              setShowShortlists={setShowShortlists}
              setIsLoading={setIsLoading}
              isLoading={isLoading}
            />
          </div>

            <div id="recent-activity-view"
            className={((showSearchResults && searchSubmitted )|| showShortlists ) ? "center-panel hide-view" :"center-panel show-view"}>
              <RecentActivityFeed/>
            </div>
         

          <div id="my-listings-calendar-placeholder" className="right-panel">
            <MyListings_Calendar />
          </div>
        </>
      ) : (
        <>
       
    
 <div className="splash-text">
  <div>
  <h1 >Recommend peers for jobs, or</h1>
  </div>
  <div>
  <h1 >get referred yourself... </h1>
  </div>
 <div>
 <h1>with Shortlisted.        </h1>
</div>
</div>
        <div className="splash-img rotate"></div>
    
        </>
      )}
    </>
  );
}

export default HomeView;
