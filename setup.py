import setuptools

with open("README.md", "r") as 自述文件:
    长描述 = 自述文件.read()

setuptools.setup(
    name="python-console-with-local-feedback",
    version="0.0.1",
    author="吴烜",
    author_email="",
    description="反馈信息为中文的Python控制台",
    long_description=长描述,
    long_description_content_type="text/markdown",
    url="https://github.com/program-in-chinese/python-console-with-local-feedback",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = """
    [console_scripts]
    明义 = 明义.解释器:解释器
    """,
)