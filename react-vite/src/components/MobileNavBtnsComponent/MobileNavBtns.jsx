import "../../../src/index.css"


function MobileNavBtns({setShowShortlists }){



// * Open MyShortlists Modal 
    const openShortlists = () => {
       
        setShowShortlists(true)
       
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