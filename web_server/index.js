import * as net from "net";
function newConn(socket) {
    console.log("new connection", socket.remoteAddress, socket.remotePort);
    // ...
}
let server = net.createServer();
server.on("connection", newConn);
server.listen({ host: "127.0.0.1", port: 1234 });
