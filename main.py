import threading
from Queue import Queue
from Spider import Spider
from Generalinfo import *
import urllib2
from bs4 import BeautifulSoup
from shutil import copyfile
import os




#PROJECT_NAME = 'History Forensics'
QUEUE_FILE = 'G:/1516PythonProject2.0/GUI/History Forensics/Chrome_Hist.csv'
CRAWLED_FILE = 'G:/1516PythonProject2.0/GUI/History Forensics/CrawledUrls.txt'
NUMBER_OF_THREADS = 2
Queue = Queue()
Spider()
keywords = ''

src = 'ChromeCode/Chrome_Hist.csv'
dst = 'History Forensics/Chrome_Hist.csv'

path = 'ChromeCode/Chrome_Hist.csv'





class MainSpider():






# Create worker threads (will die when main exits)
    def create_workers(self):
        for _ in range(NUMBER_OF_THREADS):
            t = threading.Thread(target=self.work)
            t.daemon = True
            t.start()


# Do the next job in the queue
    def work(self):
        while True:
            url = Queue.get()
            Spider.crawl_page(threading.current_thread().name, url)
            Queue.task_done()


# Each queued link is a new job
    def create_jobs(self):
        for link in file_to_set(QUEUE_FILE):
            Queue.put(link)
        Queue.join()
        self.crawl()


# Check if there are items in the queue, if so crawl them
    def crawl(self):
        queued_links = file_to_set(QUEUE_FILE)
        if len(queued_links) > 0:
            print(str(len(queued_links)) + ' links in the queue')
            self.create_jobs()


    def get_keywords(self):


            common_words = open('G:/1516PythonProject2.0/GUI//FileStorage/common.txt', 'r').readlines()
            keywords = open('G:/1516PythonProject2.0/GUI/History Forensics/keywords.txt', 'r').read().split('\n')
            f = open('G:/1516PythonProject2.0/GUI/History Forensics/keywords.txt', 'a')
            urls = file_to_set(QUEUE_FILE)
            user_agent = 'Mozilla/4.0 (compatible; 5.5; Windows NT)'
            head = {'User-Agent': user_agent}
            for i in urls:
                #print urls
                request = urllib2.Request(i[1:-1], headers=head)
                try:
                    html_content = urllib2.urlopen(request).read()
                except ValueError as e:
                    print 'Error while loading page at', i, 'continuing...'
                    continue
                soup = BeautifulSoup(html_content)
                for script in soup(["script", "style"]):
                    script.extract()
                    text = soup.get_text()
                    lines = (line.strip() for line in text.splitlines())
                    chunks = (phrase.strip() for line in lines for phrase in line.split(" "))
                    text = '\n'.join(chunk for chunk in chunks if chunk)
                    (text.encode('utf-8'))
                    visible_text = soup.getText()
                    words = visible_text.split(' ')
                    for word in words:
                        if word not in common_words and word not in keywords:
                            f.write('\n')
                            keywords.append(word)


    def CopyFile(self):

        copyfile(src, dst)
        os.remove(path)


#create_workers()
#get_keywords()
#crawl()










