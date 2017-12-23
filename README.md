Please follow me on https://steemit.com/@yuxi

## A language character counter tool

According to the latest Utopian rule, any contribution in 'translation' category must translate over a number of words. If the translator works in Crowdin, it is easy to have the word count number. However, if the translator works on Github project directly, it is a bit difficult to count the characters in a particular language as for translation work, ususlly multiple language characters exist in the same file. I have implemented a tool to do this job. It is written in Python and has been tested on Ubuntu 16.

## Implementation

The basic idea is to analysis the text and check each character against the unicode values for each language. In principle, the script works with any language - just edit the configuration file. Also, to make it handy for both translators and moderators, the tool support counting for both individual files and all files contained in a folder.

## Test

I have written a couple of test to validate if the tool works and all tests pass.

```bash
$ python test.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
```

## How to use

First, clone this repository to your PC. 

Then modify the first line of wordcounter.py to get your python folder right:
```bash
#!/home/yuxi/environments/myenv/bin/python
```

To count individual file, run:
/YOUR_FOLDER/wordcounter.py FILENAME locale

To count all files within a folder, run:
/YOUR_FOLDER/wordcounter.py FOLDER locale

