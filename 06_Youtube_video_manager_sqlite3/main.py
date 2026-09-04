# "SELECT * FROM videos"
# "INSERT INTO videos (title, duration) VALUES (?, ?)", (title, duration)
# "UPDATE videos SET title = ?, duration = ?  WHERE id = ?", (title, duration, video_id)
# "DELETE FROM videos WHERE id = ?", (video_id,)

import sqlite3
con = sqlite3.connect("youtube.db")
cursor = con.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        duration TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    con.commit()

def add_video(title, duration):
    cursor.execute("INSERT INTO videos (title, duration) VALUES (?, ?)", (title, duration))
    con.commit()

def update_video(video_id, title, duration):
    cursor.execute("UPDATE videos SET title = ?, duration = ?  WHERE id = ?", (title, duration, video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()

def main():
    print('-'*80)
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
                add_video(title, duration)
            case '3':
                video_id = input("Enter the video id to edit: ")
                title = input("Enter video title: ")
                duration = input("Duration of this video? ")
                update_video(video_id, title, duration)
            case '4':
                video_id = input("Enter the video id you want to delete: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid choice")

        print('-'*80)
    con.close()

if __name__ == "__main__":
    main()