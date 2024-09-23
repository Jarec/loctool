"""
This module automates the creation of localizations (i18n).
"""

import argparse
from googletrans import Translator

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

def main():
    """
    Main function to handle argument parsing and translation.
    """
    args = parse_arguments()

    # Define the languages and their codes
    languages = {
        'cs_CZ': ('cs', 'text'),  # Czech
        'sk_SK': ('sk', 'text'),  # Slovak
        'en_US': ('en', 'text'),  # English
        'uk_UA': ('uk', 'pronunciation')   # Ukrainian
    }

    # Get the supported languages
    supported_languages = set(map(lambda x: x[0], languages.values()))

    # Validate input language
    if args.input_language not in supported_languages:
        raise ValueError(
            f"Unsupported input language: {args.input_language}. "
            f"Supported languages are: {', '.join(supported_languages)}"
        )

    # Initialize translator
    translator = Translator()

    # Perform translations
    translations = {}
    for lang_code, (lang, result_type) in languages.items():
        translated = translator.translate(
            args.localization, src=args.input_language, dest=lang
        )
        translations[lang_code] = getattr(translated, result_type).replace("'", "''")

    # Print the results
    print(f"{PKG}.LOC_KEY('{args.key}', '{args.application}');")
    for lang_code, translation in translations.items():
        print(
            f"{PKG}.LOC_VAL('{args.key}', '{args.application}', "
            f"'{lang_code}', '{translation}');"
        )

if __name__ == '__main__':
    main()
