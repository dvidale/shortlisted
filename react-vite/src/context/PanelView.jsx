import { createContext } from 'react';


export const CenterView = createContext('hello-div');
export const LeftView = createContext('my-shortlists')

export const PanelViews = createContext(
    {'defaultLeftPanel': 'my-shortlists', 
    'defaultCenterPanel': 'recent-activity'}
)