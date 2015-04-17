function onlineUsrUpdate() {
  var curTab = document.querySelector("[type=radio]:checked ~ label ~ .content");
  var onlineUL = document.querySelector("ul#online");
  //Get users in current chatroom
}

function countUsrs() {
  var numUsrs = document.querySelector("p#numUsrs");
  var onlineUsrs = document.querySelector("ul#online");
  var i = 0;
  var num = 0;
  while (document.getElementsByClassName('usr')[i++]) num++;
  numUsrs.innerHTML = num
}

function countTabs() {
  var i = 0;
  var divCount = 0;
  while (document.getElementsByClassName('tab')[i++]) divCount++;
  return (divCount);
}

function sendMsg() {
  var curChatBox = document.querySelector("[type=radio]:checked ~ label ~ .content");
  var msg = document.createElement('p');
  msg.innerHTML = document.querySelector("input#msg").value;

  document.querySelector("input#msg").value = "";

  curChatBox.appendChild(msg);
}

function addChatRm() {
  var tabContainer = document.querySelector(".tabs");
  var numTabs = countTabs();
  var newTab = document.createElement("div");
  newTab.className = "tab";

  var newRadio = document.createElement('input');
  newRadio.id = "tab" + numTabs;
  newRadio.setAttribute('type', 'radio');
  newRadio.setAttribute('name', 'tabgroup1');
  newRadio.checked = true;

  var newLabel = document.createElement('label');
  newLabel.setAttribute('for', "tab" + numTabs);
  //var tempLabel = document.createElement('input');
  //newLabel.innerHTML = tempLabel;
  //tempLabel.addEventListener() //OI! LOOK AT EVENT TYPES!!
  newLabel.innerHTML = "Chat " + numTabs;

  var newContent = document.createElement('div');
  newContent.className = "content";

  newTab.appendChild(newRadio);
  newTab.appendChild(newLabel);
  newTab.appendChild(newContent);

  tabContainer.insertBefore(newTab, tabContainer.childNodes[numTabs + 1]);
}

function init() {
  var sendbtn = document.querySelector("button#sendbtn");
  var addTab = document.getElementById("addTab");
  sendbtn.addEventListener("click", function() {
    sendMsg();
  });

  document.onkeydown = function(e) {
    if ((e || window.event).keyCode == '13') {
      sendMsg();
    }
  };

  addTab.addEventListener("click", function() {
    addChatRm();
  });
}

window.addEventListener("load", function() {
  init();
  //onlineUsrUpdate();
  countUsrs();
});



/*                Popup Javascript!         */


function overlay()
{
    var el = document.querySelector("#overlay");
    el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}


function overlaySignIn()
{
    var sin = document.querySelector("#overlaySignIn");
    var div = document.querySelector("#grey");
    sin.style.visibility = (sin.style.visibility == "visible") ? "hidden" : "visible";
    //div.style.visibility = (div.style.visibility == "visible") ? "hidden" : "visible";
//    div.style.opacity = (div.style.opacity == "1") ? "0" : "1";
}

function overlayRegister()
{
    var sin = document.querySelector("#overlayRegister");
    var div = document.querySelector("#grey");
    sin.style.visibility = (sin.style.visibility == "visible") ? "hidden" : "visible";
    //div.style.visibility = (div.style.visibility == "visible") ? "hidden" : "visible";
//    div.style.opacity = (div.style.opacity == "1") ? "0" : "1";
}


function login()
{
  /*
  var userName = document.querySelector("#sinUserName").value;
  var password = document.querySelector("#sinPassword").value;

  console.log(userName + " " + password);

  document.querySelector("#sinUsername").value = "";
  document.querySelector("#sinPassword").value = "";
*/
  overlaySignIn();
}


function register()
{
  /*var userName = document.querySelector("#regUsername").value;
  var email = document.querySelector("#regEmail").value;
  var password = document.querySelector("#regPassword").value;
  var confPassword = document.querySelector("#regConfPassword").value;


  console.log(userName + email + password + confPassword);

  document.querySelector("#regUsername").value = "";
  document.querySelector("#regEmail").value = "";
  document.querySelector("#regPassword").value = "" ;
  document.querySelector("#regConfPassword").value = "";
*/
  overlayRegister();

}


function swapRegisterAndSignIn()
{
    var sin = document.querySelector("#overlaySignIn");
    var div = document.querySelector("#grey");
    var reg = document.querySelector("#overlayRegister");

    sin.style.visibility = (sin.style.visibility == "visible") ? "hidden" : "visible";
    //div.style.visibility = (div.style.visibility == "visible") ? "hidden" : "visible";
//    div.style.opacity = (div.style.opacity == "1") ? "0" : "1";

    reg.style.visibility = (reg.style.visibility == "visible") ? "hidden" : "visible";


}


/*              END POP UP JAVASCRIPT  */



