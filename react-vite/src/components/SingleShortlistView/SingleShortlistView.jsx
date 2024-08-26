import "../../../src/index.css";
import "./single-shortlist.css";
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import ShortlistCommentsFeed from "../ShortlistCommentsFeed/ShortlistCommentsFeed";
import SearchDetails from "../SearchDetails/SearchDetails";
import { updateShortlist } from "../../redux/shortlists";

function SingleShortlistView({ shortlistIdx }) {
  const dispatch = useDispatch();

  const [editForm, setEditForm] = useState(false);
  const [activeFields, setActiveFields] = useState("edit-off");
  const [formBorder, setFormBorder] = useState("border-off");

  const shortlist = useSelector(
    (state) => state.shortlists.saved_lists[shortlistIdx]
  );
  // console.log(">>>> current shortlist in singleview:", shortlist);
  const [title, setTitle] = useState(shortlist.title);
  const [description, setDescription] = useState(shortlist.description);

  useEffect(() => {
    setTitle(shortlist.title);
    setDescription(shortlist.description);
  }, [shortlist]);

  const submitHandler = (e) => {
    e.preventDefault();
    editSwitch();

    const formData = {
      title,
      description,
    };

    const shortlistId = shortlist.id;

    dispatch(updateShortlist(shortlistId, JSON.stringify(formData)));

    // console.log(">>>> submit successful");
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
            <button>Delete</button>
            {editForm && <button type="submit">Save Changes</button>}
          </form>

          <div>Search Details</div>
          <SearchDetails params={shortlist} />
          <ShortlistCommentsFeed shortlist={shortlist} editForm={editForm} />
        </>
      ) : (
        <></>
      )}
    </>
  );
}

export default SingleShortlistView;
