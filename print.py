import escpos.printer

p = escpos.printer.Serial("/dev/ttyUSB0", baudrate=38400)

p.set(align='center')
p.image('./assets/grey256.png')
p.text("VMSE 2000")

p.set(align='left')
p.text('\n')
p.text('You are being fined 0.00012700 BTC')
p.text('\n')
p.cut()

