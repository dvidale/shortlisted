import ReferralShortlistMsgs from "../ReferralShortlistMsgs/ReferralShortlistMsgs"
import "../SingleShortlistView/single-shortlist.css"
import { useSelector } from "react-redux"


function ReferralShortlistView({referralListIdx}){

    let referral = useSelector( state => state.referrals.referral_details[referralListIdx])
   

return (

    <>
    
    { referral && 
    
<>    
   
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