from speech_to_text import get_voice_command
from text_extractor import extract_text
from text_to_speech import speak_text

def main():
    command = get_voice_command()
    if command and ("read" in command or "start" in command):
        

        file_path = input("Enter the path to your file (PDF, DOCX, or TXT):")
        # file_path = file_path.strip().replace("\\\\", "\\")
        print(f"Trying to open file: '{file_path}' ")
        
        try:
            text = extract_text(file_path)
            speak_text(text)
        except Exception as e:
            print(f"Error reading file: {e}")
    else:
        print("No 'read' command detected. Try again.")


if __name__ == "__main__":
    main()
