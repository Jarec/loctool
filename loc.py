"""
This module automates the creation of localizations (i18n).
"""

import argparse
from deep_translator import GoogleTranslator
import transliterate

def cyrillic_to_latin(text):
    return transliterate.translit(text, 'uk', reversed=True)

PKG = "WAPL_LOCALIZATION_PKG"

def parse_arguments():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description='Automate creating localizations (i18n).'
    )
    parser.add_argument('key', type=str, help='The localization key')
    parser.add_argument(
        'localization', type=str, help='The actual localization in Czech language'
    )
    parser.add_argument(
        '--application', type=str, default='BTN',
        help='The application name to replace "BTN" in the output'
    )
    parser.add_argument(
        '--input-language', type=str, default='cs',
        help='The input language code (default is "cs" for Czech)'
    )
    return parser.parse_args()

def escape_translation(translation):
    """
    Escape single quotes in the translation.
    """
    return translation.replace("'", "''").replace('`',"''").replace('ʹ', "''")

def main():
    """
    Main function to handle argument parsing and translation.
    """
    args = parse_arguments()

    # Define the languages and their codes
    languages = {
        'cs_CZ': ('cs', lambda x: x),  # Czech
        'sk_SK': ('sk', lambda x: x),  # Slovak
        'en_US': ('en', lambda x: x),  # English
        'uk_UA': ('uk', cyrillic_to_latin)   # Ukrainian
    }

    # Get the supported languages
    supported_languages = set(map(lambda x: x[0], languages.values()))

    # Validate input language
    if args.input_language not in supported_languages:
        raise ValueError(
            f"Unsupported input language: {args.input_language}. "
            f"Supported languages are: {', '.join(supported_languages)}"
        )

    # Perform translations
    translations = {}
    for lang_code, (lang, fnc) in languages.items():
        translated = GoogleTranslator(source=args.input_language, target=lang).translate(args.localization)
        translations[lang_code] = escape_translation(fnc(translated))

    # Print the results
    print(f"{PKG}.LOC_KEY('{args.key}', '{args.application}');")
    for lang_code, translation in translations.items():
        print(
            f"{PKG}.LOC_VAL('{args.key}', '{args.application}', "
            f"'{lang_code}', '{translation}');"
        )

if __name__ == '__main__':
    main()