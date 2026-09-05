from pymongo import MongoClient
from bson import objectid  # mongodb store video_ids in bson format not in string fromat not even in json format

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.ngdvb1p.mongodb.net/") #No need to close this connection
db = client["ytmanager"]
video_collection = db["videos"]
# It won't reflect in the dashboard untill and unless you add something to it
print(client)

# print(video_collection)

def list_video():
    print("="*50)
    for video in video_collection.find(): #returns an iterateble
        print(f"ID: {video['_id']}\ntitle: {video['title']}\nduration: {video['duration']}")
        print("="*50)

def add_video(title, duration):
    video_collection.insert_one({"title": title, "duration": duration})
    # need to pass these values as an object {}

def update_video(video_id, title, duration):
    video_collection.update_one(
        {'_id': objectid(video_id)},
        {'$set': {'title': title, 'duration': duration}}
    )

def delete_video(video_id):
    video_collection.delete_one({'_id': objectid(video_id)})

def main():
    while True:
        print("\nYoutube manager")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the App")
        choice = input("Enter you choice: ")

        match choice:
            case '1':
                list_video()
            case '2':
                title = input("Enter title of that video: ")
                duration = input("Enter duration of that videos: ")
                add_video(title, duration)
            case '3':
                video_id = input("Enter the video_id to update: ")
                title = input("Enter title of that video: ")
                duration = input("Enter duration of that videos: ")
                update_video(video_id, title, duration)
            case '4':
                video_id = input("Enter the video_id to delete: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Please enter a valid choice")

if __name__ == "__main__":
    main()