import "../SingleShortlistView/single-shortlist.css"
import { useSelector } from "react-redux"


function ReferralShortlistView({referralListIdx}){

    let shortlist = useSelector( state => state.referrals.referral_details[referralListIdx])
   

return (

    <>
    <div>Referral convo here</div>
    { shortlist && 
    
<>    
    <div>{shortlist.shortlist_title}</div>
    
  </>  
}
    </>
)



}


export default ReferralShortlistView