import json
import os

NOTES_FILE = 'notes.json'

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE) as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=4)

def add_note():
    note = input("Enter your note: ")
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Note added!")

def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
    else:
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note}")

def search_notes():
    keyword = input("Enter search keyword: ")
    notes = load_notes()
    found = [note for note in notes if keyword.lower() in note.lower()]
    if found:
        for note in found:
            print(note)
    else:
        print("No matching notes found.")

def delete_note():
    list_notes()
    try:
        note_num = int(input("Enter note number to delete: "))
        notes = load_notes()
        if 0 < note_num <= len(notes):
            removed = notes.pop(note_num - 1)
            save_notes(notes)
            print(f"Deleted note: {removed}")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Invalid input.")

def main():
    while True:
        print("\n--- CLI Notes Manager ---")
        print("1. Add Note")
        print("2. List Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_note()
        elif choice == '2':
            list_notes()
        elif choice == '3':
            search_notes()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
