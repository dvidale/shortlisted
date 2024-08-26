import '../../../src/index.css'
import CommentsTile from '../CommentsTile'


function ShortlistCommentsFeed({shortlist, editForm}){


    const referralInfoObj = {}

    for (let idx of shortlist.referral_idxs){
        for (let name of shortlist.referral_name){

            referralInfoObj[idx]=`${name[0]} ${name[1]}`
        }
    }
    
 
    
    
    
    return(
        <>
        <hr/>
        {/* For every person on the list, return a comments tile */}
        {Object.keys(referralInfoObj).length > 0 && Object.entries(referralInfoObj).map(  ([idx, fullName]) => {
                
            return (
            
                <div key={idx} className='comment-tile'>{fullName} 
                <CommentsTile id={idx}/> {editForm && <button>Delete</button>}
                 </div>
 
            )
        })}
        
        </>
    )
}


export default ShortlistCommentsFeed