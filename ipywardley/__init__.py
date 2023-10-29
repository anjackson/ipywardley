"""Bringing Wardley Map magic to Jupyter notebooks."""
__version__ = '0.0.7'

from .wardley import WardleyMagics

def load_ipython_extension(ipython):
    ipython.register_magics(WardleyMagics)
