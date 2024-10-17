import './recent-activity.css'

function RecentActivityFeed(){

    const activities =[
        {
            'msg':'Brandon Carter left a comment on "NYC Editors for Indie Documentary"'
        },
        {
            'msg':'Faith Davis left a comment on "LA Assistant Editors for HBO Drama"'
        },
        {
            'msg':'Naina Raj shortlisted you for "Editors for 2025 Indies in LA"'
        },
        {
            'msg': 'Isabella Williams shortlisted you for "AEs for Award-Winning TV Series"'
        },
        {
            'msg':'Chetan Sharma joined Shortlisted with your invitation'
        },
        {
            'msg':'Karla Ybarra will become available in 30 days.'
        }



    ]

    return(
        <>
        <h1 className='recent-feed-title'>Recent Activity</h1>
        <div className='recent-activity-feed'> 
        { activities.map(activity =>(

            <div className='activity-tile' key={activity.msg}>{activity.msg}</div>
        ))}
        </div>
        </>
    )
}

export default RecentActivityFeed