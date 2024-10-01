import './server-message-modal.css'
import { useModal } from "../../context/Modal";

function ServerMessageModal({message}){

    const { closeModal } = useModal();

return(
<>
<div className="server-message-modal">
            <h2>Server Message</h2>
            <div>{Object.values(message).map(
                msg => <p key={msg}>{msg}</p>
            )}</div>
            <button className="server-message-ok-btn" type='button' onClick={()=> closeModal()}>Ok</button>
        </div>
</>
)



}

export default ServerMessageModal