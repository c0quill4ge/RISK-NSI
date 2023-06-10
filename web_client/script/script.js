const socket = new WebSocket('ws://localhost:8765');



// Connection opened
socket.addEventListener('open', function (event) {
    console.log('Connected to the WS Server!')
    token != null ? sendToken(token) : unfoundedToken();
    sendGameId();
});

// Connection closed
socket.addEventListener('close', function (event) {
    console.log('Disconnected from the WS Server!')
});

// Listen for messages
socket.addEventListener('message', function (event) {
    console.log('Message from server : ', event.data);
});
function sendToken(token) {
    socket.send(JSON.stringify({token: token}));
}
function sendGameId() {
    // game's id is in the url at 'game_id'
    socket.send(JSON.stringify({game_id: window.location.href.split('game_id=')[1]}));

}

function unfoundedToken() {
    alert("Une erreur est survenue lors de la connexion au serveur, veuillez réessayer plus tard.");
}
