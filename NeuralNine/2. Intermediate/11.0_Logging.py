import logging
"""

                5 Níveis de segurança

DEBUG    - Informação que somente o desenvolvedor precisa saber ()
INFO     - Alguma informação de valor relativo ao usuário é dado ("You've got mail!")
WARNING  - Algo pode dar errado se não consertar algum problema ("Espaço armazenado no PC está muito baixo")
ERROR    - Um erro que não afeta o sistema fundamentalmente, ("ERROR 404 Page not found")
CRITICAL - Uma parte FUNDAMENTAL do sistêma não está funcionando, terminando o sistema ("Servidor crashou") 

"""


if __name__ == '__main__':

    # Informa o mínimo nivel de segurança que deve ser informado
    logging.basicConfig(level=logging.DEBUG)

    # logging.info(f"You've got 20 mails in your inbox ")
    # logging.critical(F"All components failed!")

    logger = logging.getLogger("NeuralNine Logger")
    logger.setLevel(logging.INFO)
    logger.info("The best logger was just created")
    logger.critical("Your YouTube channel was deleted!")

    # Cria um arquivo onde os logs são registrados
    handler = logging.FileHandler("mylog.log")
    handler.setLevel(logging.INFO)

    # Cria uma fórmula em que o log é informado
    formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    logger.debug("DEBUG MESSAGE!")
    logger.info("INFO MESSAGE!")
