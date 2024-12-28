import json;

def load_Data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return [];
    


def save_Data_Helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
        
        

def list_All_Videos(videos):
    print("\n")
    print("*"*70)
    for index,video in enumerate(videos,start=1):
        print(f"{index}.{video['Name']},Duration:{video['Time']}")
    print("\n")
    print("*"*70)    
    


def add_videos(videos):
    name=input("Enter the video name : ")
    time=input("Enter the video time : ")
    videos.append({'Name' : name, 'Time' : time})
    save_Data_Helper(videos);


def update_videos(videos):
    list_All_Videos(videos)
    index=int(input("Enter the video number to update : "))
    if 1 <= index <= len(videos):
        name=input("Enter the new video name : ")
        time=input("Enter the new video time : ")
        videos[index-1]={'Name':name,'Time':time}
        save_Data_Helper(videos);
        print("Video updated successfully");
    else:
        print("Invalid index selected")

def delete_videos(videos):
    list_All_Videos(videos)
    index=int(input("Enter the video number to be deleted : "))
    
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_Data_Helper(videos);
        print("Video deleted successfully")
    else:
        print("Invalid index selected")

def main():
    videos=load_Data();
    while True:
        print("\n Youtube Manager")
        print("1. List all youtube vidoes")
        print("2. Add a youtube videos")
        print("3. Update a youtube videos")
        print("4. Delete a youtube videos")
        print("5. Exit the app")
        
        choice=input("Enter your choice : ");
        # print(videos)
        
        match choice:
            case '1':
                list_All_Videos(videos)
                
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
                
            case '4':
                delete_videos(videos)
            
            case '5':
                break; 
            
            case _:
                print("Invalid choice");

if __name__=="__main__":
    main()