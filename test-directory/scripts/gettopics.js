function getTopics(callback)
{
    var xmlhttp = new XMLHttpRequest();
    var ourPath = document.querySelector("script.topics").getAttribute("src");
    ourPath = ourPath.slice(0, ourPath.lastIndexOf("/"));
    var url = ourPath + "/../data/topics.json"; // Make it relative our directory
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