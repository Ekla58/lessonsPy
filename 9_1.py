from time import sleep


class Light:
    __color = "Черный"

    def running(self):
        while True:
            print("Red")
            sleep(7)
            print("Yellow")
            sleep(2)
            print("Green")
            sleep(7)
            print("Yellow")
            sleep(2)


light = Light()
light.running()
