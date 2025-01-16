# Deploying a basic flask app

- create new project in VSCode
- create a venv, activate and intall deps
  - py -m venv .venv
  - source .venv/Scripts/activate
  - pip install requests python-dotenv Flask
- create a git repo in your project
- add `static` and `templates` folders
- add a `styles` folder inside `static`
- we store html files in `templates`
- create index.html inside templates
  - curse VSCode since it won't provide HTML intellisense inside the templates folder
- add a link inside index.html for your stylesheet (specific to Flask):

```html
<link
  href="{{ url_for('static', filename='styles/style.css')}}"
  rel="stylesheet"
/>
```
