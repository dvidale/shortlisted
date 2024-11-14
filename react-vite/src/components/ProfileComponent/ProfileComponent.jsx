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
        {user.first_name} {user.last_name}
        
        </div>
    )
}

export default ProfileComponent