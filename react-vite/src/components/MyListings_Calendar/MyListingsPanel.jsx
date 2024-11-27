import './listings-calendar.css'
import { useSelector, useDispatch } from 'react-redux'
import {useEffect} from 'react'
import { getReferrals} from '../../redux/shortlists'


function MyListingsPanel(){
    
    const my_referrals = useSelector(state => state.shortlists.my_referrals)
  
    const user = useSelector(state => state.session.user)

    const dispatch = useDispatch()
    
    useEffect(()=>{

        dispatch(getReferrals(user.id))

    },[dispatch, user.id])

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
        {
            Object.values(my_referrals).map( referral =>(
            <div key={referral.shortlist_id} className="listing-and-button">
                <div>{referral.shortlist_title}</div>
            </div>

            )

            )
        }
        </div>
        </>
    )
}


export default MyListingsPanel