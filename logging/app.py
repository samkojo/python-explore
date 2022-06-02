"""
Exemplo de um arquivo de aplicacao
"""

import logging

def run():
    # Tipos de logs ordenado por niveis
    logging.debug('Esse é um log de debug')
    logging.info('Esse é um log de info')
    logging.warning('Esse é um log de warning')
    logging.error('Esse é um log de error')
    logging.exception('Esse é um log de exceção')
    logging.critical('Esse é um log de critical')

    # Exibe Traceback completo
    try:
        var = variable_invalid
    except Exception as e:
        logging.exception("Gerou um excessão!")
        logging.error("Gerou um excessão!", exc_info=True)

    # Esconde Traceback
    try:
        var = variable_invalid
    except Exception as e:
        logging.error("Gerou um excessão!")