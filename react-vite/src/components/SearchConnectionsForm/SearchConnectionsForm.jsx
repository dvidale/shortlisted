import './new-shortlist-form.css'
import { useMediaQuery } from 'react-responsive'
import { useEffect, useState} from 'react';
import { useDispatch} from 'react-redux'
import { buildShortlist } from "../../redux/shortlists";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { clearSearch } from '../../redux/shortlists';

function SearchConnectionsForm({setSearchSubmitted, searchFormView, setIsLoading, isLoading, toggleSymbol, setToggleSymbol}){

    const isTabletOrMobile = useMediaQuery({query: '(max-width: 1100px)'})   

    const dispatch = useDispatch();

    const [location, setLocation] = useState('')
    const [industry_area, setIndustryArea] = useState('')
    const [job_title, setJobTitle] = useState('')
    const [genre, setGenre] = useState('')
    const [start_date, setStartDate] = useState('')
    const [end_date, setEndDate] = useState('')
    
    const [errors, setErrors] = useState({})

    

    useEffect(()=>{
        if(searchFormView === false){
            setLocation('')
            setIndustryArea('')
            setJobTitle('')
            setGenre('')
            setStartDate('')
            setEndDate('')
            setErrors({})
            dispatch(clearSearch())
        }

    },[searchFormView, dispatch])


    // !BUG - if i set the job title and then switch it back to nothing, it can pass validation
    const submitHandler = (e) =>{
      e.preventDefault()

      let err ={}
    
    if(!location) err.location = 'Location required'
    if(!industry_area) err.industry_area = 'Industry area required'
    if(!job_title) err.job_title = "Job title required"
    const startDateCheck = new Date(start_date).setHours(1,0,0,0)
    
    const today = new Date().setHours(0,0,0,0)
    
    let endDateCheck
    if(end_date){
        endDateCheck = new Date(end_date)
        if(endDateCheck < today) err.end_date = 'End date cannot be in the past'
    }
         
        if(startDateCheck > endDateCheck) err.end_date = 'End date cannot be before start date'

    if(!start_date){
     err.start_date = "Start date required"   
    } else if(startDateCheck !== '' && startDateCheck !== null && startDateCheck < today) {
    err.start_date = 'Start date cannot be in the past'
    }
   

    setErrors(err)

    if(Object.keys(err).length === 0){
    
        const formData = {

            location,
            industry_area,
            job_title,
            genre: genre === '' ? null : genre,
            start_date: start_date.toISOString(),
            end_date: end_date ? end_date.toISOString() : null
        }
    //   TODO: switch "1" dispatch back to user.id after demo
        setIsLoading(true)
        dispatch(buildShortlist(1, JSON.stringify(formData)))
        .then( serverError =>{ if(serverError){
            setIsLoading(false)
            setErrors(serverError)
            setSearchSubmitted(false)
        }else{
            if(isTabletOrMobile){
                setToggleSymbol(!toggleSymbol)
            }
            // !BUG - the mobile view search submission flickers at the transition to the search results panel. Might b mor prevalent on the production server
            setSearchSubmitted(true)     
        } })
       
        
    }



}

        

// TODO: Figure out why job title dropdown moves left when a server error is returned for an invalid job title choice
// TODO: Change all errors to display through a modal instead of inline with the UI
    return(<>
    

        <form id='new-shortlist-form' 
        
        className={`show-form`} 
              
              method='POST' onSubmit={submitHandler}>
        <div>
        <label htmlFor="job-titles">
        <select name='job-titles' id='job-title-select' value={job_title} onChange={e => setJobTitle(e.target.value)} className='create-shortlist-dropdown'>
        <option value={''}>Job Title </option>
    <option value="Editor">Editor</option>
    <option value='Assistant Editor'>Assistant Editor</option>
    </select>
</label>
{/* <div >  
     <p className='error'>{errors.job_title}</p>
</div> */}

</div>
        <label htmlFor="industry-area"></label>
        <select name='industry-areas' id='industry-area-select' value={industry_area} onChange={e => setIndustryArea(e.target.value)} 
            className='create-shortlist-dropdown'>
        <option value={''}>Industry Area</option>
            <option value="Scripted Television">Scripted Television</option>
            <option value='Unscripted Television'>Unscripted Television</option>
            <option value='Dramatic Film'>Dramatic Film</option>
            <option value='Documentary'>Documentary</option>
            <option value='Commercial'>Commercial</option>
        </select>
        {/* <div >
        
 
        <p className='error'>{errors.industry_area}
            </p>
            </div> */}

        <label htmlFor="genre"></label>
        <select name='genres' id='genre-select' value={genre} onChange={e => setGenre(e.target.value)}
            className='create-shortlist-dropdown'>
            <option value={''}>Genre</option>
            <option value="Drama">Drama</option>
            <option value='Comedy'>Comedy</option>
            <option value='Horror'>Horror</option>
            <option value='Sci-Fi'>Sci-Fi</option>
            <option value='Animation'>Animation</option>
            <option value='Historical'>Historical</option>
        </select>

        {/* <div className='error'></div> */}

        <label htmlFor="location"></label>
        <select name='locations' id='location-select' value={location} onChange={e => setLocation(e.target.value)}
            className='create-shortlist-dropdown'>
            <option value={''}>Location</option>
            <option value="Los Angeles">Los Angeles</option>
            <option value='New York'>New York</option>
            <option value='Atlanta'>Atlanta</option>
            <option value='Remote'>Remote</option>
        </select>
        {/* <div >
        
     
        <p className='error'>{errors.location}</p>
        </div> */}

       

        <h2 className='panel-heading'>Start Date</h2>
       
        <div className='calendar-input' > <label htmlFor="start_date_month">
            <DatePicker selected={start_date} onChange={ start_date => setStartDate(start_date)}  />
            </label>
            {/* <div >
            
    
            <p className='error'>{errors.start_date}</p>
            </div> */}
        </div>

        <h2 className='panel-heading'>End Date</h2>
        
        <div className='calendar-input'><label htmlFor="end_date_month">
            <DatePicker selected={end_date} onChange={ end_date => setEndDate(end_date)}  />
               </label>         
            {/* <div >
               {
  
               <p className='error'>{errors.end_date}</p>}   
            </div> */}
        </div>
           
    
       <button id='submit' type="submit">SEARCH</button>
       <p className='error'>{errors.errors}</p>
       
       <h4 style={{'color': 'white'}}>{isLoading && `Loading...`}</h4>
        </form>
    

      
    </>)
}

export default SearchConnectionsForm