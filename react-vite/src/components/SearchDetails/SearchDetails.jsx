

function SearchDetails({params}){
    const startDate = new Date(params.start_date)
    const options = {month: "short"};
    // const month = new Intl.DateTimeFormat("en-US", options).format(startDate)

    let end_month
    if( params.end_date){
//  const endDate = new Date(params.end_date)
  
    // end_month = new Intl.DateTimeFormat("en-US", options).format(endDate)

    }
   
    return(
        <>
        
        <div>
            <div>{params.industry_area}</div>
        <div>{params.job_title}</div>
        {params.genre && <div className='genre-details'>{params.genre}</div>}
        </div>
        <div>
        {/* <div>Start:{month} {new Date(params.start_date).getFullYear()}</div> */}
        {/* <div>End: {params.end_date ? `${end_month} ${new Date(params.end_date).getFullYear()}` : `N/A`}</div> */}
        <div>{params.location}</div>    
        </div>
        
        
        
        </>
    )
}


export default SearchDetails