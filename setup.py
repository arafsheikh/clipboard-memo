from setuptools import setup

setup(
    name='clipboard_memo',
    version='0.1',
    description='Command-line clipboard manager',
    url='http://github.com/arafsheikh/clipboard-memo',
    author='Sheikh Araf',
    author_email='arafsheikh@rocketmail.com',
    license='MIT',
    include_package_data=True,
    entry_points='''
        [console_scripts]
        cman=clipboard_memo:main
    ''',
)