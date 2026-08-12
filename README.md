# <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="35" /> Terminal TCP Chat

---
## Índice

- [Sobre](#sobre)
- [Objetivo](#objetivo)
- [Funcionamento](#funcionamento)
- [Comandos](#comandos)
- [Instalação](#instalação)
- [Como executar](#como-executar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como usar](#como-usar)
- [Bugs](#bugs)
- [Segurança](#segurança)
- [Limitações](#limitações)
- [Aprendizados](#aprendizados)
- [Licença](#licença)
---

## Sobre
  - Um projeto de terminal com base em conceitos de redes usando Python e as bibliotecas( socket; threading; os; sys ). 
## Objetivo
  - Possibilitar que hosts de um mesma rede conversem por terminal usando um servidor central.

## Funcionamento
  - O servidor é o ponto central da comunicação, o servidor cria um SOCKET TCP e fica esperando conexões.
  - O cliente cria também um socket TCP e conecta ao servidor pelo IP fornecido
  - ou seja a conexão fica assim
    - Cliente(192.168.X.X, user="João") --> TCP --> Servidor(192.168.X.X) --> TCP --> Cliente(192.168.X.X, user="Ana")

- O caminho das mensagens é bem simples:
  - O cliente ele manda um "Olá"
  - A mensagem chega no servidor
  - O servidor distribui para todos os usuários conectados
 ```
┌───────────┐
│   Alice   │
│  Client   │
└─────┬─────┘
      │
      │ TCP
      │ "Olá"
      ▼
┌───────────────┐
│    SERVER     │
│               │
│ recebe "Olá"  │
└───────┬───────┘
        │
        │ broadcast
        ├───────────────┐
        │               │
        ▼               ▼
   ┌─────────┐     ┌─────────┐
   │  Bob    │     │  Carlos │
   │ Client  │     │ Client  │
   └─────────┘     └─────────┘
```

-E o funcionamento do /t ele só especifica o cliente que vai receber
 
## Arquitetura
```
                         REDE LOCAL
┌─────────────────────────────────────────────────────────┐
│                                                         │
│                 ┌─────────────────┐                   │
│                 │     SERVER      │                   │
│                 │                 │                   │
│                 │    server.py    │                   │
│                 │                 │                   │
│                 │    socket       │                   │
│                 │    threading    │                   │
│                 └────────┬────────┘                   │
│                          │                             │
│              ┌───────────┼───────────┐                │
│              │           │           │                │
│              ▼           ▼           ▼                │
│         ┌─────────┐ ┌─────────┐ ┌─────────┐           │
│         │ Client  │ │ Client  │ │ Client  │           │
│         │    A    │ │    B    │ │    C    │           │
│         │         │ │         │ │         │           │
│         │client.py│ │client.py│ │client.py│           │
│         └─────────┘ └─────────┘ └─────────┘           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```
> Resumindo é um servidor de uma rede local privada para enviar mensagens de texto simples usando o protocolo TCP/IP

## Comandos

| Comando | Função | Escopo |
| ------- | ------ | ------ |
| `/help` | Exibe a lista de comandos disponíveis | Local |
| `/clear` | Limpa o terminal atual | Local |
| `/wc` | Limpa os terminais de todos os usuários conectados | Global |
| `/wq` | Encerra a conexão de todos os usuários conectados | Global |
| `/users` | Exibe a lista de usuários conectados | Servidor |
| `/t usuario mensagem` | Envia uma mensagem privada para um usuário específico | Privado |
| `/quit` | Encerra a conexão do usuário atual | Local |

## Instalação
```bash
git clone https://github.com/luiz-eidt-xp/terminal-TCPchat-PY.git
```

## Como executar
Rode os .exe, o "ChatServer.exe" no host que vai servir de server e o "ChatClient.exe" para o host cliente.
```powershell
  ChatServer.exe
  ChatClient.exe
```
ou
Rode os arquivos python abrindo um terminal na pasta do projeto(server.py no servidor e o client.py no cliente)
```python
python client.py
python server.py
```

## Estrutura do Projeto

```text
terminal-TCPchat-PY/
│
├── server.py
├── client.py
│
├── ChatServer.spec
├── ChatClient.spec
│
├── build/
│   ├── ChatServer/
│   └── ChatClient/
│
├── dist/
│   ├── ChatServer.exe
│   └── ChatClient.exe
│
├── README.md
└── LICENSE
```

## Como usar:
  1. Execute o arquivo *ChatServer.exe* ou *server.py* na máquina que vai servir de servidor (a máquina que vai ser o servidor pode rodar o .exe de cliente também, ela pode fazer os dois papeis.)
  2. Agora execute os arquivos de cliente nos hosts que vão ser o cliente( *ChatClient.exe* ou *client.py* )
  3. O client vai pedir o ip do server para se conectar, o IP que aparece no terminal que ta rodando o servidor, coloque-o para se conectar
  4. Escolha um nome e use
  5. 
## bugs

| Problema | Possível causa | Solução |
| -------- | -------------- | ------- |
| Não conecta | Ip errado ou porta errada | Mudar o ip ou a porta para a correta |
| Mensagem que estava sendo escrita bugou | Recebeu uma mensagem enquanto estava escrevendo                | dar um /clear para desbugar         |

## Segurança
- As mensagens não são enviadas com criptografia, os pacotes são enviados usando texto puro.
- Podem ser interceptados usando uma ferramenta como "WireShark".
- Não a autenticação, qualquer um que ter o Client.py(ou algum arquivo que faça essa função), tiver a porta e o ip do servidor e estiver conectada na mesma rede pode conectar nas mensagens.
- 
## Limitações
- Somente hosts na mesma rede podem conversar entre si
- Meio bugado as vezes

## Aprendizados
- Aprendi a mexer com as bibliotecas scoket e threading no python, e aprendi o funcionamento de um servidor de chat usando TCP/IP, com comandos personalizados de terminal

> Licença
*Copyright: cloudsyn.ps1*
