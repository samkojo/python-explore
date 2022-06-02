"""
Exemplo de um __main__ do app configurado com Loguru 
e integracao com Sentry
"""

import os
import sys
from logging import WARNING
from loguru import logger
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration, EventHandler
import app

if __name__ == "__main__":
    # remove todas as saidas ativas anteriormente
    logger.remove()

    # adiciona saida ao terminal formatado
    logger.add(sys.stderr, 
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>", 
    level="INFO")

    # Inicia o sentry
    sentry_sdk.init(
    dsn=os.getenv('SENTRY_LOGS'),
        integrations=[LoggingIntegration(level=None, event_level=None)]
    )  

    # Adiciona o sentry ao loguru
    logger.add(
        EventHandler(level=WARNING), format='{message}'
    )  

    app.run()