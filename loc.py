"""
This module automates the creation of localizations (i18n).
"""

import argparse
from googletrans import Translator

def main():
    """
    Main function to handle argument parsing and translation.
    """
    # Set up argument parser
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
    args = parser.parse_args()

    # Define the languages and their codes
    languages = {
        'cs_CZ': 'cs',  # Czech
        'sk_SK': 'sk',  # Slovak
        'en_US': 'en',  # English
        'uk_UA': 'uk'  # Ukrainian
    }

    # Validate input language
    if args.input_language not in languages.values():
        raise ValueError(
            f"Unsupported input language: {args.input_language}. "
            f"Supported languages are: {', '.join(languages.values())}"
        )

    # Initialize translator
    translator = Translator()

    # Perform translations
    translations = {}
    for lang_code, lang in languages.items():
        if lang == args.input_language:
            translations[lang_code] = args.localization
        else:
            translated = translator.translate(
                args.localization, src=args.input_language, dest=lang
            )
            translations[lang_code] = translated.text.replace("'", "''")

    # Convert Ukrainian translation to Latin alphabet
    if 'uk_UA' in translations:
        translations['uk_UA'] = translator.translate(
            args.localization, src=args.input_language, dest='uk'
        ).pronunciation.replace("'", "''")

    # Print the results
    print(
        f"WAPL_LOCALIZATION_PKG.LOC_KEY('{args.key}', '{args.application}');"
    )
    for lang_code, translation in translations.items():
        print(
            f"WAPL_LOCALIZATION_PKG.LOC_VAL('{args.key}', '{args.application}', "
            f"'{lang_code}', '{translation}');"
        )

if __name__ == '__main__':
    main()
