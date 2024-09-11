import './listings-calendar.css'

function MyListingsPanel(){
  
    const names_lists =[

        { name:'Naina Raj' ,
            list:'Editors for 2025 Indies in LA'
        },
        { name: 'Isabella Williams',
            list:'AEs for Award-Winning TV Series'
        },
        { name:'Brandon Carter' ,
            list:'Editors with Music Doc Experience'
        },
        { name:'Chetan Sharma' ,
            list:'Rising Assistant Editors for Pilots'
        }
    ]

    return(

        <>
        <div className='my-listings'>
        {names_lists.map( shortlist => (

            <div className="listing-and-button" key={shortlist.name}><div>
                &quot;{shortlist.list}&quot;
                </div>
                by {shortlist.name} <button className='smaller-btn'>Comment</button>
                </div>
        ))}
        </div>
        </>
    )
}


export default MyListingsPanel