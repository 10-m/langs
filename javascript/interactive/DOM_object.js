// Select and Modify Elements
document.querySelector('h1').innerHTML = "Most popular TV show searches in 2016";
document.getElementById('fourth').innerHTML = "Fourth element";

// Style an element
document.body.style.backgroundColor = "lightblue";

// Create and Insert Elements
let li = document.createElement('li');
li.id = "oaxaca";
li.innerHTML = "Oaxaca, Mexico";
document.querySelector('#more-destinations').append(li);

// Remove an Element
let fifth = document.querySelector('#fifth');
document.querySelector('#more-destinations').removeChild(fifth);

// Interactivity with onclick
let element = document.querySelector("button");

function turnButtonRed (){
  element.style.backgroundColor = 'red';
  element.style.color = 'white';
  element.innerHTML = 'Red Button';
}
element.onclick = turnButtonRed;

// Traversing the DOM
let first = document.querySelector('#aaa').firstChild;
first.innerHTML = "First child";
first.parentNode.innerHTML = "I am the parent and my inner HTML has been replaced!";
