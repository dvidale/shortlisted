import './server-message-modal.css'
import { useModal } from "../../context/Modal";

function ServerMessageModal({message}){

    const { closeModal } = useModal();

// write logic for if the message is an array of messages vs a single message
console.log("message in server msg modal", message);


return(
<>
<div className="server-message-modal">
            <h2>Server Message</h2>
            <p>{Object.values(message).map(
                msg => <div key={msg}>{msg}</div>
            )}</p>
            <button className="server-message-ok-btn" type='button' onClick={()=> closeModal()}>Ok</button>
        </div>
</>
)



}

export default ServerMessageModal