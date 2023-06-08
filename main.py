from config import load_config


def main():
    """Main function."""

    config = load_config()

    host = config['database']['host']
    port = config['database']['port']
    user = config['database']['dbname']

    print(f'Host: {host}')
    print(f'Port: {port}')
    print(f'User: {user}')


if __name__ == '__main__':
    main()
