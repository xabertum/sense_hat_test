from sense_hat import SenseHat

sense = SenseHat()

sense.set_rotation(180)

red = [255, 0, 0]
green = [0,255,0]
blue = [0,0,255]


temp = round(sense.get_temperature(),2)
temp_str = str(temp)

sense.show_message(temp_str,0.6, green)

