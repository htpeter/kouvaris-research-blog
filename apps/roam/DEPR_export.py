import  re
import glob
import markdown 
import uuid
from slugify import slugify

roam_p1 = r'^- '
roam_reg1 = re.compile(roam_p1)

roam_p2 = r'\n- '
roam_reg2 = re.compile(roam_p2)

re_pattern = r'\[\[(.*?)\]\]'
bracket_regex = re.compile(re_pattern)

list_regex = re.compile(r'\n( {4}|\t| {8}|\t\t)[1-9\-]')
indent_regex = re.compile(r'( {4}|\t)')

jinja_header = """
<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
    <meta charset="utf-8">
    <title>Home</title>
</head>

<body>
    {% extends "template.html" %}
    {% block content %}
"""

jinja_footer = """
   {% endblock %}

</body>
</html>
"""

# replace slugs with this jinja function 
slug_func_replace = " /r/{0} " 

homepage = 'Research\ &\ Development.md'

class RoamNode:
    """
    Transforms markdown page to html page.
    """
    def __init__(self, path):
        self.path = path
        self.filename = self.path.split('/')[-1]
        self.slug = slugify(self.filename)
        with open(self.path, 'r') as f:
            self.content = f.read()
            self.content = self.content.replace('\t','    ')
            # replace list objects at start of newline or at beginning of file
            self.content = roam_reg1.sub('', self.content)
            self.content = roam_reg2.sub('\n', self.content)
            # transform to html. 
            self.html = markdown.markdown(self.content, extensions=['mdx_truly_sane_lists'])

        self.matches = []
        self.links_out_to = []

        self._replace_links()
        self._tufte_style_html()
        self._fix_indents()

    def _replace_links(self):
        for i in bracket_regex.findall(self.html):
            print(i)
            self.matches.append(i)
            slug = slugify(i)
            print(slug)
            jinja_slug = slug_func_replace.format(slug)
            #jinja_slug = '{{ ' + jinja_slug + ' }}'
            print(jinja_slug)
            href = '<a href="{0}"> {1} </a>'
            jinja_slug = href.format(jinja_slug, i)
            self.links_out_to.append(jinja_slug)
            self.html = self.html.replace(i, jinja_slug)

        self.html = self.html.replace('[[','').replace(']]','')
        self.html = jinja_header + '\n' + self.html + '\n' + jinja_footer
        return self

    def _tufte_style_html(self):
        self.html = self.html.replace('<h1>','<h1 id="tufte-css">')
        # self.html = self.html.replace('<h2>','<p class="subtitle">')
        # self.html = self.html.replace('</h2>','</p>')
        self.html = self.html.replace('<ul>','<ul class="user-story-items">')

        # turn images into side notes
        img_template = """
            <label for="sn-proprietary-monotype-bembo" class="margin-toggle sidenote-number"></label>
            <input type="checkbox" id="sn-proprietary-monotype-bembo" class="margin-toggle" />
            <span class="sidenote">
                {0}
            </span>
        """

        # image_regex = re.compile('<img[*]>')
        # find all images
        # for match in image_regex.findall(self.html):
        #     print(match)
        #     print(img_template.format(match))
        #     self.html = self.html.replace(match, img_template.format(match))

        return self

    def _fix_indents(self):
        pass
        # self.html = list_regex.sub('</br>',self.html) 
        # for indent in list_regex.findall(self.html):
            # how many indents aka breaks to add 
            # self.html = indent_regex.sub(r'<\br>',self.html)

def roam_static_generator(roam_export, new_folder):
    """
    1. Create nodes for every file in the input folder.
    2. Markdown to Jinja
    3. Replace [[]] with Jinja links.
    """
    roam_files = glob.glob(roam_export + '*.md')
    nodes = []
    for file in roam_files: 
        nodes.append(RoamNode(file))

    for node in nodes:
        filename = node.slug
        with open(new_folder + filename + '.html', 'w') as f:
            f.write(node.html)
        
