# random-leetcode-py
Python script to randomly select a top interview prep question from leetcode and open in browser.

*Tested on Linux.*

```shell
# clone the repo
git clone https://github.com/2ashishs/random-leetcode-py.git
# cd into repo
cd random-leetcode-py
# install the package locally
pip install . -e
# now cd into any folder of your choice
cd /path/to/a/folder/of/choice
# and run, voila!
random_leetcode
# browser should open with a leetcode question
```

### ToDo
 - [ ] Add update logic
   - [ ] Update lc_todo file when questions are updated
   - [ ] Store lc_done file in $HOME
 - [ ] Test on Windows / Mac
 - [ ] Add code to package and publish on PyPI