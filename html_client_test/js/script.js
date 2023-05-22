// Create WebSocket connection.
const socket = new WebSocket('ws://localhost:8765');
const testButton = document.querySelector("#test_message_button");

// Connection opened
socket.addEventListener('open', function (event) {
    console.log('Connected to the WS Server!')
    socket.send('TOKEN TEST');
});

// Connection closed
socket.addEventListener('close', function (event) {
    console.log('Disconnected from the WS Server!')
});

// Listen for messages
socket.addEventListener('message', function (event) {
    console.log('Message from server ', event.data);
});

// Send a msg to the websocket
testButton.addEventListener("click", () => {
    socket.send('Hello from Client2!');
});