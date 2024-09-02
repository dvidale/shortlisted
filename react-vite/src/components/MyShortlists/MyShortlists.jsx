
import '../../../src/index.css'



function MyShortlists({shortlistIdx, setShortlistIdx, saved_shortlists, setEditForm,setShowSearchResults }){

    

     
const switchShortlistAndReset = (e)=>{

    setEditForm(false)

    setShortlistIdx(e.target.value)
    setShowSearchResults(false)
}

    
   
    return(
        <>
        { Object.keys(saved_shortlists).length > 0 ?  (
            <> 
            <h1 className='panel-heading'>My Shortlists</h1>
                <div className='my-shortlists-list'>
                {Object.values(saved_shortlists).reverse().map( shortlist =>{

                    return(

                    
                        <div key={shortlist.id} 
                        
                        className={shortlist.id == shortlistIdx ?'title-and-button-pairs-clicked': 'title-and-button-pairs'}>
                            
                                {/* if current shortlist_id in single view  matches this btn shortlist_id, change the style to .clicked */}
                            <button className={shortlist.id == shortlistIdx ? 'shortlist-btn-clicked' : 'shortlist-btn'} value={shortlist.id}
                            onClick={ e => switchShortlistAndReset(e)    }
                
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
                   <h1>No Shortlists Yet?</h1> 
                   <h1>Create one!</h1>
                   
                </>)
        }
       
         
        
        </>
    )
}


export default MyShortlists