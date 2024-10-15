from googletrans import Translator

def translate_text(text, src_lang, dest_lang):
    # Initialize the Translator object
    translator = Translator()
    
    # Perform the translation
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    
    # Return the translated text
    return translation.text

if __name__ == "__main__":
    # Input text to translate
    text_to_translate = input("Enter text to translate: ")
    
    # Source language (e.g., 'en' for English)
    source_language = input("Enter source language code (e.g., 'en' for English): ")
    
    # Destination language (e.g., 'fr' for French)
    destination_language = input("Enter destination language code (e.g., 'fr' for French): ")
    
    # Perform translation
    translated_text = translate_text(text_to_translate, source_language, destination_language)
    
    # Display the translated text
    print(f"Translated Text: {translated_text}")
