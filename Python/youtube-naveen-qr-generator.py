import pyqrcode
from pyqrcode import QRCode

s = "https://www.youtube.com/channel/UCthzwwUwLx7h44kTo72W-PA"
url = pyqrcode.create(s)
url.svg("naveen.svg", scale=10)
