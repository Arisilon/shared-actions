"""Program to install Vjer from PyPI or a local directory."""
from os import getenv
from subprocess import check_call

VJER_VERSION = getenv('VJER_VERSION', 'latest')
VJER_LOCAL = getenv('VJER_LOCAL', 'false').lower() == 'true'
USE_PYPI_TEST = getenv('USE_PYPI_TEST', 'false').lower() == 'true'


def main() -> None:
    """Main function to parse arguments and install Vjer."""
    install_version = f'=={VJER_VERSION}' if (VJER_VERSION != 'latest') else ''
    pip_command = ['pip', 'install', '--no-cache-dir']
    if USE_PYPI_TEST:
        pip_command += ['--index-url', 'https://test.pypi.org/simple/',
                        '--extra-index-url', 'https://pypi.org/simple']
    pip_command += ['.' if VJER_LOCAL else f'vjer{install_version}']
    print(pip_command)
    check_call(pip_command)


if __name__ == '__main__':
    main()
