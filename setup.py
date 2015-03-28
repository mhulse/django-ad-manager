from setuptools import setup, find_packages

VERSION = '1.0.0'

setup (
    name = 'django-ad-manager',
    version = VERSION,
    description = '**BETA!** See `README.md` for more info.',
    author = 'Micky Hulse',
    author_email = 'm@mky.io',
    maintainer = 'Micky Hulse',
    maintainer_email = 'm@mky.io',
    url = 'https://github.com/mhulse/django-ad-manager',
    license = 'http://www.apache.org/licenses/LICENSE-2.0',
    platforms = ['any'],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
)
