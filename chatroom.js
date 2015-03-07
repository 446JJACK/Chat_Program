function clickSubmit() {
  var divBox = document.querySelector("div#chatbox");
  var form = document.querySelector("form");
  var submitButton = document.querySelector("button#submit");

  divBox.style.background = "white";
  divBox.style.height = "500px";
  divBox.style.width = "250px";
  divBox.style.border = "2px solid black";
  divBox.style.boxShadow = "5px 5px 5px 5px #0bF";



  form.addEventListener("submit", function(e) {
    e.preventDefault();
    var textbox = document.createElement('p');
    textbox.innerHTML = document.querySelector("input#textbox").value;

    document.querySelector("input#textbox").value = "";

    divBox.appendChild(textbox);

    clickSubmit();
  });
}

window.addEventListener("load", function() {
  console.log('hello world');
  clickSubmit();
});
