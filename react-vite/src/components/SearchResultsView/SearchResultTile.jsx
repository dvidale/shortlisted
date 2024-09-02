import { VscAccount } from "react-icons/vsc";

function SearchResultTile ({resultFirstName, resultLastName}){



    return (

<div className="search-result-tile">
<VscAccount />
{resultFirstName}{` `}{resultLastName}
</div>
    )
}

export default SearchResultTile