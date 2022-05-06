'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''
#BUILDING!
def find_and_replace(file_in, word_ori, new_word):    
    with open(file_in) as file:                
        file_read = file.read() 
        file_words = file_read.replace(word_ori,new_word)

    return file_words
        
print(find_and_replace('/Users/douglastome/03-Python-bootcamp/Session30/copy/story.txt', 'Alice', 'NEEEW'))

#UDEMY
def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }