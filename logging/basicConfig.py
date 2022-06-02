"""
Exemplo de um __main__ do app configurado com Logging 
utilizando somente basicConfig
"""

import logging
import app

if __name__ == "__main__":
    # Configura exibição do log de forma basica com somente uma saida
    logging.basicConfig(
        level=logging.INFO, 
        # filename='log.txt', # Configura log para ser salvo em um arquivo
        format='%(asctime)s %(levelname)s %(message)s',
    )

    app.run()