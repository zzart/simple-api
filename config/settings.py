""" Static variables """
import os

CURRENT_PATH = os.path.abspath(os.path.dirname(__name__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UWSGI = os.path.join(BASE_DIR, 'config/uwsgi.ini')

