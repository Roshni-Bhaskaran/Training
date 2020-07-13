<<<<<<< HEAD
import logging

def logg():
    logging.basicConfig(filename="log_.txt",
                    filemode='a',
                    format='%(asctime)s - %(message)s',
                    level=logging.INFO)
=======
import logging

def logg():
    logging.basicConfig(filename="log_.txt",
                    filemode='a',
                    format='%(asctime)s - %(message)s',
                    level=logging.INFO)
>>>>>>> 06ce908d6425d4482fe841a5d13edcee214d17f3
    return logging