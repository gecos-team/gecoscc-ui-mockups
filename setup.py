import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid>=1.4',
    'pyramid_jinja2',
    'waitress',
]

setup(name='gecoscc-mockups',
      version='0.0',
      description='gecoscc-mockups',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Junta de Andalucia',
      author_email='',
      url='https://github.com/gecos-team',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      package_data={
          'templates': ['*.jinja2'],
          'locale': ['*.pot', '*.po', '*.mo'],
          'static': ['*.js', '*.css', '*.jpg', '*.png'],
      },
      install_requires=requires,
      tests_require=requires,
      test_suite="gecoscc",
      entry_points="""\
      [paste.app_factory]
      main = gecosccmockups:main
      """,
      paster_plugins=['pyramid'],
      )
