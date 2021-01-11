# Google-Search

This repository contains an automated test suite for some basic functionality of Google Search.

To run this test suite these requirements need to be installed first:

  - pytest
  - pytest-html
  - selenium

The most reliable way to do this is using virtual environments as to avoid any issues with different versions of 
these libraries.

For example in Linux:

1) virtualenv venv
2) source venv/bin/activate
3) pip3 install -r requirements.txt 
  
To execute the whole test suite execute the following command on the command line:

    pytest -m regression --browser=chrome --open-report --driver_path=webdrivers/linux/chrome/chromedriver
