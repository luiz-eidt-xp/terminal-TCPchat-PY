"""
Feito por Luiz Eidt - Aplicação prática do meu conhecimento de redes com python
"""

import socket
import threading
import os
import sys

PORT = 53721

running = True


def clear_screen():
    os.system(
        "cls" if os.name == "nt" else "clear"
    )


def show_header(): # Função que mostra o topo do programa, aparece sempre
    print()
    print("---/Cloudsyn.ps1/---")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("           PYTHON TERMINAL CHAT")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print(f"Servidor: {SERVER}:{PORT}")
    print(f"Usuario: {name}")
    print()
    print("Digite /help para ver os comandos.")
    print()


def receive_messages(): # Recebe as mensagens do servidor e mostra para o usuário, também trata os comandos recebidos do servidor
    global running

    buffer = ""

    while running:
        try:
            data = client.recv(4096)

            if not data:
                print(
                    "\n[!] Servidor desconectado."
                )
                running = False
                break

            buffer += data.decode("utf-8")

            while "\n" in buffer:
                message, buffer = buffer.split(
                    "\n",
                    1
                )

                message = message.strip()

                if not message:
                    continue

                if message == "__CLEAR__": # comando /clear
                    clear_screen()
                    show_header()
                    continue

                if message == "__CLEAR_ALL__": # comando /wc
                    clear_screen()
                    show_header()
                    print(
                        "[WORLD CLEAR]"
                    )
                    print()
                    continue

                if message == "__WORLD_QUIT__": # comando /wq
                    clear_screen()

                    print(
                        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                    )
                    print(
                        "                WORLD QUIT"
                    )
                    print(
                        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                    )
                    print()
                    print(
                        "[SERVIDOR] "
                        "wq executado com sucesso"
                    )
                    print()

                    running = False

                    try:
                        client.shutdown(
                            socket.SHUT_RDWR
                        )
                    except:
                        pass

                    try:
                        client.close()
                    except:
                        pass

                    os._exit(0)

                print(
                    f"\r{message}"
                )

                print(
                    "> ",
                    end="",
                    flush=True
                )

        except ConnectionResetError:
            running = False
            break

        except OSError:
            running = False
            break

        except UnicodeDecodeError:
            print(
                "\n[ERRO] Dados invalidos recebidos."
            )
            running = False
            break

        except Exception as e:
            print(
                f"\n[ERRO] {e}"
            )
            running = False
            break


print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("           PYTHON TERMINAL CHAT")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

SERVER = input(
    "IP do servidor: "
).strip()

if not SERVER:
    print(
        "[ERRO] IP invalido."
    )
    sys.exit()

if ":" in SERVER:
    SERVER, port_text = SERVER.rsplit(
        ":",
        1
    )

    try:
        PORT = int(port_text)
    except ValueError:
        print(
            "[ERRO] Porta invalida."
        )
        sys.exit()

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.settimeout(10)

try:
    client.connect(
        (SERVER, PORT)
    )

except socket.timeout:
    print()
    print(
        "[ERRO] Tempo limite de conexao."
    )
    print(
        f"[INFO] Servidor: "
        f"{SERVER}:{PORT}"
    )
    sys.exit()

except ConnectionRefusedError: # Caso aconteça de não conectar, aparece para o usuário seguir esses passos
    print()
    print(
        "[ERRO] O servidor recusou a conexao."
    )
    print()
    print("Verifique se:")
    print(
        "  - server.py esta rodando"
    )
    print(
        "  - o IP esta correto"
    )
    print(
        f"  - a porta {PORT} "
        "esta acessivel"
    )
    print(
        "  - o firewall permite conexoes"
    )
    sys.exit()

except OSError as e:
    print()
    print(
        f"[ERRO] Nao foi possivel "
        f"conectar: {e}"
    )
    print()
    print(
        "Possiveis causas:"
    )
    print(
        "  - IP incorreto"
    )
    print(
        "  - porta bloqueada"
    )
    print(
        "  - firewall"
    )
    print(
        "  - hosts em redes diferentes"
    )
    sys.exit()

finally:
    client.settimeout(None)


name = input(
    "Seu nome: "
).strip()

if not name:
    name = "Anonimo"

client.sendall(
    (name + "\n").encode("utf-8")
)

print()
print(
    "Conectado ao servidor."
) # Aparece essa msg no topo quando você conecta ao servidor

print()
print("Comandos:")
print(
    "  /help              - "
    "Mostra os comandos"
)
print(
    "  /clear             - "
    "Limpa seu terminal"
)
print(
    "  /wc                - "
    "Limpa todos os terminais"
)
print(
    "  /wq                - "
    "Encerra todos os clientes"
)
print(
    "  /users             - "
    "Lista usuarios"
)
print(
    "  /t usuario msg     - "
    "Envia um TELL"
)
print(
    "  /quit              - "
    "Sair"
)
print()

thread = threading.Thread(
    target=receive_messages,
    daemon=True
)

thread.start()

while running:
    try:
        message = input("> ")

        if message == "/help":
            print()
            print(
                "Comandos disponiveis:"
            )
            print()
            print(
                "  /help              - "
                "Mostra os comandos"
            )
            print(
                "  /clear             - "
                "Limpa seu terminal"
            )
            print(
                "  /wc                - "
                "Limpa todos os terminais"
            )
            print(
                "  /wq                - "
                "Encerra todos os clientes"
            )
            print(
                "  /users             - "
                "Lista usuarios"
            )
            print(
                "  /t usuario msg     - "
                "Envia um TELL"
            )
            print(
                "  /quit              - "
                "Sair"
            )
            print()
            continue

        if message == "/clear":
            clear_screen() # apaga todas as msgs
            show_header()
            continue

        if message == "/quit":
            try:
                client.sendall(
                    "/quit\n".encode("utf-8")
                )
            except:
                pass

            print()
            print(
                "Desconectando..."
            )

            running = False
            break

        if not message.strip():
            continue

        client.sendall(
            (message + "\n").encode("utf-8")
        )

    except KeyboardInterrupt:
        print()
        print(
            "Desconectando..."
        )

        try:
            client.sendall(
                "/quit\n".encode("utf-8")
            )
        except:
            pass

        running = False
        break

    except BrokenPipeError:
        print()
        print(
            "[ERRO] Conexao perdida."
        )
        running = False
        break

    except OSError:
        print()
        print(
            "[ERRO] Conexao encerrada."
        )
        running = False
        break


try:
    client.shutdown(
        socket.SHUT_RDWR
    )
except:
    pass

try:
    client.close()
except:
    pass

print(
    "Conexao encerrada."
)