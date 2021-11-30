# tts_for_teaching
Synthesized voice for your video presentation

First get a Azure Key and Region, follow [this link](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/overview) for more details.
Add the keys in the `azure_tts\key.cfg`.

Runs the following command: 


`python azure_tts\azure_tts_create_audio.py --input_dir sample_text --out_dir output`


`input_dir` the directory contain all SSML files
`out_dir` a wave will be created per each SSML file and stored in this directory