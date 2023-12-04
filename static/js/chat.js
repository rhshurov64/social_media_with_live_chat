
const username = JSON.parse(document.getElementById('user_name').textContent)
console.log(username)

var socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + username
    + '/')      

socket.onopen = function(event){
    console.log('Connected')
    

}

socket.onmessage = function(event){
    const data = JSON.parse(event.data)
    // <!-- document.getElementById('textarea').value += (data.msg + '\n') -->
    // var chatDiv = document.getElementById('chatDiv');
    // chatDiv.innerHTML += (data.msg + '<br>');
    // chatDiv.scrollTop = chatDiv.scrollHeight;           
}


socket.onerror = function(event){
    console.log('error')
}
socket.onclose = function(){
    console.log('onclose')
}

// document.getElementById("submit").onclick = function (event) {
//     const messageInputDom = document.getElementById("textInput")
//     const message = messageInputDom.value
//     socket.send(JSON.stringify({
//         'msgs': message
//     }))
//     messageInputDom.value = ''
//     }





