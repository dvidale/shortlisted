

function SearchResultTile ({resultFirstName, resultLastName, resultPhotoUrl}){



    return (

<div className="search-result-tile">
<img className="user-avatar" src={resultPhotoUrl}/>
{resultFirstName}{` `}{resultLastName}
</div>
    )
}

export default SearchResultTile