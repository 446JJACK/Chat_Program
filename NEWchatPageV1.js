function countTabs() {
  var i = 0,
    divCount = 0;
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
  console.log(newRadio);
  
  var newLabel = document.createElement('label');
  newLabel.setAttribute('for', "tab" + numTabs);
  newLabel.innerHTML = "Chat " + numTabs;
  console.log(newLabel);
  
  var newContent = document.createElement('div');
  newContent.className = "content";
  
  newTab.appendChild(newRadio);
  newTab.appendChild(newLabel);
  newTab.appendChild(newContent);
  console.log(newTab);
  
  tabContainer.insertBefore(newTab, tabContainer.childNodes[numTabs + 1]);

  /*var xhr = new XMLHttpRequest();
  xhr.open('GET', 'data.json');
  
  var temp = "";

  xhr.addEventListener("readystatechange", function() {
    if (xhr.readyState === 4) {
      var objList = JSON.parse(xhr.responseText);
      temp += objList[0].newTab;
      
      
      //var idTemp =
      newLabel.setAttribute('for', newTab.id);
      newLabel.innerHTML = newTab.id;
      console.log(newLabel);
      newTab.innerHTML = temp;
      newTab.innerHTML += newLabel;
      console.log(newTab);
      tabContainer.insertBefore(newTab, tabContainer.childNodes[numTabs + 1]);
    }
  });
  xhr.send();*/
}

function init() {
  var sendbtn = document.querySelector("button#sendbtn");
  var addTab = document.getElementById("addTab");
  sendbtn.addEventListener("click", function() {
    sendMsg();
  });

  document.onkeydown = function() {
    if (window.event.keyCode == '13') {
      sendMsg();
    }
  };

  addTab.addEventListener("click", function() {
    addChatRm();
  });
}

window.addEventListener("load", function() {
  init();
});
