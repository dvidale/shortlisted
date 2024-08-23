import { useState, useEffect } from "react"
import { useDispatch, useSelector } from 'react-redux'
import { searchConnections } from "../../redux/connections";

function SearchConnectionsForm(){

    const dispatch = useDispatch();
    const userId = useSelector( state => state.session.user.id)


    const [location, setLocation] = useState('Los Angeles')
    const [industry_area, setIndustryArea] = useState('')
    const [ job_title, setJobTitle] = useState('')
    const [genre, setGenre] = useState('')
    const [startDay, setStartDay] = useState('1')
    const [maxStartDay, setMaxStartDay] = useState('30')
    const [startMonth, setStartMonth] = useState('')
    const [startYear, setStartYear] = useState('')
    const [start_date, setStartDate] = useState('')
    const [endDay, setEndDay] = useState('1')
    const [maxEndDay, setMaxEndDay] = useState('30')
    const [endMonth, setEndMonth] = useState('')
    const [endYear, setEndYear] = useState('')
    
    const [end_date, setEndDate] = useState('')

    setStartDate(`${startMonth}/${startDay}/${startYear}`)
    setEndDate(`${endMonth}/${endDay}/${endYear}`)

    

    useEffect(()=>{
        const thirtyFirsts = ['1' , '3', '5', '7', '8' , '10' ,'12']
        // if(startMonth === ('1' || '3'|| '5'|| '7'|| '8' || '10' ||'12')) setMaxStartDay('31')
        if(thirtyFirsts.includes(startMonth)) setMaxStartDay('31')
        if(startMonth === '2') setMaxStartDay('29')
        
        if(startMonth === ('4' || '6' || '9' || '11')) setMaxStartDay('30')


        if(endMonth === ('1' || '3'|| '5'|| '7'|| '8' || '10' ||'12')) setMaxEndDay('31')
        
            if(endMonth === '2') setMaxEndDay('29')
            
            if(endMonth === ('4' || '6' || '9' || '11')) setMaxEndDay('30')

    },[startMonth, endMonth])


   
    const submitHandler = (e) =>{
      e.preventDefault()

        const formData = {

            location,
            industry_area,
            job_title,
            genre,
            start_date,
            end_date
        }

        dispatch(searchConnections(userId, JSON.stringify(formData)))
    }



    return(<>
    
        <form id='search-connections' method='POST' onSubmit={submitHandler}>

        <label htmlFor="job-titles"></label>
        <select name='job-titles' id='job-title-select' value={industry_area} onChange={e => setJobTitle(e.target.value)}>
    
    <option value="'Editor">Editor</option>
    <option value='Assistant Editor'>Assistant Editor</option>
    </select>

        <label htmlFor="industry-area"></label>
        <select name='industry-areas' id='industry-area-select' value={industry_area} onChange={e => setIndustryArea(e.target.value)}>
    
            <option value="Scripted Television">Scripted Television</option>
            <option value='Unscripted Television'>Unscripted Television</option>
            <option value='Dramatic Film'>Dramatic Film</option>
            <option value='Documentary'>Documentary</option>
            <option value='Commercial'>Commercial</option>
        </select>

        <label htmlFor="genre"></label>
        <select name='genres' id='genre-select' value={industry_area} onChange={e => setGenre(e.target.value)}>
    
            <option value="Scripted Television">Scripted Television</option>
            <option value='Unscripted Television'>Unscripted Television</option>
            <option value='Dramatic Film'>Dramatic Film</option>
            <option value='Documentary'>Documentary</option>
            <option value='Commercial'>Commercial</option>
        </select>

        <label htmlFor="location"></label>
        <select name='locations' id='location-select' value={location} onChange={e => setLocation(e.target.value)}>
    
            <option value="Los Angeles">Los Angeles</option>
            <option value='New York'>New York</option>
            <option value='Atlanta'>Atlanta</option>
            <option value='Remote'>Remote</option>
        </select>

        <p>Start Date</p>
        <label htmlFor="start_date_month"></label>
        <input type="number" min='1' max='12' value={startMonth} onChange={ e => setStartMonth(e.target.value)}/>

        <label htmlFor="start_date_day"></label>
        <input type="number" min='1' max={maxStartDay} value={startDay} onChange={ e => setStartDay(e.target.value)}/>

        <label htmlFor="start_date_year"></label>
        <input type="number" min='2024' max='2030' value={startYear} onChange={ e => setStartYear(e.target.value)}/>


        <p>End Date</p>
        <label htmlFor="end_date_month"></label>
        <input type="number" min='1' max='12' value={endMonth} onChange={ e => setEndMonth(e.target.value)}/>

        <label htmlFor="end_date_day"></label>
        <input type="number" min='1' max={maxEndDay} value={endDay} onChange={ e => setEndDay(e.target.value)}/>

        <label htmlFor="end_date_year"></label>
        <input type="number" min='2024' max='2030' value={endYear} onChange={ e => setEndYear(e.target.value)}/>
           
    
       <button id='submit' type="submit">Search</button>

        </form>


    </>)
}

export default SearchConnectionsForm