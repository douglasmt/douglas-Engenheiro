'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

def copy(original, copy):
    with open(original) as file:
        reading = file.read()
        reversing = reading[::-1]
    with open(copy, "w") as file:
        file.write(reversing)

copy('copy/story_input.txt', 'copy/story_reverse.txt')                

'''udemy
Here's my solution:

def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()
 
    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])
'''