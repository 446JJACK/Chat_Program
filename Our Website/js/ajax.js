function getDateString()
{
    var months = [
        "Jan", "Feb", "Mar",
        "Apr", "May", "Jun",
        "Jul", "Aug", "Sep",
        "Oct", "Nov", "Dec"
    ]

    var date = new Date();
    var day = date.getDate();
    var month = date.getMonth();
    var year = date.getFullYear();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();
    var hours = date.getHours();

    return months[month] + "-" + day + "-" + year+ " "+ hours+":"  + minutes +":" + seconds;
}

function showMessage()
{
    var xmlhttp;
    var string = document.querySelector("#msg").value;

    if ( string == "" )
    {
        console.log("Empty");
        document.querySelector('.content').innerHTML="";
        return;
    }

    if ( window.XMLHttpRequest )
    {
        console.log("XMLHTTPRequest()!");
        xmlhttp= new XMLHttpRequest();
    }
    else
    {
        xmlhttp= new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.onreadystatechange = function()
    {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
        {
            var jsonObject = JSON.parse(xmlhttp.responseText);

            /*for(var i =0; i <jsonObject.length();i++)
            {
                document.querySelector('.content').innerHTML=jsonObject[i];
            }
*/
            var dateString = getDateString();

            var string = "["+dateString + "] ";
            string += jsonObject.username + ": ";
            string += jsonObject.msg;
            document.querySelector('.content').innerHTML=string;
        }
    }
    console.log("Open for get, send");

    xmlhttp.open("GET", "data.json", true);
    xmlhttp.send();
}

