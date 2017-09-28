from setuptools import setup

setup(
    description='Simple functions to make jupyter more clean for presentations',
    name='jupyter_beautifier',
    version='0.1.0a1',
    author='Caio Belfort',
    author_email='caiobelfort90@gmail.com',
    license='MIT',
    url='https://github.com/caiobelfort/jupyter_beautifier',
    packages=['jupyter_beautifier'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires=['jupyter']
)
