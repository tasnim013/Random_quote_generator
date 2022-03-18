//Load data file
import { motivational_data } from "./motivational_data.js";
import { movie_data } from "./movie_data.js";
import { humorous_data } from "./humorous_data.js";



function showQuote(singleQuote){
    //Function to show single quote on html file

    let qdiv=document.getElementById('quoteOutput');
    let adiv=document.getElementById('authorOutput');

    qdiv.innerHTML=singleQuote.Quote;

    adiv.innerHTML=singleQuote.Author;
    
}

function randomQuote(dataSource){
    //Randomly choose one quote from selected data file
    let idx=Math.floor(Math.random()*dataSource.length);
    showQuote(dataSource[idx]);
}

let btn1=document.getElementById('b1');
let btn2=document.getElementById('b2');
let btn3=document.getElementById('b3');

btn1.addEventListener("click", function(){randomQuote(motivational_data)});
btn2.addEventListener("click", function(){randomQuote(humorous_data)});
btn3.addEventListener("click", function(){randomQuote(movie_data)});