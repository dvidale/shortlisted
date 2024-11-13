import "../../../src/index.css"


function MobileNavBtns({setShowShortlists, setShowCalendar }){



// * Open MyShortlists Panel 
    const openShortlists = () => {
       
        setShowShortlists(true)
       setShowCalendar(false)
    };


// * Open Calendar Panel
const openCalendar = () =>{
    setShowCalendar(true)
    setShowShortlists(false)

}


    return(
        <>
        
        <div className="mbl-btns" onClick={openShortlists}> My Shortlists </div>
        <div className="mbl-btns"> Profile </div>
        <div className="mbl-btns" onClick={openCalendar}> My Calendar </div>

        </>

    )
}


export default MobileNavBtns