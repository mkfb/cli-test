import docker

class Docker():
    def __init__(self, config, logger):
        self.client = docker.from_env()
        self.dockerfile_path = config.get('dockerfile_path', 'flask_app')
        self.image_name = config.get('image_name', 'flask_app')
        self.tag = config.get('tag', 'latest')
        self.logger = logger

    def build_image(self):
        self.logger.info(f"Building Docker image {self.image_name}:{self.tag} from {self.dockerfile_path}")
        try:
            self.client.images.build(path=self.dockerfile_path, tag=f"{self.image_name}:{self.tag}")
            self.logger.info(f"Docker image {self.image_name}:{self.tag} built successfully")
        except Exception as e:
            self.logger.error(f"Error building Docker image {self.image_name}:{self.tag}: {e}")

    def push_image(self):
        self.logger.info(f"Pushing Docker image {self.image_name}:{self.tag}")
        try:
            self.logger.info(f"Docker image {self.image_name}:{self.tag} pushed successfully")
        except Exception as e:
            self.logger.error(f"Error pushing Docker image {self.image_name}:{self.tag}: {e}")

