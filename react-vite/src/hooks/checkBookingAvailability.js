import { useSelector } from "react-redux";

export function useAvailFilter({setShowShortlists, setIsLoading, setShowSearchResults}){

    const searchResults = useSelector(state => state.shortlists.results_pre_avail)

    const searchParams = useSelector(state => state.shortlists.parameters)

    function availCheck(connection){


        let noConflict = true
        let i = 0
        
        if (connection['bookings'].length === 0) return noConflict;
        
        while(noConflict && i < connection['bookings'].length){
            const booking = connection['bookings'][i]
            const [ bookingStart, bookingEnd ] = booking
            const booking_start = new Date(bookingStart)
            const booking_end = new Date(bookingEnd)
            const paramsStart = new Date(searchParams['start_date'])
            const paramsEndCheck = searchParams['end_date']
            const paramsEnd = paramsEndCheck ? new Date(paramsEndCheck) : null
            
            
            
            if(booking_start < paramsStart && paramsStart < booking_end ) noConflict = false
            // checks if start date overlaps with a current booking
            
            if(paramsEnd !== null){
                // console.log(">>> non-null paramsEnd", paramsEnd);
                if(booking_start < paramsEnd && paramsEnd < booking_end ) noConflict = false
                // checks if the job ending overlaps with current booking dates
                
                if(booking_start < paramsStart && paramsEnd < booking_end) noConflict = false
                // checks for current booking wrapping around job opp
                
                if(paramsStart < booking_start && booking_end < paramsEnd) noConflict = false
                // checks if job opp wraps around current booking
            }
            
            i++
        }
        
        return noConflict;
    }

    const avail_filtered_results = searchResults.filter(connection => availCheck(connection))
        
    setIsLoading(false)
    setShowSearchResults(true)
    setShowShortlists(false)
    

    return avail_filtered_results

}