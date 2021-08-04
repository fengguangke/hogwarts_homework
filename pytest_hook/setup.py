from setuptools import setup

setup(
    name="pytest-encode-log",  # Replace with your own username
    version="0.0.1",
    author="hiyongz",
    author_email="zhiyo2016@163.com@example.com",
    description="set your encoding and set log",
    long_description="show Chinese for your mark.parametrize().",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Pytest",
        "Topic :: Software Develoment :: Testing",
    ],
    license='MIT License',
    packages=['pytest_log'],
    keywords=[
        "pytest",
        "py.test",
        "pytest_log",
    ],
    install_requires=[
        'pytest'
    ],
    python_requires=">=3.6",
    # 入口模块或者入口函数
    entry_points={
        'pytest11': [
            'pytest-log = pytest_log.log'
        ]
    },

    zip_safe=False
)