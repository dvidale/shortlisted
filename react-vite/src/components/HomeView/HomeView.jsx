import "../../../src/index.css";
import { useMediaQuery } from 'react-responsive'
import SearchConnectionsForm from "../SearchConnectionsForm/SearchConnectionsForm";
import SearchResultsView from "../SearchResultsView/SearchResultsView";
import { useSelector, useDispatch } from "react-redux";
import { createContext, useEffect, useState } from "react";
import { fetchShortlists } from "../../redux/shortlists";
import { FaPlusCircle } from "react-icons/fa";
import { FaMinusCircle } from "react-icons/fa";
import SplashPageComponent from "../SplashPageComponent/SplashPageComponent";
import MyShortlists from "../MyShortlists/MyShortlists";
import MyListings_Calendar from "../MyListings_Calendar/MyListings_Calendar";
import { getCommentThreads } from "../../redux/comments";
import SingleShortlistView from "../SingleShortlistView/SingleShortlistView";
import RecentActivityFeed from "../RecentActivityFeed/RecentActivityFeed";
import MobileNavBtns from "../MobileNavBtnsComponent/MobileNavBtns"

export const DisplayContext = createContext({displayShortlists:false})



// TODO: Write all labels to match their element ids
function HomeView() {


  const isTabletOrMobile = useMediaQuery({query: '(max-width: 1100px)'})
  const dispatch = useDispatch();

  const user = useSelector((state) => state.session.user);

  const saved_shortlists = useSelector((state) => state.shortlists.saved_lists);

  let showSearchForm = saved_shortlists ? false : true


  const shortlists_state = useSelector((state) => state.shortlists);

  let newestIdx;
if(saved_shortlists && Object.keys(saved_shortlists).length > 0){
newestIdx = Object.keys(saved_shortlists).reverse()[0]
}
  

  const [shortlistIdx, setShortlistIdx] = useState(newestIdx || null);
  const [editForm, setEditForm] = useState(false);
  const [toggleSymbol, setToggleSymbol] = useState(`+`);
  const [searchFormView, setSearchFormView] = useState( showSearchForm || false);
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


  useEffect(()=>{},[shortlists_state])
  

  useEffect(() => {
    if (user) {
      setShowShortlists(false)
      dispatch(fetchShortlists(user.id));
    }
  }, [dispatch, user]);

  useEffect(() => {
    if (saved_shortlists && user) {
      dispatch(getCommentThreads(user.id));
      setShortlistIdx(newestIdx)
    
    }

    

  }, [saved_shortlists, dispatch, user, newestIdx]);


 




  return (
    <>
      {user ? (
        <>
          <div className='mobile-title-logo'>Shortlisted</div>
          <div id="search-and-my-shortlist-container">
          
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
              style={{display: searchFormView ? 'flex' : 'none'}}
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
            className="center-panel"
            
            style={{display: `${ showShortlists ? 'flex' : 'none'}`}}
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
            className='center-panel'
            style={{display: showSearchResults && searchSubmitted ? 'flex' : 'none' }}
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
            className={'center-panel'}
            style={{display: ((showSearchResults && searchSubmitted )|| showShortlists || (isTabletOrMobile && searchFormView) ) ? 'none' : 'flex'}}
            >
              <RecentActivityFeed/>
            </div>
         

          <div id="my-listings-calendar-placeholder" className="right-panel">
            <MyListings_Calendar />
          </div>

          {isTabletOrMobile && <div id="mobile-nav" className="mobile-nav-container">
            <MobileNavBtns/>
          </div>}

  </>
      ) : (
   <SplashPageComponent/>
       
      )}
    </>
  );
}

export default HomeView;
