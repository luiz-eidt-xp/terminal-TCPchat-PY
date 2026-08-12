"""
Feito por Luiz Eidt - Aplicação prática do meu conhecimento de redes com python
O objetivo era eu criar um jeito de se comunicar por terminal com outros hosts da mesma rede
"""

import socket
import threading

PORT = 5000

clients = []
names = []

lock = threading.Lock()


def get_local_ip(): # A função pega o ip local do servidor
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
        return ip
    except Exception:
        return "127.0.0.1"


def send_to_client(client, message): # Recebe o cliente e a mensagem e manda para eles
    try:
        client.sendall(message.encode("utf-8"))
        return True
    except:
        return False


def broadcast(message, sender=None):
    with lock:
        for client in clients[:]:
            if client != sender:
                try:
                    client.sendall(message.encode("utf-8"))
                except:
                    pass


def remove_client(client):
    with lock:
        if client in clients:
            index = clients.index(client)
            username = names[index]
            clients.remove(client)
            names.remove(username)
            return username
    return None


def find_user(username):
    with lock:
        for index, name in enumerate(names):
            if name.lower() == username.lower():
                return clients[index], names[index]
    return None, None


def handle_client(client, address):
    name = None

    try:
        name = client.recv(1024).decode("utf-8").strip()

        if not name: # Usuário padrão é "Anonimo"
            name = "Anonimo"

        with lock:
            clients.append(client)
            names.append(name)

        print(f"[+] {name} entrou ({address[0]}:{address[1]})")

        broadcast(f"[SERVIDOR] {name} entrou no chat.")

        while True:
            data = client.recv(4096)

            if not data:
                break

            message = data.decode("utf-8").strip()

            if not message:
                continue

            if message == "/help":
                send_to_client(
                    client,
                    "[COMANDOS] /help | /clear | /wc | /wq | /users | /t usuario mensagem | /quit"
                )
                continue

            if message == "/users": # Função que mostra todos os usuários conectados para o cliente que o executou
                with lock:
                    users = ", ".join(names)

                send_to_client(
                    client,
                    f"[USUARIOS] Conectados: {users}"
                )

                continue

            if message == "/clear": # Funçaõ apaga o terminal do cliente que executou o comando
                send_to_client(client, "__CLEAR__")
                continue

            if message == "/wc": # Função para apagar o terminal de todos os clientes conectados
                print(f"[WORLD CLEAR] {name} limpou todos os terminais.")

                with lock:
                    connected_clients = clients[:]

                for connected_client in connected_clients:
                    try:
                        connected_client.sendall(
                            "__CLEAR_ALL__".encode("utf-8")
                        )
                    except:
                        pass

                continue

            if message == "/wq": # Função para encerrar o terminal e a conexão de todos os clientes
                print(f"[WORLD QUIT] {name} encerrou todos os clientes.")

                with lock:
                    connected_clients = clients[:]

                for connected_client in connected_clients:
                    try:
                        connected_client.sendall(
                            "__WORLD_QUIT__".encode("utf-8")
                        )
                    except:
                        pass

                break

            if message.startswith("/t "): # Função para mandar msg privada para um usuário
                parts = message.split(maxsplit=2)

                if len(parts) < 3:
                    send_to_client(
                        client,
                        "[ERRO] Use: /t 'usuario' 'mensagem'"
                    )
                    continue

                target_name = parts[1]
                tell_message = parts[2]

                target_client, real_target_name = find_user(target_name)

                if target_client is None:
                    send_to_client(
                        client,
                        f"[ERRO] Usuario '{target_name}' nao encontrado."
                    )
                    continue

                send_to_client(
                    target_client,
                    f"[TELL de {name}] {tell_message}"
                )

                send_to_client(
                    client,
                    f"[TELL -> {real_target_name}] {tell_message}"
                )

                print(
                    f"[TELL] {name} -> {real_target_name}: {tell_message}"
                )

                continue

            if message == "/quit":
                send_to_client(
                    client,
                    "[SERVIDOR] Voce foi desconectado."
                )
                break

            print(f"[{name}] {message}")

            broadcast(
                f"[{name}] {message}",
                sender=client
            )

    except ConnectionResetError:
        pass

    except ConnectionAbortedError:
        pass

    except Exception as e:
        print(f"[ERRO] {name}: {e}")

    finally:
        username = remove_client(client)

        if username:
            print(f"[-] {username} saiu.")

            broadcast(
                f"[SERVIDOR] {username} saiu do chat."
            )

        try:
            client.close()
        except:
            pass


server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
)

server.bind(("0.0.0.0", PORT))
server.listen()

local_ip = get_local_ip()

print()
print("---/Cloudsyn.ps1/---")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("           PYTHON TERMINAL CHAT")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print(f"IP do servidor : {local_ip}")
print(f"Porta          : {PORT}")
print()
print("Endereco para conectar:")
print(f"    {local_ip}:{PORT}")
print()
print("Comandos:")
print("    /help")
print("    /clear")
print("    /wc")
print("    /wq")
print("    /users")
print("    /t usuario mensagem")
print("    /quit")
print()
print("Servidor aguardando conexoes...")
print()

while True:
    try:
        client, address = server.accept()

        print(
            f"[+] Nova conexao: "
            f"{address[0]}:{address[1]}"
        )

        thread = threading.Thread(
            target=handle_client,
            args=(client, address),
            daemon=True
        )

        thread.start()

    except KeyboardInterrupt:
        print("\n[!] Servidor encerrado.")
        break

    except Exception as e:
        print(f"[ERRO] Servidor: {e}")

try:
    server.close()
except:
    pass
