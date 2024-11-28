import '../../../src/index.css'
import './listings-calendar.css'
import ProfileButton from '../Navigation/ProfileButton'
import { useDispatch, useSelector } from 'react-redux'
import { getMyBookings } from '../../redux/bookings'
import { useEffect } from 'react'
import BookingsPanel from './BookingsPanel'
import MyListingsPanel from './MyListingsPanel'



function MyListings_Calendar(){

const user = useSelector(state => state.session.user)
const user_bookings = useSelector(state => state.bookings.user_bookings)

const dispatch = useDispatch()


const bannerImgStyle = {
    width: '100%',
    backgroundImage: `url(${user.profile_img_url})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    position: 'relative', // Ensure the overlay is positioned correctly
};


useEffect(()=>{

    dispatch(getMyBookings(user.id))
  

},[dispatch,user.id])


    return(
<>
<div>

<div className='profile-btn'>  <ProfileButton /></div>
{/* <img height={100} alt={`${user.first_name} profile photo`} src=

{user.profile_img_url}/> */}

<div className={'profile-img-container'} style={bannerImgStyle}> </div>

<div></div>
<h1>Me, Shortlisted</h1>

<MyListingsPanel/>
</div>
      
    <BookingsPanel user_bookings={user_bookings}/>
    

</>
    )
}

export default MyListings_Calendar