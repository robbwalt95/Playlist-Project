import os
import io
from tinytag import TinyTag


def show_info(w, x, y):
    z = x + y
    try:
        #Checking format exists
        if ".mp3" in y or ".m4a" in y or ".flac" in y:
            tag = TinyTag.get(z)
            #checking tag properly exists
            if tag:
                #open file with utf8 encoding to allow special charaters
                file1 = open("data.json", "a", encoding='utf8')
                #strip unwanted characters
                tag.title = tag.title.replace('"', '')
                #write out itemized format to file
                file1.write('\n[\n"' + tag.artist + '",\n"' + tag.title + '"\n]')
                file1.close()
    except:    
        print("error")
        
def main():
    # Get the list of all files and directories
    path = "[Put in Music directory here]"
    dir_list = os.listdir(path)

    #json starting format
    file1 = open("data.json", "a", encoding='utf8')
    file1.write('{\n"headers": [\n"Artist",\n"Title"\n],\n"rows": [')
    file1.close()

    last_item = dir_list[-1]
    count = 1
    #for file in directory list
    for i in dir_list:
        #send each file individually to have metadata formatted
        show_info(count, path, i)
        count += 1
        #while not the last item
        if i != last_item:
            file1 = open("data.json", "a", encoding='utf8')
            file1.write(',')
            file1.close()
        #if last file - close row } ]
        else:
            file1 = open("data.json", "a", encoding='utf8')
            file1.write('\n]\n}')
            file1.close()
    
main()
