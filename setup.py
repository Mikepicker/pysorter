from setuptools import setup

setup(
        name='pysorter',
        version='0.0.5',
        description='A file-type based organizer',
        url='',
        author='Chris Coetzee',
        author_email='chriscz93@gmail.com',
        license='GPL',
        packages=['pysorter'],
        zip_safe=False,
        entry_points = {
        "console_scripts": ['pysorter = pysorter.pysorter:main']
        },
    )