# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('miex.py', targetName='miex_alpha_2.exe', icon='miexlogo.ico')]

excludes = []

'''excludes = ['unicodedata', 'logging', 'unittest', 'email', 'html', 'http', 'urllib',
            'xml', 'pydoc', 'doctest', 'argparse', 'datetime', 'zipfile',
            'subprocess', 'pickle', 'threading', 'locale', 'calendar',
            'tokenize', 'base64', 'gettext',
            'bz2', 'fnmatch', 'getopt', 'string', 'stringprep',
            'contextlib', 'quopri', 'copy', 'imp', 'linecache']'''

includes = ['json', 'tkinter', 'tkinter.ttk', 'random', 'threading', 'json', 'pathlib', 'time', 'keyboard', 'pygame.mixer']

zip_include_packages = ['json', 'tkinter', 'tkinter.ttk', 'random', 'threading', 'json', 'pathlib', 'time', 'keyboard', 'pygame']

options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'includes': includes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows',
    }
}

setup(name='MIEX',
      version='0.2.5',
      description='ED: MIssion EXtender',
      executables=executables,
      options={
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'no_compress': True,
        'includes': includes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows',
    }
})
