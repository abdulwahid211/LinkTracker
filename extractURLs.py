import requests


def pair_status_code(href=''):
    r = requests.get(href, verify=False)
    return {href: r.status_code}


class extractURL:
    def __init__(self, url, main_list):
        self.url = url
        self.main_list = main_list

    def extract_main_list(self):
        l = set()
        for href in self.main_list:

            if "https" not in href:
                l.add(self.url + href)
            else:
                l.add(href)
        return l

    def verify_status_code(self,url_list):
        status_codes_list = dict()
        for url in url_list:
            status_codes_list.update(pair_status_code(href=url))

        return status_codes_list
