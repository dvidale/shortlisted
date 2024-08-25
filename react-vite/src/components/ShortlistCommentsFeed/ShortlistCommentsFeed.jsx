import CommentsTile from '../CommentsTile'


function ShortlistCommentsFeed({shortlist}){




    return(
        <>
        <hr/>
        {/* For every person on the list, return a comments tile */}
        {shortlist.referrals.map( referral => {
            return (
                <div key={referral}>Referral # {referral}  </div>

            )
        })}
        <CommentsTile/>
        </>
    )
}


export default ShortlistCommentsFeed