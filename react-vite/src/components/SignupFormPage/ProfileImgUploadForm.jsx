import { useState } from 'react'
import { useDispatch } from 'react-redux';
import { createImage } from '../../redux/img-test';
import { useNavigate } from 'react-router-dom'

function ProfileImageUploadForm(){
    const [image, setImage] = useState(null);
    const [imageLoading, setImageLoading] = useState(false);

    const navigate = useNavigate(); // so that we can redirect after the image upload is successful

    const dispatch = useDispatch()
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("image", image);
        // aws uploads can be a bit slow—displaying
        // some sort of loading message is a good idea
        setImageLoading(true);
        await dispatch(createImage(formData));
        navigate("/");
    }

    return (
        <form 
            onSubmit={handleSubmit}
            encType="multipart/form-data"
        >
            <input
              type="file"
              accept="image/*"
              onChange={(e) => setImage(e.target.files[0])}
            />
            <button type="submit">Submit</button>
            {(imageLoading)&& <p>Loading...</p>}
        </form>
    )

}


export default ProfileImageUploadForm