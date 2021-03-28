from dependencies import Injector

from jeeves_terraform.terraform import Terraform


class JeevesTerraform(Injector):
    """
    Terraform is a leading Infrastructure As Code tool.

    This class exposes a `tf` subcommand which helps install and manage
    Terraform for your project.
    """

    tf = Terraform
