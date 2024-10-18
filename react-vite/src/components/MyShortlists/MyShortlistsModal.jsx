import { useModal } from "../../context/Modal"
import MyShortlists from "./MyShortlists"

function MyShortlistsModal (){

   const { closeModal } = useModal();

    return (
        <>
        <MyShortlists/>
        <button onClick={closeModal}>Ok</button>

        </>
    )
}

export default MyShortlistsModal