import sys

from cliff import app
from cliff import commandmanager as cm
from conf import default

import tacoclient

class TacoClientApp(app.App):
    def __init__(self, **kwargs):
        super(TacoClientApp, self).__init__(
            description='tacoclient - CLI client for TACO(SKT All Container \
            Openstack)',
            version=tacoclient.__version__,
            command_manager=cm.CommandManager('tacoclient'),
            **kwargs)

    def build_option_parser(self, description, version, argparse_kwargs=None):
        parser = super(TacoClientApp, self).build_option_parser(
            description, version, argparse_kwargs)
        return parser

    def configure_logging(self):
        super(TacoClientApp, self).configure_logging()
        default.register_opts()

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    return TacoClientApp().run(argv)
