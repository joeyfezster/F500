from bs4 import BeautifulSoup

from m_and_a_crawl import utils


class Wikipedia_table:
    @staticmethod
    def __get_text(td):
        spans = td.find_all('span')
        if len(spans) > 1:
            return spans[1].text
        if len(spans) == 1:
            spans[0].replace_with('')
        for sup in td.find_all('sup'):
            sup.replace_with('')

        return td.text

    def __init__(self, html):
        self.__soup = BeautifulSoup(html, "html.parser")
        self.__html_rows = self.__soup.find_all('tr')

    def _get_headers(self):
        return [h.text for h in self.__html_rows[0].find_all('th')]

    def _get_rows(self):
        return self.__html_rows[1:]

    def _match_headers(self, headers):
        self._columns = {}
        for header in headers:
            for idx, _header in enumerate(self._get_headers()):
                if header in _header: self._columns[header] = idx

    def write_to_file(self, outfile, headers, ticker=None):
        self._match_headers(headers)
        rows = []
        for record in self._get_rows():
            row = ""
            record_items = record.find_all('td')
            for header in headers:
                td = record_items[self._columns[header]]
                cell = self.__get_text(td)
                if not utils.contains_alphanumerics(cell): cell = "N/A"
                row = row + cell + "; "
            rows.append(row)

        with open(outfile, "w+") as outfile:
            if ticker: outfile.write(ticker + '\n')
            for h in headers:
                outfile.write(h + "; ")
            outfile.write("\n")
            for row in rows:
                outfile.write(row + "\n")
                print(row)