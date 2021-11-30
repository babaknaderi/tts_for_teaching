import azure.cognitiveservices.speech as speechsdk
from os import listdir, path, mkdir


# Replace with your own subscription key and region identifier from here: https://aka.ms/speech/sdkregion
speech_key, service_region = "YourSubscriptionKey", "YourServiceRegion"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
# set the config
speech_config.speech_synthesis_language = 'en-US'
speech_config.speech_synthesis_voice_name = 'en-US-JennyNeural'

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
    file = open(text_file, mode='r')
    # read all lines at once
    tts = file.read()
    # close the file
    file.close()

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

    directory_with_text_files = '../sample_text'
    output_dir = '../output'

    text_files = [f for f in listdir(directory_with_text_files) if path.isfile(path.join(directory_with_text_files, f))]
    if not path.exists(output_dir):
        mkdir(output_dir)

    for text_file in text_files:
        output = path.join(output_dir, path.splitext(text_file)[0] + '.wav')
        create_wav(path.join(directory_with_text_files, text_file), output)


