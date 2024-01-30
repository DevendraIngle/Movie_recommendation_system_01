from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
AUTHOR_NAME = "DEVENDRA INGLE"
SRC_REPO = "src"

LIST_OF_REQUIREMENTS = ['streamlit' ]

setup(
  name='streamlit_app',
  version='0.0.1',
  author=AUTHOR_NAME,
  author_email='deveningle121@gmail.com',
  description='A simple python package to make movie recommendation',
  long_description=long_description,
  long_description_content_type="text/markdown",
  package=[SRC_REPO],
  python_requires='>=3.7',
  install_requires=LIST_OF_REQUIREMENTS,
)