import pygsheets
from pathlib import Path

print('hello world')

gc = pygsheets.authorize(Path.home() / 'sheets.json', credentials_directory=Path.home())

ss = gc.create('test sheet')
