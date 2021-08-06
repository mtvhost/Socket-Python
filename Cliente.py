import socket


def main():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip_serv = '192.168.0.102'
    porta_serv = 50000
    dest = (ip_serv, porta_serv)

    # Conectando ao servidor TCP (handshake)
    tcp.connect(dest)
    print("Conexão TCP estabelecidade")
    
    while(True):

	    # Lendo uma mensagem
	    print("Opções:")
	    print("a - Verificar email")
	    print("b - Desconto do inss")
	    print("c - Quantidade de permutações")
	    print("Qualquer outra letra - Encerra conexão TCP")
	    print("Entre com uma opção:")
	    command = input()
	    # Verificação da função escolhida
	    if(command == "a"):
	    	print("Verificar email")
	    	print("Entre com o email:")
	    	email = input()
	    	opcao = ("a").encode()
	    	tam_email = (len(email)).to_bytes(2, 'big')
	    	tcp.send(opcao + tam_email + email.encode())
	    elif(command == "b"):
	    	print("Desconto do inss")
	    	print("Entre com o salário:")
	    	salario = input()
	    	opcao = ("b").encode()
	    	tam_salario = (len(salario)).to_bytes(2, 'big')
	    	tcp.send(opcao + tam_salario + salario.encode())
	    elif(command == "c"):
	    	print("Quantidade de permutações")
	    	elementos = input()
	    	opcao = ("c").encode()
	    	tam_elementos = (len(elementos)).to_bytes(2, 'big')
	    	tcp.send(opcao + tam_elementos + elementos.encode())
	    else:
	    	print("Qualquer outra letra")
	    	break

	    # Lê o tamanho da mensagem de resposta
	    bytes_resp = tcp.recv(2)
	    tam_resp = int.from_bytes(bytes_resp, 'big')

	    # Lê a mensagem, considerando o tamanho recebido
	    resp = tcp.recv(tam_resp)

	    print('Resposta: ', resp.decode())

    tcp.close()
    input('aperte enter para encerrar')

if __name__ == "__main__":
    main()


