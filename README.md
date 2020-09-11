# django-shrotcuts
A script to generate some files like templates or static easily.
```
usage: django_shortcuts.py [-h] --app APP [-a ADD] [-t TEMPLATES] [-s STATIC]

optional arguments:
  -h, --help            show this help message and exit
  --app APP             type the app name
  -a ADD, --add ADD     add file automatically, the value must be one of
                        ['all', 'forms', 'urls', 'templates', 'static']
  -t TEMPLATES, --templates TEMPLATES
                        add templates html file
  -s STATIC, --static STATIC
                        add static css file
```

If the app name is mysite, if you type (in the path of manage.py)  
```
django_shortcuts --app mysite -a all
```
It will generate the following files :  
* myiste/forms.py
* mysite/urls.py
* mysite/templates/mysite/index.html
* mysite/static/mysite/style.css

```
django_shorts --app mysite -t hello.html
```
It will generate :  
* mysite/templates/mysite/hello.html  
