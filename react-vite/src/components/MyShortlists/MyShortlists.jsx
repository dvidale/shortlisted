
import '../../../src/index.css'



function MyShortlists({shortlistIdx, setShortlistIdx, saved_shortlists, setEditForm,setShowSearchResults, setShowShortlists }){

    

     
const switchShortlistAndReset = (e)=>{
    setShowShortlists(true)
    setEditForm(false)

    setShortlistIdx(e.target.value)
    setShowSearchResults(false)
}

    
   
    return(
        <>
        <h1 className='panel-heading'>My Shortlists</h1>
        { Object.keys(saved_shortlists).length > 0 ?  (
            <> 
            
                <div className='my-shortlists-list'>
                {Object.values(saved_shortlists).reverse().map( shortlist =>{

                    return(

                    
                        <div key={shortlist.id} 
                        
                        className={shortlist.id == shortlistIdx ?'title-and-button-pairs-clicked': 'title-and-button-pairs'}>
                            
                                {/* if current shortlist_id in single view  matches this btn shortlist_id, change the style to .clicked */}
                            <button className={shortlist.id == shortlistIdx ? 'shortlist-btn-clicked' : 'shortlist-btn'} value={shortlist.id}
                            onClick={ e => {
                                switchShortlistAndReset(e)    }}
                
                            > 
                            {shortlist.title} </button>
                    
                            
                             {/* <div className={shortlist.id != shortlistIdx ?'edit-delete-list-btns': 'edit-delete-list-btns-hidden'}>
                                <button>EDIT</button>
                                <button>DELETE</button>
                            </div> */}
                        </div>
                       
        
                    )
                })}
           </div>
                 
                </>  
                ):(
                <>
                <p style={{color: `white`}}>No Shortlists saved.</p>
                <p style={{color: `white`}}>Click the button above to create your first Shortlist.</p> 
                </>)
        }
       
         
        
        </>
    )
}


export default MyShortlists