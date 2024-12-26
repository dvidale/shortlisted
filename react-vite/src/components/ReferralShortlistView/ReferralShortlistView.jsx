import ReferralShortlistMsgs from "../ReferralShortlistMsgs/ReferralShortlistMsgs"
import "../SingleShortlistView/single-shortlist.css"
import { useSelector } from "react-redux"
import { useMediaQuery } from 'react-responsive'

function ReferralShortlistView({referralListIdx}){

    const isTabletOrMobile = useMediaQuery({query: '(max-width: 1100px)'})

    let referral = useSelector( state => state.referrals.referral_details[referralListIdx])
   

return (

    <>
    
    { referral && 
    
<>    
   { isTabletOrMobile &&  <div id="messages-back-btn">
    {`<`} Messages
   </div>}
    <div>{referral.createdby_fname} {referral.createdby_lname}{`'s`} Shortlist:</div>
    <div> <h2 className="panel-heading">{referral.shortlist_title}</h2> </div>

    <div>{referral.shortlist_desc}</div>

    <div>{referral.createdby_fname}</div>
    <div className={'comment-thread'}>
        <ReferralShortlistMsgs referral={referral}/>
    </div>
    
  </>  
}
    </>
)



}


export default ReferralShortlistView