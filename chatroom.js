console.log('hello world');

// not working completely.  It is a work in progress.  
// try to get the value to appear. Put it in Div. 
//
// for some reason textbox is showing up as null. 
// I'm probably overlooking something small as it is 12:34 AM


function clickSubmit(wrapper) {
    wrapper.innerHTML = "<br>CLICK IS WORKING<br>";
    if (document.querySelector('textbox') != null) {
        alert('VALUE IS NOT NULL');
        var message = document.querySelector('textbox').value;
        wrapper.innerHTML = "<br>" + message + "<br>";

    } else {
        var message = null;
        alert('VALUE IS NULL');
        console.log(message);
    }
}


