import './profile-panel.css'
import {useMediaQuery} from 'react-responsive';
import { resetShortlistState } from '../../redux/shortlists';
import { resetCommentsState } from '../../redux/comments';
import { resetReferralThreads } from '../../redux/my-referrals';
import { thunkLogout } from '../../redux/session';
import { useDispatch} from 'react-redux';


function ProfileComponent({user}){

    const dispatch = useDispatch();
    const isTabletOrMobile = useMediaQuery({query: '(max-width: 1100px)'})

    const bannerImgStyle = {
        width: '100%',
        backgroundImage: `url(${user.profile_img_url})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        position: 'relative', // Ensure the overlay is positioned correctly
    };

    const logout = (e) => {
    e.preventDefault();
    dispatch(resetShortlistState())
    .then(()=> dispatch(resetCommentsState()))
    .then(()=> dispatch(resetReferralThreads()))
    .then(()=> dispatch(thunkLogout()))
    .then(()=> closeMenu())
    
  };

   

    return (
        <div id='profile-container'>
            <div className={'profile-img-container'} style={bannerImgStyle}> </div>
            <div id='user-name-and-title'>

            <h1 id="user-name" className='profile-heading'>
             {user.first_name} {user.last_name}
        </h1>
        
        <div id="user-job-titles">
           <h2 className='profile-heading'> 
            {user.job_title.join(" • ")}
            </h2> 
        </div>
        </div>


        <h3 id="industry-area-title" className='profile-heading'>Industry Area:</h3>
        <div>
            {user.industry_areas.join(" • ")}
        </div>
        <h3 id="genre-title" className='profile-heading'>Genre:</h3>
        <div>
            {user.genres.join(" • ")}
        </div>
        <h3 id="location-title" className='profile-heading'>Location:</h3>
        <div>
            {user.locations.join(" • ")}
        </div>

        <h3 id='links-title' className='profile-heading'>Links:</h3>
        <div>Resume | IMDB | Portfolio</div>
        
        {isTabletOrMobile && <div><button onClick={logout}>Log Out</button></div>}
        </div>
        
    )
}

export default ProfileComponent