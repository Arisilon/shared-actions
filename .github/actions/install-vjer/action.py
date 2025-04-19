"""Program to install Vjer from PyPI or a local directory."""
from argparse import ArgumentParser
from subprocess import check_output


def main() -> None:
    """Main function to parse arguments and install Vjer."""
    parser = ArgumentParser(description='Install Vjer')
    parser.add_argument('--use-pypi-test')
    parser.add_argument('--vjer-local')
    parser.add_argument('--vjer-version')
    args = parser.parse_args()

    pypi_test_option = '--index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple' if bool(args.use_pypi_test) else ''  # noqa: E501
    install_version = f'=={args.vjer_version}' if args.vjer_version else ''
    install_location = '.' if bool(args.vjer_local) else 'vjer'
    check_output(['pip', 'install', '--quiet', '--no-cache-dir',
                  pypi_test_option,
                  f'{install_location}{install_version}'],
                 shell=True)


if __name__ == '__main__':
    main()
