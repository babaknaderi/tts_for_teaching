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

TODO: Some notes about SSML files, samples and refrence for further details.



## How to merge wave and videos
TODOD
