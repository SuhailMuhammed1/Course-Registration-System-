// function to display messages
function displayMessage() {
  var messageBox = document.getElementById("message-box");
  if (messageBox) {
    messageBox.style.display = "block";
    setTimeout(function () {
      messageBox.style.display = "none";
    }, 5000);
  }
}
