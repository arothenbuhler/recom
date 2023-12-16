import argparse

import recom
from recom.backend.uart import getSerialPortList

def pretty_print_table(header, items):
    return

def print_serial_port_list(more_info, test_port):
    port_list = getSerialPortList()
    if port_list is []:
        print("No serial ports found!")
        return
    print("ID\t\tName\t\tAdditional Info")
    for port in port_list:
        print(f'{port[0]}\t{port[1]}\t{port[2]}')




def cli(argv):
    parser = argparse.ArgumentParser(description="Open a serial port and read/write data.")
    parser.add_argument('--version', action='version', version=recom.__version__,
                                                help="Print package version")
    parser.add_argument('-p', '--port', help="Serial port path or number")
    parser.add_argument('--baud', type=int, default=115200,
                                                help="Baud rate (default: 115200)")
    parser.add_argument('-v', '--verbose', action='store_true',
                                                help="Print more information")
    parser.add_argument('-t', '--test', action='store_true',
                                                help="Test if serial port is available")

    args = parser.parse_args(argv)

    # If no port was provided, then we simply print the list of serial ports
    print_serial_port_list(args.verbose, args.test)
    return 0

