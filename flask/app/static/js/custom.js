// Add form field dynamically

$(document).ready(function() {
    let maxField = 25; // field limit
    let addButton = $('.add-button'); // add button selector
    let wrapper = $('.dynamic-field') // materialize 
    let fieldHTML = `<div class="input-field dynamic-field">
                        <input id="question-questoin" name="question-question" type="text" value="">
                        <label for="question">Another question</label>
                     </div>
                    `;
    let x = 1;

    $(addButton).click(function(){
        //Check maximum number of input fields
        if(x < maxField){ 
            x++; //Increment field counter
            $(wrapper).append(fieldHTML); //Add field html
        }
    });

});
