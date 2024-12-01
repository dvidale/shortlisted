
import '../../../src/index.css'
import { useContext } from 'react'
import { PanelViews } from '../../context/PanelView'

function MyShortlists({shortlistIdx, setShortlistIdx, saved_shortlists, setEditForm}){

    const {setCenterPanel} = useContext(PanelViews)  

    // TODO: Replace the EditForm logic with absolute positioned form fields over the title and description areas
     
const switchShortlistAndReset = (e)=>{
    setCenterPanel('single-shortlist')
    setEditForm(false)
    setShortlistIdx(e.target.value)

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
                            onClick={ e => { switchShortlistAndReset(e) }}
                
                            > 
                            {shortlist.title} </button>
                    
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