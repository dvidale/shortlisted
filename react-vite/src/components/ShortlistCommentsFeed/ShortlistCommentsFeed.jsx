import '../../../src/index.css'
import CommentsTile from '../CommentsTile'
import { useModal } from '../../context/Modal'


function ShortlistCommentsFeed({shortlist, editForm}){


    const referralInfoObj = {}
    let i=0
    
    for (let name of shortlist.referral_name){
            const referral_id = shortlist.referral_idxs[i]
            referralInfoObj[referral_id]=`${name[0]} ${name[1]}`
            i++;
        }
 
        const deleteReferralHandler =() =>{
            

        }
    
    
    
    return(
        <>
        <hr/>
        {/* For every person on the list, return a comments tile */}
        {Object.keys(referralInfoObj).length > 0 && Object.entries(referralInfoObj).map(  ([idx, fullName]) => {
                
            return (
            
                <div key={idx} className='comment-tile'>{fullName} 
                <CommentsTile id={idx}/> {editForm && <button className='delete-comment-btn' onClick={()=> deleteReferralHandler(idx)}>Delete</button>}
                 </div>
 
            )
        })}
        
        </>
    )
}


export default ShortlistCommentsFeed