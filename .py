import datetime

MOOD_LOG_FILE = "mood_log.txt"

def get_current_timestamp():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def log_mood():
    print("\n📝 Let's log your mood!")
    mood = input("How are you feeling today? (e.g., Happy, Sad, Anxious): ").strip()
    note = input("Want to add a short note? (Optional, press Enter to skip): ").strip()

    timestamp = get_current_timestamp()
    entry = f"[{timestamp}] Mood: {mood}"
    if note:
        entry += f" | Note: {note}"

    with open(MOOD_LOG_FILE, "a", encoding="utf-8") as file:
        file.write(entry + "\n")

    print("✅ Mood logged successfully!\n")

def view_logs():
    print("\n📖 Your Past Mood Logs:\n")
    try:
        with open(MOOD_LOG_FILE, "r", encoding="utf-8") as file:
            logs = file.readlines()
            if not logs:
                print("No mood logs yet. Start tracking today!\n")
            else:
                for line in logs:
                    print(line.strip())
                print()
    except FileNotFoundError:
        print("No log file found yet. Add your first mood entry!\n")

def show_menu():
    print("===== MoodMate 🧠 =====")
    print("1. Log a Mood")
    print("2. View Mood History")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            log_mood()
        elif choice == "2":
            view_logs()
        elif choice == "3":
            print("👋 Exiting MoodMate. Take care of your mental health!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
