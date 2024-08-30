import "../../../src/index.css";
import "./single-shortlist.css";
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import ShortlistCommentsFeed from "../ShortlistCommentsFeed/ShortlistCommentsFeed";
import SearchDetails from "../SearchDetails/SearchDetails";
import { fetchShortlists, updateShortlist } from "../../redux/shortlists";
import { useModal } from "../../context/Modal";
import DeleteShortlistModal from "../DeleteShortlistModal/DeleteShortlistModal";

// !BUG - the default shortlist does not load automatically
function SingleShortlistView({ setEditForm, editForm, setShortlistIdx, shortlistIdx, showSearchResults }) {
  const dispatch = useDispatch();

  const { setModalContent } = useModal();

  // console.log("shortlistIdx at top of SingleShortListView", shortlistIdx);

  const [activeFields, setActiveFields] = useState("edit-off");
  const [formBorder, setFormBorder] = useState("border-off");

  const userId = useSelector((state) => state.session.user.id);

  const shortlist = useSelector(
    (state) => state.shortlists.saved_lists[shortlistIdx]
  );

  useEffect(() => {
    if (userId && shortlistIdx) {
      dispatch(fetchShortlists(userId));
    }
  }, [userId, dispatch, shortlistIdx]);

  // console.log(">>>> current shortlist in singleview:", shortlist);
  const [title, setTitle] = useState(shortlist ? shortlist.title : null);
  const [description, setDescription] = useState(
    shortlist ? shortlist.description : null
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
    if(description !== null){
      if (description.length === 255)
        warn.description = "There is a 255 character limit.";
    }
    setWarnings(warn);
  }, [description]);

  /* -------------------
         Form Submission
  ---------------------- */
  const submitHandler = (e) => {
    e.preventDefault();

    const err = {};
    
    if (title === null || title.length === 0) err.title = "A title is required";

    setErrors(err);

    if (Object.keys(err).length === 0) {
      editSwitch();

      const formData = {
        title,
        description,
      };

      const shortlistId = shortlist.id;

      dispatch(updateShortlist(shortlistId, JSON.stringify(formData)));
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
  const handleDelete = (shortlist) => {
    setModalContent(
      <DeleteShortlistModal userId={userId} shortlist={shortlist} setShortlistIdx={setShortlistIdx} />
    );
  };

  return (
    <>
      <h2>Shortlist:</h2>
      {shortlist ? (
        <>
          <form id="edit-shortlist-form" onSubmit={submitHandler}>
           <div className="shortlist-title-and-edit-btns">
            <div className={formBorder}>
              <textarea
                id="edit-shortlist-title"
                className={activeFields}
                disabled={editForm === false}
                value={title}
                placeholder="Please give this shortlist a title"
                onChange={(e) => setTitle(e.target.value)}
              />
              {errors.title && <p className="error">{errors.title}</p>}
            </div>
            <div className="edit-delete-save-btns">
{editForm && <button type="submit">Save</button>}
            {!editForm && (
              <button type={`button`} onClick={editSwitch}>{`Edit`}</button>
            )}

            <button
              disabled={editForm}
              className="single-shortlist-delete-btn"
              onClick={() => handleDelete(shortlist, shortlist.id)}
            >
              Delete
            </button></div>
</div>
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
