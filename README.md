# Localization Automation Tool

This tool automates the creation of localizations (i18n) using the `googletrans` library.

## Requirements

- Python 3.x
- `googletrans` library

## Installation and usage

### Using Docker

1. Build the Docker image:
    ```sh
    docker build -t loctool .
    ```

2. Run the Docker container:
    ```sh
    docker run --rm loctool <key> <localization> [--application <application>] [--input-language <input-language>]
    ```

   - `<key>`: The localization key.
   - `<localization>`: The actual localization text.
   - `--application`: (Optional) The application name to replace "BTN" in the output. Default is "BTN".
   - `--input-language`: (Optional) The input language code. Default is "cs" (Czech).

### Using Virtual Environment (alternative)

1. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

2. Activate the virtual environment:

    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
   
4. Run the tool:
    
    ```sh
    python loc.py <key> <localization> [--application <application>] [--input-language <input-language>]
    ```

   - `<key>`: The localization key.
   - `<localization>`: The actual localization text.
   - `--application`: (Optional) The application name to replace "BTN" in the output. Default is "BTN".
   - `--input-language`: (Optional) The input language code. Default is "cs" (Czech).

## Useful tips and Examples

- create shell alias in `.bashrc` or `.zshrc`:
    ```sh
    alias loc="python loc.py"
    ```
- create shell alias for docker in `.bashrc` or `.zshrc` (you need to build the docker image first as per instructions above):
    ```sh
    alias loc="docker run --rm loctool"
    ```
- create translation and copy to clipboard (MacOS):
    ```sh
    loc "pct.userinfo.mode" "Jméno uživatele" | pbcopy
    ```

- create translation for different application and copy to clipboard (MacOS):
    ```sh
    loc "ppt.userinfo.mode" "Jméno uživatele" --application PPT | pbcopy
    ```
  
- use different input language (e.g. english):
    ```sh
    loc "pct.userinfo.mode" "Username" --input-language en
    ```