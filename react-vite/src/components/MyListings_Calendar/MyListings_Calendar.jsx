import '../../../src/index.css'
import ProfileButton from '../Navigation/ProfileButton'
import { useSelector } from 'react-redux'


function MyListings_Calendar(){

const user = useSelector(state => state.session.user)




    return(
<>
<div>

<div className='profile-btn'>  <ProfileButton /></div>
<img alt={`${user.first_name} profile photo`} src={user.profile_img_url}/>

<h1>Me, Shortlisted</h1>
<hr/>
<h2>Shortlisting 1</h2>
<h2>Shortlisting 2</h2>
<h2>Shortlisting 3</h2>
</div>

<div>
    <h1>My Calendar</h1>
</div>
</>
    )
}

export default MyListings_Calendar