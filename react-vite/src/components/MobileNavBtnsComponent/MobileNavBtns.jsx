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
        <div className="mbl-btns" onClick={() => setCenterPanel('my-listings')}> Messages </div>
        <div className="mbl-btns" onClick={() => setCenterPanel('calendar')}> Calendar </div>

        </>

    )
}


export default MobileNavBtns