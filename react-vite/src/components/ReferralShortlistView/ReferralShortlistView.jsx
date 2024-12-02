import "../SingleShortlistView/single-shortlist.css"
import { useSelector } from "react-redux"


function ReferralShortlistView({referralListIdx}){

    const shortlist = useSelector( state => state.shortlists.my_referrals[referralListIdx])
   

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