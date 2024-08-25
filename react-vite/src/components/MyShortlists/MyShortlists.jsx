import '../../../src/index.css'




function MyShortlists({saved_shortlists}){

    




    return(
        <>
        <h1>My Shortlists</h1>
        { Object.keys(saved_shortlists).length ? 0 (
            <> 
                {Object.values(saved_shortlists).map( shortlist =>{

                    return(
                        <div key={shortlist.id}>
                            <button>{shortlist.title}</button>
                        </div>
        
                    )
                })}
                </>
                ):(
                <>
                    
                    
                </>)
        }
       
        
        
        </>
    )
}


export default MyShortlists