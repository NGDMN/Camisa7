﻿# Camisa7
## Descrição do Script

Este script automatiza o acesso a um site específico e realiza login utilizando o Bitwarden. Após o login, o script abre um link interno da página para receber a bonificação por login. 

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
- **Sucesso**: Indica que o script rodou com sucesso e a bonificação foi recebida.
- **Falha**: Indica que houve um problema durante a execução e o site não foi acessado corretamente.

### Requisitos

- Python 3.x
- Bitwarden CLI
- Bibliotecas adicionais: requests, beautifulsoup4, etc.

### Exemplo de Execução

```bash
python Camisa7.py
#   H u b - d e - P r o j e t o s  
 