import re
import json

from slugify import slugify

from roam.constants import jinja_header, jinja_footer, bracket_regex

def has_bracket(text):
    matches = bracket_regex.findall(text)
    if matches > 0:
        return True, matches

    else:
        return False, matches


class RoamPage:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.slug = slugify(name)

        self.links_to = []

        self.html = jinja_header

    def _build_page(self):
        self.add_html(self.name, '<h1 id="tufte-css">')
        self.add_html('', '<section>')

        continue = True
        depth = 0
        while continue:

        


        self.add_html('','</section>'))

    def add_html(text, start_tag, end_tag):
        addition = '\n' + start_tag + text + end_tag 
        self.html += addition
        return self

    def add_list(children):
        pass 

class RoamGraph:
    def __init__(self, json):
        self.json = json 
        self.root_pages = []

        # run funcs
        self._parse_root()
        print(self.root_pages)

    def _parse_root(self):
        for root in self.json:
            self.root_pages.append(root['title'])


def build_from_json(json_file):
    with open(json_file, 'r') as f:
        parsed_json = json.load(f) 

    RoamGraph(parsed_json)
