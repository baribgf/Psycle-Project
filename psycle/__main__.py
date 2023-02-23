
from sys import argv

__version__ = "1.0"

if argv[1] in ('-v', '--version', '-version'):
    print(f"""@ Psycle v{__version__}\n@ Bari BGF 2023""")
