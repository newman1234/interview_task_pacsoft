import re

ret_list = []

file_path = '/Users/newman/Downloads/free_text_mining.txt'

f = open(file_path, 'r')
rows = f.readlines()
for i, line in enumerate(rows):
    if re.search('.* - .*, \d{4} - .*', line):
        if re.search('\[\w+\] .*', rows[i-1]):
            m = re.search('(\[\w+\]) (.+)', rows[i-1])
            ret_list.append(m.group(2).split('\n')[0])
        else:
            ret_list.append(rows[i-1].split('\n')[0])
print({'paper_title':ret_list})