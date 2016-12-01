import http.server as hs;
from CustomHandlerClass import Handler;

server_address = ("",1337);
http_daemon = hs.HTTPServer(server_address,Handler);

try:
    print("Starting server...");
    http_daemon.serve_forever();
except KeyboardInterrupt:
    print("\n\n[+] Server killed...");
exit();
