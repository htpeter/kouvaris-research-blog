"""
Roam parser static variables.
"""

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

bracket_pattern = r'\[\[(.*?)\]\]'
bracket_regex = re.compile(bracket_pattern)


"""
<ul class="menu">
                    <li>
                        <a href="/posts/tiered_open_education">
                            A System for Opening Educational Institutions at 2020-04-15 8:32:50 AM
                        </a>
                        <!-- <br><button class="green-pill">Machine Learning Tool</button> -->
                    </li>
                    <li>
                        <a href="/posts/model_monitoring">
                            Model Monitoring Spec published at 2020-04-13 10:59:53 PM
                        </a>
                        <!-- <br><button class="green-pill">Machine Learning Tool</button> -->
                    </li>
                    <!-- <li>About published at 2020-04-03 12:43:50 PM</li> -->
                </ul>
"""
