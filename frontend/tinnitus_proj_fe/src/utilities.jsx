// in order to utilize axios everywhere
import axios from 'axios'

// create axios instance. 
// This is not creating an api call its just creating an instance and saving that instance to the api.
// so you dont have to add url on every page youre doing an api call
export const api = axios.create({
    baseURL: "https://frozen-fortress-37540-a8f70bce221d.herokuapp.com/api/"
});


