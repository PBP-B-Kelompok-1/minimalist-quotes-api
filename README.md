# Minimalist Quotes API

Made for our assignment, minlife-community. ha

## Where we got these quotes

https://www.becomingminimalist.com/minimalism-quotes/

## Build?

Here are instructions if you want to run it locally:

1. Clone the repository
```bash
git clone https://github.com/PBP-B-Kelompok-1/minimalist-quotes-api && cd minimalist-quotes-api
```
2. Enable venv and install dependencies
```bash
# Make venv
python -m venv env

# For POSIX shells
source env/bin/activate
# Powershell
env\bin\Activate.ps1 # honestly dont know
# csh
./env/bin/activate.csh
# fish
./env/bin/activate.fish
# yeah the point is activate venv

pip install -r requirements.txt
```
3. Run migrations
```bash
python manage.py migrate
```
4. Run server
```bash
python manage.py runserver
```
5. Access it through `localhost:8000` (default) in your web browser!


