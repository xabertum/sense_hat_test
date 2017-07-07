from sense_hat import SenseHat

sense = SenseHat()

sense.set_rotation(180)

red = [255, 0, 0]
green = [0,255,0]
blue = [0,0,255]
<<<<<<< HEAD
color = str(raw_input('indique el color de la temperatura'))


def probando():
    temp = round(sense.get_temperature(),2)
    temp_str = 'Temp: ' + str(temp)

    sense.show_message(temp_str,0.1,color,blue)

    pressure = sense.get_pressure()
    press_str = 'Press: ' + str(pressure)

    sense.show_message(press_str,0.1,blue)

probando()
=======


temp = round(sense.get_temperature(),2)
temp_str = 'Temp: ' + str(temp)

sense.show_message(temp_str,0.1, green)

>>>>>>> 807c0aee33de4e08dc4c87e3185c65b4a74e59fe
