function countUsrs() {
  var numUsrs = document.querySelector("p#numUsrs");
  var onlineUsrs = document.querySelector("ul#online");
  var i = 0;
  var num = 0;
  while (document.getElementsByClassName('usr')[i++]) num++;
  numUsrs.innerHTML = num;
}

function fontStuff(mp) {
  var cur = document.querySelector("textarea#msg");
  var siz = document.defaultView.getComputedStyle(cur, null).getPropertyValue('font-size');
  var col = document.defaultView.getComputedStyle(cur, null).getPropertyValue('color');
  var sty = document.defaultView.getComputedStyle(cur, null).getPropertyValue('font-family');
  mp.style.setProperty('font-size', siz);
  mp.style.setProperty('color', col);
  mp.style.setProperty('font-family', sty);
}

function sendMsg() {
  var curChatBox = document.querySelector("[type=radio]:checked ~ label ~ .content");
  var msg = document.createElement('p');
  fontStuff(msg);
  msg.innerHTML = document.querySelector("textarea#msg").value;
  document.querySelector("textarea#msg").value = "";
  curChatBox.appendChild(msg);
  curChatBox.scrollTop = curChatBox.scrollHeight;
}

function addChatRm() {
  var tabContainer = document.querySelector(".tabs");
  var numTabs = tabContainer.childElementCount;
  var tt = tabContainer.lastChild.previousSibling;
  var nt = tt.previousSibling.previousSibling;
  var newTab = document.createElement("div");
  newTab.className = "tab";

  var newRadio = document.createElement('input');
  newRadio.id = "tab" + numTabs;
  newRadio.setAttribute('type', 'radio');
  newRadio.setAttribute('name', 'tabgroup1');
  newRadio.checked = true;

  var newLabel = document.createElement('label');
  newLabel.setAttribute('for', "tab" + numTabs);
  newLabel.innerHTML = "Chat " + numTabs;

  var newContent = document.createElement('div');
  newContent.className = "content";

  newTab.appendChild(newRadio);
  newTab.appendChild(newLabel);
  newTab.appendChild(newContent);
  tabContainer.insertBefore(newTab, tt);
}

function init() {
  var sendbtn = document.querySelector("button#sendbtn");
  var addTab = document.getElementById("addTab");
  var msgbox = document.querySelector("textarea#msg");

  console.log(startWidth = document.defaultView.getComputedStyle(msgbox).width); //parseInt(document.defaultView.getComputedStyle(msgbox).width, 10));
  sendbtn.style.left = (msgbox.clientWidth + 20) + "px";

  msgbox.addEventListener("mouseover", function() {
    msgbox.style.resize = "both";
    msgbox.style.minWidth = "10%";
    window.addEventListener("mousemove", function() {
      sendbtn.style.left = (msgbox.clientWidth + 20) + "px";
    });
  });

  sendbtn.addEventListener("click", function() {
    sendMsg();
  });

  document.onkeydown = function(e) {
    if ((e || window.event).keyCode == '13' && !(e || window.event).shiftKey) {
      (e || window.event).preventDefault();
      sendMsg();
    }
  };

  addTab.addEventListener("click", function() {
    addChatRm();
  });
}

window.addEventListener("load", function() {
  init();
  countUsrs();
});

/* Popup Javascript! */
function overlay() {
  var el = document.querySelector("#overlay");
  el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}

function overlaySignIn() {
  var sin = document.querySelector("#overlaySignIn");
  var div = document.querySelector("#grey");
  sin.style.visibility = (sin.style.visibility == "visible") ? "hidden" : "visible";
  //div.style.visibility = (div.style.visibility == "visible") ? "hidden" : "visible";
  // div.style.opacity = (div.style.opacity == "1") ? "0" : "1";
}

function overlayRegister() {
  var sin = document.querySelector("#overlayRegister");
  var div = document.querySelector("#grey");
  sin.style.visibility = (sin.style.visibility == "visible") ? "hidden" : "visible";
  //div.style.visibility = (div.style.visibility == "visible") ? "hidden" : "visible";
  // div.style.opacity = (div.style.opacity == "1") ? "0" : "1";
}

function overlaySettings() {
  var sin = document.querySelector("#overlaySettings");
  var div = document.querySelector("#grey");
  var cur = document.querySelector("textarea#msg");
  sin.style.visibility = (sin.style.visibility == "visible") ? "hidden" : "visible";
  var e = document.querySelector("select#color");
  var f = document.querySelector("select#size");
  var g = document.querySelector("select#font");
  var colorset = e.options[e.selectedIndex].value;
  var sizeset = f.options[f.selectedIndex].value;
  var fontset = g.options[g.selectedIndex].value;
  cur.style.setProperty('font-size', sizeset);
  cur.style.setProperty('color', colorset);
  cur.style.setProperty('font-family', fontset);
}

function login() {
  /*
var userName = document.querySelector("#sinUserName").value;
var password = document.querySelector("#sinPassword").value;
console.log(userName + " " + password);
document.querySelector("#sinUsername").value = "";
document.querySelector("#sinPassword").value = "";
*/
  overlaySignIn();
}

function register() {
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

function swapRegisterAndSignIn() {
  var sin = document.querySelector("#overlaySignIn");
  var div = document.querySelector("#grey");
  var reg = document.querySelector("#overlayRegister");
  sin.style.visibility = (sin.style.visibility == "visible") ? "hidden" : "visible";
  //div.style.visibility = (div.style.visibility == "visible") ? "hidden" : "visible";
  // div.style.opacity = (div.style.opacity == "1") ? "0" : "1";
  reg.style.visibility = (reg.style.visibility == "visible") ? "hidden" : "visible";
}
/* END POP UP JAVASCRIPT */
