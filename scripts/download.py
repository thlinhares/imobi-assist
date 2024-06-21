import os
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

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

        Returns:
        - itbi_dict: Dictionary containing url files.
        """
        try:
            teste = self.search_html_table()
            print(f"RESULT: {teste}")
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
        itbi_dict = {}
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
            if (ref_date < 202312):
                continue

            itbi_dict[ref_date] = link
        
        return itbi_dict

    
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