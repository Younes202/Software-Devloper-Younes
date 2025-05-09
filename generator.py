import qrcode

url = "https://younes202.github.io/Software-Devloper-Younes/"
qr = qrcode.make(url)
qr.save("images/younesq-r.png")
