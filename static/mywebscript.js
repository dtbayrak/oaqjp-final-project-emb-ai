/**
 * This function takes the text typed by the user and sends it to the Python backend
 * via an HTTP GET request.
 * 
 * This can also be done without using JavaScript by using the Python route decorator.
 * However, in this case, the page will reload each time. Asynchronous operations 
 * cannot be performed.
 * 
 * The Fetch API is recommended instead of XHR (XMLHttpRequest) because it is more
 * functional and modern.
 */

let RunEmotionDetection = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}
