class Command:
    """Basic CLI command."""

    def log(self, message: str, **kwargs):
        """Print something."""
        formatted_message = message.format(**kwargs)
        print(f'{self.__class__.__name__} | {formatted_message}')
