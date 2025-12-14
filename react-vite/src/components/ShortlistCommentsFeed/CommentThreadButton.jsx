import { VscAccount } from "react-icons/vsc";
import { FaRegComments } from "react-icons/fa";

function CommentThreadButton({fullName, referral_photo_url}){


    return(
<>
{referral_photo_url ? <img className='user-avatar' src={referral_photo_url} alt={<VscAccount />} /> : <span className="user-avatar-fallback"><VscAccount /></span>}
<span className='referral-fullName'>{fullName}</span>
<FaRegComments />
</>

    )
}


export default CommentThreadButton