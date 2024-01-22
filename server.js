const net = require("net");

const server = net.createServer();

server.listen({
  host: "localhost",
  port: 8080,
});

server.on("connection", (client) => {
  console.log("New client connected!");

  client.on("data", (data) => {
    console.log(`Client says: ${data.toString()}`);
  });

  client.write("Hello there!");
  client.end();
});
