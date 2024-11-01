﻿# Camisa7

## Descrição do Script
Este script automatiza o acesso ao site camisa7.botafogo.com.br e realiza login utilizando o Bitwarden. Após o login, o script captura o saldo total de pontos do programa de sócio torcedor e salva no log.

### Funcionalidades
- **Login Automático**: Utiliza Bitwarden para gerenciar e preencher as credenciais de login.
- **Acesso a Link Interno**: Navega para um link específico dentro do site para coletar a bonificação diária.
- **Registro de Log**: Cria um registro (log) informando o status da execução do script, incluindo sucesso ou falha devido a problemas de acesso.

### Instruções de Uso
1. Configure o Bitwarden com suas credenciais de login para o site específico.
2. Execute o script.
3. Verifique o arquivo de log para confirmar se a execução foi bem-sucedida ou se houve algum problema.

### Logs
O script gera um arquivo de log (`log_acesso_site.log`) que contém informações sobre a execução:
- **Sucesso**: Salva o saldo atual de pontos.
- **Falha**: Indica que houve um problema durante a execução e o site não foi acessado corretamente.

### Requisitos
- Python 3.x
- Bitwarden CLI
- Bibliotecas adicionais: requests, time, logging, json e selenium.
