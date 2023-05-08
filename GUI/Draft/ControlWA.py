from pywinauto.application import Application

app = Application(backend='uia').start('Arduino/arduino.exe').connect(title='sketch_jul21a | Arduino 1.8.19', timeout=100)
app.Sketch_jul21aArduino.print_control_identifiers()