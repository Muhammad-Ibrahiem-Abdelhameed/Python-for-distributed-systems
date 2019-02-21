
import logging
import os
from time import time

from sec_3.links_soap import setup_download_dir, get_links, download_link

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    ts = time()
        
    download_dir = setup_download_dir()
    links = get_links()
    
    #for link in links:
    #download_link(download_dir, link)
    logging.info('Took %s seconds', time() - ts)
    
    print(links)

if __name__ == '__main__':
    main()




    
