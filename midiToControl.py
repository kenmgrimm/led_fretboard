#!/usr/bin/python

import midi
import time

# introspect object
# dir(guitar1[0])

NOTE_NAMES = ['C','Cs','D','Ds','E','F','Fs','G','Gs','A','As','B']
NOTES_PER_OCTAVE = len( NOTE_NAMES )

pattern = midi.read_midifile("SunshineofYourLove.mid")

# print pattern

guitar1 = list(pattern)[2]

for event in guitar1:
  if len(event.data) == 0 or (event.name != 'Note On' and event.name != 'Note Off') :
    continue

  tick = event.tick
  pitch = event.data[0]
  velocity = 0

  # time.sleep(tick * 0.0005 * 10) 
  print "time.sleep(" + str(tick * 0.0005 * 10) + " * tempo)"

  if len(event.data) == 2:
    velocity = event.data[1]

  if event.name == 'Note On':
    note = pitch % NOTES_PER_OCTAVE
    note_name = NOTE_NAMES[note]
    # print str(tick) + ": ON: " + note_name + " (" + str(pitch) + ")"
    print "turnOn(ledIndexesByMidiNote(" + str(pitch) + "), Color(0, 30, 0))"

  if event.name == 'Note Off':
    note = pitch % NOTES_PER_OCTAVE
    note_name = NOTE_NAMES[note]
    # print str(tick) + ": OFF: " + note_name + " (" + str(pitch) + ")"
    print "turnOn(ledIndexesByMidiNote(" + str(pitch) + "), Color(0, 0, 0))"
    print "lightUpScales(48)"

