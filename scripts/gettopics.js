function getTopics(callback)
{
    var xmlhttp = new XMLHttpRequest();
    var url = "/data/topics.json";
    var topics;
    
    xmlhttp.onreadystatechange = function (){
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
        {
            callback(JSON.parse(xmlhttp.responseText));
        }
    };
    
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}