import wmi


class Brightness():

    c = wmi.WMI(namespace='wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]

    def get_brightness(self):
        return self.c.WmiMonitorBrightness()[0]

    def set_brightness(self, desired_brightness):
        self.methods.WmiSetBrightness(desired_brightness, 0)