import configparser


class TypeDevice:
    def __init__(self, configPath) :
        self.configPath = configPath

    def getInfoDevices(self, deviceType, keyword) :

        config = configparser.ConfigParser()

        config.read(self.configPath)

        device = config[deviceType]

        return device.get(keyword)


def main() :
    qualcomDevices = TypeDevice('src/config/devices.ini')

    qualcomDevices.getInfoDevices('at_switches', 'path')

if __name__ == '__main__' :
    main()