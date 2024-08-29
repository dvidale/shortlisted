import { VscAccount } from "react-icons/vsc";
import { FaRegComments } from "react-icons/fa";

function CommentThreadButton({fullName}){


    return(
<>
<VscAccount />
{fullName}
<FaRegComments />
</>

    )
}


export default CommentThreadButton