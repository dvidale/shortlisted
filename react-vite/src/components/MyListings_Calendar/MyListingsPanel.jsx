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


    return(

        <>
        <div className='my-listings'>
        
        { Object.values(my_referrals).length > 0 ? (<>
        {

         Object.values(my_referrals).map( referral =>(
            <div key={referral.shortlist_id} className="listing-and-button">
                <div className="referral-thread-tile">
                    <div> • </div>
                    <div>
                    <img className="user-avatar" src={referral.createdby_photo}/>
                    </div>
                <div className='username-subject-preview'>
                    <div style={{fontWeight:`bold`}}>{referral.shortlist_title}</div>
                    <div style={{fontSize:`14px`}}>by {referral.createdby_fname} {referral.createdby_lname}</div>
                    <div className='comment-preview'>{referral.comment_thread[referral.comment_thread.length-1].text}</div>
                </div>
                </div>
            </div>

            )

            )        
        }
         </>):(<>
         No shortlistings yet.
         </>)
           
        }
        </div>
        </>
    )
}


export default MyListingsPanel