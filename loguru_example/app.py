"""
Exemplo de um arquivo de aplicacao
"""

from loguru import logger

def run():
    # Tipos de logs ordenado por niveis
    logger.debug('Esse é um log de debug')
    logger.info('Esse é um log de info')
    logger.warning('Esse é um log de warning')
    logger.error('Esse é um log de error')
    logger.exception('Esse é um log de exceção')
    logger.critical('Esse é um log de critical')

    # Exibe Traceback completo
    try:
        var = variable_invalid
    except Exception as e:
        logger.exception("Gerou um excessão!")
        logger.error("Gerou um excessão!", exc_info=True)

    # Esconde Traceback
    try:
        var = variable_invalid
    except Exception as e:
        logger.error("Gerou um excessão!")