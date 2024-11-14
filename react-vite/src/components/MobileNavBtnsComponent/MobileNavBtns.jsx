import "../../../src/index.css"


function MobileNavBtns({setShowShortlists, setShowCalendar, viewSearchForm, setSearchSubmitted, setShowSearchResults, setSearchFormView, setShowProfile }){



// * Open MyShortlists Panel 
    const openShortlists = () => {
       
    setShowShortlists(true)
    setShowCalendar(false)
    setSearchSubmitted(false)
    setShowSearchResults(false)
    setSearchFormView(false)
    setShowProfile(false)
    };


// * Open Calendar Panel
const openCalendar = () =>{
    setShowCalendar(true)
    setShowShortlists(false)
    setSearchSubmitted(false)
    setShowSearchResults(false)
    setSearchFormView(false)
    setShowProfile(false)

}

// * Open Profile Panel
const openProfilePanel = () =>{
    
    setShowProfile(true)
    setShowShortlists(false)
    setSearchSubmitted(false)
    setShowSearchResults(false)
    setSearchFormView(false)
    setShowCalendar(false)

}


    return(
        <>
        <div className="mbl-btns" onClick={viewSearchForm}> New Shortlist</div>
        <div className="mbl-btns" onClick={openShortlists}> My Shortlists </div>
        <div className="mbl-btns" onClick={openProfilePanel}>  Profile </div>
        <div className="mbl-btns" onClick={openCalendar}> My Calendar </div>

        </>

    )
}


export default MobileNavBtns