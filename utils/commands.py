from utils.base import CLIBase

class DeployCLI(CLIBase):
    def run(self):
        self.logger.info("Starting deployment process")
        self.docker.build_image()
        self.docker.push_image()
        self.ansible.deploy()
        self.logger.info("Deployment process completed")

class UpdateCLI(CLIBase):
    def run(self):
        self.logger.info("Starting update process")
        self.docker.build_image()
        self.docker.push_image()
        self.ansible.update()
        self.logger.info("Update process completed")

class RollbackCLI(CLIBase):
    def run(self):
        self.logger.info("Starting rollback process")
        self.ansible.rollback()
        self.logger.info("Rollback process completed")
