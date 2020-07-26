# try-pyramid
This project is based on the flowing [tutorial](https://docs.pylonsproject.org/projects/pyramid/en/latest/tutorials/wiki2/index.html)

## Install environment
**Clone the project**
```bash
git clone https://github.com/galloramiro/try-pyramid.git
```
**Create de virtual environment and install dependencies**
```bash
python3 -m venv ./venv/
source /venv/bin/activate
pip3 install --upgrade pip3 setuptools
cd try_pyramid
pip3 install -e ".[testing]"
```
**Extras**
```bash
alembic -c development.ini revision --autogenerate -m "init"
alembic -c development.ini upgrade head
```
**Run the proyect**
```bash
pserve development.ini --reload
```
