# Projeto Cliente-Servidor UDP

Este projeto consiste em uma aplicação de **cliente-servidor** utilizando o protocolo **UDP (User Datagram Protocol)**. O cliente envia mensagens para o servidor, que as processa e envia respostas de volta. O servidor pode responder com uma mensagem fixa ou simplesmente ecoar as mensagens recebidas.

## Tecnologias Utilizadas

- **Python 3.x**
- **Socket Programming (UDP)**

## Estrutura do Projeto

O projeto é composto por dois módulos principais:

1. **Cliente (UDP Client)**:
    - Envia mensagens para o servidor e aguarda respostas.
    - Permite que o usuário digite uma mensagem, que será enviada ao servidor.
    - Emite a resposta do servidor no console.

2. **Servidor (UDP Server)**:
    - Escuta uma porta específica (porta 8585 no exemplo) e aguarda mensagens do cliente.
    - Responde com uma mensagem fixa ou ecoa a mensagem recebida.

## Requisitos

- Python 3.x instalado em sua máquina.
- Bibliotecas padrão do Python (não há dependências externas).

## Como Rodar o Projeto

### 1. Rodando o Servidor

Para iniciar o servidor, execute o seguinte comando na linha de comando:

```bash
python server.py
```

Isso iniciará o servidor, que ficará esperando por conexões dos clientes na porta `8585`.

### 2. Rodando o Cliente

Em seguida, para rodar o cliente, execute o seguinte comando em outra janela do terminal:

```bash
python client.py
```

O cliente começará a enviar mensagens para o servidor e exibirá as respostas que ele receber. A comunicação continuará até que o usuário digite `"Sair"` (se estiver utilizando a versão do cliente que contém a funcionalidade de saída).

## Como Funciona

### Comunicação Cliente-Servidor

1. O cliente envia uma mensagem ao servidor utilizando o protocolo UDP.
2. O servidor recebe a mensagem, processa-a (ou apenas a ecoa) e envia uma resposta.
3. O cliente exibe a resposta recebida do servidor.

### Protocolos e Funcionalidades

- O projeto utiliza o **UDP** para a comunicação entre o cliente e o servidor. O UDP é um protocolo sem conexão, o que significa que não há garantia de entrega ou ordem das mensagens.
- O servidor pode ser configurado para responder com uma mensagem fixa ou simplesmente ecoar a mensagem recebida.

## Exemplos

### Cliente - Exemplo de Interação

Ao rodar o cliente, você verá o seguinte comportamento:

```
Informe a msg a ser enviada para o servidor: Hello, Server!
Informação devolvida do servidor: Hello, Server!
```

Se o cliente estiver utilizando a versão com controle de saída, você pode digitar `"Sair"` para encerrar a comunicação:

```
Informe a msg a ser enviada para o servidor: Sair
Saindo...
```

### Servidor - Exemplo de Saída

O servidor, ao receber uma mensagem, pode exibir algo como:

```
Mensagem recebida: Hello, Client!
```

## Contribuindo

Se você deseja contribuir para este projeto, sinta-se à vontade para fazer um **fork** do repositório e enviar um **pull request**. Fique à vontade para melhorar a funcionalidade do servidor, adicionar novas funcionalidades ou corrigir bugs.

1. Faça um fork do projeto.
2. Crie uma nova branch para sua modificação.
3. Realize suas modificações.
4. Envie um pull request com a descrição do que foi alterado.

## Licença

Este projeto é de código aberto e pode ser utilizado e modificado sob a licença [MIT](LICENSE).
