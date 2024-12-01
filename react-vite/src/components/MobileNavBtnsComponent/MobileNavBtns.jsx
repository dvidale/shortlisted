import "../../../src/index.css"
import { useContext } from "react";
import { PanelViews } from "../../context/PanelView";


function MobileNavBtns(){

const {setCenterPanel} = useContext(PanelViews)








    return(
        <>
        <div className="mbl-btns" onClick={ () => setCenterPanel('shortlist-search')}> New Shortlist</div>
        <div className="mbl-btns" onClick={() => setCenterPanel('single-shortlist')}> My Shortlists </div>
        <div className="mbl-btns" onClick={() => setCenterPanel('profile')}>  Profile </div>
        <div className="mbl-btns" onClick={() => setCenterPanel('calendar')}> My Calendar </div>

        </>

    )
}


export default MobileNavBtns