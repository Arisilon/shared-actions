"""Program to install Vjer from PyPI or a local directory."""
from subprocess import check_call
from sys import argv, exit as sys_exit, stderr


def main() -> None:
    """Main function to parse arguments and install Vjer."""
    if len(argv) != 4:
        print('Usage: action.py <version> <use_local> <use_pypi_test>',
              file=stderr)
        sys_exit(1)
    (version, use_local, use_pypi_test) = argv[1:4]
    install_version = f'=={version}' if (version != 'latest') else ''
    pip_command = ['pip', 'install', '--no-cache-dir']
    if bool(use_pypi_test):
        pip_command += ['--index-url', 'https://test.pypi.org/simple/',
                        '--extra-index-url', 'https://pypi.org/simple']
    pip_command += ['.' if bool(use_local) else f'vjer{install_version}']
    print(pip_command)
    check_call(pip_command)


if __name__ == '__main__':
    main()
