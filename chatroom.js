console.log('hello world');

// not working completely.  It is a work in progress.
// try to get the value to appear. Put it in Div.
//
// for some reason textbox is showing up as null.
// I'm probably overlooking something small as it is 12:34 AM


function clickSubmit() {

    var textbox = document.getElementById("textbox").value.indexOf("@");
    var divBox = document.getElementById("chatbox").value;
    var submitButton = document.getElementById("submit").value;

    if (submitButton = "send") {
        console.log('true');

    }

    /*var wrapper = document.querySelector("chatbox");
    //wrapper.innerHTML = "<br>CLICK IS WORKING<br>";
    var newElement = document.createElement('div');
    newElement.innerHTML = "Whats up?!";
    if (document.querySelector('textbox') != null) {
        alert('VALUE IS NOT NULL');
        var message = document.querySelector('textbox').value;
        wrapper.innerHTML = "<br>" + message + "<br>";
        //document.querySelector('wrapper').appendChild(message);

    } else {
        var message = null;
        alert('VALUE IS NULL');
        console.log(message);
    }
    */
}


window.addEventListener("load", function() {
    clickSubmit();
});

