# Django

<!-- vim-markdown-toc GFM -->

* [Settings.py](#settingspy)
  - [development.py](#developmentpy)
  - [production.py](#productionpy)
  - [__init__.py](#init__py)
* [Wagtail Embed Video](#wagtail-embed-video)
  - [blocks.py](#blockspy)
  - [video_card_block.html](#video_card_blockhtml)

<!-- vim-markdown-toc -->

## Settings.py

Sometimes more than one `settings.py` may be useful. E.g. having one `settings.py` for development and another for production is convenient. This paradigm is similar to Flasks app environments.

This is best achieved by creating a `settings/` directory. The original `settings.py` should be moved into `settings/` and renamed to `base.py`. The `base.py` will contain configuration settings that would be agnostic to any app. Specific information such as debug mode and allowed apps will be triggered through two new files; `development.py` and `production.py`. Finally, we create `__init.py__` inside the directory, using this to call our `base.py` through either the `production` or `development` module. See below for a detailed break down.

```sh
# steps to create our new settings directory arrangement
mkdir settings
mv settings.py settings/base.py # move and rename settings.py
cd settings/ 
touch production.py development.py __init__.py
```

After creating the directory and new files, we populate their contents.

### development.py

```python
from .base import *

DEBUG = True
```

### production.py

```python
from .base import *

DEBUG = False
ALLOWED_HOSTS=['app.project_name.com']
```

### __init__.py

```python
# this where we dictate which settings file to run
# example we want to run the production
from .production import *
```

This works because directories with a `__init__.py` file are python packages and are loaded into memory by python as if they are a module. This effectively makes Django load `settings/` as if it were `settings.py`. This is why we call the script relating to the type of environment we want to run inside the `__init__.py`. 

The most important thing to remember when running multiple settings files is that they should inherit from a common base. If we add `django-debug-toolbar` to our `INSTALLED_APPS`, we should be able to do that without redefining all the `INSTALLED_APPS`.

## Wagtail Embed Video

This is hard and poorly explained by Wagtail.

If you want to embed a responsive Bootstrap embed along the lines of 

```html
<div class="embed-responsive embed-responsive-16by9">
  <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/zpOULjyy-n8?rel=0" allowfullscreen></iframe>
</div>
```

then using the default embed video inside the RichTextBlock is definitely not the way to go. It renders its own custom iframe which is difficult to wrangle and in my opinion, useless.

**How do we make it?**

### blocks.py
```python
class VideoBlock(blocks.StructBlock):
    """Only used for Video Card modals."""
    video = EmbedBlock() # <-- the part we need

    class Meta:
        template = "streams/video_card_block.html"
        icon = "media"
        label = "Embed Video"
```
### video_card_block.html
```html
{% load wagtailcore_tags wagtailembeds_tags %}

{% block content %}
    <div class="embed-responsive embed-responsive-16by9">
  <iframe class="embed-responsive-item" src="{{ self.video.url }}?rel=0" allowfullscreen></iframe>
</div>
{% endblock %}
```

The magic here is being able to access the `{{ self.video.url }}` within the template which lets us push that string into the html attribute.

Search the internet for hours and you'll eventually unlock this riddle!
