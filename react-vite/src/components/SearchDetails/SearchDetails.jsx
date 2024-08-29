// !BUG - throwing an "invalid date" error

function SearchDetails({ params, searchSubmitted, showSearchResults }) {
  // const startDate = new Date(params.start_date)
  // const options = {month: "short"};
  // const month = new Intl.DateTimeFormat("en-US", options).format(startDate) //! the problem is with this formatting line

  // let end_month
  if (params.end_date) {
    //  const endDate = new Date(params.end_date)
    // end_month = new Intl.DateTimeFormat("en-US", options).format(endDate)
  }

  return (
    <>
      <div className="search-params">
        {searchSubmitted || showSearchResults === false && (<>
        <div>
       
          <h3 className="shortlist-details-heading">Search Details</h3>{" "}
        </div>
          <div className="actual-params-details">
            <div className="industry-job-title-genre">
              <div className="param-detail-text">{params.industry_area}</div>
              <div className="param-detail-text">{params.job_title}</div>
              {params.genre && (
                <div className="param-detail-text">
                    {params.genre}</div>
              )}
            </div>
            <div className="dates-location">
              {/* <div className="param-detail-text">Start:{month} {new Date(params.start_date).getFullYear()}</div> */}
              {/* <div className="param-detail-text">End: {params.end_date ? `${end_month} ${new Date(params.end_date).getFullYear()}` : `N/A`}</div> */}
              <div className="param-detail-text">{params.location}</div>
            </div>
          </div>
        </>)}
      </div>
    </>
  );
}

export default SearchDetails;
