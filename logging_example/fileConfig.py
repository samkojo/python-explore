"""
Exemplo de um __main__ do app configurado com Logging
utilizando handlers
"""

import logging.config
import app

if __name__ == "__main__":
    logging.config.fileConfig(fname='logs/logging.conf')
    app.run()