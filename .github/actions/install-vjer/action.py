"""Program to install Vjer from PyPI or a local directory."""
from argparse import ArgumentParser
from subprocess import check_call


def main() -> None:
    """Main function to parse arguments and install Vjer."""
    parser = ArgumentParser(description='Install Vjer')
    parser.add_argument('--use-pypi-test')
    parser.add_argument('--vjer-local')
    parser.add_argument('--vjer-version')
    args = parser.parse_args()

    install_version = f'=={args.vjer_version}' if args.vjer_version else ''
    pip_command = ['pip', 'install', '--no-cache-dir',
                   '.' if bool(args.vjer_local) else f'vjer{install_version}']
    if bool(args.use_pypi_test):
        pip_command += ['--index-url', 'https://test.pypi.org/simple/',
                        '--extra-index-url', 'https://pypi.org/simple']
    print(pip_command)
    check_call(pip_command, shell=True)


if __name__ == '__main__':
    main()
