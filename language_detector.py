import tkinter as tk
from tkinter import ttk
from langdetect import detect

class LanguageDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Detector")
        self.root.geometry("400x200")
        
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(main_frame, text="Enter text to detect language:").grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        
        self.text_entry = ttk.Entry(main_frame, width=40)
        self.text_entry.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        detect_button = ttk.Button(main_frame, text="Detect Language", command=self.detect_language)
        detect_button.grid(row=2, column=0, sticky=tk.W, pady=(0, 10))
        
        self.result_label = ttk.Label(main_frame, text="")
        self.result_label.grid(row=3, column=0, sticky=tk.W)
        
    def detect_language(self):
        text = self.text_entry.get()
        if text.strip():
            try:
                language_code = detect(text)
                language_names = {
                    'en': 'English',
                    'es': 'Spanish',
                    'fr': 'French',
                    'de': 'German',
                    'it': 'Italian',
                    'pt': 'Portuguese',
                    'nl': 'Dutch',
                    'pl': 'Polish',
                    'ru': 'Russian',
                    'ja': 'Japanese',
                    'ko': 'Korean',
                    'zh': 'Chinese',
                    'ar': 'Arabic',
                    'hi': 'Hindi',
                    'tr': 'Turkish',
                    'sv': 'Swedish',
                    'da': 'Danish',
                    'fi': 'Finnish',
                    'el': 'Greek',
                    'he': 'Hebrew',
                    'th': 'Thai',
                    'vi': 'Vietnamese',
                    'id': 'Indonesian',
                    'fa': 'Persian',
                    'uk': 'Ukrainian',
                    'cs': 'Czech',
                    'ro': 'Romanian',
                    'hu': 'Hungarian',
                    'ca': 'Catalan',
                    'af': 'Afrikaans',
                    'ms': 'Malay',
                    'no': 'Norwegian',
                    'cy': 'Welsh',
                    'ta': 'Tamil',
                    'lv': 'Latvian',
                    'bn': 'Bengali',
                    'sr': 'Serbian',
                    'az': 'Azerbaijani',
                    'sl': 'Slovenian',
                    'kn': 'Kannada',
                    'et': 'Estonian',
                    'mk': 'Macedonian',
                    'br': 'Breton',
                    'eu': 'Basque',
                    'is': 'Icelandic',
                    'hy': 'Armenian',
                    'ne': 'Nepali',
                    'mn': 'Mongolian',
                    'bs': 'Bosnian',
                    'kk': 'Kazakh',
                    'sq': 'Albanian',
                    'sw': 'Swahili',
                    'gl': 'Galician',
                    'mr': 'Marathi',
                    'pa': 'Punjabi',
                    'si': 'Sinhala',
                    'km': 'Khmer',
                    'sn': 'Shona',
                    'yo': 'Yoruba',
                    'so': 'Somali',
                    'ha': 'Hausa',
                    'lb': 'Luxembourgish',
                    'uz': 'Uzbek',
                    'am': 'Amharic',
                    'tg': 'Tajik',
                    'tt': 'Tatar',
                    'gu': 'Gujarati',
                    'ka': 'Georgian',
                    'te': 'Telugu',
                    'xh': 'Xhosa',
                    'zu': 'Zulu',
                    'ga': 'Irish',
                    'gd': 'Scottish Gaelic',
                    'ml': 'Malayalam',
                    'my': 'Burmese',
                    'ps': 'Pashto',
                    'ku': 'Kurdish',
                    'sd': 'Sindhi',
                    'bo': 'Tibetan',
                    'tk': 'Turkmen',
                    'as': 'Assamese',
                    'ma': 'Maithili',
                    'bh': 'Bihari',
                    'dz': 'Dzongkha',
                    'ht': 'Haitian Creole',
                    'jw': 'Javanese',
                    'su': 'Sundanese',
                    'ceb': 'Cebuano',
                    'ny': 'Chichewa',
                    'co': 'Corsican',
                    'haw': 'Hawaiian',
                    'ig': 'Igbo',
                    'yi': 'Yiddish',
                    'hmn': 'Hmong',
                    'la': 'Latin',
                    'lb': 'Luxembourgish',
                    'mg': 'Malagasy',
                    'mt': 'Maltese',
                    'mi': 'Maori',
                    'mr': 'Marathi',
                    'my': 'Burmese',
                    'ne': 'Nepali',
                    'no': 'Norwegian',
                    'or': 'Odia',
                    'ps': 'Pashto',
                    'pt': 'Portuguese',
                    'pa': 'Punjabi',
                    'ro': 'Romanian',
                    'ru': 'Russian',
                    'sm': 'Samoan',
                    'gd': 'Scottish Gaelic',
                    'sr': 'Serbian',
                    'st': 'Sesotho',
                    'sn': 'Shona',
                    'sd': 'Sindhi',
                    'si': 'Sinhala',
                    'sk': 'Slovak',
                    'sl': 'Slovenian',
                    'so': 'Somali',
                    'es': 'Spanish',
                    'su': 'Sundanese',
                    'sw': 'Swahili',
                    'sv': 'Swedish',
                    'tl': 'Tagalog',
                    'tg': 'Tajik',
                    'ta': 'Tamil',
                    'tt': 'Tatar',
                    'te': 'Telugu',
                    'th': 'Thai',
                    'tr': 'Turkish',
                    'tk': 'Turkmen',
                    'uk': 'Ukrainian',
                    'ur': 'Urdu',
                    'ug': 'Uyghur',
                    'uz': 'Uzbek',
                    'vi': 'Vietnamese',
                    'cy': 'Welsh',
                    'xh': 'Xhosa',
                    'yi': 'Yiddish',
                    'yo': 'Yoruba',
                    'zu': 'Zulu'
                }
                language_name = language_names.get(language_code, f"Language (code: {language_code})")
                self.result_label.config(text=f"Detected Language: {language_name}")
            except Exception as e:
                self.result_label.config(text="Error: Could not detect language")
        else:
            self.result_label.config(text="Please enter some text")

def main():
    root = tk.Tk()
    app = LanguageDetectorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 