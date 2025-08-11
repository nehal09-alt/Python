import sqlite3
con = sqlite3.connect("youtube.db")


cur = con.cursor()
cur.excute(''' 
        CREATE TABLE IF NOT EXISTS videos(
           id Integer PRIMARY KEY , 
           name Text NOT NULL ,
           time Text NOT NULL
           )  

''')
def list_all_videos(videos):
     pass 
def add_your_video(videos):
     pass 
def update_video(videos):
     pass 
def delete_video(vicdeos):
     pass 

def main():
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

if __name__  == '__main__':
    main()