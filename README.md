<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="80" />

---
# Terminal TCP Chat

## Sobre
  - Um projeto de terminal com base em conceitos de redes usando Python e as bibliotecas( socket; threading; os; sys ). 
## Objetivo
  - Possibilitar que hosts conversem por terminal usando um servidor central.

## Funcionamento
  - O Server abre a porta 5000 e os host usam para se comunicar, mandar mensagens simples de texto para cada.

## Comandos

| Comando | Função |
| ------- | ------ |
| `/help` | Exibe a lista de comandos disponíveis |
| `/clear` | Limpa apenas o terminal do usuário que executou o comando |
| `/w` | Limpa o terminal de todos os clientes conectados |
| `/users` | Exibe a lista de usuários conectados ao servidor |
| `/quit` | Encerra a conexão com o servidor |

## Instalação
```bash
git clone https://github.com/luiz-eidt-xp/terminal-TCPchat-PY.git
```

## Executáveis

```powershell
  ChatServer.exe
  ChatClient.exe
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
  1. Execute o arquivo *ChatServer.exe* na máquina que vai servir de servidor(a máquina que vai ser o servidor pode rodar o .exe de cliente também, ela pode fazer os dois papeis.
  2. 
## Troubleshooting

| Problema | Possível causa | Solução |
| -------- | -------------- | ------- |
|          |                |         |
|          |                |         |
|          |                |         |

## Segurança

## Limitações


## Aprendizados

## Licença
