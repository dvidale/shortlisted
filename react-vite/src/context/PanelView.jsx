import { useState, createContext } from 'react';


export const AppPanelsContext = createContext();


export function CenterPanelView(){

    const [ centerView, setCenterView ] = useState('recent-activity')
    const [ showRecentActivity, setShowRecentActivity ] = useState( centerView === 'recent-activity')
    const [ showSearchResults, setShowSearchResults ] = useState( centerView === 'search-results');
    const [ showShortlists, setShowShortlists ] = useState( centerView === 'single-shortlist')  
    const [ showProfile, setShowProfile ] = useState( centerView === 'user-profile');
    
}

export function LeftPanelView(){
    
    const [ leftView, setLeftView ] = useState('my-shortlists')
    const [ myShortlists, setMyShortlists ] = useState( leftView === 'my-shortlists')
    const [ searchFormView, setSearchFormView ] = useState( leftView === 'search-form');





}