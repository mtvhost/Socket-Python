import socket
import re
import math

# Expressao regular para validar email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check_email(email):
    if(re.match(regex, email)):
        return("Email valido")
    else:
        return("Email invalido")


def inss_taxes(salary):
    # primeira faixa salarial
    taxes = 0
    if(salary <= 1038.99):
        taxes = salary * 0.075
        return taxes

    taxes += 1038.99 * 0.075

    # segunda faixa salarial
    if(salary <= 2098.60):
        taxes += (salary - 1038.99) * 0.09
        return taxes

    taxes += (2098.60 - 1038.99) * 0.09

    # terceira faixa salarial
    if(salary <= 3134.40):
        taxes += (salary - 2098.60) * 0.12
        return taxes

    taxes += (3134.40 - 2098.60) * 0.12

    # quarta faixa salarial
    if(salary <= 6101.06):
        taxes += (salary - 3134.40) * 0.14
        return taxes

    # valor fixo
    taxes = 604.44
    return taxes


def permutation(number):
    return math.factorial(number)


def main():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = ''
    porta = 50000
    origem = (ip, porta)

    # Vincula com a porta e IP usados
    tcp.bind(origem)

    # Aguarda a chegada de uma conexão TCP
    # Se chegar mais de uma, as demais serão recusadas
    tcp.listen(1)

    # Aceitar a conexão TCP recebida a mais tempo
    tcp_dados, cliente = tcp.accept()

    while(True):
        print("Aguardando ...")

        # Opção de função a ser executada
        command = tcp_dados.recv(1)

        # Tamanho da mensagem que será recebida
        tam_bytes = tcp_dados.recv(2)
        tam_msg = int.from_bytes(tam_bytes, 'big')
        print("Tamanho mensagem:", tam_msg)

        # Mensagem recebida
        msg = tcp_dados.recv(tam_msg)
        print('Mensagem recebida: ', msg.decode())

        # Conversão de Byte para String
        command_dec = command.decode()

        # Verificação da função escolhida
        if(command_dec == "a"):
            print("a")
            resp = check_email(msg.decode())
        elif(command_dec == "b"):
            print("b")
            resp = str(inss_taxes(float(msg.decode())))
        elif(command_dec == "c"):
            print("c")
            resp = str(permutation(int(msg.decode())))
        else:
            print("Encerrando ...")
            break

        # Enviando a resposta ao servidor
        tam_resp = (len(resp)).to_bytes(2, 'big')
        tcp_dados.send(tam_resp + resp.encode())

    # Fechando os sockets
    tcp.close()
    tcp_dados.close()

    input('aperte enter para encerrar')


if __name__ == "__main__":
    main()