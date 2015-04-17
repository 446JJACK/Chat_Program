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
	var userName = document.querySelector("#msgUserName").value;
	var password = document.querySelector("#msgPassword").value;

	console.log(userName + " " + password);

	document.querySelector("#msgUserName").value = "";
	document.querySelector("#msgPassword").value = "";

	overlaySignIn();
}


function register()
{
	var userName = document.querySelector("#regUserName").value;
	var email = document.querySelector("#regEmail").value;
	var password = document.querySelector("#regPassword").value;
	var confPassword = document.querySelector("#regConfPassword").value;


	console.log(userName + email + password + confPassword);

	document.querySelector("#regUserName").value = "";
	document.querySelector("#regEmail").value = "";
	document.querySelector("#regPassword").value = "" ;
	document.querySelector("#regConfPassword").value = "";

	overlayRegister();

}



