import re
# Most of these are ripped from zamboni for now, ideally we'd like share
# these constants around a little more without having to do this.

APP_GUIDS = {'{aa3c5121-dab2-40e2-81ca-7ea25febc110}': 61,
             '{3550f703-e582-4d05-9a08-453d09bdfdc6}': 18,
             '{92650c4d-4b8e-4d2a-b7eb-24ecf4f6b63a}': 59,
             '{a23983c0-fd0e-11dc-95ff-0800200c9a66}': 60,
             '{ec8030f7-c20a-464f-9b0e-13a3a9e97384}': 1}
ADDON_PREMIUMS = (1, 2)
ADDON_SLUGS_UPDATE = {1: 'extension', 2: 'theme', 3: 'extension', 4: 'search',
                      5: 'item', 6: 'extension', 7: 'plugin', 9: 'persona',
                      11: 'app'}
D2C_MAC_VERSIONS = {1: '4.0', 18: '5.0', 59: '2.1', 60: '11.0'}
PLATFORMS = {u'ALL_mobile': 9, u'WINNT': 5, u'ALL': 1, 'SunOS': 6, u'Maemo': 8,
             u'Linux': 2, u'BSD_OS': 4, u'Darwin': 3, u'Android': 7}

STATUS_NULL = 0
STATUS_UNREVIEWED = 1
STATUS_PENDING = 2
STATUS_NOMINATED = 3
STATUS_PUBLIC = 4
STATUS_DISABLED = 5
STATUS_LISTED = 6
STATUS_BETA = 7
STATUS_LITE = 8
STATUS_LITE_AND_NOMINATED = 9
STATUS_PURGATORY = 10
STATUS_DELETED = 11
STATUS_REJECTED = 12
STATUS_PUBLIC_WAITING = 13


STATUSES_PUBLIC = {'STATUS_PUBLIC': 4, 'STATUS_LITE': 8,
                   'STATUS_LITE_AND_NOMINATED': 9}

VERSION_BETA = re.compile('(a|alpha|b|beta|pre|rc)\d*$')
WATERMARK_KEYS = ('purchaser', 'purchaser-hash')
