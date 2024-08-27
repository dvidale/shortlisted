import '../../../src/index.css'
import CommentsTile from '../CommentsTile'
import { useModal } from '../../context/Modal'
import DeleteReferralModal from '../DeleteReferralModal/DeleteReferralModal';
import { useSelector } from 'react-redux';


function ShortlistCommentsFeed({shortlist, editForm}){

    const { setModalContent } = useModal();

    const userId = useSelector(state => state.session.user.id)

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
        {/* For every person on the list, return a comments tile */}
        {Object.keys(referralInfoObj).length > 0 && Object.entries(referralInfoObj).map(  ([idx, fullName]) => {
                
            return (
            
                <div key={idx} className='comment-tile'>{fullName} 
                <CommentsTile id={idx}/> {editForm && <button className='delete-referral-btn' onClick={()=> deleteReferralHandler(idx, fullName, userId)}>Delete</button>}
                 </div>
 
            )
        })}
        
        </>
    )
}


export default ShortlistCommentsFeed