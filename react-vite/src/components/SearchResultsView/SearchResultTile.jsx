import { VscAccount } from "react-icons/vsc";

function SearchResultTile ({resultFirstName}){



    return (

<div className="search-result-tile">
<VscAccount />
{resultFirstName}
</div>
    )
}

export default SearchResultTile