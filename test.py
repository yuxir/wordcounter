import unittest
from wordcounter import WordCounter

class CountTest(unittest.TestCase):
  def testFile(self):
    ranges = ('[\u4e00-\u9fff]+')
    self.assertEqual(WordCounter.countfile(ranges,'samples/1.yaml'),6)

  def testFolder(self):
    ranges = ('[\u4e00-\u9fff]+')
    extensions = ('.yaml')
    self.assertEqual(WordCounter.countfolder(ranges,'samples/', extensions),15)

def main():
  unittest.main()

if __name__ == '__main__':
    main()
