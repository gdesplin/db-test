var displayMessages = function (messages) {
	var messageDiv = document.getElementById("messages");
	messageDiv.innerHTML = "";
	mlen = messages.length;
	for (i = 0; i < mlen; i++) {
		decodeMes = decodeURIComponent(messages[i]["message"]);
		var newp =  document.createElement("p");
		messageDiv.appendChild(newp);
		newp.innerHTML = decodeMes; 
	}
}
var getRequest = function () {
    var request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState == XMLHttpRequest.DONE) {
            if (request.status >= 200 && request.status < 400) {
                messages = JSON.parse(request.responseText);
                console.log(messages);
                displayMessages(messages)
            }
            else {
                alert("Not Worky")
            }
        }
    };

    request.open("GET", "http://localhost:8080/messages");
    request.send();
};

var postRequest = function () {
	var request = new XMLHttpRequest();
	request.onreadystatechange = function () {
        if (request.readyState === XMLHttpRequest.DONE) {
            if (request.status >= 200 && request.status < 400) {
                getRequest();
            }
            else {
                alert("Uh");
            }
        }
	};
    var messageInput = document.getElementById("message");
    var encodedData = encodeURIComponent(messageInput.value); 
    request.open("POST", "http://localhost:8080/messages");
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.send(encodedData);
};

getRequest();
var  submitButton = document.getElementById('submit');
submitButton.onclick = function () {
    console.log("Submit Pressed");
    postRequest();
    console.log("Message Sent Successfully");
};
