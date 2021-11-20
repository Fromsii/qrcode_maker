import qrcode


link = input('Type your link:')
img = qrcode.make(link)
type(img)
Savename = input('Name to save:')
img.save(Savename + '.png')
