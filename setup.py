from setuptools import setup, find_packages
PACKAGES = find_packages()

opts = dict(name="package",
            maintainer="mrabdullahsahin",
            maintainer_email="",
            description="Python with Coding Challenges",
            long_description="Python with Coding Challenges",
            url="https://github.com/mrabdullahsahin/python-coding-challenges",
            download_url="https://github.com/mrabdullahsahin/python-coding-challenges",
            license="MIT",
            packages=PACKAGES)


if __name__ == '__main__':
    setup(**opts)
