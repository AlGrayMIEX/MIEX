# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('settings/settings.py', targetName='miex_settings_alpha.exe', icon='miexlogo.ico', base="Win32GUI")]

excludes = []

'''excludes = ['unicodedata', 'logging', 'unittest', 'email', 'html', 'http', 'urllib',
            'xml', 'pydoc', 'doctest', 'argparse', 'datetime', 'zipfile',
            'subprocess', 'pickle', 'threading', 'locale', 'calendar',
            'tokenize', 'base64', 'gettext',
            'bz2', 'fnmatch', 'getopt', 'string', 'stringprep',
            'contextlib', 'quopri', 'copy', 'imp', 'linecache']'''

includes = ['json', 'tkinter', 'tkinter.ttk',  'tkinter.filedialog', 'PIL', 'pathlib']

zip_include_packages = ['json', 'tkinter', 'tkinter.ttk',  'tkinter.filedialog', 'PIL', 'pathlib']

options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'includes': includes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows',
    }
}

setup(name='MIEX settings',
      version='0.0.5',
      description='MIEX settings app',
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
