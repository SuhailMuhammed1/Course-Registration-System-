// Function to display messages and hide after 5 seconds
function displayMessage() {
  var messageBox = document.getElementById("message-box");
  if (messageBox) {
    messageBox.style.display = "block";
    setTimeout(function () {
      messageBox.style.display = "none";
    }, 5000);
  }
}
