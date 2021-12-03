import azure.cognitiveservices.speech as speechsdk
from os import listdir, path, mkdir
import argparse
import configparser as CP
import xml.dom.minidom


def print_warning(txt):
    print(f"  WARNING:{txt}")


def create_wav(text_file, output):
    # Creates an audio configuration that points to an audio file.
    # Replace with your own audio filename.
    audio_filename = output
    audio_output = speechsdk.audio.AudioOutputConfig(filename=audio_filename)

    # Creates a synthesizer with the given settings
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output)

    # Synthesizes the text to speech.
    # Replace with your own text.
    print(f'Start with {text_file}')
    # read the text
    file = open(text_file, mode='r',encoding='utf8')
    # read all lines at once
    tts = file.read()
    # close the file
    file.close()
    try:
        xml.dom.minidom.parseString(tts)
    except:
        print_warning(f"XML in file {text_file} is not valid. Continue with next file.")
        return

    # speak_ssml_async
    result = speech_synthesizer.speak_ssml_async(tts).get()

    # Checks result.
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized to [{}]]".format(audio_filename))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
        print("Did you update the subscription info?")


if __name__ == '__main__':
    print("Welcome, create wave files fromm SSML using Azure")
    parser = argparse.ArgumentParser(description='Create wave files fromm SSML using Azure')
    parser.add_argument("--input_dir", help="Directory contains all SSML files", required=True)
    parser.add_argument("--out_dir", help="Directory that will contain all wave files", required=True)
    args = parser.parse_args()

    cfg = CP.ConfigParser()
    cfg._interpolation = CP.ExtendedInterpolation()
    cfg.read(path.join(path.dirname(__file__), 'key.cfg'))

    cfg = cfg['speech_service_key']
    speech_key = cfg['speech_key']
    service_region = cfg['service_region']
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # set the config

    speech_config.speech_synthesis_language = 'en-US'
    speech_config.speech_synthesis_voice_name = 'en-US-JennyNeural'

    directory_with_text_files = args.input_dir
    output_dir = args.out_dir

    text_files = [f for f in listdir(directory_with_text_files) if path.isfile(path.join(directory_with_text_files, f))]
    if not path.exists(output_dir):
        mkdir(output_dir)

    for text_file in text_files:
        output = path.join(output_dir, path.splitext(text_file)[0] + '.wav')
        create_wav(path.join(directory_with_text_files, text_file), output)


