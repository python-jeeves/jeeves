import logging
from dataclasses import dataclass
from pathlib import Path

import requests
from dependencies import Injector, this

from jeeves.commands.project_root import ProjectRoot
from jeeves.models import Command

logger = logging.getLogger(__name__)


def infrastructure_directory(project_root: Path) -> Path:
    """Directory to store Terraform files."""
    return project_root / 'infra'


@dataclass
class InfrastructureDirectory:
    project_root: ProjectRoot

    def __call__(self):
        return self.project_root() / 'infra'


@dataclass
class Install(Command):
    """Install Terraform."""

    version: str
    infrastructure_directory: InfrastructureDirectory

    def __call__(self):
        """Install Terraform."""
        self.log('Installing Terraform {version}...', version=self.version)
        target_path = self.infrastructure_directory() / f'.bin/terraform-{self.version}'
        url = f'https://releases.hashicorp.com/terraform/{self.version}/terraform_{self.version}_linux_amd64.zip'

        target_path.parent.mkdir(parents=True, exist_ok=True)

        with target_path.open('wb+') as f:
            f.write(requests.get(url).content)


class Terraform(Injector):
    """Terraform is a leading Infrastructure As Code tool."""

    project_root = (this << 1).project_root

    version = '0.13.1'
    infrastructure_directory = InfrastructureDirectory

    install = Install
