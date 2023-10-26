# go_flask
A python framework for web and gui apps, It is built on flask, eel and pyinstaller

if you want to start a web app - run index.py
![Web app](documentation/images/run_web_app.png "Web App")


if you want to start a GUI app - run main.py
![GUI app](documentation/images/create_gui_app.png "GUI App")


Using YoYo Migration

once package is installed, 
initially configure your Database

with this code  
```bash
python -m yoyo init -d 'go_flask.db' 'migrations'
```

```bash
python -m yoyo new -m "initial_migration"
```
initial_migration - can be your name

```bash
python -m yoyo apply
```