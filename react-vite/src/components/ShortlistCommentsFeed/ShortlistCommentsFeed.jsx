import "../../../src/index.css";
import "../SingleShortlistView/single-shortlist.css";
import CommentsTile from "../CommentsTile";
import { useModal } from "../../context/Modal";
import DeleteReferralModal from "../DeleteReferralModal/DeleteReferralModal";
import { useSelector } from "react-redux";
import CommentThreadButton from "./CommentThreadButton";
import { useState } from "react";

function ShortlistCommentsFeed({ shortlist, editForm }) {

    const [currentReferral, setCurrentReferral ] = useState(null)

  const { setModalContent } = useModal();

  const userId = useSelector((state) => state.session.user.id);


const toggleOpenThread = (clickedIdx) =>{

  if(currentReferral !== clickedIdx){
   setCurrentReferral(clickedIdx)
  }else{
    setCurrentReferral(null)
  }



}
 

  // TODO: refactor with a join query to pull the referral ids and referred user names in one object

  // ? This object creates the combo of referral id and referred user name that I didn't know how to do in SQLAlchemy

  const referralInfoObj = {};
  let i = 0;

  for (let name of shortlist.referral_name) {
    const referral_id = shortlist.referral_idxs[i];
    referralInfoObj[referral_id] = `${name[0]} ${name[1]}`;
    i++;
  }

  const deleteReferralHandler = (id, full_name, user_id) => {
    setModalContent(
      <DeleteReferralModal idx={id} userId={user_id} fullName={full_name} />
    );
  };

  return (
    <>
 
      {/* For every referral, return a comments tile */}
      {Object.keys(referralInfoObj).length > 0 &&
        Object.entries(referralInfoObj).map(([referralIdx, fullName]) => {
          return (
            <div key={referralIdx} className="comment-tile">
              <div className="comment-thread-btn" onClick={()=> toggleOpenThread(referralIdx)} >
                <CommentThreadButton fullName={fullName} />

                {editForm && (
                  <button
                    className="delete-referral-btn"
                    onClick={() =>
                      deleteReferralHandler(referralIdx, fullName, userId)
                    }> Delete
                  </button>
                )}
              </div>
              <div className={currentReferral != referralIdx ? 'open-thread': 'close-thread'}>
              <CommentsTile shortlist={shortlist} referralIdx={referralIdx}/>
              </div>
            </div>
          );
        })}
    </>
  );
}

export default ShortlistCommentsFeed;
