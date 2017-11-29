from abc import ABCMeta, abstractmethod


class ISwitch(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_on(self):
        pass

    @abstractmethod
    def press(self):
        pass


class ISwitchable(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class ElectricPowerSwitch(ISwitch):

    def __init__(self, switchable_client):
        self.client = switchable_client
        self.on = False

    def is_on(self):
        return self.on

    def press(self):
        check_on = self.is_on()
        if check_on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


class LightBulb(ISwitchable):
    def turn_on(self):
        print "Lightbulb: Bulb turned on.."

    def turn_off(self):
        print "LightBulb: bulb turned off.."


class Fan(ISwitchable):
    def turn_on(self):
        print "Fan: Fan turned on.."

    def turn_off(self):
        print "Fan: Fan turned off.."

class AirCondition(ISwitchable):
    def turn_off(self):
        print "AirCondition: AC turned off..."

    def turn_on(self):
        print "AirCondition: AC turned on..."


def main():
    light_bulb = LightBulb()
    bulb_power_switch = ElectricPowerSwitch(light_bulb)
    bulb_power_switch.press()
    bulb_power_switch.press()

    fan = Fan()
    fan_power_switch = ElectricPowerSwitch(fan)
    fan_power_switch.press()
    fan_power_switch.press()

    air_condition = AirCondition()
    ac_power_switch = ElectricPowerSwitch(air_condition)
    ac_power_switch.press()
    ac_power_switch.press()


if __name__ == '__main__':
    main()
