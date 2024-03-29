from app import app
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--source', default='kipoi', help='Kipoi source to use')
    parser.add_argument('--host', default='0.0.0.0', help='The hostname to listen on.')
    parser.add_argument('-p', '--port', type=int, default=5000, help='The port of the webserver.')
    parser.add_argument('-d', '--debug', action='store_true', help='If given, enable or disable debug mode.')

    args = parser.parse_args()

    app.config.update(
        DEBUG=args.debug,
        SOURCE=args.source
    )

    app.run(host=args.host, port=args.port, debug=args.debug)
