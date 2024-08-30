import '../../../src/index.css'
import ProfileButton from '../Navigation/ProfileButton'
import { useSelector } from 'react-redux'


function MyListings_Calendar(){

const user = useSelector(state => state.session.user)

const bannerImgStyle = {
    width: '100%',
    backgroundImage: `url(${user.profile_img_url})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    position: 'relative', // Ensure the overlay is positioned correctly
};


    return(
<>
<div>

<div className='profile-btn'>  <ProfileButton /></div>
{/* <img height={100} alt={`${user.first_name} profile photo`} src=

{user.profile_img_url}/> */}

<div className={'profile-img-container'} style={bannerImgStyle}>Upload photo feature coming soon. </div>

<div></div>
<h1>Me, Shortlisted</h1>
<hr/>
<h2>Shortlisting 1</h2>
<h2>Shortlisting 2</h2>
<h2>Shortlisting 3</h2>
</div>

<div>
    <h1>My Calendar</h1>
    <div className='cal-box'>
        Feature Coming Soon
    </div>
</div>
</>
    )
}

export default MyListings_Calendar