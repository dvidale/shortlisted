import './listings-calendar.css'
import { useSelector, useDispatch } from 'react-redux'
import { useEffect, useContext } from 'react'
import { getReferrals} from '../../redux/shortlists'
import { PanelViews } from '../../context/PanelView'


function MyListingsPanel({setReferralListIdx}){
    
    const my_referrals = useSelector(state => state.shortlists.my_referrals)
    
    const user = useSelector(state => state.session.user)

    const { setCenterPanel } = useContext(PanelViews)

    const dispatch = useDispatch()
    
    useEffect(()=>{

        dispatch(getReferrals(user.id))

    },[dispatch, user.id])

    const switchReferralList = (e)=>{
        setReferralListIdx(e.target.value)
        // console.log("referral list id:", e.target.value);
        setCenterPanel('referral-shortlist');
    }


    return(

        <>
        <div className='my-listings'>
        
        { Object.values(my_referrals).length > 0 ? (<>
        {

         Object.values(my_referrals).map( referral =>(
            <div key={referral.shortlist_id} className="listing-and-button"
            value={referral.shortlist_id}
            onClick={ (e) =>{ switchReferralList(e)  }}
            >
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