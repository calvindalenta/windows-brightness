from args_helper import Args

a = Args()
a.init()
args = a.get_args()
temp = vars(args)
print(vars(args))
# args.print()

if args.test:
    # Just do printing and do nothing else
    pass

if args.verbose:
    # Do verbose
    pass

if args.start:
    # Do normal start
    # Check if one or file
    # Get the input based on the check
    # Check if hook or timer
    # Do
    pass
