import "../../../src/index.css";
import { useMediaQuery } from 'react-responsive'
import SearchConnectionsForm from "../SearchConnectionsForm/SearchConnectionsForm";
import SearchResultsView from "../SearchResultsView/SearchResultsView";
import { useSelector, useDispatch } from "react-redux";
import { useContext, useEffect, useState } from "react";
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
import BookingsPanel from "../MyListings_Calendar/BookingsPanel";
import ProfileComponent from "../ProfileComponent/ProfileComponent";
import ReferralShortlistView from "../ReferralShortlistView/ReferralShortlistView";
import { PanelViews } from "../../context/PanelView";





// TODO: Write all labels to match their element ids
function HomeView() {


  const isTabletOrMobile = useMediaQuery({query: '(max-width: 1100px)'})
  const dispatch = useDispatch();

  const user = useSelector((state) => state.session.user);

  const { centerPanel, setCenterPanel, leftPanel, setLeftPanel } = useContext(PanelViews)

  const saved_shortlists = useSelector((state) => state.shortlists.saved_lists);
  const user_bookings = useSelector(state => state.bookings.user_bookings)
  
  const shortlists_state = useSelector((state) => state.shortlists);

  let newestIdx;
if(saved_shortlists && Object.keys(saved_shortlists).length > 0){
newestIdx = Object.keys(saved_shortlists).reverse()[0]
}
  

  const [shortlistIdx, setShortlistIdx] = useState(newestIdx || null);
  const [editForm, setEditForm] = useState(false);
  const [toggleSymbol, setToggleSymbol] = useState(`+`);
  const [referralListIdx, setReferralListIdx ] = useState(null)
console.log("referral state:", referralListIdx);
 
  const [isLoading, setIsLoading] = useState(false)


  
  const toggleFormView = () => {
    setToggleSymbol(!toggleSymbol);

    if(leftPanel === 'my-shortlists'){
      setLeftPanel('shortlist-search')
    }else{
      setLeftPanel('my-shortlists')
    }

    setCenterPanel('recent-activity')
  
  };

  


  useEffect(()=>{},[shortlists_state])
  

  useEffect(() => {
    if (user) {
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
              style={{display: leftPanel === 'shortlist-search' || centerPanel === 'shortlist-search' ? 'flex' : 'none'}}
            >
              <SearchConnectionsForm
                setIsLoading={setIsLoading}
                isLoading={isLoading}
                toggleSymbol={toggleSymbol}
                setToggleSymbol={setToggleSymbol}
              />
            </div>
           
         
        {!isTabletOrMobile && 
          <div
          id="my-shortlists"
          className={'left-panel'}
          style={{display: leftPanel === 'my-shortlists' ? 'flex' : 'none'}}
          
          >
              <MyShortlists
                shortlistIdx={shortlistIdx}
                setShortlistIdx={setShortlistIdx}
                saved_shortlists={saved_shortlists}
                setEditForm={setEditForm}
                />
            </div>
            }
              

          </div>
          <div
            id="single-shortlist-view"
            className="center-panel"
            style={{display: centerPanel === 'single-shortlist' ? 'flex' : 'none'}}
          >
            <SingleShortlistView
              setEditForm={setEditForm}
              editForm={editForm}
              setShortlistIdx={setShortlistIdx}
              shortlistIdx={shortlistIdx}
              
            />
          </div>

          <div
            id="search-results-view"
            className='center-panel'
            style={{display: centerPanel === 'search-results' ? 'flex' : 'none'}}
          >
            <SearchResultsView
              user={user}
              toggleSymbol={toggleSymbol}
              setToggleSymbol={setToggleSymbol} 
            />
          </div>


            <div id="recent-activity-view"
            className={'center-panel'}
            style={{display: centerPanel === 'recent-activity' ? 'flex' : 'none'}}
            >
              <RecentActivityFeed/>
            </div>

           <div id="referral-shortlist-view"
           className={"center-panel"}
           style={{display: centerPanel === 'referral-shortlist' ? 'flex' : 'none'}}>
            <ReferralShortlistView referralListIdx={referralListIdx}/>
            </div> 
         
            {isTabletOrMobile && centerPanel === 'calendar' &&
          <div>
            <BookingsPanel user_bookings={user_bookings}/>
          </div>
          }


          <div id='user-profile'
          className="center-panel"
          style={{display: centerPanel === 'profile' ? 'flex' : 'none' }}>
            <ProfileComponent user={user}/></div>

          <div id="my-listings-calendar-placeholder" className="right-panel">
            <MyListings_Calendar setReferralListIdx={setReferralListIdx} />
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
