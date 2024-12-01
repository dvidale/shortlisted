import './profile-panel.css'


function ProfileComponent({user}){

    const bannerImgStyle = {
        width: '100%',
        backgroundImage: `url(${user.profile_img_url})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        position: 'relative', // Ensure the overlay is positioned correctly
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

        
        </div>
    )
}

export default ProfileComponent