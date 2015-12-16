#!/usr/bin/python

import midi

# dir(guitar1[0])

NOTE_NAMES = ['C','Cs','D','Ds','E','F','Fs','G','Gs','A','As','B']
NOTES_PER_OCTAVE = len( NOTE_NAMES )

pattern = midi.read_midifile("since_ive_been_loving_you.mid")


guitar1 = list(pattern)[17]

for event in guitar1:
  if len(event.data) == 0:
    continue

  tick = event.tick
  pitch = event.data[0]
  velocity = 0

  if len(event.data) == 2:
    velocity = event.data[1]

  if event.name == 'Note On':
    note = pitch % NOTES_PER_OCTAVE
    note_name = NOTE_NAMES[note]
    print str(tick) + ": ON: " + note_name + " (" + str(pitch) + ")"

  if event.name == 'Note Off':
    note = pitch % NOTES_PER_OCTAVE
    note_name = NOTE_NAMES[note]
    print str(tick) + ": OFF: " + note_name + " (" + str(pitch) + ")"

