
import logging
import os
from queue import Queue
from threading import Thread
from time import time

from links_soap import setup_download_dir, get_links, download_link, setup_url_file


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

all_links = []
url = 'https://www.programiz.com'
#count = 0
class DownloadWorker(Thread):

    def __init__(self, queue, file):
        Thread.__init__(self)
        self.queue = queue
        self.file = file

    def run(self):
        x = 0
        while True:
            # Get the work from the queue and expand the tuple
            num, link = self.queue.get()
            self.file.write(link+"\n")
            count = num + 1
            temp_links = call_all_links(url+link)
            for lnk in temp_links:
                print(lnk)
                self.file.write(lnk + "\n")
                if count != 1:
                    self.queue.put((count, lnk))

            self.queue.task_done()
            x += 1
            print(count)
        print('finish')

def call_all_links(url):
    links = get_links(url)
    return links[:15]

def improve_file(file_name):
    uniqlines = set(open(file_name).readlines())
    file = open(file_name, 'w')
    file.writelines(set(uniqlines))
    file.close()

def main():
    #count = 0
    global all_links
    ts = time()
    links = call_all_links(url)
    #directory = setup_download_dir()
    file_name = 'urls.txt'

    file = open(file_name, 'a+')
    # Create a queue to communicate with the worker threads
    queue = Queue()
    # Create 8 worker threads
    setup_url_file()
    for x in range(8):
        worker = DownloadWorker(queue, file)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()
    # Put the tasks into the queue as a tuple
    for link in links:
        logger.info('Queueing {}'.format(link))
        queue.put((0, link))

    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()
    file.close()
    improve_file(file_name)
    logging.info('Took %s', time() - ts)


if __name__ == '__main__':
    main()




