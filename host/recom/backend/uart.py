import serial
import serial.tools.list_ports

def getSerialPortList():
    ports = serial.tools.list_ports.comports()
    #port_list = []
    #for p in ports:
    #    this_port = []

    #    port_list.append(this_port)

    return ports