import logging
FORMAT = '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s'
logging.basicConfig(filename="hata.log",format=FORMAT,level=logging.WARNING)
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
logging.critical("Dalek! Dalek!")
logging.error("Dalek! Dalek!")