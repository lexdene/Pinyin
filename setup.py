from setuptools import setup, find_packages

with open('README.md', 'rt') as f:
    long_description = f.read()

setup(
    name='smart_pinyin',
    version='0.4.6',
    description='Smart Chinese-to-Pinyin converter.',
    author='Elephant Liu',
    url='https://github.com/lexdene/Pinyin',
    license='MIT',
    packages=find_packages(),
    package_data={
        'pinyin': [
            'data/*.dic',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    install_requires=['jieba', 'six'],
    long_description_content_type='text/markdown',
    long_description=long_description,
)
