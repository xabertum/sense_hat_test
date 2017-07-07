from sense_hat import SenseHat

sense = SenseHat()
humidity = sense.get_humidity()

print("Humidity from SenseHat by RaspberryPi2 \n")

print (str(sense.humidity)) + " % humidity "

