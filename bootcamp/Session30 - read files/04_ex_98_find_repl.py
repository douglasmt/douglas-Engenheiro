'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

#BUILDING!
def find_and_replace(file_in, word_ori, new_word):    
    with open(file_in, 'r') as file:                
        file_read = file.read() 
    
    file_read = file_read.replace(word_ori,new_word)

    with open(file_in, 'w') as file:
        file.write(file_read)

    return None
        
print(find_and_replace('copy/story.txt', 'Alice', 'NEEEW'))

#UDEMY
