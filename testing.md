## Testing and Bugs

During the development of this project I ran into to multiple bugs and errors and decided to 
document some of them here which took the most work.

#### To-do list display page

I ran into the difficulties creating My To-Do list display page:

* the font awesome icons was not displaying inline with the to do list items
* part of the to do list was accepting input using JS which when refreshed would disapear and would not be saved on the 
local storage or session or anywhere and you would have to type in your list again
* I have connected Mongo DB to my list and was using for loop to loop over the lists created. I got
to diplay the name of the list and the list_item name which would stay even before setting the session however I was not sure
how to add the list items to Mongo DB and was confused over it.
* the tick did not work, or underline when the list is completed


