import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ ="0.0.0"

REPO_NAME = 'Text-Summarizer-Project'
AUTHOR_USER_NAME = 'shyamkumaran'
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "shyamkumaran@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shyamkumaran/textSummarizer",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages = setuptools.find_packages(where="src")
)
