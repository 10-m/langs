import random
import datetime

r = random.randint(1, 6)
print(r)

print(datetime.date.today())
import qrcode

img = qrcode.make("http://kujiranand.com")
img.save('qrcode-test.png')
