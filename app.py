import os
import sys
import importlib

ROOT_DIR = os.path.dirname(__file__)
sys.path.insert(0, ROOT_DIR)

nst_app = importlib.import_module('NST_Code.app')
app = nst_app.app
