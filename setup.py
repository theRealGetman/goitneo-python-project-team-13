from setuptools import find_namespace_packages, setup

setup(
    name='muaddib',
    version='1',
    description='GoIT Neoversity Team 13 Python module project',
    url='https://github.com/theRealGetman/goitneo-python-project-team-13',
    author='Team 13',
    author_email='a.e.getman@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=['faker', 'termcolor', 'wcwidth', 'prompt_toolkit'],
    entry_points={'console_scripts': ['muaddib = src.main:main']},
)
