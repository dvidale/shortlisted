import ReferralShortlistMsgs from "../ReferralShortlistMsgs/ReferralShortlistMsgs"
import "../SingleShortlistView/single-shortlist.css"
import { useSelector } from "react-redux"


function ReferralShortlistView({referralListIdx}){

    let referral = useSelector( state => state.referrals.referral_details[referralListIdx])
   

return (

    <>
    
    { referral && 
    
<>    
   
    <div>{referral.shortlist_title}</div>
    <div>{referral.shortlist_desc}</div>
    
     <div><img className="user-avatar" src={referral.createdby_photo}/></div>
    <div>{referral.createdby_fname} {referral.createdby_lname}</div>
    <div className={'comment-thread'}>
        <ReferralShortlistMsgs referral={referral}/>
    </div>
    
  </>  
}
    </>
)



}


export default ReferralShortlistView