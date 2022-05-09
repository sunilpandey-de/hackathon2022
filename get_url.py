import sys,argparse

try:
    import mechanicalsoup
    import requests
except Exception as e:
    print('mechanicalsoup package Not Installed\n')
    print('type pip3 install mechanicalsoup')
    exit()

from lib import Parser

urls = []

class crawl(object):

    auth = {
        1:[
            'https://www.google.com',
            'class="r"><a href="/url\?q=(.*?)&amp',
            'fl'
        ],
        2:[
            'https://www.bing.com',
            'h=".*?" href="(h.*?")',
            "b_widePag sb_bp"
        ]
    }

    def __init__(
            self,
            search_keyword):
        self.search_keyword = search_keyword

    def Bing(self):
        bing = Parser(
            self.search_keyword,
            crawl.auth[2][0],
            crawl.auth[2][1],
            crawl.auth[2][2],
        )
        bing.request()
        for url in dir(bing):
            if 'microsoft.com' in url or 'bing.com' in url:
                pass
            else:
                urls.append(url)

    def Google(self):
        google = Parser(
            self.search_keyword,
            crawl.auth[1][0],
            crawl.auth[1][1],
            crawl.auth[1][2],
        )
        google.request()
        for url in dir(google):
            if 'google.com' in url or 'google.co.in' in url:
                pass
            else:
                urls.append(url)


fel = sys.argv[0]
par = argparse.ArgumentParser(
    prog=fel,
    usage="%(prog)s --search_keyword [keyword]",
    formatter_class=argparse.RawTextHelpFormatter,
    description="""Descriptions: Crawl Web Use Google search_keyword & Bing search_keyword""")

par.add_argument('--search_keyword',
                 help="""Your search_keyword e.g inurl:.php?id=""",
                 metavar='[keywords]',
                 type=str)
arg = par.parse_args()

try:
    if arg.search_keyword != None:
        _ = crawl(arg.search_keyword)
        _.Bing()
        _.Google()
        if urls != []:
            for url in list(set(urls)):
                urlval = '{}\n'.format(url)
                # Open a file with access mode 'a'
                file_object = open('sample.txt', 'a')
                # Append 'hello' at the end of file
                file_object.write(urlval)
                # Close the file
                file_object.close()
        else:
            print('\nNo Url Found !\n')
    else:
        par.print_help()
except Exception as e:
    print(e)
except KeyboardInterrupt:
    exit()






