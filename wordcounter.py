#!/home/yuxi/environments/myenv/bin/python

import re,sys,yaml,os

class WordCounter:
  def countfile(ranges, filename):
    str = ''
    with open (filename, "r") as f:
      str=f.read().replace('\n', '')

    count = 0
    for n in re.findall(ranges, str):
      count = count+len(n)
    return count

  def countfolder(ranges, foldername,file_extensions):
    total = 0
    for path, subdirs, files in os.walk(foldername):
      for name in [file for file in files if file.endswith(file_extensions)]:
        total = total + WordCounter.countfile(ranges, os.path.join(path, name))

    return total

  def count():
    filename = sys.argv[1]
    locale   = sys.argv[2]

    dict = []
    with open("%s/config/system.yaml" % os.path.dirname(sys.argv[0]), 'r') as stream:
      try:
        dict = yaml.load(stream)
      except yaml.YAMLError as exc:
        print(exc)

    if locale not in dict:
      print ('Cannot find settings for language: ' + locale)
      exit()

    locale_ranges = '[' + dict[locale]['ranges'] + ']+'
    file_extensions = tuple(['.'+s for s in dict['system']['file_extensions'].split(',')])

    if os.path.isfile(filename) and filename.lower().endswith(file_extensions):
      return WordCounter.countfile(locale_ranges, filename)
    elif os.path.isdir(filename):
      return WordCounter.countfolder(locale_ranges, filename,file_extensions)
    else:
      return -1

if __name__ == '__main__':
  if len(sys.argv) !=3:
    print ('Usage: python wordcounter.py FOLDER_OR_FILENAME locale')
    exit()

  print(WordCounter.count())
