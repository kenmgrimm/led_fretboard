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
OPEN_NOTES = [40, 45, 50, 55, 59, 65]
NUM_LEDS = 100

NUM_STRINGS = len(OPEN_NOTES)
LEDS_IN_AN_OCTAVE = 12 * NUM_STRINGS

# brightness = strip.setBrightness

def ledIndexesByMidiNote(midiNote):
  ledIndexes = []

  for stringNumber in range(0, NUM_STRINGS):
    ledIndexes.extend(indexesOnString(stringNumber, midiNote))

  if len(ledIndexes) > 0:
    print "Midi Note {0} maps to led indexes {1} ".format(midiNote, ", ".join(ledIndexes))

  return sorted(ledIndexes)


def indexesOnString(stringNumber, midiNote):
  ledIndexes = []

  ledIndex = firstIndexOnString(stringNumber, midiNote)
  # print "{0}: {1}: {2}".format(stringNumber, midiNote, ledIndex)

  if ledIndex >= 0 and ledIndex < NUM_LEDS:
    ledIndexes.append(str(ledIndex))
  # if we wanted to find all octaves of note
  # while ledIndex >= 0 and ledIndex < NUM_LEDS:
  #   ledIndexes.append(str(ledIndex))

  #   ledIndex += LEDS_IN_AN_OCTAVE

  return ledIndexes


def firstIndexOnString(stringNumber, midiNote):
  openNote = OPEN_NOTES[stringNumber]

  firstLedOffsetFromOpen = midiNote - openNote

  return NUM_STRINGS * firstLedOffsetFromOpen + stringNumber


def lightUpScales(lowestNote):
  for octave in [0, 1, 2, 3, 4, 5]: # (octaves)
    # for scaleSemiTone in [0, 1, 3, 5, 6, 8, 10]:   # (nat_minor_scale_semi_tone)
    #   turnOn(ledIndexesByMidiNote(lowestNote + (octave * 12) + scaleSemiTone))

    # for pentatonicSemiTone in [0, 1, 3, 5, 6, 10]:    #  (pentatonic_semi_tone)
    #   turnOn(ledIndexesByMidiNote(lowestNote + (octave * 12) + pentatonicSemiTone))

    turnOn(ledIndexesByMidiNote(lowestNote + (octave * 12)))

def turnOn(indexes):
  red = Color(0, 100, 0)

  for led_index in indexes:
    strip.setPixelColor(int(led_index), red)
    strip.show()

def clearStrip
  for i in range(0, 255):
    strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()


# Main program logic follows:
if __name__ == '__main__':
  # Create NeoPixel object with appropriate configuration.
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
  # Intialize the library (must be called once before other functions).
  strip.begin()

  # red = Color(0, 100, 0)

#  for led_index in ledIndexesByMidiNote(55):
#    strip.setPixelColor(int(led_index), red)
#    strip.show()
#    time.sleep(900.0 / 1000.0)

  ledIndexesByMidiNote(40)
  ledIndexesByMidiNote(45)
  ledIndexesByMidiNote(47)
  ledIndexesByMidiNote(50)
  ledIndexesByMidiNote(55)

  print "Scales for 50"
  lightUpScales(50)

  time.sleep(5)
  clearStrip

