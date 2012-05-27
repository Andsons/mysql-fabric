import sys
import os.path

# Compute the directory where this script is. We have to do this
# fandango since the script may be called from another directory than
# the repository top directory.
script_dir = os.path.dirname(os.path.realpath(__file__))

# First item is the script directory or the empty string (for example,
# if running interactively) so we replace the first entry with the
# library directory.
sys.path[0] = os.path.join(script_dir, 'lib')

from unittest import (
    TestLoader,
    TextTestRunner,
    )

def get_options():
    from optparse import OptionParser
    parser = OptionParser()
    # TODO: Fix option parsing so that -vvv and --verbosity=3 give same effect.
    parser.add_option("-v", action="count", dest="verbosity",
                      help="Verbose mode. Multiple options increase verbosity")
    return parser.parse_args()

def run_tests(pkg, opt, args):
    if len(args) == 0:
        import mysql.hub.tests
        args = mysql.hub.tests.__all__
    suite = TestLoader().loadTestsFromNames(pkg + '.' + mod for mod in args)
    TextTestRunner(verbosity=opt.verbosity).run(suite)

if __name__ == '__main__':
    run_tests('mysql.hub.tests', *get_options())
