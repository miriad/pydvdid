# pydvdid

[![Travis][1]][2]
[![Coveralls][3]][4]
[![Scrutinizer][5]][6]

## Overview

[pydvdid][7] is a pure Python implementation of the Windows API [IDvdInfo2::GetDiscID][8] method, as used by Windows Media Center to compute a 'practically unique' 64-bit [CRC][9] for metadata retrieval. 

## Motivation

I needed a zero-knowledge way to recover some basic information about an inserted DVD or a mounted ISO image, and whilst googling ran across [dvdid][10]. A compiled solution didn't fit with my requirement, so I re-implemented it as a Python module. Kudos go to Christopher Key for originally developing dvdid and documenting the algorithm so thoroughly.

pydvdid is envisaged to be useful for DVD ripping scripts, custom Growl notifications, and media centre related home automation tasks.

## Compatibility

Works for Python versions 2 and 3, from 2.6 through to the nightly build.

## Availability

Get it from PyPI or directly from GitHub.

#### PyPI:

[![PyPI status][11]][12]
[![PyPI version][13]][12]
[![PyPI format][14]][12]
[![PyPI python versions][15]][12]

```sh
pip install pydvdid
```

#### GitHub:

[Releases][16]

## Example

pydvdid has a decidely simple API, with the important bits imported into the package level so they can be conveniently imported directly from the package.

#### Computing a dvdid value

```sh
>>> import pydvdid
>>> crc64 = pydvdid.compute("/mnt/dvd")
>>> str(crc64)
'9376311e277b3e90'
```

#### Using a dvdid value

```sh
>>> import urllib
>>> urllib.urlopen("http://metaservices.windowsmedia.com/pas_dvd_B/template/GetMDRDVDByCRC.xml?CRC={0}".format(crc64)).read()
'<?xml version=\'1.0\' encoding="UTF-8" ?><METADATA xmlns:sql="urn:schemas-microsoft-com:xml-sql">\r\n\t\r\n\t<MDR-DVD><version>4.0</version><dvdTitle>Shrek</dvdTitle><studio></studio><leadPerformer></leadPerformer><actors></actors><director></director><MPAARating>NR</MPAARating><releaseDate>2004 05 11</releaseDate><genre>Children&apos;s/Family</genre><dataProvider>AMG</dataProvider><wmid_dvd>E0F3B718-D539-48E8-A77C-72B71603F38E</wmid_dvd><dv_id>E    50745_1        </dv_id><dataProviderParams>Provider=AMG</dataProviderParams><dataProviderLogo>Provider=AMG</dataProviderLogo><moreInfoParams></moreInfoParams><title><titleNum>1</titleNum><titleTitle>Shrek</titleTitle><studio></studio><director></director><leadPerformer></leadPerformer><actors></actors><MPAARating>NR</MPAARating><genre>Children&apos;s/Family</genre><communityRating></communityRating><chapter><chapterNum>1</chapterNum><chapterTitle>Once Upon a Time (Main Title) [:34]</chapterTitle></chapter><chapter><chapterNum>2</chapterNum><chapterTitle>A Flying Talking Donkey [2:59]</chapterTitle></chapter><chapter><chapterNum>3</chapterNum><chapterTitle>What Are You Doing in My Swamp? [1:22]</chapterTitle></chapter><chapter><chapterNum>4</chapterNum><chapterTitle>Lord Farquaad [1:45]</chapterTitle></chapter><chapter><chapterNum>5</chapterNum><chapterTitle>The Kingdom of DuLoc [1:33]</chapterTitle></chapter><chapter><chapterNum>6</chapterNum><chapterTitle>Ogres Are Like Onions [:19]</chapterTitle></chapter><chapter><chapterNum>7</chapterNum><chapterTitle>The Dragon&apos;s Keep [2:00]</chapterTitle></chapter><chapter><chapterNum>8</chapterNum><chapterTitle>Rescuing the Princess [:31]</chapterTitle></chapter><chapter><chapterNum>9</chapterNum><chapterTitle>Remove Your Helmet [:36]</chapterTitle></chapter><chapter><chapterNum>10</chapterNum><chapterTitle>Campfire [2:22]</chapterTitle></chapter><chapter><chapterNum>11</chapterNum><chapterTitle>Merry Men [1:55]</chapterTitle></chapter><chapter><chapterNum>12</chapterNum><chapterTitle>Weedrat Dinner [1:35]</chapterTitle></chapter><chapter><chapterNum>13</chapterNum><chapterTitle>You Are the Princess [2:36]</chapterTitle></chapter><chapter><chapterNum>14</chapterNum><chapterTitle>The Proposal [:01]</chapterTitle></chapter><chapter><chapterNum>15</chapterNum><chapterTitle>Wedding Preparation [3:03]</chapterTitle></chapter><chapter><chapterNum>16</chapterNum><chapterTitle>That&apos;s What Friends Are For [2:05]</chapterTitle></chapter><chapter><chapterNum>17</chapterNum><chapterTitle>The Wedding [:59]</chapterTitle></chapter><chapter><chapterNum>18</chapterNum><chapterTitle>Love&apos;s True Form [3:19]</chapterTitle></chapter><chapter><chapterNum>19</chapterNum><chapterTitle>I&apos;m a Believer [1:50]</chapterTitle></chapter><chapter><chapterNum>20</chapterNum><chapterTitle>End Credits [:11]</chapterTitle></chapter></title></MDR-DVD>\r\n</METADATA>'
```

## License

[Apache License, Version 2.0][17]

  [1]: https://img.shields.io/travis/sjwood/pydvdid.svg
  [2]: https://travis-ci.org/sjwood/pydvdid
  [3]: https://img.shields.io/coveralls/sjwood/pydvdid.svg
  [4]: https://coveralls.io/r/sjwood/pydvdid
  [5]: https://img.shields.io/scrutinizer/g/sjwood/pydvdid.svg
  [6]: https://scrutinizer-ci.com/g/sjwood/pydvdid
  [7]: https://github.com/sjwood/pydvdid
  [8]: https://msdn.microsoft.com/en-us/library/windows/desktop/dd376453.aspx
  [9]: https://en.wikipedia.org/wiki/Cyclic_redundancy_check
  [10]: http://dvdid.cjkey.org.uk/
  [11]: https://img.shields.io/pypi/status/pydvdid.svg
  [12]: https://pypi.python.org/pypi/pydvdid
  [13]: https://img.shields.io/pypi/v/pydvdid.svg
  [14]: https://img.shields.io/pypi/format/pydvdid.svg
  [15]: https://img.shields.io/pypi/pyversions/pydvdid.svg
  [16]: https://github.com/sjwood/pydvdid/releases
  [17]: https://raw.githubusercontent.com/sjwood/pydvdid/master/LICENSE
