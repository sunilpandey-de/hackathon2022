from mechanicalsoup import StatefulBrowser
from re import findall


agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'


class scrape(StatefulBrowser):

      def __repr__(
        fitur = {
            'features':'html.parser'
                 },
        uag = agent
      ):
          return StatefulBrowser(
            soup_config = fitur,
            user_agent = agent
          )

class Parser(object):

      __list = []

      def __init__(
        self,
        search_keyword,
        URL,
        pattern,
        class_tag
      ):
          self.search_keyword = search_keyword
          self.URL = URL
          self.__pattern = pattern
          self.class_tag = class_tag
          
          
      def __dir__(self):
          return list(set(self.__list))

          
      def get_page(self):
          self.__req = scrape()
          s = self.__req.open(
            self.URL,
            timeout = 10
          )
          self.__req.select_form(
            'form[action="/search"]'
          )
          self.__req['q'] = self.search_keyword
          self.__req.submit_selected()
          _content = str(self.__req.get_current_page())
          for urls in findall(
            self.__pattern,
            _content                        
          ):  
              if 'www.google.com' in self.URL: self.__list.append(urls)
              else: self.__list.append(urls[:-1])
          return self.__req.get_current_page().find_all(
            'a',
            class_=self.class_tag
          )
          
      def request(self):
          self.__req = scrape()
          for page in self.get_page():
              try:
                  self.__req.open(
                    f'{self.URL}{page.get("href")}'
                  )
                  content = str(self.__req.get_current_page())
                  for urls in findall(
                  self.__pattern,
                  content
                  ):
                      if 'www.google.com' in self.URL: self.__list.append(urls)
                      else: self.__list.append(urls[:-1])
              except Exception as e:
                  print(e)