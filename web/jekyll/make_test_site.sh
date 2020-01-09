#!/bin/bash

# gem install jekyll
mkdir -p test_site
cd test_site
jekyll new test_site
jekyll serve -H 0.0.0.0
# http://localhost:4000/
# git remote add origin https://github.com/your-user-name/your-user-name.github.io.git
# git add .
# git commit -m "Save my work"
# git push -u origin master
