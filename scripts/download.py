import os
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import urllib.request

ITBI_DATA_URL = 'https://dados.pbh.gov.br/dataset/relatorio-itbi'

class Download:
    def __init__(self, data_dir):
        """
        Initialize the Download class with a data directory.

        Args:
        - data_dir (str): Directory path for download files.
        """
        self.data_dir = data_dir


    def get_itbi_report(self):
        """
        Download itbi report CSV file in the specified directory.

        """
        try:
            itbi_report_dict = self.search_html_table()
            for key, value in itbi_report_dict.items():
                csv_file_path = self.download_file(key, value['url'])
                value['path'] = csv_file_path
            
            print(f"Download completed successfully!")
            return itbi_report_dict
        except Exception as e:
            print(f"Unexpected error download itbi report: {e}")
            raise

    def search_html_table(self):
        """ Parse the table HTML and store the collected metadata
            in the result dictionary.
        """
        req = Request(
            url=ITBI_DATA_URL, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        page = urlopen(req)
        html = page.read().decode("utf-8")
        parsed_html = BeautifulSoup(html, "html.parser")
        rows = parsed_html.find_all('li', {'class': 'resource-item'})
        itbi_report_dict = {}
        for row in rows:
            heading = row.find('a', {'class': 'heading'})
            title = heading.get('title')
            if ('Relatório ITBI' not in title) or ('Dicionário de Dados' in title) or (' a ' in title): 
                continue

            title = title.split(' - ')
            ano = title[0]
            mes = self.monthToNum(title[1].lower())
            if not mes:
                continue

            link = row.find('a', {'class': 'dropdown-item resource-url-analytics'})['href']
            ref_date = int("%s%s"%(ano,mes))
            if (ref_date <= 202403):
                continue
            files = {
                'url': link
            }
            itbi_report_dict[ref_date] = files
        
        return itbi_report_dict

    def download_file(self, key, url):
        extension = os.path.splitext(url)[1]
        csv_file_path = os.path.join(os.path.dirname(self.data_dir), str(key) + extension)

        print(f'Starting download of {csv_file_path}')
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url, csv_file_path)
        return csv_file_path
    
    def monthToNum(self, month):
        months = {
                'janeiro': '01',
                'fevereiro': '02',
                'março': '03',
                'abril': '04',
                'maio': '05',
                'junho': '06',
                'julho': '07',
                'agosto': '08',
                'setembro': '09', 
                'outubro': '10',
                'novembro': '11',
                'dezembro': '12'
        }
        try:
            return months[month]
        except:
            return ""