import '../../../src/index.css'
import CommentsTile from '../CommentsTile'
import { useModal } from '../../context/Modal'
import DeleteReferralModal from '../DeleteReferralModal/DeleteReferralModal';
import { useSelector } from 'react-redux';


function ShortlistCommentsFeed({shortlist, editForm}){

    const { setModalContent } = useModal();

    const userId = useSelector(state => state.session.user.id)

      

// TODO: refactor with a join query to pull the referral ids and referred user names in one object

// ? This object creates the combo of referral id and referred user name that I didn't know how to do in SQLAlchemy

    const referralInfoObj = {}
    let i=0
    
    for (let name of shortlist.referral_name){
            const referral_id = shortlist.referral_idxs[i]
            referralInfoObj[referral_id]=`${name[0]} ${name[1]}`
            i++;
        }
 
        const deleteReferralHandler =(id, full_name, user_id) =>{

            setModalContent(<DeleteReferralModal idx={id} userId={user_id} fullName={full_name}/>)
        }
    
    
    
    return(
        <>
        <hr/>
        {/* For every referral, return a comments tile */}
        {Object.keys(referralInfoObj).length > 0 && Object.entries(referralInfoObj).map(  ([referralIdx, fullName]) => {
                
            return (
            
                <div key={referralIdx} className='comment-tile'>{fullName} 
                {editForm && <button className='delete-referral-btn' onClick={()=> deleteReferralHandler(referralIdx, fullName, userId)}>Delete</button>} <CommentsTile shortlist={shortlist} referralIdx={referralIdx}/>
                 </div>
 
            )
        })}
        
        </>
    )
}


export default ShortlistCommentsFeed