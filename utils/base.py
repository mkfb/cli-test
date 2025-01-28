from utils.ansible import Ansible
from utils.docker import Docker
from utils.logging import Logging
from utils.config import Config


class CLIBase:
    def __init__(self, config_path, environment, verbose, log_path, secret):
        self.config_path = config_path
        self.environment = environment
        self.verbose = verbose
        self.log_path = log_path
        self.secret = secret
        self.logger = Logging(log_path=log_path, verbose=verbose).get_logger()
        self.ansible = Ansible(verbose=self.verbose)
        self.config = Config(config_path).get_docker_config()
        self.docker = Docker(config=self.config, logger=self.logger)
