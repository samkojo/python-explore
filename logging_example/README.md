# Overview

Demonstrações de uso de log com a biblioteca nativa logging

## Utilização

- Modo simplificado (basicConfig)
```
python logging_example/basicConfig.py
```

- Utilizando handlers
```
python logging_example/handler.py
```

- Configurando via arquivo .conf
```
python logging_example/fileConfig.py
```

- Integrando com Sentry

Necessário preencher variavel de ambiente `SENTRY_LOGS`, 
com a chave do sentry do seu projeto (dns)
```
python logging_example/sentry_integration.py
```