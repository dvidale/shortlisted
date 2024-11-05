import "../../../src/index.css"
import MyShortlistsModal from "../MyShortlists/MyShortlistsModal"
import { useModal } from "../../context/Modal"

function MobileNavBtns(){

const { setModalContent } = useModal();

// * Open MyShortlists Modal 
    const openShortlists = () => {
        setModalContent(
            <MyShortlistsModal />
        );
    };


    return(
        <>
        
        <div className="mbl-btns" onClick={openShortlists}> My Shortlists </div>
        <div className="mbl-btns"> Profile </div>
        <div className="mbl-btns"> My Calendar </div>

        </>

    )
}


export default MobileNavBtns