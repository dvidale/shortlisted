

function SearchDetails({params}){

    return(
        <>
        
        <div>{params.industry_area}</div>
        <div>{params.job_title}</div>
        {params.genre && <div>{params.genre}</div>}
        
        <div>Start: {params.start_date}</div>
        <div>End: {params.end_date ? params.end_date : `None given`}</div>
        <div>{params.location}</div>
        
        </>
    )
}


export default SearchDetails