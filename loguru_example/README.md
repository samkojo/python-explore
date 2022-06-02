# Overview

Demonstrações de uso de log com a biblioteca Loguru

## Utilização

- Configurando para saida em terminal e arquivo formatado
```
python loguru_example/main.py
```

- Integrando com Sentry

Necessário preencher variavel de ambiente `SENTRY_LOGS`, 
com a chave do sentry do seu projeto (dns)
```
python loguru_example/sentry_integration.py
```