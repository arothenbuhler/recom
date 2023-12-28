from interface import DeviceInterface
import enum

class BASE_DEV_CMDS(enum.IntEnum):
    CMD_PING            = 0x00,
    CMD_HW_ID           = 0x01,
    CMD_HW_REV          = 0x02,
    CMD_FW_REV          = 0x03,
    CMD_SERIAL          = 0x04,
    CMD_RESET           = 0x05
    CMD_GET_INTERFACES  = 0x06,

class BaseDevice:
    
    def __init__(self):
        self._interfaces = []
        self._comsBackend = None

        # TODO: Detect and setup COMs backend

        controlDescriptor = {
            'id':       0,
            'name':     'Control',
        }
        self._controlItf = DeviceInterface(self._comsBackend, controlDescriptor)

    def _detectInterfaces(self):
        #If USB, get the interfaces from the USB library/descriptor
        #If UART or other interface, use the control interface to query the available interfaces
        pass

    def getAllInterfaces(self):
        """Returns a list of available interfaces"""
        pass

    def getInterfaceHandle(self, interfaceNum):
        pass


class Device(BaseDevice):

    def __init__(self, kwargs):
        pass

    def reset(self):
        pass

    @property
    def hw_id(self):
        return ''

    @property
    def hw_revision(self):
        return ''

    @property
    def fw_revision(self):
        return ''


