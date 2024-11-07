// document.addEventListener('DOMContentLoaded', function () {
//     const chatLog = document.getElementById('chat-log');
//     const userInput = document.getElementById('user-input');
//     const sendButton = document.getElementById('send-button');
//     const userHistoryList = document.getElementById('user-history-list');

//     sendButton.addEventListener('click', sendMessage);

//     function sendMessage() {
//         const message = userInput.value;
//         if (message.trim() !== '') {
//             addUserMessage(message);
//             // Send the message to the server for processing
//             // and receive a response to display back to the user
//             // For simplicity, just echoing the message for nowa
//             addBotMessage("Echo: " + message);
//             userInput.value = '';
//         }
//     }

//     function addUserMessage(message) {
//         const messageElement = document.createElement('div');
//         messageElement.innerText = "You: " + message;
//         chatLog.appendChild(messageElement);
//         chatLog.scrollTop = chatLog.scrollHeight;

//         // Add message to user history  
//         const historyItem = document.createElement('li');
//         historyItem.innerText = message;
//         userHistoryList.appendChild(historyItem);
//     }

//     function addBotMessage(message) {
//         const messageElement = document.createElement('div');
//         messageElement.innerText = "AdvoAdvice: " + message;
//         chatLog.appendChild(messageElement);
//         chatLog.scrollTop = chatLog.scrollHeight;
//     }
// });

document.addEventListener("DOMContentLoaded", function() {
    const sendButton = document.getElementById("send-button");
    const userInput = document.getElementById("user-input");
    const chatLog = document.getElementById("chat-log");
    const userHistoryList = document.getElementById("user-history-list");

    // Function to send message to REST API
    function sendMessageToAPI(message, userAuthDetails) {
        // Make a POST request to your Django REST Framework API endpoint
        fetch('your_api_endpoint_url', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // Add any additional headers if required
                'Authorization': `Bearer ${userAuthDet  ails.token}`, // Assuming token-based authentication
                // Include other authentication details as needed
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response from the API
            // For example, you can display the response in the chat log
            chatLog.innerHTML += `<div class="response">${data.response}</div>`;
            // Scroll to the bottom of the chat log
            chatLog.scrollTop = chatLog.scrollHeight;
        })
        .catch(error => {
            console.error('Error:', error);
            // Handle error, if any
        });
    }

    // Event listener for send button click
    sendButton.addEventListener("click", function() {
        const message = userInput.value.trim();
        if (message !== "") {
            // Add the user message to the chat log
            chatLog.innerHTML += `<div class="user">${message}</div>`;
            // Clear the input field
            userInput.value = "";
            // Scroll to the bottom of the chat log
            chatLog.scrollTop = chatLog.scrollHeight;
            // Get user authentication details
            const userAuthDetails = getUserAuthDetails(); // Implement this function to get user authentication details
            // Send the message to the API along with user authentication details
            sendMessageToAPI(message, userAuthDetails);
        }
    });
});

