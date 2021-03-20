// Selecting Elements
const clear = document.querySelector(".clear");
const dateElement = document.getElementById("date");
const list = document.getElementById("list");
const input = document.getElementById("input");

// Classes names

const CHECK = "fa-check-circle";
const UNCHECK = "fa-circle";
const LINE_THROUGH = "lineThrough";

// Show today's date

const options = {weekday: "long", month: "short", day: "numeric"};
const today = new Date();

dateElement.innerHTML = today.toLocaleDateString("en-US", options);

// add to-do function


function addToDo(toDo, id, done, trash){

        if(trash){return; }

        const DONE = done ? CHECK : UNCHECK;
        const LINE = done ? LINE_THROUGH : "";

    const item = `
                <i class="fas ${DONE} co" job="complete" id="${id}"></i>
                <p class="text ${LINE}">${toDo}</p>
                <i class="far fa-trash-alt de" job="delete" id="${id}"></i>
    `;
    const position = "beforeend";
    list.insertAdjacentHTML(position, item);
}

// add an item to the list using the enter key

document.addEventListener("keyup", function(even){
    if(event.keyCode == 13){
        const toDo = input.value;
        // if the input isn't empty
        if(toDo){
            addToDo(toDo);
        }
    }
});

