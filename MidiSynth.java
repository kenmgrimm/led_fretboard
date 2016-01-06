import java.io.*;

import javax.sound.midi.MidiSystem;
import javax.sound.midi.Synthesizer;
import javax.sound.midi.MidiChannel;

class MidiSynth {

  public static void main(String[] args) {
    InputStreamReader isReader = new InputStreamReader(System.in);
    BufferedReader bufReader = new BufferedReader(isReader);



    int channel = 0; // 0 is a piano, 9 is percussion, other channels are for other instruments

    int volume = 80; // between 0 et 127
    int duration = 200; // in milliseconds

    try {
      Synthesizer synth = MidiSystem.getSynthesizer();
      synth.open();
      MidiChannel[] channels = synth.getChannels();


        while (true) {
          try {
            String inputStr = null;
            if ((inputStr = bufReader.readLine()) != null) {
               channels[channel].noteOn(Integer.parseInt(inputStr), volume);

               Thread.sleep(duration);
              
               channels[channel].noteOff(Integer.parseInt(inputStr));
            } else {
               System.out.println("inputStr is null");
            }
          } catch (Exception e) {
            System.out.println(e);
          }
        }


      // synth.close();
    } catch (Exception e) {
      e.printStackTrace();

    }


  }
}