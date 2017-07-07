from sense_hat import SenseHat

sense = SenseHat()
temp = sense.get_temperature()
temp_humidity = sense.get_temperature_from_humidity()


print ("Temperature from Temperature sensor: \n")
print (str(sense.temp) + " C") 

print ("Temperature from humidity sensor \n")
print (str(temp_humidity) + " C") 

