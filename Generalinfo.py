import os



# Each website is a separate project (folder)
"""
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)
"""


# Create queue and crawled files (if not created)
def create_files():
    crawled = 'History Forensics/CrawledUrls.txt'
    keywords = 'History Forensics/keywords.txt'
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    if not os.path.isfile(keywords):
        write_file(keywords, '')


# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass




# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a line in a file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)