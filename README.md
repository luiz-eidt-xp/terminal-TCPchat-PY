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
