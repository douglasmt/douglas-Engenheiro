'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''
#BUILDING!
def statistics(file_in):
    
    with open(file_in) as file:        
        num_lines = sum(1 for line in file)

    with open(file_in) as file:                
        file_read = file.read() 
        num_words2 = 0 
        for word in file_read.split():
            num_words2 += 1
        print(num_words2)

    with open(file_in) as file:                
        file_read_char = file.read() 

    return dict(lines=num_lines, words=num_words2, characters = len(file_read_char) )

print(statistics('/Users/douglastome/03-Python-bootcamp/Session30/copy/story.txt'))

#UDEMY
def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }