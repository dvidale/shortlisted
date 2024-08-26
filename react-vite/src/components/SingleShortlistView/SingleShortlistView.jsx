import "../../../src/index.css";
import './single-shortlist.css'
import { useSelector} from "react-redux";
import { useEffect, useState } from 'react'
import ShortlistCommentsFeed from "../ShortlistCommentsFeed/ShortlistCommentsFeed";
import SearchDetails from "../SearchDetails/SearchDetails";


function SingleShortlistView({shortlistIdx}) {
  
  const [editForm, setEditForm] = useState(false)
  const [activeFields, setActiveFields] = useState('edit-off')
const [formBorder, setFormBorder] = useState('border-off')


  const shortlist = useSelector((state) => state.shortlists.saved_lists[shortlistIdx]);

  const [title, setTitle] = useState(shortlist.title)

  useEffect(()=>{

   setTitle(shortlist.title)


  },[shortlist])



  const editSwitch = () =>{
    editForm ? setEditForm(false) : setEditForm(true)
    activeFields === 'edit-on' ? setActiveFields('edit-off') : setActiveFields('edit-off')
    formBorder === 'border-on' ? setFormBorder('border-off') : setFormBorder('border-on')
  }

  const submitHandler = () =>{

  }

  return (
    <>
    <h2>Shortlist:</h2>
      {shortlist ? (
        <>
          
          <form id='edit-shortlist-form' onSubmit={submitHandler}>
            <div className={formBorder}>
            <textarea id='edit-shortlist-title' className={activeFields}  disabled={editForm === false} value={title} onChange={(e)=> setTitle(e.target.value)  }/>
            </div>

           
          </form>
          
          <button onClick={editSwitch}>Edit</button>
          <button>Delete</button>
          <p>{shortlist.description}</p>

          <div>Search Details</div>
          <SearchDetails params={shortlist} />
          <ShortlistCommentsFeed shortlist={shortlist} /> 
        </>
      ) : (
        <></>
      )}
    </>
  );
}

export default SingleShortlistView;
