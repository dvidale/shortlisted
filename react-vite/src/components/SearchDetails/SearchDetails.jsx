

function SearchDetails({params}){

    return(
        <>
        
        <div>{params.industry_area}</div>
        <div>{params.job_title}</div>
        {params.genre && <div>{params.genre}</div>}
        
        <div>Start: {params.start_date}</div>
        {params.end_date && <div>End: {params.end_date}</div>}
        <div>{params.location}</div>
        
        </>
    )
}


export default SearchDetails