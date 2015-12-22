import time

from neopixel import *


# LED strip configuration:
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

#  E A D G B E
openNotes = [40, 45, 50, 55, 59, 65]

def ledIndexesByMidiNote(midiNote):
  lightNumbers = []

  stringIndex = -1
  for openNote in openNotes:
    stringIndex += 1
    if midiNote < openNote: continue;

    diff = midiNote - openNote
    lightNumber = 6 * diff + stringIndex

    if lightNumber > 99: continue;

    lightNumbers.append(str(lightNumber))

  print "Midi Note {0} maps to led indexes {1} ".format(midiNote, ", ".join(lightNumbers))
  return lightNumbers;


def lightUpScales(lowestNote):
  for octave in [0, 1, 2, 3, 4, 5]: # (octaves)
    for scaleSemiTone in [0, 1, 3, 5, 6, 8, 10]:   # (nat_minor_scale_semi_tone)
      turnOn(ledIndexesByMidiNote(lowestNote + (octave * 12) + scaleSemiTone))

    for pentatonicSemiTone in [0, 1, 3, 5, 6, 10]:    #  (pentatonic_semi_tone)
      turnOn(ledIndexesByMidiNote(lowestNote + (octave * 12) + pentatonicSemiTone))

    turnOn(ledIndexesByMidiNote(lowestNote + (octave * 12)))

def turnOn(indexes):
  red = Color(0, 100, 0)

  for led_index in indexes:
    strip.setPixelColor(int(led_index), red)
    strip.show()


# Main program logic follows:
if __name__ == '__main__':
  # Create NeoPixel object with appropriate configuration.
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
  # Intialize the library (must be called once before other functions).
  strip.begin()

  red = Color(0, 100, 0)
  
#  for led_index in ledIndexesByMidiNote(55):
#    strip.setPixelColor(int(led_index), red)
#    strip.show()
#    time.sleep(900.0 / 1000.0)

  ledIndexesByMidiNote(45)
  ledIndexesByMidiNote(47)
  ledIndexesByMidiNote(50)
  ledIndexesByMidiNote(55)

  lightUpScales(50)

  time.sleep(5)

  for i in range(0, 255):
    strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()


