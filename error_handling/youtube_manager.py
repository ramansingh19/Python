
def list_all_videos(videos):
  pass

def add_videos(videos):
  pass

def update_videos(videos):
  pass

def delete_videos(videos):
  pass

videos = []

def main():
  while True:
    print(" Choose any option ")
    print("1. list all youtube videos")
    print("2. add video ")
    print("3. update video details ")
    print("4. delete video ")
    print("5. Exit app")
    choose = input("Enter any number to choose ")

    match choose:
      case '1':
        list_all_videos(videos)
      case '2':
        add_videos(videos)
      case '3':
        update_videos(videos)
      case '4':
        delete_videos(videos)
      case '5':
        break
      case _:
        print("Invalid_number")





