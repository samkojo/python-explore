"""
Exemplo de um __main__ do app configurado com Logging
utilizando handlers
"""

import logging
import app

if __name__ == "__main__":

    # Logger padrao Root
    logger = logging.getLogger('root')
    logger.setLevel(logging.NOTSET)

    # Utilizando como saida o terminal e um arquivo
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(filename='logs.log')

    # Podemos definir a partir de qual nivel deve exibir em cada
    stream_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)

    # Podemos definir formatadores para cada
    stream_format = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    file_format = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
    stream_handler.setFormatter(stream_format)
    file_handler.setFormatter(file_format)

    # Definimos os handlers no logging
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    app.run()