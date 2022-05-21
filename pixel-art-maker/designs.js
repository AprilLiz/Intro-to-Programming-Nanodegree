// Selects submit button input:
const submit = document.querySelector('#submitButton');

// Selects size input:
const canvas = document.querySelector('#pixelCanvas');
const sizePicker = document.getElementById('sizePicker');

// Selects color input:
const colorPicker = document.querySelector('#colorPicker');

// When size is submitted by the user, call makeGrid()
sizePicker.addEventListener('submit', function(event) {
    event.preventDefault();
    let width = document.querySelector('#inputHeight').value;
    let height = document.querySelector('#inputWidth').value;
    makeGrid(width, height);   
});

function makeGrid(width, height) {
    canvas.innerHTML = '';
    for (let row = 0; row < width; row++) {
        const newRow = canvas.insertRow();
        for (let cell = 0; cell < height; cell++) {
            newRow.insertCell();
        }
    }
    //Change cell color:
    canvas.addEventListener('click', function(event) {
        event.target.style.background = colorPicker.value;
    });
}