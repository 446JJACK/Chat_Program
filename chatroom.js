console.log('hello world');

window.addEventListener("load", function() {

    document.querySelector('button#submit').addEventListener('click', function() {


        var container = document.querySelector('div#wrapper');

        var newNode = document.createElement('div');
        newNode.innerHTML = "hello";
        container.appendChild(newNode);

        var xhr = new XMLHttpRequest();

        xhr.open('GET', "data.json");

        xhr.addEventListener('readystatechange', function (){

            if (xhr.readyState === 4) {
                alert('ready state 4');
                var objList = JSON.parse(xhr.responseText);

                for(var i =0; i < objList.length; i++) {
                    var obj = objList[i];

                    var elem = document.createElement(obj.tag);
                    elem.classList.add(obj.class);

                    elem.innerHTML = obj.content;

                    container.appendChild(elem);
                }
            }
         });

        xhr.send();
    });
/*
    document.getElementById('submit').onclick = function() {
        var textbox = document.getElementById('textbox').value;
        document.querySelector('').innerHTML = "<p>" + textbox + "</p>";
        alert('button was clicked');

    };
*/
});


