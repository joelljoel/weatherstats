from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import RPi.GPIO as GPIO
import requests
import pprint
import time

response=requests.get("insert your api key here")
print("status code:",response.status_code)
print()
weather=response.json()['main']
wind=response.json()['wind']

temp=weather.get("temp")
humidity=weather.get("humidity")
airpres=weather.get("pressure")
windspeed=wind.get("speed")
winddeg=wind.get("deg")
print("temp:",temp)
print("humidity:",humidity)
print("air pressure:",airpres)
print("wind speed:",windspeed)
print("wind deg:",winddeg)

# initialize GPIO
GPIO.setwarnings(False)

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.

disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)


# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.

width = disp.width
height = disp.height
image = Image.new("1", (width, height))


# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)


# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

padding = -2
top = padding
bottom = height - padding

x = 0

font = ImageFont.load_default()

while True:

    # Draw a black filled box to clear the image
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((x, top + 0), "Temp:"+ str(temp) , font=font, fill=255)
    draw.text((x, top + 10), "Humidity:"+ str(humidity) , font=font, fill=255)
    draw.text((x, top + 20), "Air pressure: " +str(airpres), font=font, fill=255)
    draw.text((x, top + 30), "Wind speed:"+ str(windspeed) , font=font, fill=255)
    draw.text((x, top + 40), "Wind degree: " +str(winddeg), font=font, fill=255)


    # Display image.
    disp.image(image)
    disp.show()
    time.sleep(2)
