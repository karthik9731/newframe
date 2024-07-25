import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=r"C:\Users\ckart\PycharmProjects\pythonProject1\newframe\Logs\automation.log",
                            format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger