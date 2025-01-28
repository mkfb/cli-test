import logging

class Logging:
    def __init__(self, log_path=None, verbose=False):
        logging.basicConfig(
            filename=log_path,
            level=logging.DEBUG if verbose else logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger()

    def get_logger(self):
        return self.logger
