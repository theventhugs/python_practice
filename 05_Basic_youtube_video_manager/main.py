import json
FILE_NAME = "youtube.txt"

def load_data_helper():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_data_helper(data):
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file)

def list_videos():
    data = load_data_helper()
    for index, video in enumerate(data, start=1):
        print(f'{index}. {video}')

def update_video(videos):
    index = int(input("At which index you want to update data? "))
    if index >= 1 and index <= len(videos):
        title = input("Enter video title: ")
        duration = input("Duration of this video? ")
        videos[index-1]["Title"] = title
        videos[index-1]["Duration"] = duration
        save_data_helper(videos)
    else:
        print("index out of range")

def delete_video(videos):
    index = int(input("Enter the index you want to delete: "))
    del videos[index-1]
    save_data_helper(videos)
        

def main():
    print('-'*80)
    videos = load_data_helper()
    while True:
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video details")
        print("4. Delete a video")
        print("5. Exit")
        print() #Empty line space
        choice = input("Enter you choice: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                title = input("Enter video title: ")
                duration = input("Duration of this video? ")
                videos.append({"Title": title, "Duration": duration})
                save_data_helper(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")

        print('-'*80)


if __name__ == "__main__":
    main()