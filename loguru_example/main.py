"""
Exemplo de um __main__ do app configurado com Loguru
"""

from importlib import import_module
import app
from loguru import logger
import sys

if __name__ == "__main__":
    # remove todas as saidas ativas anteriormente
    logger.remove()

    # adiciona saida a um arquivo
    logger.add('logs.log', format="{time} {level} {message}", level="INFO")

    # adiciona saida ao terminal formatado
    logger.add(sys.stderr, 
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>", 
    level="INFO")
    app.run()

# default format Loguru
# "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
