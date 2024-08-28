import { useSelector } from "react-redux"
import { useModal } from "../../context/Modal"
import './user-profile.css'
import ProfileFormModal from "../ProfileFormModal/ProfileFormModal";



function UserProfileComponent(){

    const user = useSelector(state => state.session.user)
    const { setModalContent } = useModal();

    const profileEditor = () => {
        setModalContent(<ProfileFormModal/>)
        
    }

    return (
<>

<h1>User Profile</h1>

<div><img className='profile-img' alt="" width={150} height={150} src={user.profile_img_url}/></div>
<div>{user.first_name} {user.last_name}</div>

<button onClick={ () => profileEditor()}>Upload Photo</button>
<hr/>
<div>Profile Info Coming Soon!</div>
{/* 
<div>Industry:<ul> {user.industry_areas.map( area =>{
    return (
        <li key={area}>{area}</li>
    )
})}
</ul>

</div>

<div>
    Job Title:
    <br/>
    <ul>
        {user.job_title.map( title =>{
            return (
                <div key={title}>{title}</div>
            )
        })}
    </ul>
</div>


<div>
    Genres:
    <br/>
    <ul>
        {user.genres.map( genre =>{
            return(
                <div key={genre}>{genre}</div>
            )
        })}
    </ul>
</div>

<div>
    Locations:
    <br/>
    <ul>
        {user.locations.map( location =>{
            return (
                <div key={location}>{location}</div>
            )
        })}
    </ul>
</div> */}
</>


    )
}


export default UserProfileComponent