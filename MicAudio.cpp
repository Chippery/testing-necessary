#include <iostream>
#include <cmath>
#include <portaudio.h>

constexpr int SAMPLE_RATE = 44100;
constexpr int FRAMES_PER_BUFFER = 256;

// Called repeatedly when microphone data is available
int audioCallback(
    const void* input,
    void* output,
    unsigned long frameCount,
    const PaStreamCallbackTimeInfo* timeInfo,
    PaStreamCallbackFlags statusFlags,
    void* userData)
{
    // We're only using input, so interpret it as floats
    const float* samples = static_cast<const float*>(input);

    if (samples == nullptr)
        return paContinue;

    // Calculate average volume (RMS)
    float sum = 0.0f;

    for (unsigned long i = 0; i < frameCount; i++)
    {
        sum += samples[i] * samples[i];
    }

    float rms = std::sqrt(sum / frameCount);

    if(rms > 0.65)
    {
        std::cout << "Clap! ";
    }

    std::cout << "Volume: " << rms << '\n';


    return paContinue;
}

int main()
{
    PaError err;

    // Initialize PortAudio
    err = Pa_Initialize();

    if (err != paNoError)
    {
        std::cerr << "PortAudio initialization failed: "
                  << Pa_GetErrorText(err) << '\n';
        return 1;
    }

    PaStream* stream;

    // Open microphone
    err = Pa_OpenDefaultStream(
        &stream,

        1,                  // 1 input channel (microphone)
        0,                  // 0 output channels
        paFloat32,          // microphone samples are floats
        SAMPLE_RATE,        // 44.1 kHz
        FRAMES_PER_BUFFER,  // buffer size
        audioCallback,      // callback function
        nullptr             // user data
    );

    if (err != paNoError)
    {
        std::cerr << "Could not open microphone: "
                  << Pa_GetErrorText(err) << '\n';

        Pa_Terminate();
        return 1;
    }

    // Start recording
    err = Pa_StartStream(stream);

    if (err != paNoError)
    {
        std::cerr << "Could not start microphone: "
                  << Pa_GetErrorText(err) << '\n';

        Pa_CloseStream(stream);
        Pa_Terminate();
        return 1;
    }

    std::cout << "Listening...\n";
    std::cout << "Press ENTER to stop.\n";

    std::cin.get();

    // Stop recording
    Pa_StopStream(stream);

    // Clean up
    Pa_CloseStream(stream);
    Pa_Terminate();

    return 0;
}