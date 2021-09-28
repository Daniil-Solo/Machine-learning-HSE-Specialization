import requests
import pandas as pd
import datetime
import bs4
import time
import tqdm


class ArticleParser:
    __domain_part = 'https://zadolba.li/'
    __first_date = '20090908'
    __time_out = 1

    def __init__(self, user_agent=None):
        self.__user_agent = user_agent
        self.table = pd.DataFrame(columns=['title', 'text', 'tags', 'date'])

    def start(self, parsing_type, clean_table=True):
        if clean_table:
            self.table = pd.DataFrame(columns=['title', 'text', 'tags', 'date'])

        start_day, last_day = self.__calculate_dates(parsing_type)
        days = (start_day - last_day).days
        day = start_day

        for current_days in tqdm.tqdm(range(1, days + 1)):
            date_part = str(day).replace('-', '')
            link = ArticleParser.__domain_part + date_part
            html = self.__get_html(link)
            day = start_day - datetime.timedelta(days=current_days)
            if html is None:
                continue
            story_blocks = self.__get_story_blocks(html)
            for story_block in story_blocks:
                description = self.__get_description(story_block)
                self.table = self.table.append(description, ignore_index=True)
            time.sleep(ArticleParser.__time_out)

    def save_table(self, path):
        self.table.to_csv(path, sep=';', index=False)

    def __calculate_dates(self, parsing_type):
        if parsing_type[:4] == 'last':
            today = datetime.date.today()
            try:
                number = int(parsing_type.split(' ')[1])
            except ValueError:
                raise ValueError('The parsing type should be followed by a number (days)')
            last_day = today - datetime.timedelta(days=number)
            return today, last_day

        elif parsing_type[:5] == 'first':
            last_day = datetime.date(int(ArticleParser.__first_date[:4]),
                                     int(ArticleParser.__first_date[4:6]),
                                     int(ArticleParser.__first_date[6:8]))
            try:
                number = int(parsing_type.split(' ')[1])
            except ValueError:
                raise ValueError('The parsing type should be followed by a number (days)')
            start_day = last_day + datetime.timedelta(days=number)
            return start_day, last_day

        elif parsing_type == 'all':
            today = datetime.date.today()
            last_day = datetime.date(int(first_date[:4]), int(first_date[4:6]), int(first_date[6:8]))
            return today, last_day

        else:
            raise ValueError('Uncorrect pasring type. Parsing types starts with only these key-words: last or all')

    def __get_html(self, link):
        response = requests.get(link, headers={'User-Agent': self.__user_agent})
        if response.ok:
            return response.content
        else:
            return None

    def __get_story_blocks(self, html):
        soup = bs4.BeautifulSoup(html, 'html.parser')
        content_block = soup.find('div', {'class': 'content'})
        story_blocks = content_block.find_all('div', {'class': 'story'})
        return story_blocks

    def __get_description(self, story_block):

        try:
            title = story_block.h2.text.replace('\xa0', ' ')
        except AttributeError:
            title = None

        try:
            text = story_block.find('div', {'class': 'text'}).text.replace('\xa0', ' ').replace('\n', ' ').strip()
        except AttributeError:
            text = None

        try:
            html_tags = story_block.find('div', {'class': 'tags'}).ul.find_all('li')
            tags = [html_tag.a.text for html_tag in html_tags]
            tags = ', '.join(tags)
        except AttributeError:
            tags = None

        try:
            meta_block = story_block.find('div', {'class': 'meta'})
            datetime = meta_block.find('time').get('datetime')
            date = datetime.split('T')[0]
        except AttributeError:
            date = None

        return {'title': title, 'text': text, 'tags': tags, 'date': date}