"""
Autor: JacquesFernandes
Codigo para criar um server em python
Qualquer duvidas, pesquisa no Google, pergunta no grupo ou direitamente pra mim ^_^
"""

import os;
import http.server as hs;

class Handler(hs.BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Essa funcao eh responsavel para resolvendo GET requests
        exemplo: nos forms do sites, tem aquele "method='GET'" para mandar data para o server.
        para realizar a versao "POST", eh a mesma coisa. So que a data vai mandar data do browser de um outro jeito
        """
        self.send_response(200); # primera coisa pra fazer. Eh parta do protocol HTTP, da uma olhada online
        self.send_header("Content-Type","text/html"); # Os headers eh parte do HTTP. "Content-Type" fala pra o browser que ta retornando texto ou HTML data.
        self.send_header("Content-Encoding","UTF-8"); # "Content-Encoding" fala pro browser que o binary data que vai receber eh realmente texto no formato de "UTF-8"
        self.end_headers(); # Manda o codigo de controle para o server saber que os headers acabaram

        """
        Fazer coisas aqui, o que voce quer...
        """

        response = bytes("<script>alert(\"Sucesso!\")</script>","UTF-8"); # temos que retornar data binary, no python eh um objeto "bytes"
        self.wfile.write(response);
        return;

    def do_POST(self):
        self.send_response(200);
        self.send_header("Content-Encoding","UTF-8");
        self.send_header("Content-Type","text/html");
        self.end_headers();

        data = self.rfile.read(int(self.headers["Content-Length"])); # data eh recebido em python como um objeto "file". Como outros files em python, tem que dar um numero de quantas caraters pra leer de um file.
        data = bytes.decode(data,encoding="UTF-8");
        print(data);
        return;
