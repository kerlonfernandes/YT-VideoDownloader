from pytube import YouTube

def Download(link):
        #Options
    print("Witch resolution do u want ?")
    print(15*'-=')
    print('Press [1] to lowest')
    print(15*'-=')
    print('Press [2] to highest')
    print(15*'-=')
    print('Press [3] to only audio')
    print(15*'-=')

    choose = input("")
    youtubeObject = YouTube(link)    

    if choose == '1':
        youtubeObject = youtubeObject.streams.get_lowest_resolution()
    elif choose == '2':
            youtubeObject = youtubeObject.streams.get_highest_resolution()
    elif choose == '3':
            youtubeObject = youtubeObject = youtubeObject.streams.get_audio_only()

    try:
            youtubeObject.download()
    except:
        print('There has been an error in downloading your YouTube video!')
        print('Check if your YT link is valid')
    print('''Download is getting start...
    
    this little project was made by: Zzmid/kerlo:) enjoy :D''')

link = input("Put your YouTube link: ")
Download(link)