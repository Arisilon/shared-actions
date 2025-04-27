"""Program to install Vjer from PyPI or a local directory."""
# flake8: noqa: E501
from os import getenv
from subprocess import check_call


class Environment:
    """Class to access environment variables."""
    def __getattr__(self: 'Environment', name: str) -> str:
        """Get an environment variable."""
        return getenv(name, '')

    def bool(self: 'Environment', name: str) -> bool:
        """Get a boolean environment variable."""
        return getenv(name, 'false').lower() == 'true'


def main() -> None:
    """Main function to parse arguments and install Vjer."""
    env = Environment()
    install_version = f'=={env.vjer_version}' if (env.vjer_version != 'latest') else ''
    print(pip_command := ['pip', 'install', '--no-cache-dir', '.' if env.bool('vjer_local') else f'vjer{install_version}'])
    check_call(pip_command)


if __name__ == '__main__':
    main()
