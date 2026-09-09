paragraph='''Python is a programming language.
This python course teaches programming basics and advanced concepts.
It is an interesting course for an beginners.'''
print("Length:",len(paragraph))
print("First character:",paragraph[0])
print("Second charactr:",paragraph[-1])
print("Preview:",paragraph[:50])
replaced=paragraph.replace("python","PYTHON")
print("\n After replacement:")
print(replaced)
lowercase= paragraph.lower()
print("\nLowercase:")
print(lowercase)
paragraph = paragraph.strip()
print("\nAfterstrip")
print("paragraph")
words=paragraph.split()
print("\nwords list:",words)

if "course" in paragraph:
    print("\nThe word 'course' is found.")
else:
    print("\nThe word 'course' is not found.")
print("\nThe course description is {} characters long and has {} words.".format (len(paragraph),len(words) ) )  



