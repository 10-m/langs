// Event Handler Registration
let button = document.getElementById('event-handler')
let text = document.getElementById('event-handler-text')
button.onclick = function() {
    text.style.display = 'block';
}

// Adding Event Handlers
let button2 = document.getElementById('add-event-handler')
let text2 = document.getElementById('add-event-handler-text')

let clickButton2 = function() {
    text2.style.display = 'block';
}
button2.addEventListener('click', clickButton2);

// Removing Event Handlers
let button3 = document.getElementById('remove-event-handler')
button3.addEventListener('click', function() {
	button2.removeEventListener('click', clickButton2);
});

// Event Object Properties
let button4 = document.getElementById('event-object-properties');
button4.addEventListener('click', function(event) {
  event.target.style.display = 'none';
  alert(event.type + ':' + event.timeStamp);
});

// Event Types
let button5 = document.getElementById('event-types');
button5.onwheel = function(event) {
  event.target.style.display = 'none';
};

// Mouse Events
let button6 = document.getElementById('mouse-events');
button6.onmouseover = function(event){
  event.target.style.width = '430px';
};

button6.onmouseout = function(event){
  event.target.style.width = '200px';
};

// Keyboard Events
document.onkeydown = function(event) {alert(event.key);};
