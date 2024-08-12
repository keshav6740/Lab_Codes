import socket 

ip = socket.gethostbyname('www.google.com')
print (ip)

with open('demo.txt', 'r') as file:
    data = file.read()
    words = data.split()

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

def get_count(word_count):
    return word_count[1]

sorted_words = sorted(word_counts.items(), key=get_count, reverse=True)
for word, count in sorted_words:
    print(f"{word}: {count}")
