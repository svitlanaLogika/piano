import os
import numpy as np
from pygame import mixer
import wave


def generate_tone(frequency, duration=1.0, sample_rate=44100, amplitude=0.3):
    """Генерує простий синусоїдальний тон"""
    frames = int(duration * sample_rate)
    arr = np.sin(2 * np.pi * frequency * np.linspace(0, duration, frames))
    arr = (arr * amplitude * 32767).astype(np.int16)
    return arr


def save_wave_file(filename, audio_data, sample_rate=44100):
    """Зберігає аудіо дані у WAV файл"""
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)  # моно
        wav_file.setsampwidth(2)  # 16-біт
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio_data.tobytes())


def generate_random_bank(output_dir, num_sounds=7):
    """
    Генерує банк випадкових звуків

    Args:
        output_dir (str): директорія для збереження файлів
        num_sounds (int): кількість звуків для генерації

    Returns:
        list: список шляхів до згенерованих файлів
    """
    # Створюємо директорію якщо її немає
    os.makedirs(output_dir, exist_ok=True)

    # Базові частоти для різних звуків
    base_frequencies = [
        261.63,  # C4
        293.66,  # D4
        329.63,  # E4
        349.23,  # F4
        392.00,  # G4
        440.00,  # A4
        493.88,  # B4
    ]

    generated_files = []

    for i in range(num_sounds):
        # Вибираємо базову частоту та додаємо невелику варіацію
        base_freq = base_frequencies[i % len(base_frequencies)]
        # Додаємо випадкову варіацію ±50 Hz
        frequency = base_freq + np.random.uniform(-50, 50)

        # Випадкова тривалість між 0.5 та 2 секундами
        duration = np.random.uniform(0.5, 2.0)

        # Випадкова амплітуда
        amplitude = np.random.uniform(0.1, 0.4)

        # Генеруємо звук
        audio_data = generate_tone(frequency, duration, amplitude=amplitude)

        # Зберігаємо файл
        filename = f"random_sound_{i + 1}.wav"
        filepath = os.path.join(output_dir, filename)
        save_wave_file(filepath, audio_data)
        generated_files.append(filepath)

    return generated_files