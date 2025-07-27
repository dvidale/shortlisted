import {
  legacy_createStore as createStore,
  applyMiddleware,
  compose,
  combineReducers,
} from "redux";
import thunk from "redux-thunk";
import sessionReducer from "./session";
import imgReducer from "./img-test";
import shortlistsReducer from "./shortlists";
import commentsReducer from "./comments";
import bookingsReducer from "./bookings";
import myReferralsReducer from "./my-referrals";

const rootReducer = combineReducers({
  session: sessionReducer,
  img:imgReducer,
  shortlists: shortlistsReducer,
  comments: commentsReducer,
  bookings: bookingsReducer,
  referrals: myReferralsReducer
});

let enhancer;
if (import.meta.env.MODE === "production") {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = (await import("redux-logger")).default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
