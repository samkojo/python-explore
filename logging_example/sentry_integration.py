"""
Exemplo de um __main__ do app configurado com Logging 
utilizando somente basicConfig
"""

import os
import logging
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
import app

if __name__ == "__main__":
    # Inicia o sentry
    sentry_sdk.init(
        os.getenv('SENTRY_LOGS'),
        integrations=[LoggingIntegration(level=logging.WARNING, event_level=logging.WARNING)]
    )

    # Configura exibição do log de forma basica com somente uma saida
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s %(levelname)s %(message)s',
    )

    app.run()