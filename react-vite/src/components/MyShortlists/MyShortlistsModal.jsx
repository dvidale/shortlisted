import { useModal } from "../../context/Modal"
// import MyShortlists from "./MyShortlists"

function MyShortlistsModal (){

   const { closeModal } = useModal();

    return (
        <>
        
        <button onClick={closeModal}>Close</button>

        </>
    )
}

export default MyShortlistsModal