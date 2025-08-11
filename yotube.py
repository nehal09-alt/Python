import json

def load_data():
    try:
        with open('youtube.json', 'r') as file:  # Changed to .json
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):  # Handle JSON errors
        return []

def helper_method(videos):
    with open('youtube.json', 'w') as file:
        json.dump(videos, file, indent=4)  # Add indent for readable JSON

def list_all_videos(videos):
    if not videos:
        print("\nNo videos found, bruh! Add some first.\n")
        return
    print("\n" + "*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} | Duration: {video['time']}")
    print("*" * 70 + "\n")

def add_your_video(videos):
    name = input("Enter Video Name: ").strip()
    time = input("Enter Video Time (e.g., 5:30): ").strip()
    # Basic validation for time
    if not name or not time:
        print("Yo, name and time can't be empty!")
        return
    videos.append({'name': name, 'time': time})
    helper_method(videos)
    print(f"Video '{name}' added, my dude!")

def update_video(videos):
    if not videos:
        print("\nNo videos to update, homie!\n")
        return
    list_all_videos(videos)
    try:
        index = int(input("Enter the number of video to update: "))
        if 1 <= index <= len(videos):
            name = input("Enter the new video name: ").strip()
            time = input("Enter the new video time (e.g., 5:30): ").strip()
            if not name or not time:
                print("Name and time can't be empty, yo!")
                return
            videos[index-1] = {'name': name, 'time': time}  # Fixed key 'time'
            helper_method(videos)
            print(f"Video {index} updated, lookin' fresh!")
        else:
            print("Invalid index, man. Pick a number in range!")
    except ValueError:
        print("Yo, enter a proper number, not some random stuff!")

def delete_video(videos):
    if not videos:
        print("\nNo videos to delete, bruh!\n")
        return
    list_all_videos(videos)
    try:
        index = int(input("Enter the number of video to delete: "))
        if 1 <= index <= len(videos):
            deleted_video = videos.pop(index-1)  # Use pop for cleaner delete
            helper_method(videos)
            print(f"Video '{deleted_video['name']}' deleted, gone for good!")
        else:
            print("Invalid index, dude. Try again!")
    except ValueError:
        print("C'mon, give me a real number!")

def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager | Choose an option, fam:")
        print("1. List Your Favorite Videos")
        print("2. Add a Video")
        print("3. Update a Video")
        print("4. Delete a Video")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_your_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Peace out, homie!")
                break
            case _:
                print("Invalid choice, yo. Pick 1-5!")

if __name__ == "__main__":
    main()