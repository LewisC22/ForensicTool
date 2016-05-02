from Generalinfo import *


class Spider:

    #project_name = ''
    queue_file = ''
    crawled_file = ''
    keyword_file = ''
    queue = set()
    crawled = set()
    keywords = ()

    def __init__(self):
        #Spider.project_name = project_name
        Spider.queue_file = 'History Forensics/Chrome_Hist.csv'
        Spider.crawled_file = 'History Forensics/CrawledUrls.txt'
        #self.boot()
        #self.crawl_page('First spider', Spider.queue)

    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        #create_project_dir(Spider.project_name)
        create_files()
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)



    # Updates user display
    @staticmethod
    def crawl_page(thread_name, page_url):



        if page_url not in Spider.crawled:
            print page_url
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.crawled)))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()


    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)






