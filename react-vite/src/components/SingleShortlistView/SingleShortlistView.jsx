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
function SingleShortlistView({ shortlistIdx }) {
  const dispatch = useDispatch();

  const { setModalContent } = useModal();

  // console.log("shortlistIdx at top of SingleShortListView", shortlistIdx);
  const [editForm, setEditForm] = useState(false);
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

  useEffect(() => {
    if (shortlist) {
      setTitle(shortlist.title);
      setDescription(shortlist.description);
    }
  }, [shortlist, shortlistIdx]);

  const submitHandler = (e) => {
    e.preventDefault();
    editSwitch();

    const formData = {
      title,
      description,
    };

    const shortlistId = shortlist.id;

    dispatch(updateShortlist(shortlistId, JSON.stringify(formData)));
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

  const handleDelete = (shortlist) => {

    setModalContent(<DeleteShortlistModal userId={userId} shortlist={shortlist}/>)
  };

  return (
    <>
      <h2>Shortlist:</h2>
      {shortlist ? (
        <>
          <form id="edit-shortlist-form" onSubmit={submitHandler}>
            <div className={formBorder}>
              <textarea
                id="edit-shortlist-title"
                className={activeFields}
                disabled={editForm === false}
                value={title}
                onChange={(e) => setTitle(e.target.value)}
              />
            </div>

            <div className={formBorder}>
              <textarea
                id="edit-shortlist-desc"
                className={activeFields}
                disabled={editForm === false}
                value={description}
                onChange={(e) => setDescription(e.target.value)}
              />
            </div>

            <button type={`button`} onClick={editSwitch}>{`Edit`}</button>
            <button disabled={editForm}
              className="single-shortlist-delete-btn"
              onClick={() => handleDelete(shortlist, shortlist.id)}
            >
              Delete
            </button>
            {editForm && <button type="submit">Save Changes</button>}
          </form>

          <div>Search Details</div>
          <SearchDetails params={shortlist} />
          <ShortlistCommentsFeed shortlist={shortlist} editForm={editForm} />
        </>
      ) : (
        <>
          {" "}
          <p> Loading...</p>
        </>
      )}
    </>
  );
}

export default SingleShortlistView;
