const http = require("node:http");

const target = "https://amg01602-themahqfrance-vivekanald-samsungspain-uu2zn.amagi.tv/ts-eu-w1-n2/playlist/amg01602-themahqfrance-vivekanald-samsungspain/cb56380079766c909bc32164d5f1629ba65928d80b6c852a6ab4548561924c5d84bef396e956bb3b559c02df605c6c4c0c629f1fc32d03c08b2efc59327814759cfae241f1a1c3f27fea25184fd0682334a0575185714341cde80e0d964fcd13673dc979a3d2afefc764d3291081d81afa227cc9f48e30134d406f9d4b653d977f706a4aa955081ed198d42b46baeea3eab2d3eb6de6d59602cd129905a94dcec3a7d4b931b8bdec3ce30eee3808177733c9f219e9a957d483c2895859b881f178d0e2054d7f6c7563b3a540b550e54f81/98/848x480_1686360/index.m3u8";

const server = http.createServer((req, res) => {
  const path = new URL(req.url, "http://localhost").pathname;
  if (path === "/health") {
    res.writeHead(200, { "content-type": "text/plain; charset=utf-8", "cache-control": "no-store" });
    return res.end("ok");
  }
  if (path === "/kanald" || path === "/kanald/") {
    res.writeHead(302, {
      Location: target,
      "Cache-Control": "no-store",
      "Access-Control-Allow-Origin": "*"
    });
    return res.end();
  }
  res.writeHead(404, { "content-type": "text/plain; charset=utf-8" });
  res.end("Not found");
});

const port = Number(process.env.PORT || 3000);
server.listen(port, "0.0.0.0", () => console.log(`Kanal D Drama redirect listening on ${port}`));
