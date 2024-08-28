import { useState } from 'react';
import { useDispatch} from 'react-redux'
import { buildShortlist } from "../../redux/shortlists";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";


function SearchConnectionsForm({user}){

    const dispatch = useDispatch();
    


    const [location, setLocation] = useState(null)
    const [industry_area, setIndustryArea] = useState(null)
    const [job_title, setJobTitle] = useState(null)
    const [genre, setGenre] = useState(null)
    const [start_date, setStartDate] = useState(new Date())
    const [end_date, setEndDate] = useState(null)

    const [errors, setErrors] = useState({})

   
    const submitHandler = (e) =>{
      e.preventDefault()

      let err ={}
    
    if(!location) err.location = 'Location required'
    if(!industry_area) err.industry_area = 'Industry area required'
    if(!job_title) err.job_title = "Job title required"
    if(!start_date) err.start_date = "Start date required"
    const startDateCheck = new Date(start_date)

    const today = new Date().setHours(0,0,0,0)

    let endDateCheck
    if(end_date){
    endDateCheck = new Date(end_date)
    if(endDateCheck < today) err.end_date = 'End date cannot be in the past'
    if(startDateCheck > endDateCheck) err.end_date = 'End date cannot be before start date'
    }
   
    if(startDateCheck < today) err.start_date = 'Start date cannot be in the past'
    

setErrors(err)

if(!Object.keys(errors).length){

const formData = {

            location,
            industry_area,
            job_title,
            genre,
            start_date: start_date.toISOString(),
            end_date: end_date ? end_date.toISOString() : null
        }

        dispatch(buildShortlist(user.id, JSON.stringify(formData)))
      
    }



}

        


    return(<>

    <h1>Build a Shortlist</h1>
        <form id='search-connections' method='POST' onSubmit={submitHandler}>
        <div>
        <label htmlFor="job-titles">
        <select name='job-titles' id='job-title-select' value={job_title} onChange={e => setJobTitle(e.target.value)}>
        <option value={null}>Job Title </option>
    <option value="Editor">Editor</option>
    <option value='Assistant Editor'>Assistant Editor</option>
    </select>
</label>
{errors.job_title && <p className='error'>{errors.job_title}</p>}
</div>
        <label htmlFor="industry-area"></label>
        <select name='industry-areas' id='industry-area-select' value={industry_area} onChange={e => setIndustryArea(e.target.value)}>
        <option value={null}>Industry Area</option>
            <option value="Scripted Television">Scripted Television</option>
            <option value='Unscripted Television'>Unscripted Television</option>
            <option value='Dramatic Film'>Dramatic Film</option>
            <option value='Documentary'>Documentary</option>
            <option value='Commercial'>Commercial</option>
        </select>
        {errors.industry_area && <p className='error'>{errors.industry_area}</p>}

        <label htmlFor="genre"></label>
        <select name='genres' id='genre-select' value={genre} onChange={e => setGenre(e.target.value)}>
            <option value={null}>Genre</option>
            <option value="Drama">Drama</option>
            <option value='Comedy'>Comedy</option>
            <option value='Horror'>Horror</option>
            <option value='Sci-Fi'>Sci-Fi</option>
            <option value='Animation'>Animation</option>
            <option value='Historical'>Historical</option>
        </select>

        <label htmlFor="location"></label>
        <select name='locations' id='location-select' value={location} onChange={e => setLocation(e.target.value)}>
            <option value={null}>Location</option>
            <option value="Los Angeles">Los Angeles</option>
            <option value='New York'>New York</option>
            <option value='Atlanta'>Atlanta</option>
            <option value='Remote'>Remote</option>
        </select>
        {errors.location && <p className='error'>{errors.location}</p>}

       

        <p>Start Date</p>
        <label htmlFor="start_date_month"></label>
        <div>
            <DatePicker selected={start_date} onChange={ start_date => setStartDate(start_date)}  />
            {errors.start_date && <p className='error'>{errors.start_date}</p>}
        </div>

        <p>End Date</p>
        <label htmlFor="end_date_month"></label>
        <div>
            <DatePicker selected={end_date} onChange={ end_date => setEndDate(end_date)}  />

            {errors.end_date && <p className='error'>{errors.end_date}</p>}               
        </div>
           
    
       <button id='submit' type="submit">Search</button>

        </form>
    

      
    </>)
}

export default SearchConnectionsForm