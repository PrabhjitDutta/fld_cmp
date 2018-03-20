from setuptools import setup

setup(name="fld-cmp",
      version="1.0",
      py_modules=['file-folder_cmp'],
      install_requires=['Click'],
      entry_points='''
      [console_scripts]
      fld_cmp = file_folder_cmp:cli
      ''',
)