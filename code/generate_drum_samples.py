#!/usr/bin/env python3
import numpy as np
import wave
import struct

def create_wav_file(filename, duration, sample_rate=44100):
    """Helper to create WAV file"""
    num_samples = int(duration * sample_rate)
    return filename, num_samples, sample_rate

def write_wav(filename, audio_data, sample_rate=44100):
    """Write audio data to WAV file"""
    audio_data = np.clip(audio_data, -1.0, 1.0)
    audio_data = (audio_data * 32767).astype(np.int16)
    
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio_data.tobytes())

def generate_kick():
    """Generate kick drum sound"""
    sample_rate = 44100
    duration = 0.5
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Frequency sweep from 150Hz to 40Hz
    freq_start = 150
    freq_end = 40
    freq = np.linspace(freq_start, freq_end, len(t))
    
    # Generate sine wave with frequency sweep
    phase = 2 * np.pi * np.cumsum(freq) / sample_rate
    kick = np.sin(phase)
    
    # Apply exponential decay envelope
    envelope = np.exp(-8 * t)
    kick = kick * envelope
    
    # Add some punch with a click at the start
    click = np.exp(-100 * t) * np.random.randn(len(t)) * 0.3
    kick = kick + click
    
    return kick

def generate_snare():
    """Generate snare drum sound"""
    sample_rate = 44100
    duration = 0.3
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Tone component (200Hz)
    tone = np.sin(2 * np.pi * 200 * t)
    
    # Noise component
    noise = np.random.randn(len(t))
    
    # Mix tone and noise
    snare = 0.3 * tone + 0.7 * noise
    
    # Apply envelope
    envelope = np.exp(-10 * t)
    snare = snare * envelope
    
    return snare

def generate_hihat():
    """Generate hi-hat sound"""
    sample_rate = 44100
    duration = 0.1
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # High-frequency noise
    hihat = np.random.randn(len(t))
    
    # High-pass filter effect (simple)
    hihat = np.diff(hihat, prepend=0)
    
    # Apply sharp decay
    envelope = np.exp(-50 * t)
    hihat = hihat * envelope
    
    return hihat

def generate_clap():
    """Generate clap sound"""
    sample_rate = 44100
    duration = 0.2
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Multiple short bursts of noise for clap effect
    clap = np.zeros(len(t))
    
    # First clap
    clap1 = np.random.randn(len(t)) * (t < 0.01)
    # Second clap (slightly delayed)
    clap2 = np.random.randn(len(t)) * ((t > 0.02) & (t < 0.03))
    # Third clap (more delayed)
    clap3 = np.random.randn(len(t)) * ((t > 0.04) & (t < 0.05))
    
    clap = clap1 + clap2 * 0.8 + clap3 * 0.6
    
    # Apply envelope
    envelope = np.exp(-15 * t)
    clap = clap * envelope
    
    return clap

def generate_tom():
    """Generate tom drum sound"""
    sample_rate = 44100
    duration = 0.4
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Frequency sweep from 220Hz to 80Hz
    freq_start = 220
    freq_end = 80
    freq = np.linspace(freq_start, freq_end, len(t))
    
    # Generate sine wave
    phase = 2 * np.pi * np.cumsum(freq) / sample_rate
    tom = np.sin(phase)
    
    # Add overtone
    tom += 0.3 * np.sin(2 * phase)
    
    # Apply envelope
    envelope = np.exp(-7 * t)
    tom = tom * envelope
    
    return tom

def main():
    output_dir = '/workspace/drum-machine/public/samples'
    
    print("Generating drum samples...")
    
    # Generate and save each sample
    samples = {
        'kick.wav': generate_kick(),
        'snare.wav': generate_snare(),
        'hihat.wav': generate_hihat(),
        'clap.wav': generate_clap(),
        'tom.wav': generate_tom()
    }
    
    for filename, audio_data in samples.items():
        filepath = f"{output_dir}/{filename}"
        write_wav(filepath, audio_data)
        print(f"Generated {filename}")
    
    print("All samples generated successfully!")

if __name__ == "__main__":
    main()
