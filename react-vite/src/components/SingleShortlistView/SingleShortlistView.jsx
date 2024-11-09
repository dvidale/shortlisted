import "../../../src/index.css";
import "./single-shortlist.css";
import { useMediaQuery } from 'react-responsive'
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import ShortlistCommentsFeed from "../ShortlistCommentsFeed/ShortlistCommentsFeed";
import SearchDetails from "../SearchDetails/SearchDetails";
import { fetchShortlists, updateShortlist } from "../../redux/shortlists";
import { useModal } from "../../context/Modal";
import DeleteShortlistModal from "../DeleteShortlistModal/DeleteShortlistModal";


function SingleShortlistView({ setEditForm, editForm, shortlistIdx, setShortlistIdx, showSearchResults }) {
  const dispatch = useDispatch();

  const isTabletOrMobile = useMediaQuery({query: '(max-width: 1100px)'})

  const { setModalContent } = useModal();

  // console.log("shortlistIdx at top of SingleShortListView", shortlistIdx);

  const [activeFields, setActiveFields] = useState("edit-off");
  const [formBorder, setFormBorder] = useState("border-off");

  const userId = useSelector((state) => state.session.user.id);

  const shortlist = useSelector(
    (state) => state.shortlists.saved_lists[shortlistIdx]
  );

  const saved_shortlists = useSelector(
    (state) => state.shortlists.saved_lists
  );

  useEffect(() => {
    if (userId && shortlistIdx) {
      dispatch(fetchShortlists(userId));
    }
  }, [userId, dispatch, shortlistIdx]);

  
  const [title, setTitle] = useState(shortlist ? shortlist.title : '');
  const [description, setDescription] = useState(
    shortlist ? shortlist.description : ''
  );
  const [errors, setErrors] = useState({});
  const [warnings, setWarnings] = useState({});

  useEffect(() => {
    if (shortlist) {
      setTitle(shortlist.title);
      setDescription(shortlist.description);
    }
  }, [shortlist, shortlistIdx]);




  // * Description Validation
  useEffect(() => {
    const warn = {};
    if(description !== ''){
      if (description.length === 255)
        warn.description = "There is a 255 character limit.";
    }
    setWarnings(warn);
  }, [description]);

  /* ---------------------------------------------
         Form Submission
  ----------------------------------------------- */
  const submitHandler = (e) => {
    e.preventDefault();

    const err = {};
    
    if (title === '' || title.length === 0) err.title = "A title is required";

    setErrors(err);

    if (Object.keys(err).length === 0) {
      editSwitch();

      const formData = {
        title,
        description,
      };

      const shortlistId = shortlist.id;

      dispatch(updateShortlist(shortlistId, JSON.stringify(formData)));
      // TODO: Add server response modal
    }
  };

  const editSwitch = () => {
    if (editForm) {
      setEditForm(false);
      setActiveFields("edit-off");
      setFormBorder("border-off");
    } else {
      setEditForm(true);
      setActiveFields("edit-on");
      setFormBorder("border-on");
    }
  };

  
  // * Disable and hide the edit fields for title and description
  useEffect(() => {
    if (editForm === false) {
      setActiveFields("edit-off");
      setFormBorder("border-off");
    }
  }, [editForm]);


// * DELETE Shortlist
  const handleDelete = (shortlistId) => {
    
    setModalContent(
      <DeleteShortlistModal userId={userId} shortlistId={shortlistId} />
    );
  };
// TODO: Try to remove the formBorder variable. I don't think we need it at all.
  return (
    <>
     { !isTabletOrMobile && 
      <h2 className="single-shortlist-view-heading">Shortlist:</h2>
     }
      {shortlist ? (
        <>
          <form id="edit-shortlist-form" onSubmit={submitHandler}>
           <div className="shortlist-title-and-edit-btns">
             {
               isTabletOrMobile ? (
                 
                <div>
                  <label>
                    My Shortlists
                    <div>

                    <select
                    className={"mbl-shortlists-dropdown"}
                    value={shortlistIdx}
                    onChange={e => setShortlistIdx(e.target.value)}
                    >
                      {Object.values(saved_shortlists).map( shortlist => {

                        return(
                          <option key={shortlist.id} value={shortlist.id}>{shortlist.title}</option>
                        )
                      }

                      )}
                  </select>
                    </div>
                  </label>
                  </div>
                
              ):(
                
                <div className={formBorder}>
                <textarea
                id="edit-shortlist-title"
                className={activeFields}
                disabled={editForm === false}
                value={title}
                placeholder="Please give this shortlist a title"
                onChange={(e) => setTitle(e.target.value)}
              />
               <p className="error">{errors.title}</p>
            </div>
              
              )

             } 
            <div className="edit-delete-save-btns">
            
            {(!isTabletOrMobile && editForm) && <button type="submit">Save</button>}
            {(!isTabletOrMobile && !editForm) && (
              <button type='button' onClick={editSwitch}>{`Edit`}</button>
            )}
            { isTabletOrMobile &&
              <button type='button' onClick={""}>{`Edit`}</button>
            }


            <button type='button'
              disabled={editForm}
              className="single-shortlist-delete-btn"
              onClick={() => handleDelete(shortlist.id)}
            >
              Delete
            </button>
            
            </div>
</div>
           {
              isTabletOrMobile ? (<>
              </>):
              (
               <div className={formBorder}>
              <textarea
                id="edit-shortlist-desc"
                className={activeFields}
                disabled={editForm === false}
                value={description}
                maxLength={255}
                onChange={(e) => setDescription(e.target.value)}
              />
            </div>
              )

           }
           
          </form>
              <p className="error">{warnings.description}</p>
              
          <SearchDetails params={shortlist} showSearchResults={showSearchResults} />
         
          
          <div className='shortlist-comments-feed'>
          <ShortlistCommentsFeed shortlist={shortlist} editForm={editForm} />
          </div>
        </>
      ) : (
        <>
          <p> Choose a Shortlist to view!</p>
        </>
      )}
    </>
  );
}

export default SingleShortlistView;
