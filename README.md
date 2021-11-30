# tts_for_teaching
Synthesized voice for your video presentation

## Get started

First get a Azure Key and Region, follow [this link](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/overview) for more details.
Add the keys in the `azure_tts\key.cfg`.

Go to the main diretory of the project and run 

   ```bash
    cd tts_for_teaching
    pip install -r requirements.txt
   ```
    
## Runs the first test
Runs the following command: 

   ```bash
    cd tts_for_teaching
    python azure_tts\azure_tts_create_audio.py --input_dir sample_text --out_dir output
   ```

`input_dir` the directory contain all SSML files

`out_dir` a wave will be created per each SSML file and stored in this directory


## Create your SSML files
For each slide create one SSML file and store it in a directory 'group_[GROUP_number]'

You can specifiy the voice and style of it in the SSML file. We will use "en-US-JennyNeural" voice with "newscast" style
and pitch of 0.86. You can listen to that [here](https://azure.microsoft.com/en-us/services/cognitive-services/text-to-speech/#features) after setting the properties in the right-hand side.
To make sure your text follow the same structure, then the SSML file should have the following header/footer:


   ```xml
    <speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US">
        <voice name="en-US-JennyNeural">
            <mstts:express-as style="newscast" >
                <prosody rate="0%" pitch="-7%">

You can replace this text with any text you wish. You can either write in this text box or paste your own text here.

Try different languages and voices. Change the speed and the pitch of the voice. You can even tweak the SSML (Speech Synthesis Markup Language) to control how the different sections of the text sound. Click on SSML above to give it a try!

Enjoy using Text to Speech!

                </prosody>
             </mstts:express-as>
        </voice>
     </speak>
   ```
 
 
 
TODO: Some notes about SSML files, samples and refrence for further details.



## How to merge wave and videos
TODOD
