import argparse

class C():
    verbose = False
    test = False
    start = False
    one = False
    file = False
    timer = False
    hook = False
    path = ""
    window_name = ""
    brightness_true = 0
    brightness_false = 0

class Args():

    parser = None
    def init(self):
        self.parser = argparse.ArgumentParser(
            description="Change your computer's brightness based on windows' names specified",
            prog="PROG"
        )
        self.parser.add_argument('-v', '--verbose', action='store_true', help='Prints detailed output')

        subparsers = self.parser.add_subparsers(help='help for subcommand')

        # Create the "start" command
        parser_start = subparsers.add_parser('start',
                                             help='Starts program with the specified options. Detailed options: start -h')
        parser_start.add_argument('start', action="store_true")

        # Define subparsers for "start"
        subparser_start = parser_start.add_subparsers()

        # Define parser for "start one"
        start_one = subparser_start.add_parser("one",
                                               help="Expects a window's name, brightness if true, and brightness if false. Example: \"'Mywebsite - Chrome' 40 0\"")
        start_one.add_argument("one", action="store_true")
        start_one.add_argument("window_name", type=str)
        start_one.add_argument("brightness_true", type=int)
        start_one.add_argument("brightness_false", type=int)

        # Define parser for "start file"
        start_file = subparser_start.add_parser("file", help='Expects a file path')
        start_file.add_argument("file", action="store_true")
        start_file.add_argument("path", type=str)

        # Define method after the start subparser. "start --timer/hook"
        exclusive_start_method = parser_start.add_mutually_exclusive_group()
        exclusive_start_method.add_argument("--timer", dest="timer", action="store_true", help="Method timer (default)")
        exclusive_start_method.add_argument("--hook", dest="hook", action="store_true", help="Method hook")

        # Add "test" subparser
        parser_test = subparsers.add_parser('test', help='Outputs the current window')
        # If user type "PROG test", save the flag as a boolean
        parser_test.add_argument("test", action="store_true")

    def get_args(self):
        c = C()
        args = self.parser.parse_args(namespace=c)
        return args
