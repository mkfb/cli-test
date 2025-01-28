import subprocess

class Ansible:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def run_playbook(self, playbook_path):
        cmd = f"ansible-playbook {playbook_path}"
        if self.verbose:
            cmd += " -vvv"
        subprocess.run(cmd, shell=True, check=True)

    def deploy(self):
        self.run_playbook('playbooks/deploy.yml')

    def update(self):
        self.run_playbook('playbooks/update.yml')

    def rollback(self):
        self.run_playbook('playbooks/rollback.yml')
