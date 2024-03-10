__author__ = "joe di castro <joe@joedicastro.com>"
__license__ = "GNU General Public License version 3"
__date__ = "03/12/2011"
__version__ = "0.3"

try:
    import sys
    import os
    from argparse import ArgumentParser
    from subprocess import Popen, PIPE
except ImportError:
    # Checks the installation of the necessary python modules
    print((os.linesep * 2).join(["An error found importing one module:",
          str(sys.exc_info()[1]), "You need to install it", "Stopping..."]))
    sys.exit(-2)


def check_execs(*progs):
    """Check if the programs are installed, if not exit and report."""
    for prog in progs:
        try:
            Popen([prog, '--help'], stdout=PIPE, stderr=PIPE)
        except OSError:
            msg = 'The {0} program is necessary to run the script'.format(prog)
            sys.exit(msg)
    return


def arguments():
    """Defines the command line arguments for the script."""
    main_desc = """Converts a djvu file into a pdf file"""

    parser = ArgumentParser(description=main_desc)
    parser.add_argument("file", nargs="+", help="The djvu file")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d", dest="qlty", action="store_const", const="-d",
                       help="no compression. Best quality but big files.")
    group.add_argument("-z", dest="qlty", action="store_const", const="-z",
                       help="zip compression. More quality, more size.")
    parser.add_argument("-v", "--version", action="version",
                        version="%(prog)s {0}".format(__version__),
                        help="show program's version number and exit")
    return parser


def process(command, fname):
    """Process the external commands and report the errors."""
    errors = Popen(command, stderr=PIPE).stderr.readlines()
    for line in errors:
        print("{0}: {1}".format(fname.upper(), line.rstrip(os.linesep)))

def convert_djvu2pdf(djvu_file_path: str):
    print(f'djvu_file_path: {djvu_file_path}')
    for djvu in djvu_file_path:
        if not os.path.exists(djvu):
            print("ERROR: cannot open '{0}' (No such file)".format(djvu))
        else:
            djvu_filename = djvu.split(".djvu")[0]
            tiff = '{0}.tif'.format(djvu_filename)
            pdf = '{0}.pdf'.format(djvu_filename)
            process(['ddjvu', '-format=tiff', djvu, tiff], tiff)
            if os.path.exists(tiff):
                quality = '-d'
                process(['tiff2pdf', quality, '-o', pdf, tiff], pdf)
                os.remove(tiff)
