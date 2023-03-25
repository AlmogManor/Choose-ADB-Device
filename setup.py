from setuptools import setup

setup(
    name='ichoose-device',
    version="1.0.0",
    description="Interactivly choose which adb device you want to work with in the current shell session",
    author="Almog Manor",
    author_email="ManorAlmog@outlook.com",
    packages=["ichoose_device"],
    entry_points={
        'console_scripts': [
            'choose-adb-serial = ichoose_device.scripts.ichoose_device:main',
        ]
    },
    install_requires=["inquirer~=3.1"],
    python_requires=">=3.7"
)
