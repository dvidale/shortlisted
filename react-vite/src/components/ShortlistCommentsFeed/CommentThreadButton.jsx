import { VscAccount } from "react-icons/vsc";
import { FaRegComments } from "react-icons/fa";

function CommentThreadButton({fullName}){


    return(
<>
<span className='avatar'><VscAccount /> </span>
<span className='referral-fullName'>{fullName}</span>
<FaRegComments />
</>

    )
}


export default CommentThreadButton