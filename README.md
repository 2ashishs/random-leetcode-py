# random-leetcode-py
Python script to randomly select a top interview prep question from leetcode and open in browser.

*Tested on Linux.*

### Install using pip
```shell
pip install -i https://test.pypi.org/simple/ random-leetcode
# now run in shell
random_leetcode
# browser should open with a leetcode question
```

### Install from source
```shell
# clone the repo
git clone https://github.com/2ashishs/random-leetcode-py.git
# cd into repo
cd random-leetcode-py
# install the package locally
pip install . -e
# now run in shell
random_leetcode
# browser should open with a leetcode question
```

### ToDo
 - [x] Add update logic
   - [x] Store lc_done file in $HOME
 - [ ] Test on Windows / Mac
 - [x] Add code to package and publish on PyPI


### Code to publish on https://test.pypi.org/
```shell
# Create account and generate API token on https://test.pypi.org/
# Create a file .pypirc in home directory with token credentials
# cd to this git repo
cd /path/to/this/repo/
# remove the old dist/ folder (if present)
rm -rf dist/
# build the dist
python3 -m build
# publish to testpypi
python3 -m twine upload --repository testpypi dist/*
```
