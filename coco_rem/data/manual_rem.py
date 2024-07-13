"""
Few instances in COCO are covered by multiple overlapping masks. For example,
see "couch" and "chair" - https://cocodataset.org/#explore?id=131927 .
Merging (COCO + LVIS) also adds some duplicate instances. We manually examine
instance pairs with IOU > 0.8 and choose to remove some, listed below.

Inline comments below are formatted as "category1 -> category2", denoting that
the listed mask is labeled "category1", which we remove in favor of a more
accurate "category2" mask already present in COCO JSON, at the same location.
"""

# fmt: off
INSTANCES_TO_REMOVE = [
    {"image_id": 1000, "source": "lvis", "source_id": 36623},      # backpack -> handbag
    {"image_id": 1000, "source": "lvis", "source_id": 36622},      # backpack -> handbag
    {"image_id": 2157, "source": "lvis", "source_id": 20375},      # cup -> wine glass
    {"image_id": 2157, "source": "lvis", "source_id": 20376},      # cup -> wine glass
    {"image_id": 2157, "source": "lvis", "source_id": 20377},      # cup -> wine glass
    {"image_id": 2157, "source": "lvis", "source_id": 20378},      # cup -> wine glass
    {"image_id": 2157, "source": "lvis", "source_id": 20380},      # cup -> wine glass
    {"image_id": 2157, "source": "lvis", "source_id": 20381},      # cup -> wine glass
    {"image_id": 2157, "source": "lvis", "source_id": 20382},      # cup -> wine glass
    {"image_id": 2157, "source": "lvis", "source_id": 20383},      # cup -> wine glass
    {"image_id": 2685, "source": "lvis", "source_id": 92393},      # bottle -> bottle
    {"image_id": 6723, "source": "coco", "source_id": 167862},     # bus -> truck
    {"image_id": 9590, "source": "coco", "source_id": 1885626},    # cup -> bowl
    {"image_id": 9891, "source": "lvis", "source_id": 27273},      # suitcase -> backpack
    {"image_id": 9914, "source": "coco", "source_id": 1921713},    # hot dog -> sandwich
    {"image_id": 15335, "source": "lvis", "source_id": 6689},      # bench -> couch
    {"image_id": 16228, "source": "coco", "source_id": 1739202},   # person -> person
    {"image_id": 18380, "source": "coco", "source_id": 2183182},   # wine glass -> cup
    {"image_id": 18380, "source": "coco", "source_id": 703843},    # spoon -> fork
    {"image_id": 18837, "source": "lvis", "source_id": 48530},     # car -> truck
    {"image_id": 20553, "source": "coco", "source_id": 1992825},   # vase -> bottle
    {"image_id": 22192, "source": "coco", "source_id": 1611095},   # bed -> X (not visible)
    {"image_id": 23023, "source": "lvis", "source_id": 16814},     # suitcase -> handbag
    {"image_id": 26204, "source": "lvis", "source_id": 34121},     # car -> truck
    {"image_id": 26204, "source": "lvis", "source_id": 34126},     # car -> bus
    {"image_id": 26204, "source": "lvis", "source_id": 34127},     # car -> truck
    {"image_id": 32941, "source": "coco", "source_id": 1373021},   # truck -> car
    {"image_id": 35682, "source": "coco", "source_id": 1089333},   # cake -> donut
    {"image_id": 35682, "source": "coco", "source_id": 1927521},   # cake -> donut
    {"image_id": 38678, "source": "coco", "source_id": 1573660},   # donut -> sandwich
    {"image_id": 39769, "source": "coco", "source_id": 1612051},   # bed -> couch
    {"image_id": 43314, "source": "coco", "source_id": 524440},    # person -> person
    {"image_id": 44590, "source": "lvis", "source_id": 45054},     # truck -> car
    {"image_id": 54967, "source": "lvis", "source_id": 30236},     # car -> bus
    {"image_id": 57597, "source": "coco", "source_id": 2052603},   # truck -> car
    {"image_id": 57597, "source": "coco", "source_id": 1799084},   # truck -> car
    {"image_id": 60449, "source": "coco", "source_id": 1942577},   # chair -> couch
    {"image_id": 61171, "source": "lvis", "source_id": 37661},     # horse -> cow
    {"image_id": 61171, "source": "lvis", "source_id": 37662},     # horse -> cow
    {"image_id": 61960, "source": "coco", "source_id": 315132},    # bed -> bed
    {"image_id": 61960, "source": "coco", "source_id": 1957837},   # bed -> bed
    {"image_id": 63047, "source": "coco", "source_id": 1726220},   # person -> person
    {"image_id": 66817, "source": "lvis", "source_id": 12974},     # fork -> spoon
    {"image_id": 66817, "source": "lvis", "source_id": 12975},     # fork -> spoon
    {"image_id": 67213, "source": "lvis", "source_id": 12782},     # truck -> car
    {"image_id": 67213, "source": "lvis", "source_id": 12783},     # truck -> car
    {"image_id": 67213, "source": "lvis", "source_id": 12784},     # truck -> car
    {"image_id": 67616, "source": "lvis", "source_id": 45910},     # car -> truck
    {"image_id": 70048, "source": "coco", "source_id": 1879073},   # cup -> bowl
    {"image_id": 73702, "source": "coco", "source_id": 1420481},   # backpack -> handbag
    {"image_id": 74256, "source": "coco", "source_id": 247738},    # bus -> train
    {"image_id": 76417, "source": "coco", "source_id": 1796674},   # truck -> car
    {"image_id": 78266, "source": "coco", "source_id": 1051621},   # orange -> apple
    {"image_id": 84362, "source": "coco", "source_id": 1932147},   # chair -> couch
    {"image_id": 84752, "source": "lvis", "source_id": 45072},     # car -> truck
    {"image_id": 84752, "source": "lvis", "source_id": 45080},     # car -> truck
    {"image_id": 84752, "source": "lvis", "source_id": 45081},     # car -> truck
    {"image_id": 86220, "source": "coco", "source_id": 268029},    # bus -> train
    {"image_id": 89556, "source": "coco", "source_id": 2052646},   # truck -> car
    {"image_id": 91500, "source": "coco", "source_id": 2215190},   # cup -> bowl
    {"image_id": 91779, "source": "coco", "source_id": 2217799},   # sandwich -> hot dog
    {"image_id": 91779, "source": "lvis", "source_id": 20468},     # cup -> bowl
    {"image_id": 92660, "source": "coco", "source_id": 2101064},   # cup -> bowl
    {"image_id": 92939, "source": "coco", "source_id": 1505011},   # cup -> wine glass
    {"image_id": 93261, "source": "coco", "source_id": 1721168},   # person -> person
    {"image_id": 95786, "source": "coco", "source_id": 676406},    # cup -> vase
    {"image_id": 97337, "source": "coco", "source_id": 105448},    # chair -> couch
    {"image_id": 99428, "source": "coco", "source_id": 326781},    # cell phone -> remote
    {"image_id": 100274, "source": "coco", "source_id": 1371413},  # truck -> car
    {"image_id": 113589, "source": "coco", "source_id": 1072662},  # pizza -> sandwich
    {"image_id": 115245, "source": "lvis", "source_id": 26043},    # suitcase -> backpack
    {"image_id": 116208, "source": "coco", "source_id": 678620},   # cup -> wine glass
    {"image_id": 116362, "source": "lvis", "source_id": 30546},    # carrot -> apple
    {"image_id": 116479, "source": "coco", "source_id": 1936804},  # chair -> couch
    {"image_id": 118367, "source": "coco", "source_id": 283},      # hot dog -> sandwich
    {"image_id": 121506, "source": "coco", "source_id": 1965018},  # dining table -> bench
    {"image_id": 121506, "source": "coco", "source_id": 2120806},  # chair -> bench
    {"image_id": 122166, "source": "coco", "source_id": 2052505},  # truck -> car
    {"image_id": 122166, "source": "coco", "source_id": 2052530},  # truck -> car
    {"image_id": 124277, "source": "coco", "source_id": 132335},   # car -> truck
    {"image_id": 124277, "source": "coco", "source_id": 1779363},  # car -> truck
    {"image_id": 124798, "source": "coco", "source_id": 397357},   # truck -> car
    {"image_id": 125778, "source": "lvis", "source_id": 22165},    # vase -> bottle
    {"image_id": 125778, "source": "lvis", "source_id": 22166},    # vase -> bottle
    {"image_id": 125778, "source": "coco", "source_id": 84523},    # bottle -> vase
    {"image_id": 136715, "source": "coco", "source_id": 139124},   # car -> truck
    {"image_id": 137727, "source": "coco", "source_id": 2176278},  # handbag -> backpack
    {"image_id": 137727, "source": "coco", "source_id": 2176462},  # handbag -> backpack
    {"image_id": 139099, "source": "coco", "source_id": 1422982},  # backpack -> handbag
    {"image_id": 139684, "source": "lvis", "source_id": 1314},     # bottle -> vase
    {"image_id": 140583, "source": "coco", "source_id": 1820769},  # cow -> sheep
    {"image_id": 140583, "source": "coco", "source_id": 1820797},  # cow -> sheep
    {"image_id": 141597, "source": "lvis", "source_id": 31324},    # car -> truck
    {"image_id": 142472, "source": "coco", "source_id": 2052117},  # truck -> car
    {"image_id": 142585, "source": "lvis", "source_id": 28039},    # car -> bus
    {"image_id": 142585, "source": "coco", "source_id": 1797641},  # truck -> car
    {"image_id": 142790, "source": "coco", "source_id": 617671},   # snowboard -> skis
    {"image_id": 144300, "source": "coco", "source_id": 1795182},  # bus -> truck
    {"image_id": 144300, "source": "coco", "source_id": 1795279},  # bus -> truck
    {"image_id": 144706, "source": "coco", "source_id": 1369864},  # truck -> car
    {"image_id": 147338, "source": "coco", "source_id": 2170286},  # car -> truck
    {"image_id": 147518, "source": "coco", "source_id": 1623801},  # toilet -> toilet
    {"image_id": 150224, "source": "coco", "source_id": 2073828},  # backpack -> handbag
    {"image_id": 150417, "source": "coco", "source_id": 1877869},  # cup -> bowl
    {"image_id": 151820, "source": "lvis", "source_id": 3716},     # cup -> wine glass
    {"image_id": 151820, "source": "lvis", "source_id": 3717},     # cup -> wine glass
    {"image_id": 151820, "source": "lvis", "source_id": 3719},     # cup -> wine glass
    {"image_id": 151820, "source": "lvis", "source_id": 3720},     # cup -> wine glass
    {"image_id": 153011, "source": "lvis", "source_id": 29111},    # car -> truck
    {"image_id": 153011, "source": "lvis", "source_id": 29112},    # car -> truck
    {"image_id": 153011, "source": "coco", "source_id": 365762},   # bus -> truck
    {"image_id": 153527, "source": "coco", "source_id": 1950631},  # couch -> chair
    {"image_id": 153529, "source": "lvis", "source_id": 18278},    # backpack -> handbag
    {"image_id": 153529, "source": "lvis", "source_id": 18298},    # suitcase -> backpack
    {"image_id": 153529, "source": "lvis", "source_id": 18280},    # backpack -> suitcase
    {"image_id": 153529, "source": "lvis", "source_id": 18281},    # backpack -> suitcase
    {"image_id": 157601, "source": "coco", "source_id": 760},      # hot dog -> sandwich
    {"image_id": 158744, "source": "coco", "source_id": 1933050},  # chair -> couch
    {"image_id": 158744, "source": "coco", "source_id": 2190184},  # chair -> couch
    {"image_id": 161128, "source": "coco", "source_id": 2052459},  # truck -> bus
    {"image_id": 162035, "source": "lvis", "source_id": 903},      # bear -> teddy bear
    {"image_id": 162035, "source": "lvis", "source_id": 904},      # bear -> teddy bear
    {"image_id": 165681, "source": "lvis", "source_id": 42140},    # motorcycle -> motorcycle
    {"image_id": 165681, "source": "coco", "source_id": 2171910},  # truck -> car
    {"image_id": 166391, "source": "lvis", "source_id": 21022},    # car -> truck
    {"image_id": 166391, "source": "lvis", "source_id": 21023},    # car -> truck
    {"image_id": 166391, "source": "lvis", "source_id": 21025},    # car -> truck
    {"image_id": 166391, "source": "lvis", "source_id": 21029},    # car -> truck
    {"image_id": 166391, "source": "lvis", "source_id": 21032},    # car -> truck
    {"image_id": 166391, "source": "lvis", "source_id": 21033},    # car -> truck
    {"image_id": 166391, "source": "lvis", "source_id": 21037},    # car -> truck
    {"image_id": 166747, "source": "coco", "source_id": 1302749},  # person -> person
    {"image_id": 168337, "source": "coco", "source_id": 1168521},  # backpack -> suitcase
    {"image_id": 169076, "source": "coco", "source_id": 1816275},  # cat -> dog
    {"image_id": 169996, "source": "lvis", "source_id": 41500},    # car -> truck
    {"image_id": 171757, "source": "coco", "source_id": 1957225},  # bed -> couch
    {"image_id": 172595, "source": "coco", "source_id": 2073019},  # backpack -> handbag
    {"image_id": 174482, "source": "coco", "source_id": 1374126},  # truck -> car
    {"image_id": 179392, "source": "coco", "source_id": 11242},    # dog -> cat
    {"image_id": 180296, "source": "lvis", "source_id": 15755},    # suitcase -> backpack
    {"image_id": 181753, "source": "lvis", "source_id": 32644},    # vase -> bowl
    {"image_id": 181753, "source": "coco", "source_id": 114563},   # couch -> chair
    {"image_id": 181753, "source": "coco", "source_id": 2098799},  # cup -> bowl
    {"image_id": 182611, "source": "coco", "source_id": 2100899},  # cup -> bowl
    {"image_id": 182611, "source": "coco", "source_id": 1088383},  # cake -> sandwich
    {"image_id": 183246, "source": "coco", "source_id": 1357979},  # car -> truck
    {"image_id": 183965, "source": "coco", "source_id": 1068719},  # hot dog -> sandwich
    {"image_id": 184324, "source": "coco", "source_id": 1364448},  # bus -> truck
    {"image_id": 184611, "source": "lvis", "source_id": 5305},     # suitcase -> handbag
    {"image_id": 189475, "source": "lvis", "source_id": 47620},    # fork -> knife
    {"image_id": 189752, "source": "coco", "source_id": 2097457},  # wine glass -> cup
    {"image_id": 192871, "source": "lvis", "source_id": 27044},    # orange -> apple
    {"image_id": 193162, "source": "coco", "source_id": 61683},    # sheep -> dog
    {"image_id": 194832, "source": "coco", "source_id": 116970},   # couch -> bench
    {"image_id": 194832, "source": "coco", "source_id": 114768},   # couch -> bench
    {"image_id": 194832, "source": "coco", "source_id": 1933922},  # chair -> bench
    {"image_id": 194832, "source": "coco", "source_id": 1934615},  # chair -> bench
    {"image_id": 194832, "source": "coco", "source_id": 1943732},  # chair -> bench
    {"image_id": 194832, "source": "coco", "source_id": 1943324},  # chair -> bench
    {"image_id": 194832, "source": "coco", "source_id": 1946175},  # chair -> bench
    {"image_id": 194832, "source": "coco", "source_id": 1946593},  # chair -> bench
    {"image_id": 194832, "source": "coco", "source_id": 1947172},  # chair -> bench
    {"image_id": 194832, "source": "coco", "source_id": 2223617},  # couch -> bench
    {"image_id": 195754, "source": "coco", "source_id": 116193},   # couch -> chair
    {"image_id": 199395, "source": "coco", "source_id": 1300923},  # person -> person
    {"image_id": 201426, "source": "coco", "source_id": 1930281},  # chair -> chair
    {"image_id": 203294, "source": "coco", "source_id": 1824723},  # backpack -> handbag
    {"image_id": 205514, "source": "coco", "source_id": 114482},   # couch -> chair
    {"image_id": 205514, "source": "coco", "source_id": 2224329},  # couch -> chair
    {"image_id": 209530, "source": "coco", "source_id": 1497631},  # wine glass -> cup
    {"image_id": 210230, "source": "coco", "source_id": 1065015},  # carrot -> hot dog
    {"image_id": 210230, "source": "coco", "source_id": 2221243},  # hot dog -> hot dog
    {"image_id": 210520, "source": "coco", "source_id": 680670},   # cup -> X (it's a candle)
    {"image_id": 218091, "source": "coco", "source_id": 2223835},  # couch -> chair
    {"image_id": 221754, "source": "coco", "source_id": 1373849},  # truck -> car
    {"image_id": 222094, "source": "coco", "source_id": 1194683},  # car -> truck
    {"image_id": 222094, "source": "coco", "source_id": 1338481},  # car -> truck
    {"image_id": 222299, "source": "coco", "source_id": 1648151},  # book -> laptop
    {"image_id": 227044, "source": "coco", "source_id": 90507},    # bottle -> cup
    {"image_id": 227399, "source": "lvis", "source_id": 1205},     # backpack -> handbag
    {"image_id": 227399, "source": "lvis", "source_id": 1206},     # backpack -> suitcase
    {"image_id": 227491, "source": "coco", "source_id": 1080415},  # donut -> sandwich
    {"image_id": 228942, "source": "coco", "source_id": 1247255},  # person -> person
    {"image_id": 229311, "source": "coco", "source_id": 2214914},  # cup -> vase
    {"image_id": 229659, "source": "coco", "source_id": 1625045},  # tv -> laptop
    {"image_id": 230993, "source": "coco", "source_id": 1171589},  # backpack -> handbag
    {"image_id": 231097, "source": "coco", "source_id": 2100333},  # cup -> bowl
    {"image_id": 231831, "source": "coco", "source_id": 1635740},  # cell phone -> remote
    {"image_id": 233567, "source": "lvis", "source_id": 31813},    # sheep -> X (it's goat)
    {"image_id": 233567, "source": "coco", "source_id": 1407965},  # cow -> X (it's goat)
    {"image_id": 236721, "source": "lvis", "source_id": 28555},    # cup -> bowl
    {"image_id": 237517, "source": "coco", "source_id": 705060},   # spoon -> fork
    {"image_id": 239627, "source": "coco", "source_id": 673788},   # cup -> bowl
    {"image_id": 239627, "source": "coco", "source_id": 1882508},  # cup -> bowl
    {"image_id": 239627, "source": "coco", "source_id": 714390},   # bowl -> cup
    {"image_id": 251119, "source": "coco", "source_id": 2221191},  # hot dog -> sandwich
    {"image_id": 253742, "source": "coco", "source_id": 2211271},  # handbag -> backpack
    {"image_id": 253742, "source": "lvis", "source_id": 10444},    # backpack -> handbag
    {"image_id": 255917, "source": "coco", "source_id": 2052814},  # truck -> car
    {"image_id": 260470, "source": "coco", "source_id": 1925566},  # donut -> cake
    {"image_id": 260470, "source": "coco", "source_id": 1925325},  # donut -> cake
    {"image_id": 263966, "source": "coco", "source_id": 1817770},  # sheep -> horse
    {"image_id": 266981, "source": "coco", "source_id": 1350827},  # car -> car
    {"image_id": 268378, "source": "coco", "source_id": 1878436},  # cup -> wine glass
    {"image_id": 268378, "source": "coco", "source_id": 2214979},  # cup -> wine glass
    {"image_id": 273711, "source": "coco", "source_id": 2215425},  # cup -> bowl
    {"image_id": 273711, "source": "coco", "source_id": 1049666},  # apple -> X (it's pear)
    {"image_id": 273711, "source": "coco", "source_id": 2231095},  # orange -> X (it's pear)
    {"image_id": 275198, "source": "coco", "source_id": 1892966},  # knife -> knife
    {"image_id": 275198, "source": "coco", "source_id": 708186},   # spoon -> fork
    {"image_id": 276024, "source": "lvis", "source_id": 1167},     # horse -> cow
    {"image_id": 276024, "source": "lvis", "source_id": 1168},     # horse -> cow
    {"image_id": 276720, "source": "coco", "source_id": 1373202},  # truck -> car
    {"image_id": 276720, "source": "coco", "source_id": 1373507},  # truck -> car
    {"image_id": 277051, "source": "coco", "source_id": 2230033},  # bird -> bird
    {"image_id": 277689, "source": "coco", "source_id": 1884804},  # cup -> wine glass
    {"image_id": 277689, "source": "coco", "source_id": 1884015},  # cup -> wine glass
    {"image_id": 277689, "source": "coco", "source_id": 1881437},  # cup -> wine glass
    {"image_id": 279730, "source": "coco", "source_id": 2219923},  # hot dog -> sandwich
    {"image_id": 283717, "source": "coco", "source_id": 1641448},  # oven -> microwave
    {"image_id": 286908, "source": "lvis", "source_id": 35273},    # bowl -> cup
    {"image_id": 287291, "source": "coco", "source_id": 1372825},  # truck -> car
    {"image_id": 288584, "source": "coco", "source_id": 1417931},  # backpack -> handbag
    {"image_id": 291791, "source": "coco", "source_id": 1169272},  # backpack -> handbag
    {"image_id": 292456, "source": "coco", "source_id": 1445962},  # suitcase -> handbag
    {"image_id": 293804, "source": "coco", "source_id": 99325},    # couch -> chair
    {"image_id": 293858, "source": "coco", "source_id": 2220396},  # hot dog -> sandwich
    {"image_id": 297085, "source": "coco", "source_id": 34564},    # tv -> tv
    {"image_id": 300276, "source": "coco", "source_id": 1958857},  # dining table -> bench
    {"image_id": 301135, "source": "lvis", "source_id": 16960},    # backpack -> handbag
    {"image_id": 301135, "source": "lvis", "source_id": 16962},    # backpack -> handbag
    {"image_id": 303713, "source": "coco", "source_id": 1432692},  # handbag -> backpack
    {"image_id": 304365, "source": "coco", "source_id": 1446883},  # suitcase -> backpack
    {"image_id": 304984, "source": "coco", "source_id": 1577273},  # cake -> sandwich
    {"image_id": 309391, "source": "lvis", "source_id": 5982},     # car -> bus
    {"image_id": 309467, "source": "lvis", "source_id": 37560},    # skis -> skis
    {"image_id": 309655, "source": "coco", "source_id": 1848565},  # skis -> snowboard
    {"image_id": 310072, "source": "coco", "source_id": 1368385},  # truck -> car
    {"image_id": 310072, "source": "coco", "source_id": 1369143},  # truck -> car
    {"image_id": 310200, "source": "coco", "source_id": 1895705},  # spoon -> fork
    {"image_id": 312237, "source": "coco", "source_id": 1863567},  # surfboard -> kite
    {"image_id": 313034, "source": "coco", "source_id": 91374},    # bottle -> vase
    {"image_id": 313588, "source": "lvis", "source_id": 33723},    # car -> truck
    {"image_id": 316666, "source": "lvis", "source_id": 25026},    # vase -> bottle
    {"image_id": 316666, "source": "coco", "source_id": 2101640},  # cup -> vase
    {"image_id": 319696, "source": "lvis", "source_id": 6122},     # teddy bear -> bear
    {"image_id": 319935, "source": "coco", "source_id": 99646},    # couch -> chair
    {"image_id": 322429, "source": "coco", "source_id": 1515846},  # cup -> vase
    {"image_id": 322429, "source": "coco", "source_id": 1887647},  # cup -> vase
    {"image_id": 322429, "source": "lvis", "source_id": 15500},    # vase -> cup
    {"image_id": 322429, "source": "lvis", "source_id": 15505},    # vase -> cup
    {"image_id": 322574, "source": "coco", "source_id": 717071},   # bowl -> cup
    {"image_id": 326082, "source": "lvis", "source_id": 3525},     # couch -> chair
    {"image_id": 326627, "source": "coco", "source_id": 1386294},  # traffic light -> traffic light
    {"image_id": 329319, "source": "coco", "source_id": 573846},   # bench -> chair
    {"image_id": 329456, "source": "coco", "source_id": 1080280},  # donut -> sandwich
    {"image_id": 334309, "source": "coco", "source_id": 2217927},  # sandwich -> pizza
    {"image_id": 334417, "source": "coco", "source_id": 310316},   # sandwich -> pizza
    {"image_id": 334555, "source": "lvis", "source_id": 24813},    # car -> truck
    {"image_id": 336053, "source": "coco", "source_id": 1507330},  # cup -> wine glass
    {"image_id": 336053, "source": "coco", "source_id": 1513790},  # cup -> wine glass
    {"image_id": 336053, "source": "coco", "source_id": 1881066},  # cup -> wine glass
    {"image_id": 336232, "source": "coco", "source_id": 1364524},  # bus -> truck
    {"image_id": 338560, "source": "lvis", "source_id": 3551},     # truck -> car
    {"image_id": 341469, "source": "coco", "source_id": 1447632},  # suitcase -> handbag
    {"image_id": 341469, "source": "coco", "source_id": 1446679},  # suitcase -> handbag
    {"image_id": 343218, "source": "coco", "source_id": 1460435},  # sports ball -> sports ball
    {"image_id": 344888, "source": "coco", "source_id": 2042747},  # car -> truck
    {"image_id": 346703, "source": "coco", "source_id": 2183585},  # wine glass -> cup
    {"image_id": 349860, "source": "lvis", "source_id": 36505},    # truck -> car
    {"image_id": 350122, "source": "coco", "source_id": 1366823},  # train -> bus
    {"image_id": 351530, "source": "coco", "source_id": 1597383},  # chair -> bench
    {"image_id": 351530, "source": "coco", "source_id": 1601162},  # chair -> bench
    {"image_id": 356427, "source": "coco", "source_id": 1176682},  # handbag -> backpack
    {"image_id": 356612, "source": "lvis", "source_id": 32203},    # bus -> truck
    {"image_id": 359833, "source": "coco", "source_id": 1911732},  # orange -> apple
    {"image_id": 361103, "source": "coco", "source_id": 1433565},  # handbag -> backpack
    {"image_id": 361238, "source": "coco", "source_id": 1075255},  # pizza -> pizza
    {"image_id": 361238, "source": "coco", "source_id": 1075580},  # pizza -> pizza
    {"image_id": 361551, "source": "lvis", "source_id": 8546},     # suitcase -> backpack
    {"image_id": 361551, "source": "lvis", "source_id": 8555},     # backpack -> suitcase
    {"image_id": 361551, "source": "lvis", "source_id": 8556},     # backpack -> suitcase
    {"image_id": 361551, "source": "lvis", "source_id": 8557},     # backpack -> suitcase
    {"image_id": 361551, "source": "lvis", "source_id": 8560},     # backpack -> suitcase
    {"image_id": 361551, "source": "lvis", "source_id": 8561},     # backpack -> suitcase
    {"image_id": 361919, "source": "coco", "source_id": 1302077},  # person -> person
    {"image_id": 367082, "source": "coco", "source_id": 1950811},  # couch -> chair
    {"image_id": 367386, "source": "coco", "source_id": 1633257},  # remote -> remote
    {"image_id": 368335, "source": "coco", "source_id": 1369353},  # truck -> car
    {"image_id": 368684, "source": "coco", "source_id": 124155},   # tv -> laptop
    {"image_id": 369812, "source": "lvis", "source_id": 35571},    # car -> truck
    {"image_id": 370486, "source": "lvis", "source_id": 19468},    # handbag -> backpack
    {"image_id": 373353, "source": "coco", "source_id": 1827613},  # backpack -> handbag
    {"image_id": 375078, "source": "coco", "source_id": 1485363},  # bottle -> vase
    {"image_id": 375278, "source": "coco", "source_id": 49062},    # cat -> dog
    {"image_id": 377368, "source": "coco", "source_id": 1960233},  # dining table -> bench
    {"image_id": 377882, "source": "coco", "source_id": 1862908},  # surfboard -> boat
    {"image_id": 377882, "source": "coco", "source_id": 2181838},  # surfboard -> boat
    {"image_id": 378244, "source": "coco", "source_id": 618088},   # snowboard -> skis
    {"image_id": 379476, "source": "coco", "source_id": 2227124},  # dining table -> dining table
    {"image_id": 381971, "source": "coco", "source_id": 1178795},  # handbag -> backpack
    {"image_id": 393014, "source": "coco", "source_id": 2221181},  # hot dog -> sandwich
    {"image_id": 393014, "source": "coco", "source_id": 2221544},  # hot dog -> sandwich
    {"image_id": 394677, "source": "lvis", "source_id": 31586},    # backpack -> handbag
    {"image_id": 394677, "source": "lvis", "source_id": 31584},    # backpack -> handbag
    {"image_id": 394677, "source": "lvis", "source_id": 31583},    # backpack -> handbag
    {"image_id": 394677, "source": "lvis", "source_id": 31585},    # backpack -> handbag
    {"image_id": 396338, "source": "lvis", "source_id": 30399},    # truck -> car
    {"image_id": 396338, "source": "coco", "source_id": 1833047},  # handbag -> backpack
    {"image_id": 401991, "source": "coco", "source_id": 49934},    # cat -> dog
    {"image_id": 402433, "source": "coco", "source_id": 1073961},  # pizza -> pizza
    {"image_id": 403817, "source": "coco", "source_id": 1968569},  # tv -> laptop
    {"image_id": 404678, "source": "coco", "source_id": 112403},   # couch -> bench
    {"image_id": 414034, "source": "coco", "source_id": 1880459},  # cup -> bottle
    {"image_id": 414510, "source": "coco", "source_id": 1828804},  # backpack -> handbag
    {"image_id": 416104, "source": "coco", "source_id": 82046},    # bottle -> bottle
    {"image_id": 416104, "source": "lvis", "source_id": 33218},    # chair -> chair
    {"image_id": 419601, "source": "coco", "source_id": 319432},   # bed -> couch
    {"image_id": 419601, "source": "coco", "source_id": 1951465},  # couch -> chair
    {"image_id": 425221, "source": "coco", "source_id": 1594339},  # chair -> bench
    {"image_id": 429109, "source": "lvis", "source_id": 29774},    # bus -> train
    {"image_id": 429281, "source": "coco", "source_id": 1907763},  # apple -> orange
    {"image_id": 431568, "source": "coco", "source_id": 1077195},  # pizza -> pizza
    {"image_id": 431568, "source": "coco", "source_id": 1076279},  # pizza -> pizza
    {"image_id": 435081, "source": "lvis", "source_id": 33753},    # fork -> spoon
    {"image_id": 435206, "source": "coco", "source_id": 580498},   # elephant -> cow
    {"image_id": 436883, "source": "coco", "source_id": 1798647},  # truck -> car
    {"image_id": 441247, "source": "coco", "source_id": 1932251},  # chair -> couch
    {"image_id": 441247, "source": "coco", "source_id": 1949954},  # couch -> chair
    {"image_id": 441247, "source": "coco", "source_id": 1981230},  # oven -> microwave
    {"image_id": 441586, "source": "lvis", "source_id": 21105},    # bicycle -> motorcycle
    {"image_id": 442456, "source": "coco", "source_id": 354441},   # car -> truck
    {"image_id": 447342, "source": "coco", "source_id": 2051709},  # truck -> bus
    {"image_id": 449190, "source": "coco", "source_id": 669853},   # cup -> bowl
    {"image_id": 449432, "source": "lvis", "source_id": 12956},    # backpack -> handbag
    {"image_id": 451571, "source": "coco", "source_id": 1554556},  # sandwich -> pizza
    {"image_id": 453722, "source": "coco", "source_id": 115945},   # couch -> chair
    {"image_id": 454404, "source": "coco", "source_id": 1584753},  # chair -> bench
    {"image_id": 455937, "source": "coco", "source_id": 1445133},  # suitcase -> handbag
    {"image_id": 455937, "source": "coco", "source_id": 112741},   # couch -> chair
    {"image_id": 458255, "source": "coco", "source_id": 1956682},  # bed -> bed
    {"image_id": 462904, "source": "coco", "source_id": 1955551},  # potted plant -> potted plant
    {"image_id": 463542, "source": "coco", "source_id": 2212679},  # skis -> snowboard
    {"image_id": 465806, "source": "coco", "source_id": 1878076},  # cup -> bowl
    {"image_id": 465806, "source": "coco", "source_id": 671068},   # cup -> bowl
    {"image_id": 467776, "source": "lvis", "source_id": 24742},    # cow -> sheep
    {"image_id": 467776, "source": "lvis", "source_id": 24744},    # cow -> sheep
    {"image_id": 468505, "source": "coco", "source_id": 1951491},  # couch -> bench
    {"image_id": 469067, "source": "coco", "source_id": 329572},   # cell phone -> remote
    {"image_id": 470773, "source": "coco", "source_id": 1897829},  # spoon -> knife
    {"image_id": 470924, "source": "coco", "source_id": 667285},   # wine glass -> cup
    {"image_id": 472678, "source": "coco", "source_id": 2135470},  # remote -> cell phone
    {"image_id": 474164, "source": "lvis", "source_id": 44412},    # truck -> car
    {"image_id": 475387, "source": "coco", "source_id": 1175309},  # handbag -> backpack
    {"image_id": 476704, "source": "lvis", "source_id": 47421},    # car -> truck
    {"image_id": 476704, "source": "lvis", "source_id": 47423},    # car -> bus
    {"image_id": 478721, "source": "coco", "source_id": 1374232},  # truck -> car
    {"image_id": 479248, "source": "coco", "source_id": 1994680},  # vase -> cup
    {"image_id": 479248, "source": "coco", "source_id": 1994741},  # vase -> cup
    {"image_id": 482275, "source": "coco", "source_id": 673126},   # cup -> wine glass
    {"image_id": 484978, "source": "coco", "source_id": 1886211},  # cup -> bowl
    {"image_id": 488166, "source": "coco", "source_id": 2218998},  # sandwich -> pizza
    {"image_id": 488673, "source": "coco", "source_id": 2213841},  # cup -> wine glass
    {"image_id": 490936, "source": "coco", "source_id": 1360837},  # motorcycle -> motorcycle
    {"image_id": 491497, "source": "coco", "source_id": 2223647},  # couch -> chair
    {"image_id": 492077, "source": "lvis", "source_id": 47104},    # suitcase -> backpack
    {"image_id": 492758, "source": "coco", "source_id": 1950244},  # couch -> chair
    {"image_id": 498286, "source": "coco", "source_id": 1369213},  # truck -> car
    {"image_id": 500257, "source": "coco", "source_id": 1416660},  # backpack -> suitcase
    {"image_id": 504074, "source": "coco", "source_id": 1938151},  # chair -> chair
    {"image_id": 509824, "source": "lvis", "source_id": 38728},    # vase -> bowl
    {"image_id": 511599, "source": "coco", "source_id": 1415626},  # backpack -> handbag
    {"image_id": 512564, "source": "lvis", "source_id": 50588},    # bus -> truck
    {"image_id": 513688, "source": "coco", "source_id": 1961842},  # dining table -> X (it's a desk)
    {"image_id": 514376, "source": "lvis", "source_id": 11057},    # car -> bus
    {"image_id": 515025, "source": "lvis", "source_id": 30272},    # car -> truck
    {"image_id": 515025, "source": "lvis", "source_id": 30273},    # car -> truck
    {"image_id": 517056, "source": "coco", "source_id": 1520087},  # fork -> knife
    {"image_id": 520264, "source": "coco", "source_id": 96007},    # bottle -> bottle
    {"image_id": 520707, "source": "lvis", "source_id": 29734},    # suitcase -> handbag
    {"image_id": 520707, "source": "lvis", "source_id": 29735},    # suitcase -> handbag
    {"image_id": 520707, "source": "lvis", "source_id": 29737},    # suitcase -> handbag
    {"image_id": 522007, "source": "coco", "source_id": 2213886},  # cup -> bowl
    {"image_id": 524850, "source": "coco", "source_id": 1829085},  # backpack -> handbag
    {"image_id": 524850, "source": "coco", "source_id": 2081699},  # suitcase -> handbag
    {"image_id": 524850, "source": "coco", "source_id": 2212226},  # handbag -> backpack
    {"image_id": 525083, "source": "coco", "source_id": 2225240},  # couch -> chair
    {"image_id": 530836, "source": "lvis", "source_id": 5131},     # bowl -> cup
    {"image_id": 532901, "source": "lvis", "source_id": 25501},    # bed -> couch
    {"image_id": 542423, "source": "coco", "source_id": 1177265},  # handbag -> backpack
    {"image_id": 546964, "source": "coco", "source_id": 2167590},  # person -> person
    {"image_id": 548246, "source": "coco", "source_id": 2088849},  # sports ball -> sports ball
    {"image_id": 551822, "source": "lvis", "source_id": 48781},    # cup -> bowl
    {"image_id": 552612, "source": "coco", "source_id": 2177007},  # sheep -> sheep
    {"image_id": 554291, "source": "coco", "source_id": 1817465},  # dog -> cat
    {"image_id": 554291, "source": "coco", "source_id": 1931767},  # chair -> couch
    {"image_id": 555050, "source": "coco", "source_id": 98245},    # couch -> chair
    {"image_id": 555050, "source": "coco", "source_id": 116550},   # couch -> chair
    {"image_id": 559543, "source": "coco", "source_id": 1580399},  # chair -> couch
    {"image_id": 565012, "source": "coco", "source_id": 1372614},  # truck -> car
    {"image_id": 565853, "source": "coco", "source_id": 2077624},  # handbag -> backpack
    {"image_id": 567640, "source": "coco", "source_id": 1771662},  # car -> truck
    {"image_id": 568584, "source": "lvis", "source_id": 2135},     # couch -> chair
    {"image_id": 571313, "source": "coco", "source_id": 2228054},  # microwave -> tv
    {"image_id": 572408, "source": "coco", "source_id": 2068090},  # sheep -> cow
    {"image_id": 572678, "source": "coco", "source_id": 108266},   # chair -> couch
    {"image_id": 573094, "source": "coco", "source_id": 113392},   # couch -> chair
    {"image_id": 577932, "source": "coco", "source_id": 2211738},  # handbag -> backpack
    {"image_id": 578500, "source": "coco", "source_id": 115862},   # couch -> chair
    {"image_id": 578922, "source": "lvis", "source_id": 23883},    # vase -> cup
    #
    # Remove existing (grouped) instances if we add new ungrouped instances,
    # see `INSTANCES_TO_ADD` - below are ``apple, banana, carrot, skis``.
    {"image_id": 473406, "source": "coco", "source_id": 1048544},
    {"image_id": 303566, "source": "coco", "source_id": 1548592},
    {"image_id": 303566, "source": "coco", "source_id": 1549573},
    {"image_id": 303566, "source": "coco", "source_id": 1550289},
    {"image_id": 303566, "source": "coco", "source_id": 1550671},
    {"image_id": 303566, "source": "coco", "source_id": 1551079},
    {"image_id": 303566, "source": "coco", "source_id": 1551082},
    {"image_id": 303566, "source": "coco", "source_id": 1551096},
    {"image_id": 303566, "source": "coco", "source_id": 1551417},
    {"image_id": 303566, "source": "coco", "source_id": 1551555},
    {"image_id": 303566, "source": "coco", "source_id": 1552005},
    {"image_id": 303566, "source": "coco", "source_id": 1552226},
    {"image_id": 303566, "source": "coco", "source_id": 905300303566},
    {"image_id": 386210, "source": "coco", "source_id": 1047182},
    {"image_id": 386210, "source": "coco", "source_id": 1049887},
    {"image_id": 473406, "source": "coco", "source_id": 1048544},
    {"image_id": 8844, "source": "coco", "source_id": 1043844},
    {"image_id": 8844, "source": "coco", "source_id": 1042043},
    {"image_id": 460494, "source": "coco", "source_id": 1563796},
    {"image_id": 2532, "source": "coco", "source_id": 611486},
    {"image_id": 3255, "source": "coco", "source_id": 607021},
    {"image_id": 5529, "source": "coco", "source_id": 2200513},
    {"image_id": 38118, "source": "coco", "source_id": 606207},
    {"image_id": 41990, "source": "coco", "source_id": 2179320},
    {"image_id": 64462, "source": "coco", "source_id": 613521},
    {"image_id": 85682, "source": "coco", "source_id": 1850450},
    {"image_id": 85682, "source": "coco", "source_id": 1850717},
    {"image_id": 96825, "source": "coco", "source_id": 1449685},
    {"image_id": 129812, "source": "coco", "source_id": 609899},
    {"image_id": 131556, "source": "coco", "source_id": 608777},
    {"image_id": 172935, "source": "coco", "source_id": 1451308},
    {"image_id": 205333, "source": "coco", "source_id": 2199676},
    {"image_id": 280779, "source": "coco", "source_id": 1454090},
    {"image_id": 326542, "source": "coco", "source_id": 606707},
    {"image_id": 341719, "source": "coco", "source_id": 2199828},
    {"image_id": 341719, "source": "coco", "source_id": 2083700},
    {"image_id": 341719, "source": "coco", "source_id": 1845231},
    {"image_id": 377113, "source": "coco", "source_id": 1449293},
    {"image_id": 384666, "source": "coco", "source_id": 1453700},
    {"image_id": 384666, "source": "coco", "source_id": 1452322},
    {"image_id": 384666, "source": "coco", "source_id": 2202638},
    {"image_id": 384666, "source": "coco", "source_id": 609086},
    {"image_id": 384666, "source": "coco", "source_id": 614409},
    {"image_id": 411530, "source": "coco", "source_id": 1846076},
    {"image_id": 411530, "source": "coco", "source_id": 2199968},
    {"image_id": 411530, "source": "coco", "source_id": 2203490},
    {"image_id": 411530, "source": "coco", "source_id": 2199363},
    {"image_id": 411530, "source": "coco", "source_id": 1848207},
    {"image_id": 414170, "source": "coco", "source_id": 610416},
    {"image_id": 414170, "source": "coco", "source_id": 611772},
    {"image_id": 414170, "source": "coco", "source_id": 609517},
    {"image_id": 430377, "source": "coco", "source_id": 607131},
    {"image_id": 430377, "source": "coco", "source_id": 1846396},
    {"image_id": 469828, "source": "coco", "source_id": 610247},
    {"image_id": 470779, "source": "coco", "source_id": 2201510},
    {"image_id": 470779, "source": "coco", "source_id": 2201176},
    {"image_id": 470779, "source": "coco", "source_id": 608345},
    {"image_id": 509014, "source": "coco", "source_id": 609790},
    {"image_id": 509014, "source": "coco", "source_id": 1849656},
    {"image_id": 509014, "source": "coco", "source_id": 1848376},
    {"image_id": 509014, "source": "coco", "source_id": 2202612},
    {"image_id": 509014, "source": "coco", "source_id": 2200721},
    {"image_id": 509014, "source": "coco", "source_id": 2199009},
    {"image_id": 509014, "source": "coco", "source_id": 2201202},
    {"image_id": 509014, "source": "coco", "source_id": 2202244},
    {"image_id": 516601, "source": "coco", "source_id": 2202529},
    {"image_id": 516601, "source": "coco", "source_id": 606634},
    {"image_id": 516601, "source": "coco", "source_id": 1846650},
    {"image_id": 562818, "source": "coco", "source_id": 2085253},
    {"image_id": 562818, "source": "coco", "source_id": 1450716},
    {"image_id": 562818, "source": "coco", "source_id": 2083006},
    {"image_id": 562818, "source": "coco", "source_id": 2200324},
    {"image_id": 576031, "source": "coco", "source_id": 1453611},
]


INSTANCES_TO_CROWD = [
    {"image_id": 272566, "source": "coco", "source_id": 1550099},  # apple
    {"image_id": 303566, "source": "coco", "source_id": 1552174},  # apple
    {"image_id": 303566, "source": "coco", "source_id": 2111385},  # apple
    {"image_id": 388903, "source": "coco", "source_id": 1047942},  # apple
    {"image_id": 429281, "source": "coco", "source_id": 1908064},  # apple
    {"image_id": 479155, "source": "coco", "source_id": 1049257},  # apple
    {"image_id": 479155, "source": "coco", "source_id": 1049481},  # apple
    {"image_id": 479155, "source": "coco", "source_id": 1548373},  # apple
    {"image_id": 8844, "source": "coco", "source_id": 1042520},  # banana
    {"image_id": 50149, "source": "coco", "source_id": 1542009},  # banana
    {"image_id": 50149, "source": "coco", "source_id": 1543901},  # banana
    {"image_id": 50149, "source": "coco", "source_id": 1545760},  # banana
    {"image_id": 50149, "source": "coco", "source_id": 1904612},  # banana
    {"image_id": 50149, "source": "coco", "source_id": 1905131},  # banana
    {"image_id": 50149, "source": "coco", "source_id": 1905708},  # banana
    {"image_id": 50149, "source": "coco", "source_id": 1905751},  # banana
    {"image_id": 90891, "source": "coco", "source_id": 1542855},  # banana
    {"image_id": 90891, "source": "coco", "source_id": 1543673},  # banana
    {"image_id": 90891, "source": "coco", "source_id": 1543762},  # banana
    {"image_id": 90891, "source": "coco", "source_id": 1544190},  # banana
    {"image_id": 90891, "source": "coco", "source_id": 1545708},  # banana
    {"image_id": 90891, "source": "coco", "source_id": 1546181},  # banana
    {"image_id": 90891, "source": "coco", "source_id": 1546276},  # banana
    {"image_id": 90891, "source": "coco", "source_id": 1546610},  # banana
    {"image_id": 90891, "source": "coco", "source_id": 1547278},  # banana
    {"image_id": 90891, "source": "coco", "source_id": 1547553},  # banana
    {"image_id": 90891, "source": "coco", "source_id": 1547654},  # banana
    {"image_id": 90891, "source": "coco", "source_id": 1547739},  # banana
    {"image_id": 90891, "source": "coco", "source_id": 2110428},  # banana
    {"image_id": 112378, "source": "coco", "source_id": 1042081},  # banana
    {"image_id": 112378, "source": "coco", "source_id": 1046206},  # banana
    {"image_id": 272566, "source": "coco", "source_id": 1547741},  # banana
    {"image_id": 272566, "source": "coco", "source_id": 1547814},  # banana
    {"image_id": 293794, "source": "coco", "source_id": 1542086},  # banana
    {"image_id": 293794, "source": "coco", "source_id": 1543490},  # banana
    {"image_id": 293794, "source": "coco", "source_id": 1545444},  # banana
    {"image_id": 293794, "source": "coco", "source_id": 1545559},  # banana
    {"image_id": 293794, "source": "coco", "source_id": 1545949},  # banana
    {"image_id": 293794, "source": "coco", "source_id": 1546797},  # banana
    {"image_id": 293794, "source": "coco", "source_id": 1547084},  # banana
    {"image_id": 293794, "source": "coco", "source_id": 1547577},  # banana
    {"image_id": 293794, "source": "coco", "source_id": 1547707},  # banana
    {"image_id": 293794, "source": "coco", "source_id": 1547767},  # banana
    {"image_id": 293794, "source": "coco", "source_id": 2110125},  # banana
    {"image_id": 356428, "source": "coco", "source_id": 1044769},  # banana
    {"image_id": 356428, "source": "coco", "source_id": 1044975},  # banana
    {"image_id": 356428, "source": "coco", "source_id": 1543787},  # banana
    {"image_id": 356428, "source": "coco", "source_id": 1545176},  # banana
    {"image_id": 356428, "source": "coco", "source_id": 1905383},  # banana
    {"image_id": 378515, "source": "coco", "source_id": 1042355},  # banana
    {"image_id": 378515, "source": "coco", "source_id": 1542431},  # banana
    {"image_id": 378515, "source": "coco", "source_id": 1544163},  # banana
    {"image_id": 378515, "source": "coco", "source_id": 1544785},  # banana
    {"image_id": 378515, "source": "coco", "source_id": 1904221},  # banana
    {"image_id": 378515, "source": "coco", "source_id": 1904326},  # banana
    {"image_id": 378515, "source": "coco", "source_id": 1905149},  # banana
    {"image_id": 378515, "source": "coco", "source_id": 1905714},  # banana
    {"image_id": 378515, "source": "coco", "source_id": 1905767},  # banana
    {"image_id": 378515, "source": "coco", "source_id": 1905676},  # banana
    {"image_id": 378515, "source": "coco", "source_id": 2110699},  # banana
    {"image_id": 453708, "source": "coco", "source_id": 1042273},  # banana
    {"image_id": 453708, "source": "coco", "source_id": 1042298},  # banana
    {"image_id": 453708, "source": "coco", "source_id": 1045177},  # banana
    {"image_id": 453708, "source": "coco", "source_id": 1045405},  # banana
    {"image_id": 480275, "source": "coco", "source_id": 1043417},  # banana
    {"image_id": 480275, "source": "coco", "source_id": 1045099},  # banana
    {"image_id": 527029, "source": "coco", "source_id": 1547070},  # banana
    {"image_id": 406570, "source": "coco", "source_id": 1053573},  # orange
    {"image_id": 406570, "source": "coco", "source_id": 1912222},  # orange
    {"image_id": 429281, "source": "coco", "source_id": 1913189},  # orange
    {"image_id": 523100, "source": "coco", "source_id": 1051742},  # orange
    {"image_id": 523100, "source": "coco", "source_id": 1053656},  # orange
    {"image_id": 523100, "source": "coco", "source_id": 1911836},  # orange
    {"image_id": 7991, "source": "coco", "source_id": 1062435},  # carrot
    {"image_id": 34257, "source": "coco", "source_id": 1564414},  # carrot
    {"image_id": 227765, "source": "coco", "source_id": 1917065},  # carrot
    {"image_id": 253452, "source": "coco", "source_id": 1563588},  # carrot
    {"image_id": 313562, "source": "coco", "source_id": 1566841},  # carrot
    {"image_id": 397351, "source": "coco", "source_id": 1564752},  # carrot
    {"image_id": 397681, "source": "coco", "source_id": 1566520},  # carrot
    {"image_id": 397681, "source": "coco", "source_id": 1567779},  # carrot
    {"image_id": 397681, "source": "coco", "source_id": 1567493},  # carrot
    {"image_id": 397681, "source": "coco", "source_id": 1567528},  # carrot
    {"image_id": 397681, "source": "coco", "source_id": 2188511},  # carrot
    {"image_id": 456143, "source": "coco", "source_id": 1565449},  # carrot
    {"image_id": 530052, "source": "coco", "source_id": 2115785},  # carrot
]


INSTANCES_TO_ADD = [
    #
    # "airplane"
    {"image_id": 5477, "category_id": 5, "segmentation": {"size": [349, 640], "counts": b"]W]16g:3M7I1O1O0101N2O1N2O00000O1O00100N100O10000O2O_Q20^nM40O0001O1O00000000000O10000000000000000000000000000000001O0000000000O10001O00000000001O000000000000001O000000000000001O00000000000000000000001O00000O1000000000000000001O00000OUZT4"}},
    {"image_id": 456865, "category_id": 5, "segmentation": {"size": [427, 640], "counts": b"d]94V=5L10O100O1O1O0001O00000000001O000000O1010OO10000000000000000000000000001O0000001Ogm_7"}},
    #
    # "boat"
    {"image_id": 92091, "category_id": 9, "segmentation": {"size": [480, 640], "counts": b"j[b74j>2O2N3N1I8N1O1N1000O10O1000O01000O10O10O1000O0100DgA0Z>OkAMU>2oAJR>5=O100O001O2NfWY1"}},
    {"image_id": 353518, "category_id": 9, "segmentation": {"size": [414, 640], "counts": b"QkT34j<1N1N2M4N2M3N1O2O0O10O10O1000000O10000O100O1000000O10000001O001OO100000000O100000000O10J61O3M_OmC8R<FQD8P<GRD4IJV<2c0OjlX4"}},
    {"image_id": 353518, "category_id": 9, "segmentation": {"size": [414, 640], "counts": b"US=1l<2L3O1O1N3M3M3M2L4N2N3M2O1O100O02O1O1O1O1O001OIXOZDf0c;]OcD=\\;EcD;Z;GhD8W;IiD7W;IjD6Y;EjD9W;GiD9W;GjD8V;HjD8U;JmD3Q;0nDOS;2lDNT;2lDLW;3jDJ[;3j0L]SU7"}},
    {"image_id": 396863, "category_id": 9, "segmentation": {"size": [426, 640], "counts": b"Vgn21X=3M10001O000000000O100O010N2000001O00000O11O0O100O1000000O100O10000O2O0O101OhYk4"}},
    {"image_id": 455872, "category_id": 9, "segmentation": {"size": [375, 500], "counts": b"`c]12d;2O001O000000O11O0KNeD2Z;0eD0[;51N11000001O001O1O3M1O2N0000001O00001O2N10OO11O0000000BQE4o:1REIn:8TEEl:c003N0O000001O4L3M000001O0001O0000001O1D`ib3"}},
    {"image_id": 457078, "category_id": 9, "segmentation": {"size": [480, 640], "counts": b"]^Y1;b>6ACSB`0l=@SBb0l=@PBc0o=71O6J1OK501N1JROZBn0c=UO]Bk0b=WO]Bi0b=XO]Bj0c=94L5K1N10000000001O00O1000O10001N1OO10O2M3EjAJh>N2Mci_7"}},
    {"image_id": 457078, "category_id": 9, "segmentation": {"size": [480, 640], "counts": b"b5X1h=1N4L2N1N2N2N2N2N2O1N2N2O11O000001O0001O0000O100O10000001O1O001O0000000000000000001O001N4M8H6J5K3M1O001N3N6E<Feaa8"}},
    {"image_id": 531495, "category_id": 9, "segmentation": {"size": [438, 640], "counts": b"RZf35`=2O1O2K3N30O011N010O100O1O10O01O00000000001O001N101O1O00001O1Nfg]4"}},
    {"image_id": 540932, "category_id": 9, "segmentation": {"size": [480, 640], "counts": b"jmi15k>2M10000000000O1000000000000000000000O100000O10000000O100000000000000O1000000000000000001O000O1000000000000000000000001O000000000O1000000000000O010O10O101O001O00000O1000000000000000000000O100000000000000000000O1000000000000000001O0OZWk5"}},
    #
    # "traffic light"
    {"image_id": 2006, "category_id": 10, "segmentation": {"size": [480, 640], "counts": b"oYj09f>3M10001O01N10Rn]8"}},
    {"image_id": 165039, "category_id": 10, "segmentation": {"size": [427, 640], "counts": b"ZhP7435g<:dC_Oj;e0oCAn;P1N3M00000000000003fNQDR1c<@`0A\\jS1"}},
    {"image_id": 169996, "category_id": 10, "segmentation": {"size": [480, 640], "counts": b"USl64j>6L2M101O1N100O1O1O11N102LQ[Y2"}},
    {"image_id": 284762, "category_id": 10, "segmentation": {"size": [426, 640], "counts": b"j^Z3<2Gg<R1\\O001O00000O1000000O10000O100O100O1O1O1O1O100O100002WOZDJf;4`DHa;6aDI_;6bDJ^;6cDI];7cDI];7cDI^;6bDJ^;6bDJ^;5cDK];5cDK];5cDK];5dDJ];5cDK];5cDK];5cDK];4dDL\\;4dDL\\;3fDL[;2fDNZ;0iDOY;KS^[4"}},
    {"image_id": 372260, "category_id": 10, "segmentation": {"size": [640, 427], "counts": b"Thn6<dc01O0001IQPY1"}},
    {"image_id": 372260, "category_id": 10, "segmentation": {"size": [640, 427], "counts": b"V\\T7:ec02N1000O101N3Kl_Q1"}},
    {"image_id": 476704, "category_id": 10, "segmentation": {"size": [428, 640], "counts": b"aSn6Y1S<2N02N=B7J6HR^Z1"}},
    #
    # "dog"
    {"image_id": 70254, "category_id": 18, "segmentation": {"size": [384, 640], "counts": b"gi^12m;2O1O1O3M1O00001bD2<M^9d101N10000000000000000000000000000000000001O000000001kNPF_O2<n90YF\\O0a0k9NdFOa9KaF5b9DbF<a:00EaD5_;KbD3^;NbD2^;NcD1];OcD1];OcD1];OdD0];OdD0];NeD0Vh^5"}},
    {"image_id": 362682, "category_id": 18, "segmentation": {"size": [427, 640], "counts": b"cf^37R=4L3N2\\CIQ<8mCLQ<5mCMQ<4nCNQ<2oCNQ<2nC0P<f000O1000O10000O01N2M3N101N2O1O1O100O1000000O2O000001O01O01O010O100O1O2O2M5K010O01O010O1O010O001N1O2M3N2N1O2M3J5L5K5M3N2O1N2O100O1001OO1010O010O01O2N1O2N1N1O100O01O001O01O01N101O1N1N3M2K6M201O100O1O1O1O2N1O1ROlDCV;9nDDT;8QEES;5REHR;0VELX<JWmZ3"}},
    {"image_id": 369541, "category_id": 18, "segmentation": {"size": [500, 375], "counts": b"cod4;W?4L2O100O2O001O1N101N100O2O1N1N3O0O1O2N1O1O2M2O10000OBiAAW>>nA^OS>a0nA^OR>`0QB_OQ>>SB\\OQ>c0`0O2M2OVOF]B9_=DkA5f07]=NbB3\\=OdB1Z=2eBNZ=3fBLY=6gBJW=8iBGW=;gBFX=;hBDW=?gBAY=`0gB@X=b0gB]OX=e0hB[OW=f0iB\\OS=f0mB]Oo<d0QCBi<>XCEd<;^CE`<;`CE_<<aCC_<>aCB_<>`CBb<=^CBc<=]C@f<a0YC[Ok<e0UCVOQ=j0nBoNZ=P1g0N3N0O3N4JRO"}},
    {"image_id": 447200, "category_id": 18, "segmentation": {"size": [480, 640], "counts": b"U_34i>7L1O1O2N2N2N2O1N3M4kAVOm=o0O10001`BVOg<c1]CWNl;i1nC^NQ<b1jCcNV<T2O10O010O00010O0001O100O0000000001O0O1O2N2O0O1O2N1O2O0N2O1O1N2N101O001O01O100O101O1O001O1O001O001O00001O000010O0000O100000000O01000O101O0O2O0O2O2M3N1N2O1N3N1O1O1O1O1O1O2N3M2N2N1O2N1N101O1O1O1O0`FcL]7^3^HQMW7P3fHVMV7j2iHYMU7h2hH]MT7e2jH^MT7c2jHaMS7`2kHeMQ7\\2mHiMP7V2PImMm6T2QIoMm6Q2RIQNm6P2QIRNn6o1QISNm6m1RIUNn6k1QIWNm6j1RIXNm6h1QIYNo6h1PIXNQ7h1nHYNQ7i1mHXNR7h1nH[NP7e1oH]No6d1PI^Nn6b1RI_Nm6b1RI^Nn6b1RI_Nm6b1RI_Nn6`1RIaNm6_1RIeNk6\\1TIeNk6]1SIbNn6`1oH`NR7b1lH]NV7f1eH[N[7i1`HWNb7b41O2N101O1N2N4M1O1hIPH^5P8aJRH^5n7aJTH^5k7bJXH]5g7bJ[H]5e7bJ\\H_5b7bJ^H`5`7`J`Ha5_7_JbHa5\\7`JdHa5[7_JeHc5Z7]JeHd5Z7\\JgHd5X7]JgHd5Y7[JhHe5X7[JgHf5X7ZJhHf5Y7YJhHg5W7ZJhHf5X7[JhHd5Y7\\JfHc5[7]JfH_5^7`JbH_5_7aJbH]5`7cJ_H\\5c7cJ]H]5c7dJ]HZ5e7eJ[HZ5g7eJYHZ5h7fJYHX5i7gJXHU5l7jJTHU5n7kJQHS5R8mJmGR5U8nJkGQ5W8mJiG\\4GYKO:b80hG\\4ObKZ82hGY40eKY82fGX44cKX84eGW46cKV86cGV49bKW86aGU4:dKW86_GU4<bKY87\\GS4>eK[84WGV4>gK]80VGW4Z:N1O1010O2O2M4L`0A2N9F1O0100O2N2N3M5K4L4L5K3M2M5L3L3M4M2M2O3M3L4D`DQMe;j2;M<TOhCYN]<_1h0J7I9G?A``e5"}},
    {"image_id": 494869, "category_id": 18, "segmentation": {"size": [640, 427], "counts": b"TgT52mc02N2O1N101O001O1O2g]OMb`04m^OG\\O;da02j^Oc0Pa0^Om^Oe0Qa0^Oi^Of0Wa0W1K1O00003M9G1O01M2L8A?J6lMT^Oj1Sb0O1N2Al]OmNVb0o0n]OPOUb0k0n]OTOTb06f]O1_Rb2"}},
    #
    # "horse"
    {"image_id": 51309, "category_id": 19, "segmentation": {"size": [360, 640], "counts": b"o\\T34P;9hE2j8X1M3M2O2M2M4M2N2N3M3O0000hNZGNg8NaGM_80hGWOA;g8;\\H_Od7>`H@`7=dHA]7=gHAZ7=hHBX7>hHBX7>iHAW7`0h12N2N101N1O2N2N2N2N103L5K3MkN_Ff0JXOZ9OQGR1n8lNVGT1`9O001O0O2O3LO2000N4K7J110O00\\Od0?AVfd0XObZ[O1O0O1M4N104L8H6J5K5K8jLdNPL`1l3`NTLb1j3_NULd1h3\\NXLj1bMXN]5OQM_2k2bMTM`2j2`MVMa2i2_MWMa2h2`MXMa2g2_MYMb2f2^MZMb2f2^MZMc2e2]M[Mc2d2^M\\M6iN<k3^O]M2oN<d3C\\M1SO9a3F\\M1SO9a3F\\M2nN<g3A[M4\\M2NO<>o4]O[Ma2e2_M[Ma2e2_M[Ma2e2`MZM`2e2aM[M_2e2aM[M_2e2aM[M^2f2bM[M]2e2cM[M]2e2cM[M\\2f2dMZM_1dMgNR5JZMZ1nMfNi40YMT1WNhN`45YMk0U4UOkKc0]4]OcK`0`4A`K;b4F^K7d4J\\K3f4NZKOh42XKNg43YKLh44XKKj44VKKl44TKIP56R3O1O001O000000001O1O001O1O1N2Oocj1"}},
    {"image_id": 185473, "category_id": 19, "segmentation": {"size": [194, 640], "counts": b"Sc^34W57lJ9h4d0L3O1OH91O4L3M1O01O0O1F;K4M4L3N3N3M4K]f6"}},
    {"image_id": 185473, "category_id": 19, "segmentation": {"size": [194, 640], "counts": b"gT37j52N2M3O1O01O1O001O001O10O2N2N4L2N1mJ@a4e0YK^Of4o00000001N2I6N3O1N1O1O1O2O0O1000O1000000000O1000001O00OH9N2JYj\\3"}},
    {"image_id": 191288, "category_id": 19, "segmentation": {"size": [400, 600], "counts": b"VSe31]<2H800O10000001O001O000000001O00000000000000O010O100O1001O1O000000000000000000O1O1L4J6O1O001000000000000000000O1000000001O0O100000001O0000001O1O1N2O2N2N2NWjf2"}},
    {"image_id": 191288, "category_id": 19, "segmentation": {"size": [400, 600], "counts": b"^cf2?n;4N0100O10001O00000001O000010O000001O1O1O001O1O2N4L00000000000001O001O0000001O001O001O0N3N10001O0002N001O00000001O0000001O0O10001O00001O001O001O001O0000000O100JlSd3"}},
    {"image_id": 267933, "category_id": 19, "segmentation": {"size": [328, 500], "counts": b"m2;m90O2O000O01N200001O002YFE]9e0NO1O1N20000002N1O00O1N200000O01000001O01O100O00O2N3M4O1N2N2KoXb4"}},
    {"image_id": 289222, "category_id": 19, "segmentation": {"size": [480, 640], "counts": b"mWW43j>4K4N2O1O002fAEm=g000000O1M2M4O11O2N3L3N1O00CTBGg==ZBBb=b0_B\\O\\=j0;3N100001O:F2N2NjA_On=k0N1N1O1O1OH9N1100O2O1OCPBLn=4TBOg=1ZBOe=1\\BNd=2^BLc=3_BJe=2_BHXh]4"}},
    {"image_id": 453341, "category_id": 19, "segmentation": {"size": [480, 640], "counts": b"oSj54j>3M2O1O1N1O2N1N3M3O0101O1000O1N101O1O4M>A2O0O2N7J4L3ZCWNm;n1jCVNW<Y21O1O001N2N2ZOjC]NZ<^1i0J6K3L4G9K6J5K5LTh;1nWD2N4]AGW>g0J3M1O01O0000O1O1ZOTOXCk0j<YOPCh0Q=XOnBh0R=ZOkBg0V=[OfBf0\\=YObBh0a=:3M2N4K6J7J6H`hU2"}},
    #
    # "elephant"
    {"image_id": 286994, "category_id": 22, "segmentation": {"size": [480, 640], "counts": b"WPl43410M[>b0NJ600K_AKa>e0D1001O000O10000000000]OlA:U>CoA;\\>N10^]8GkbG2N003M4K5L:F1O0005K1O1O1OH8000000000000007I9FZR>JhmA0YA1a>:N2M3M^OgA=]>03G90O11N1ON0XAOoWo2"}},
    {"image_id": 320743, "category_id": 22, "segmentation": {"size": [360, 640], "counts": b"V_P34T;2M3N1O1O00000O100O001O1O000O00N21N1O2M3K5G:M3N2N2M3N2N1O1O10001O10000000000000O1000000O10000O1000O0100O1000M201O101O1O1O1O01N10001N2O001O001O0O01O1N2M3M201O1O10O0100000O10O1000O10000000000O100000000000O1000O10O101OO10O2O00000O100000000O10000000000O101O000000000000000010O0000000001O01O00000001O01O00000000010O00001O001O001O001O0^OeFWO\\9b0lF]OT9>QGAo8:VGFj87YGJg82\\GNe8O^G0b8MbG3^8KeG3\\8JgG5Y8JiG5X8IjG6k9Igdh0OX[WO5bM;PHD63g7c0cGDb0Li7Y1RHjNn7V1jGQOW8o0bGXO^8h12N1O1O2N1N2N3M2M3K5D=L3M3N3N100O1000001O8G100O01O1O1O001N2G:I6O1O1O1Ob0_O7H4L4L5K4M3L5L4mHfLo5_3lIcLS6c3eI`LY6e3bI\\L^6g3\\I\\Lc6U4000000O100000000000000O100000O1oN]IXMNZOf6\\3`IWMd6i2_ITMb6j2aIUM_6j2bIUM_6j2cITM^6k2dISM\\6m2fIQM[6n2gIPMZ6o2gIoL[6P3gInLZ6Q3o0O001O100O1O10000O1O1O1N2O100001O0001O0001O01O000O2N1O2N1O1O2N1O101N1OeM"}},
    {"image_id": 341058, "category_id": 22, "segmentation": {"size": [640, 359], "counts": b"gQY44_c0>N1O0O02O2N1O23L1N100O00I80O1M2O101O002N4M3M0000IP]O]OQc09n\\OKZc03h\\OMWc03i\\ONWc00k\\O0Uc00j\\O0Wc0Ok\\OOVc00>OJO]\\O1cc00\\\\O0dc061N2NTon1"}},
    {"image_id": 383921, "category_id": 22, "segmentation": {"size": [480, 640], "counts": b"Q5g2Y<100O101N101N2N2N2O1N1O3N0O2N2N2N1O1O000000O1000000O10OjNgDgNY;X1mDcNS;]1PEaNo:_1UE]Nk:b1YE[Nh:d1[EYNe:h1\\EVNd:j1_ESNa:o1`EmMb:S2U11O100O011O002O1012NO3L1OO0O2M2N3kM[Cj1Z=C5K4L4L6J6J<D[f^8"}},
    {"image_id": 445248, "category_id": 22, "segmentation": {"size": [427, 640], "counts": b"_oZ34V=8I6J7H8I7YDkNj:o1L3M001O0O101O0001ASE^Ni;a0]D^Oh<01O1N]=OcB3N1O2N1QNLfF5Y94_FLa9;WFFi9f0iE\\OW:S1XEoNh:j100000000000000000000000000000O2O001_O`0I8K4G:G9H9E^aX4"}},
    {"image_id": 493284, "category_id": 22, "segmentation": {"size": [427, 640], "counts": b"iRc32T=6M2N2N2N2N2N2N2O1N2N2N2M3N2N2M3M3N2N2M3M3L4L4K5L4I7I7N2O1000000001O000000000000000000001O9G8H9G:F7H8H8DmfQ4"}},
    #
    # "zebra"
    {"image_id": 60770, "category_id": 24, "segmentation": {"size": [375, 500], "counts": b"RSk12e;2M3N1O1O2N1O1O001O1N101O00001O001O1O1O101N2N7H2O0O2O0000000000000001O001O001O0010N1001O000000000@`0001O00001N2O2N1NKSE@0Nm:b0SE_O14g:>YEDg:;ZEGe:7]EHj:OXE1k:IXE8T;O00001N101N3LicQ3"}},
    {"image_id": 486046, "category_id": 24, "segmentation": {"size": [480, 640], "counts": b"W=f0Z>01N10000O1000000O100O10000O101O00000O101O00000O2O00001O001O00001O001N101O00010O0O2O1O]nf8"}},
    {"image_id": 508586, "category_id": 24, "segmentation": {"size": [360, 640], "counts": b"d\\[54T;1N3M2N3M2O3L2O0000N1O2010O6J000000_ObE9g:N2O0O3J``]1"}},
    {"image_id": 562121, "category_id": 24, "segmentation": {"size": [454, 640], "counts": b"XX[19l=3L101N100O2N2O1O001N110O1O101N101N2O1O00001O1O5K001OO100O1O1N201O0O010001O1O3M3M4L2N000001L4N3M2M5C?HZ^i6"}},
    #
    # "giraffe"
    {"image_id": 25096, "category_id": 25, "segmentation": {"size": [500, 375], "counts": b"cUX42b?0O1O1O101N1O100O2NM40O001O0001O01O000RAL]>5cAL\\>3dAN[>3dAN[>3dAN\\>2cAN]>3bAM^>5`AL_>6_AJb>7[AJe>c0O00010O00001O00100O1O[OaA6_>HgA4Y>KjA3V>MmA0S>OQBMP>3j0N1O2MXQg0"}},
    {"image_id": 563603, "category_id": 25, "segmentation": {"size": [640, 459], "counts": b"SYk41lc03N2O001N101O0O2N1OJb\\ON\\c03e\\OLn04Sa00P^OLk09Pa0LZ_O7a`0J`_O9[`0Hf_O:V`0Fl_O?m?BT@X1P?hNRAX1m>hNUAW1h>kNZAT1d>lN`AR1_>mNdA6\\N0o?KiAGkNOb?:T3O010O1O2N1O2O1O2M3O0002M1O2N1O10001O000100O100O1N2M[hS3"}},
    #
    # "umbrella"
    {"image_id": 16228, "category_id": 28, "segmentation": {"size": [440, 640], "counts": b"Rh2:^=3M000001O000000001O00010O001O1O1O001O1O1O1O1NdmU8"}},
    {"image_id": 54628, "category_id": 28, "segmentation": {"size": [500, 375], "counts": b"^iQ14^?4N1N101N2O1N2N100O10000O100O1UAA15P>d0PBWOMLT>c0kABi>KPP18`PO6J10O1O001O001O001O00001O001O001O00001O001O001O001O001N10k\\l3"}},
    {"image_id": 54628, "category_id": 28, "segmentation": {"size": [500, 375], "counts": b"Tel13a?0O2O0O2O0O1O010O010O011N100O100O100O100O100O13K[n17aQN7H2bAYOk==k001O000O2O001O1O001O00001O001N10001O001O001O001Mjcn2"}},
    {"image_id": 74058, "category_id": 28, "segmentation": {"size": [427, 640], "counts": b"Shm09l<5N2010O100O2O0010O00100O0UCBi<b0N00000001O000011N4L00000001O0000D[OSDd0l;^OSDb0m;^OSDb0m;_ORD`0o;@RD=P<BQD`0n;^OSDc0k;ARD?m;CmCJ0d0Q<DnCI1b0P<FnCI2a0o;LQD4o;LQD4n;LSD4m;LTD3l;IXD7g;IZD7g;HYD8g;IoCE8a0j;NTD1l;MVD3k;KVD6i;E\\D:f;A^D>Y<Kfhe6"}},
    {"image_id": 156643, "category_id": 28, "segmentation": {"size": [480, 640], "counts": b"0j2V<000000001O0000000000001O0000000000O1000000O1001O001O1O001O001O00kM[ENf:LZ2L4N2N2O1O1O1O1O1O100OQkU2NRUjM4L2N001O1O3M1O00000000N2N2O1LbA1[>:F7M3O1O3M8H1O1O1jBkN_<V1^CPOGI^<X1bCEY<<eCFZ<;dCG[<_10001O0000001O00001O000000001O0000001O0000001O00001O000000O1L4M3J600009G4L1O00001O1O1O000000001O000000000000001O00000000000000001O000000000000000000000000000000001O0000000000O100mMXDm0i;ROZDk0g;TOZDk0g;TO[Dj0f;UO\\Dh0f;XOZDf0h;XOZDg0g;XO[Dg0e;XO\\Dg0e;XO\\Dh0d;WO]Di0c;VO^Dj0b;UO`Dj0`;UObDj0^;UOdDj0\\;TOiDi0W;SOPEj0P;QOZEj0a<M2N3M2M5L102M101N2N1O1O3LWbc1Oi]\\N2N3N1N2O01N1OM7M2M3M2O1N2N2N2M3O1M3N2M2O2M3L4M3L4M3M3N200O100UORNdDm1];TNbDl1^;UNaDk1_;VN_Dk1a;VN^Dj1b;WN]Di1c;WN\\Dj1d;WN[Di1e;WNZDj1f;WNXDj1h;WNVDj1j;VNUDk1k;VNSDk1m;d00O1000000000000000000000000O1000000000000000000O10000000000000000000000000000O10000000000000000O1000000000000000000O10000000000O100000000000000000000000000O100000000000000O100000000O10000O100O100O1O100O1O1O1O1O1N2O1N2N2K5C=00001O1O001O1O1O1O1O2N1O2N1O2N1O001O1O1O1O1O1O1O001O000000"}},
    {"image_id": 254814, "category_id": 28, "segmentation": {"size": [480, 640], "counts": b"]jh42l>4M2M2O1O2N100O1000000O11O0O1Ome[4"}},
    {"image_id": 254814, "category_id": 28, "segmentation": {"size": [480, 640], "counts": b"Yk`44k>2N101N1O1O1O1O1000000O100O1000O1N3M3N2MoYa4"}},
    {"image_id": 291634, "category_id": 28, "segmentation": {"size": [640, 433], "counts": b"UZ`17ic0000O1O1O1000000O100001O3Moc0KU\\O6J2O0000000O1000O1000001O0000001O001O001O001NkmU6"}},
    {"image_id": 431876, "category_id": 28, "segmentation": {"size": [640, 425], "counts": b"RP[53lc02N2N2M3N2M3N2N1O2M2O1O001O00Bm\\O1Sc0No\\O0Rc0OP]OOQc0IY]O4X[c2"}},
    {"image_id": 496854, "category_id": 28, "segmentation": {"size": [480, 640], "counts": b"dQT32m>1N3N1O1O2N1O1O001N2O1N2O1O001O100O001O1O01O001O00100O001O010O1O010O1O101N1O3M2N1O2M3Md[20[dM3N2O1O001O010O00100O00000O11O1O1O2N101N1OoeV5"}},
    {"image_id": 530162, "category_id": 28, "segmentation": {"size": [427, 640], "counts": b"f\\a15U=3N1O001O1O00000J6O2O000O10000001N10000O10001N2O2J5MVW^6"}},
    {"image_id": 530162, "category_id": 28, "segmentation": {"size": [427, 640], "counts": b"lQh11X=3N100O100O101O001O0O0100000000O100O101N101N101Ne\\X6"}},
    {"image_id": 530854, "category_id": 28, "segmentation": {"size": [425, 640], "counts": b"_RP22V=1O2N100O1O010O1O100O100O1O100O1O1O100O100O100O01000000000O10O100000000000O100000O1000O1000O10000O1O1O010O1O1O1O1O10O01O1O1O1O100O1O001O1Ob`\\5"}},
    #
    # "tie"
    {"image_id": 169076, "category_id": 32, "segmentation": {"size": [612, 612], "counts": b"ebW3:Yb0Ko]O:oa0Hm]O<Qb0<00001O009G3L3N4L4KT]n7"}},
    {"image_id": 397303, "category_id": 32, "segmentation": {"size": [480, 640], "counts": b"ahf13i>4M3J7J5M3O1O101O000O101O000000000O1000O10O10O10O01000O0100O010O10O0100O100O010O10O10O0100O1O10O01O100O1001N1000001O00000000O10000000O0100O10000O100O1O1O1N2O1000O01000O100000000O01000O010O1O10O0N3M2OZO\\B4c=JbB3_=KfB1[=NhBOY=0jBNV=1nBJT=6k0010O00O2O0O2N2LY\\o5"}},
    {"image_id": 397303, "category_id": 32, "segmentation": {"size": [480, 640], "counts": b"e]U1?_>2N3L3M3O2N1O1O10O01O010O010O010O010O010O10O1O1NPOVOmCh0o;CmC;R<JkC5V<MiC2X<OXC@3a0e<0UCB4?g<;YCEf<<ZCCg<=XCDh<<XCDh<;YCEg<;YCDh<<WCCl<<TC@P=`0PC]OR=d0nBTOZ=4`B=m=BUB=k=BWB<j=CYB;g=EZB:f=F\\B8d=G^B7c=I^B6b=I`B6`=JaB5_=JdB3^=Lk001N10ST=0lkB2N100O2N2O0O1O1O100O1O100O100O01N2M201001O1O0000O101N1O010Ofg`6"}},
    {"image_id": 397303, "category_id": 32, "segmentation": {"size": [480, 640], "counts": b"PP>3l>2N2N1O100O0010O01O010O010O010O010O101N101N101N1O1O100O1O10O010N10001O01O01O1O01N1001O000N3M3O001O001O0010O010O01O01000O10O010O0100O0010000O0100000O01000O010O1000O10O100O10000O01000000000O0100000000000000O010000000O010000O010O10O10O10O1000O10O100O10O0100O01000O010O000001O010O0100O100O101N1O1O1O1O100O1O010O00100O1O01O00001O0010O010O0100000000000O1000O10000O1000000O1O1M2M4O100O2O0Oo]8ORbG2O0O100O101O0O100000001O000001O010O1O1N3N_Za5"}},
    {"image_id": 417632, "category_id": 32, "segmentation": {"size": [480, 640], "counts": b"SUi68e>5K6J5L5J6K6ZOmNTCX1i<a0N01M2O2N2N1O2N1O2N101mNdB`0^=^OhB<[=BjB8\\=ChB8W>HUcW2"}},
    {"image_id": 417632, "category_id": 32, "segmentation": {"size": [480, 640], "counts": b"Q`g2g0j=g0^NgN[DP2];m0L3M2NN1POQ11O1010O2O:E<TOTa]6"}},
    #
    # "skis"
    {"image_id": 2532, "category_id": 35, "segmentation": {"size": [640, 480], "counts": b"Qk`41nc01O2N010O10O010O1O010O00100N1010N0mc02R\\O10OO20O0O0101O000O1L4M2O12N3M5KSfT4"}},
    {"image_id": 2532, "category_id": 35, "segmentation": {"size": [640, 480], "counts": b"ZWQ41nc01O1O1O1O1O001O00001O01N2O10O0N2001N2O100O1NX]l4"}},
    {"image_id": 3255, "category_id": 35, "segmentation": {"size": [363, 640], "counts": b"P\\U33X;00000001Nn[k3"}},
    {"image_id": 3255, "category_id": 35, "segmentation": {"size": [363, 640], "counts": b"oUR32Y;1N11O0000oan3"}},
    {"image_id": 5529, "category_id": 35, "segmentation": {"size": [640, 444], "counts": b"_iP25ic02N2AIS]O:kb0Jo\\O9Pc0<001O0XOk\\Of0Tc030001O000O2N101O0010O001O00003M1O1O2N2Ei\\OHZc00XoQ6"}},
    {"image_id": 5529, "category_id": 35, "segmentation": {"size": [640, 444], "counts": b"Rac21mc03L4M201M2O2O0O4M3M1O0O10001O001O1O001O01O1O1O100O0\\Oi\\O?Wc0@k\\O?Uc0@m\\O?]c0M10N100O000001O010O10O1000000000000000O2O001O1O1O2Llbo4"}},
    {"image_id": 38118, "category_id": 35, "segmentation": {"size": [427, 640], "counts": b"^go12Y=5J2M3N202M0001IUCLl<3UCLl<91O1O2N1O2N2N^QT6"}},
    {"image_id": 38118, "category_id": 35, "segmentation": {"size": [427, 640], "counts": b"m\\l14V=3H7O001O01O00002N2M4M2N1OUdX6"}},
    {"image_id": 41990, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"Wca11n>2O1N2N3L201N2O1O1N2O1O2N1O1O2O0;D1O1O1O1O10O01O1O00001O00000000000000000000000O1O1N]WV7"}},
    {"image_id": 41990, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"\\^\\11n>2O2N9G10O0001O01OO100O11O00001O001O100O2N1O1O2M2O001OX]b7"}},
    {"image_id": 64462, "category_id": 35, "segmentation": {"size": [378, 500], "counts": b"PS]27`;i0ZOh0YO1N000O1001O010O001O2N4L5K5K2N3M4L6I8I2N1O2N10001N1O2N2N3Lbco2"}},
    {"image_id": 64462, "category_id": 35, "segmentation": {"size": [378, 500], "counts": b"S_\\31h;2N;F3L6K7H5L3M3M2M4M3O9FO101N4L3M2N4L2N2N2N2N1O2N2N3M2N2N2N3M3M2N4L2M3N1OdPn1"}},
    {"image_id": 85682, "category_id": 35, "segmentation": {"size": [427, 640], "counts": b"Rkb52X=101O2M2N10N200O1O2O0O2Nbe66XZI20OoBJm<7SCIn<5RCKT=OlB1U=30O3M_UX2"}},
    {"image_id": 85682, "category_id": 35, "segmentation": {"size": [427, 640], "counts": b"Z^l52Y=0O2O0O1000010jBLT=52O0O001OSPY2"}},
    {"image_id": 96825, "category_id": 35, "segmentation": {"size": [503, 640], "counts": b"hmU51f?2N0001O0001O0001O0001O0001O0001O0001O0000001O00O2O0O1O10O1OnVU4"}},
    {"image_id": 96825, "category_id": 35, "segmentation": {"size": [503, 640], "counts": b"b^W41f?2N001O1O010O0010O01O01000O02OO10000O100000O2O0O100O1NjTU5"}},
    {"image_id": 129812, "category_id": 35, "segmentation": {"size": [426, 640], "counts": b"ih91X=4L3M3N1O100O2N1O1O100O010O10O001000O010O010O01O1O10O01O00010O00010O00001O0001O01O00001O01O0000000001O0000000010O01O0000010O0001O00000000000001O0000000000000000000O1000000000001O00000000000010O00000000010O000000001O0001O0000000000000001O01O000000000001O01O0000000001O0001O00000000000001O01O000001O0001O00O11O000001O0000000000000001O0001O00000000000001O01O000000000001O000001O000001O000001O01O00000000001O0000010N2O1O01O0001O00000000010O000000000001O0000000001O00001O01O00000000000010O00000000001O00100O1NWR<OimC3O000M4N1010O1O000001O00001N101O01O0000000000011N000000000000000000002N001O1O1O010N10001O010O00100O001O010O00O11O00]Z80beG10000000011N000000000000000001O00001O0001O0010O0000000000NOkB2S=300O10000001O000001O001O000002N1OO1000001O00001O000000001O01O0000001O000000001O01O001O0000010O000010O01O00000001O000010O0000000010O00000000000010O0000010O000000001O00000000010O000001O01O0000000001O01O0000001O01O000000001O01O00O11OLPCOo<0RC0o<ORC0o<ORC0o<OPC3S=000001O1O1O_lX1"}},
    {"image_id": 129812, "category_id": 35, "segmentation": {"size": [426, 640], "counts": b"Uo<8o<5M3M2O2N1O1O1O1O100O10O1000000O10000O2O001O0O101O0O101N101N101O0O2O000O10000O010O10000O01000O0100O0100O0100O01000O010O01000O01000O010O10O10O01000O010O10O10O10O010O10O10O10O10O010O01000O0100O010O10O10O010O10O0100O010O0100O010000O010O10O100O2O000O10O010O10O1000O1O0010O01O1O010000O10O10O10O10O10000O10000O100O0100O10O10000O01O1000O0100O010O1O010O1O001O1000O01000O0100O010000O01000O010000O10O10O100O010O10O02O00O100O1O2O0000000O100O010001O00O010O0100O1000O10O100O1000O00100O0002O0O100O010O10O10O10O0100O010O01000O010O10O010O100000O01000O10O10O10O100000000O10001N0100000O10O1000O10O1000O1000O01000O10O1000O10O10O10O1000O10O01000O1000O10O10O10O10O1000O0100000O010O1000O010000O010O010O1000O0100O010O1O010O10O0100O010O1O010O1O010O010O010O0001O010O000010O0001O00001O0001O01O00000O101O00000000000000000000000001O00001O001N101O001N2O1N]i`2"}},
    {"image_id": 131556, "category_id": 35, "segmentation": {"size": [425, 640], "counts": b"ddf12W=1N200O10O010O1O100O010O00010O000001O000001O0001O0000000010O00000000010O00000001O0001O00000001O0001O000001O0000000000001O010O1O1O000001O00000000001O0000000010O0000000001O0000001O00001O0001O000000O1000000000000001O01O01O0000001O01O00O100000010O00000000001O01O000000000000000000000O11O00000000000001O0000000000010O00000001O0000000000000000000001O0000O2O0001O00000000000000000001O01O0000000000001O00O103NO00000O1O1O100001O0000O1001O00000001O000000O10000001OO100000000001O000000000000000000000000000000O1000000001O000000000000000000000O01000000000000000O10O100000O10O10O010O10O0010O1O100OZ[i2"}},
    {"image_id": 131556, "category_id": 35, "segmentation": {"size": [425, 640], "counts": b"U`i23V=1O001O00010kWg0LXhXO2N1O0000000000000O11O0000000O1000000000001O000000000000O100000000001O000O10O1000001O000000000O2O0000000000000001O00001O000000O100000000000000000O10000000O10000O1000000O10000000000001O000O1000O1000000000000000000000000001O000000000000000000O100000000000001O000000O100000000000000O10000000000000O1000000O01000O1000O01O100O000100O011N1O1Oij_2"}},
    {"image_id": 172935, "category_id": 35, "segmentation": {"size": [364, 488], "counts": b"WZR21Z;2O00O1000O0N3O100O10O000100O01O01O010O0010O1O001O]]1MebN2O100O100O1000O01O01O01O01O01O01O01O01O010O000010O00010O0010O010O0001O001O01O00001N10010O00100O1O\\h^2"}},
    {"image_id": 172935, "category_id": 35, "segmentation": {"size": [364, 488], "counts": b"gXl12Y;2N10000O10000O0100000O010000O010O10O100O0010O010O010O010O01O010O01O010O00010O010O010O001O010O00010O01O010O10O010O10O01O0001O01O010O00010O010O00010O0010O0010O01O01O001O00010O00010O0010O00100O01O1OjQ^2"}},
    {"image_id": 205333, "category_id": 35, "segmentation": {"size": [164, 640], "counts": b"\\[c02R501O[?0jE0jJ1000000001O0001O0000010O0001O00000000U^11iaN1000000000000000000000000000000001O0000XkY2"}},
    {"image_id": 205333, "category_id": 35, "segmentation": {"size": [164, 640], "counts": b"VVc03Q501O0000000000000001O0001O0000001O0000000001O1O01O00001OU^10jaN1O100010O000000000000000000000000001O00XkY2"}},
    {"image_id": 280779, "category_id": 35, "segmentation": {"size": [501, 640], "counts": b"YZ]43b?1NMb@1[?2f@MZ?340O101O1O2N10N2OO100000O1000O1000O2O000000O10O01000000O010000000000O01000001O0000000000000000O010000O10000000000O10000000000000O100001O11N3M1O001O0000000O1N[^20Ujm3"}},
    {"image_id": 280779, "category_id": 35, "segmentation": {"size": [501, 640], "counts": b"[hW51]?1h@OX?2f@OX?1f@2\\?Nd@0b?O1O00M3000O2NL051O2M1O1O11N100O10O01000O100O0100000O10O10O10O0100O13Lmim3"}},
    {"image_id": 326542, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"Uc_61n>100N2N2O010O1O10O2N3LRif2"}},
    {"image_id": 326542, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"PQ[51n>3N1O001O01O001O001O001O001O000001O000000000000000000000O1N2O1000NWANh>500000000000O2O0O2NoZ\\3"}},
    {"image_id": 341719, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"edf51n>2O1O000000O100000000O10\\X_3"}},
    {"image_id": 341719, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"cSg52m>2O01N10001OO100O100001O000001O0001O0000\\Q[3"}},
    {"image_id": 341719, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"[b_54o0Oi<_1F00fN\\1JiRj3"}},
    {"image_id": 341719, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"^ma58110a0_=ZOaBX1k=FZeh3"}},
    {"image_id": 341719, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"lWY41n>2O010O00010O010O0001OO1000000O1O010O1O1O010O100O0010O100O101O000O2O0000000O100000O010000000iZ22UeM000O100O010O100O10000000O1000O10O10O1O001O10O1O100O1O2Ohil3"}},
    {"image_id": 341719, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"kfY43m>0010O00100O0001O01OO100MNXA2g>OYA1g>3010JYA3i>1N110N20O10O10O00100O2O1O001Nin7OVQH3O00100O00100M30O0010O01O2N2Nk[S4"}},
    {"image_id": 377113, "category_id": 35, "segmentation": {"size": [427, 640], "counts": b"bia33X=1O1O00000000000O10000000O1000000000O10000O1000O100000O01000000O01000000O10O10000000O10O1000000O010000O10O010000O100O010O100O1O010O10O0100O1O010O100O10O10O10O1O101N1O1O2N3KVjd3"}},
    {"image_id": 377113, "category_id": 35, "segmentation": {"size": [427, 640], "counts": b"Qma42X=2OO01O0100O10O010O0100O01000000O1000O1000O10000O01000O010000O0100O01000O01000O10O10O010O010O010O1O1O010N2O010O001O1O1O010O1O01O010O010O1O1O2N2Nkaj2"}},
    {"image_id": 384666, "category_id": 35, "segmentation": {"size": [332, 500], "counts": b"VmW33Y:0O1O10O1OUXh1"}},
    {"image_id": 384666, "category_id": 35, "segmentation": {"size": [332, 500], "counts": b"`]]32Y:1O11Nb\\c1"}},
    {"image_id": 384666, "category_id": 35, "segmentation": {"size": [332, 500], "counts": b"[nU21[:4K2O00O11O010001N002N1OSng2"}},
    {"image_id": 384666, "category_id": 35, "segmentation": {"size": [332, 500], "counts": b"Sdi14V:2O1O1M3M3000N2J7MPXU3"}},
    {"image_id": 384666, "category_id": 35, "segmentation": {"size": [332, 500], "counts": b"YPk31Z:1000000000000001O_kS1"}},
    {"image_id": 384666, "category_id": 35, "segmentation": {"size": [332, 500], "counts": b"kSg31Z:20O01O01O\\QY1"}},
    {"image_id": 384666, "category_id": 35, "segmentation": {"size": [332, 500], "counts": b"gQ\\22Y:2OO0000011NYic2"}},
    {"image_id": 384666, "category_id": 35, "segmentation": {"size": [332, 500], "counts": b"lUc21[:000O10000N11O10O010O10O01O02NkgY2"}},
    {"image_id": 384666, "category_id": 35, "segmentation": {"size": [332, 500], "counts": b"XcZ12Z:0001O00000000O10000000000001O000000000000000000k\\_3"}},
    {"image_id": 384666, "category_id": 35, "segmentation": {"size": [332, 500], "counts": b"l^_12Z:000\\:0dE01O00000000000000[S^3"}},
    {"image_id": 411530, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"Y]Y7;a>400000000O100002M5L3Mcnl1"}},
    {"image_id": 411530, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"nfg53m>1O010O0O10000000001OO0100000000000O10000000O1000O100000000000O10O10000000001O000O101O0000000000O0100000000000O10O1000000O10O1N2N200000000000O10000000000000O10O1000000000000000O0100000000O10O100001N3NZnT2"}},
    {"image_id": 411530, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"Q`R5=e>32IfRX4"}},
    {"image_id": 411530, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"daQ59h>32KTQY4"}},
    {"image_id": 411530, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"VXj73l>2O1N1O100O010O11N1O0O20O01O000Nl>2TA1M3N110001N2N4L[SU1"}},
    {"image_id": 411530, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"olg74l>2N3M0100OO10001ON9Iim^1"}},
    {"image_id": 411530, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"[^]82m>101OO011O01O00000000000000000000000001O0000ehc0"}},
    {"image_id": 411530, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"WaT83l>2N2O00010O02N2N01O100O001N100001O2N001NR?1n@1O000O1000001O00000000000000000001O000O3M`jb0"}},
    {"image_id": 411530, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"lmb52n>001O000Q?NPA20O00001O01O000RQb3"}},
    {"image_id": 411530, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"oRh51o>000000001O000000001O000Qj]3"}},
    {"image_id": 414170, "category_id": 35, "segmentation": {"size": [640, 425], "counts": b"_Vo41mc04M5L3M3M2O10N3N1N2N2M4KWYR3"}},
    {"image_id": 414170, "category_id": 35, "segmentation": {"size": [640, 425], "counts": b"gjc51lc06L4M2M3O0O21N101N010O0O101N1O1O2Mk`Z2"}},
    {"image_id": 414170, "category_id": 35, "segmentation": {"size": [640, 425], "counts": b"^Tb32nc02N2N1O10N2O3L^_b4"}},
    {"image_id": 414170, "category_id": 35, "segmentation": {"size": [640, 425], "counts": b"bTi27hc01001O^o]5"}},
    {"image_id": 414170, "category_id": 35, "segmentation": {"size": [640, 425], "counts": b"jfY43lc010O00Y]m3"}},
    {"image_id": 414170, "category_id": 35, "segmentation": {"size": [640, 425], "counts": b"knU42mc01N1100OYaP4"}},
    {"image_id": 430377, "category_id": 35, "segmentation": {"size": [640, 439], "counts": b"\\a:1nc02O001N10001O0O10001O0000001O0000010O000001O01O001O010O0001O001NVT3KnkL4M10000O1000000000000000010O00000000001O00000001O00010O00000010O01O00010O000000001O00001O0O101M\\l`00fS_O00002N001O0000001N1000010O0000001O00000O2O01O0001O0000001N1000001O0001O01O010O0000010O0001O0001O010O000010O0000001O01O0000010O00010O0000010O000001O0001O01O0001O01O01O0001O01O00010O0001O01O0001O0001O01O0001O010O000010O0000010O0001O01O01O01O0001O01O0000010O0000010O0001O01O0000010O0000001O0001O01O001O000010O01O00001O00000O1000000000000000000O1000O10O1000O010O010O010O001O10O01O000O2O00010O01O1O1O1N3M]mR2"}},
    {"image_id": 430377, "category_id": 35, "segmentation": {"size": [640, 439], "counts": b"haR41oc0000N20001O1O1N1000001O0O100O2O00001O000001O001O010O000010O0000001O01O0001O0001O0001O01O000000010O00000010O00000010O0000010O000000010O000001O01O000001O01O00000010O0000010O000001O01O000001O01O00000010O000000010O0000010O000001O01O000001O0001O00000001O01O01O01O0001O0001O0000010O0000001O01O01O00000000000000000000000O10000000000O10000O10000O10O0100O010O00010O0001O00001O00001O000001N2OPjg0"}},
    {"image_id": 430377, "category_id": 35, "segmentation": {"size": [640, 439], "counts": b"Th<2nc00000000000000000000lgn7"}},
    {"image_id": 430377, "category_id": 35, "segmentation": {"size": [640, 439], "counts": b"Rd91oc01O00000000O100000000000000000ngn7"}},
    {"image_id": 469828, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"QnQ21o>0000000O2O0000000000000001O000000000001O0T^8NnaG1O0O100000000O10001O000000000000000000001O00000005Knm02nQO2000000000000001O2NiaT6"}},
    {"image_id": 469828, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"dlh21n>2N11O0000000001O0O1001O0000001NQ]10obN2O000010O000000001N\\bT6"}},
    {"image_id": 470779, "category_id": 35, "segmentation": {"size": [479, 640], "counts": b"XaS12g>7N1L4N3bABV>e0D=^OTOiBQ1c<iN\\CO8i1\\<\\N]Cj1d<800O10000O1K6O0011N1N3N1N11OH8SO_C[Ob<=fCCZ<2RDMo;NUDHPO1l<2bDM_;0cDLb;1]oh7"}},
    {"image_id": 470779, "category_id": 35, "segmentation": {"size": [479, 640], "counts": b"ncU23d>91OL5K6M3M3M2N3N1N4N2M10001O1N101O0O1O01N2N2N2N2N1O2M3N1O2N2M2O2N1O2N2M2O2N1O2M2O2N1NTTa6"}},
    {"image_id": 470779, "category_id": 35, "segmentation": {"size": [479, 640], "counts": b"QP[67b>7ADnAg0m=9M2M3N2O1KiNaBX1]=6ZOfNbC_1]<b0N2O1N2O1O12N4L1O001O00001O0O1OKmM\\CU2d<03oNQ1Eana2"}},
    {"image_id": 470779, "category_id": 35, "segmentation": {"size": [479, 640], "counts": b"Umf75j>1O2N1N301N2N001O1aACY>n0D3N4L1O1N01O0O2O001O01O01O10O000001O0O2N100O001O001O1O1O1O1N2O3M2N3M1O2N1O2N4L0O2O1O2M_Tk0"}},
    {"image_id": 470779, "category_id": 35, "segmentation": {"size": [479, 640], "counts": b"jUZ31n>00000O10000000000I0_A0a>0^A1b>O^A1a>0`AO\\>5dAK[>6eAJZ>8eAHZ>9fAGY>:fAGX>;gAFW><iADU>>jACT>e0O1O100O1O1O1N2OKVBWOi=i0XBWOg=i0[BVOe=h0]BXO^=0^Bf05ZOZ=5_B?9\\OX=l0iBTOZ=g0hBYOY=e0hB[OP=2gB?;_Om<4gBNL9a0El<4hBMK8d0Fh<6dBJ32M6f0He<9hBIM5g0IP<2gC9EEN6g0Ko;1fC<CB35e0Lo;1fC=FGe0KP<0dC?GEg0Kn;1cCa0IAf0Mn;1cC>LD^=MeB`0NB]=NdB`00B\\=NcB`02BZ=OcB`0l=@QB`0Q>2401O0000100O1O1J7M2N2O10`^Q5"}},
    {"image_id": 470779, "category_id": 35, "segmentation": {"size": [479, 640], "counts": b"_o_24j>1O2O0O100O1O1O1O100O1N2OLdAF\\>:40000M_AJ_>75007]ABV>d0OGkAEO1T>:TBEk=;VBEj=:XBEg=<>000O0O020N2O1O1O10N1O0100001O0N20000000N01100O101O0001O00000000010O1M3O104K1O2N1OP?ORA1O0VAOf>231O00N2Oc]g5"}},
    {"image_id": 509014, "category_id": 35, "segmentation": {"size": [281, 640], "counts": b"n[Q34e81O0000Nld1OW[N0000001O0000000000001O00O10000O10[e40dZK1000000000001O00000000000000000000000000O10000O00g_j1"}},
    {"image_id": 509014, "category_id": 35, "segmentation": {"size": [281, 640], "counts": b"mUo21g82O1O010O000000000O11Ohd1OY[N0000000000000000000000000000010O0000000000000001O000000O1000000000000000000O11O001O000000O1000000000000000000O0100O1OTQk1"}},
    {"image_id": 509014, "category_id": 35, "segmentation": {"size": [281, 640], "counts": b"S`j23f80001O010N\\j01dUO00O1000O110O0000000O02OeR_2"}},
    {"image_id": 509014, "category_id": 35, "segmentation": {"size": [281, 640], "counts": b"YTi23f8001O01N10O01001O0000000000O10000O110O00ca00Z[_2"}},
    {"image_id": 509014, "category_id": 35, "segmentation": {"size": [281, 640], "counts": b"eoc31h8000000000000000000000000000d`g1"}},
    {"image_id": 509014, "category_id": 35, "segmentation": {"size": [281, 640], "counts": b"foc32f811O01O00000000000000000000O2O00US10klN1O0000000001O0000000000eYb1"}},
    {"image_id": 509014, "category_id": 35, "segmentation": {"size": [281, 640], "counts": b"PW_42g81N101O0000000O0100O1000O1000O100000000O010000000O10000O1OgUh0"}},
    {"image_id": 509014, "category_id": 35, "segmentation": {"size": [281, 640], "counts": b"Tfa42g81N100000000O10000000O0100000O010000O01O01001O00`Rg0"}},
    {"image_id": 509014, "category_id": 35, "segmentation": {"size": [281, 640], "counts": b"^VU31f83O0000O100000n[10QdN1001OeP3N\\oL1N2O01O10000000000000000O2OQdn1"}},
    {"image_id": 509014, "category_id": 35, "segmentation": {"size": [281, 640], "counts": b"bXf11h8000O20O010O00000000O1O10O011Oond3"}},
    {"image_id": 509014, "category_id": 35, "segmentation": {"size": [281, 640], "counts": b"lVk11h80\\j01cUO0O101O00010O1N11O0O1O101NXV_3"}},
    {"image_id": 509014, "category_id": 35, "segmentation": {"size": [281, 640], "counts": b"^ZW51g82O000000O10O10O1000O010O10O10O10Ng[3"}},
    {"image_id": 509014, "category_id": 35, "segmentation": {"size": [281, 640], "counts": b"V``43f80000000000O10dd12Z[N0000O10100O][i0"}},
    {"image_id": 516601, "category_id": 35, "segmentation": {"size": [360, 640], "counts": b"gja43S;2000O10O01Oef\\2"}},
    {"image_id": 516601, "category_id": 35, "segmentation": {"size": [360, 640], "counts": b"Sbi4220Q;4O1O1003L1OnnT2"}},
    {"image_id": 516601, "category_id": 35, "segmentation": {"size": [360, 640], "counts": b"Pnd62U;100001O10^n9"}},
    {"image_id": 516601, "category_id": 35, "segmentation": {"size": [360, 640], "counts": b"Rg`62V;0O1000010]U>"}},
    {"image_id": 562818, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"fXj21o>1O000000O[m^6"}},
    {"image_id": 562818, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"fRm22n>00000ZQ]6"}},
    {"image_id": 562818, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"PcS71o>1O0000000000000PVT2"}},
    {"image_id": 562818, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"01o>0000000PeY9"}},
    {"image_id": 562818, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"Xi_72n>0000OQl11oSN00000O1001O0Oifd1"}},
    {"image_id": 576031, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"bSo23l>1000001O0001O00000000000001O0000000000000000000000000000000000001O000000000000000000001O0000000000000000000001O00000001O0000000000000000000000000000000000001O000001N10001MX_?Nk`@2O000O2O0000001O000000001O000001O000001O0000000000000000000000000000001N0100001O000O1O10000O100000000000000001O0000001O000001O0001O00000000000000000000001O0000000000000000000001O0001O0000000000000000001O0001O000000000000000001O000000000000001O0000000001O00000001O00000001O000000000001O0000000001O00000000000001O00000001O00000000000001O0000000001O00000001O00000000000000000000001O0001O00000000000000000001O000000000001O00000001O00000000000000000000000000000000001O00000000O01O10O0100O100O10000Ol[P1"}},
    {"image_id": 576031, "category_id": 35, "segmentation": {"size": [480, 640], "counts": b"UnQ31n>101O00010O010O01O01O000010O01O00010O0000001O01O01O000010O0000010O00010O0000010O0010O0001O01O00010O00000010O0000001O000010O01O01O0001O01O00000010O010O010O01O00010O00000001O0001O000001O0000001O0O2O0000P?0PA0RYi4"}},
    #
    # "bottle"
    {"image_id": 632, "category_id": 44, "segmentation": {"size": [483, 640], "counts": b"^n]1:g>=E5CVOVBk0i=WOTBk0l=600001N5L2N1O10O01O005Hnlg7"}},
    {"image_id": 9590, "category_id": 44, "segmentation": {"size": [427, 640], "counts": b"`nZ6:m<8J4_NAPFb0o9GeE=Z:[1O0O2O0000001O0000000000001O00000001O001Of0ZOa0_O4K3N2N1O2M4L4L\\Za1"}},
    {"image_id": 10977, "category_id": 44, "segmentation": {"size": [375, 500], "counts": b"QcV4:U;9M2J6M300001O3M4L2Mh_\\1"}},
    {"image_id": 10977, "category_id": 44, "segmentation": {"size": [375, 500], "counts": b"`ba4`0R;6M21O001O1O2M6KZWR1"}},
    {"image_id": 15956, "category_id": 44, "segmentation": {"size": [480, 640], "counts": b"gY^7`0^>2N20000001^Om]j1"}},
    {"image_id": 32817, "category_id": 44, "segmentation": {"size": [640, 480], "counts": b"VdX6\\1^b0e0A5K0000000000O100000000O1000000000000O10000000000O100000000O3N1O3L5J8^OlW\\2"}},
    {"image_id": 32817, "category_id": 44, "segmentation": {"size": [640, 480], "counts": b"X\\P72jc0=Z\\O2gb0Q1C6K2M1O001N100O100N200001N10001O001O1O1O1O1O1N4M:F>\\OS_i1"}},
    {"image_id": 32817, "category_id": 44, "segmentation": {"size": [640, 480], "counts": b"n`W63^c0W1fNm0D2N10000000000000O1000000O100O1O2dNZ_OYOWa0NY]g2"}},
    {"image_id": 32817, "category_id": 44, "segmentation": {"size": [640, 480], "counts": b"moc689W1fa0d0N00000000000000O1000001N1O1O3]NP^OR1hb0Fm0POaR\\2"}},
    {"image_id": 32817, "category_id": 44, "segmentation": {"size": [640, 480], "counts": b"kom62mc05Ll0SOd0]O8H2N1O1O00000010N10002N=C4L001O0O2O2N7I5K:E7HeRm1"}},
    {"image_id": 51598, "category_id": 44, "segmentation": {"size": [640, 360], "counts": b"eV]21kc07_O?K4000000001O0000000000000K5H9HVbX4"}},
    {"image_id": 51598, "category_id": 44, "segmentation": {"size": [640, 360], "counts": b"bnb16bc08H9H7N2N2N2M3O1O1000001O01O003L7J1I6K7@anP5"}},
    {"image_id": 103585, "category_id": 44, "segmentation": {"size": [640, 425], "counts": b"^YW48gc09H0J600O11O5K1O00002Dkjj3"}},
    {"image_id": 110042, "category_id": 44, "segmentation": {"size": [640, 425], "counts": b"Wb^5k0ob06O1001O3M4L3LfQf2"}},
    {"image_id": 117908, "category_id": 44, "segmentation": {"size": [320, 500], "counts": b"jaj22m93N1O1O1O1O001O1O1O1O7I1O1O10O01O01O01O0010O01O010O010O010O010O00010O010O0100O010O001O001O1O0O2N1O2Kjga1"}},
    {"image_id": 133969, "category_id": 44, "segmentation": {"size": [427, 640], "counts": b"kn\\72Y=0XC`0d;BYDa0f;_OXDc0h;]OWDd0i;\\OVDd0k;>00001lNQDj0Z<N1O1N3M3M`dg0"}},
    {"image_id": 180751, "category_id": 44, "segmentation": {"size": [480, 640], "counts": b"dQ]1;e>k0TOd0^O1N0;E6J1O1O2N2N6Jd0SOTjh7"}},
    {"image_id": 180751, "category_id": 44, "segmentation": {"size": [480, 640], "counts": b"RR_4b0[>4B=000000=CQei4"}},
    {"image_id": 180751, "category_id": 44, "segmentation": {"size": [480, 640], "counts": b"TXk4`0]>4D<N10000<C5Hoo\\4"}},
    {"image_id": 180751, "category_id": 44, "segmentation": {"size": [480, 640], "counts": b"ZbU5<`>5K4G:N1001O<CleR4"}},
    {"image_id": 186632, "category_id": 44, "segmentation": {"size": [640, 480], "counts": b"_Pk72mc0>B2O001O1N2L5DYOY]Om0bb0;N1O1O00Ed]OnN`b0g0c0[Oo\\O7Sc0IP]O3Qc0LQ]O3ob0MR]O1ob00`00000000001NQhP1"}},
    {"image_id": 186980, "category_id": 44, "segmentation": {"size": [640, 457], "counts": b"WYa47Xc0a0N2O1N2O10001O01O:F:F5JgVT4"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"ko[8833Ra0`0L2L4H8O11O2N6J5K2Mnbd2"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"QkU86_a0:ADY_O>c`0`0I7O1001O7I5K2MYhj2"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"o_[75da07M2O000000000O100000OQad3"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"Pc\\7;Za0:O1O1N101O10O018G2Meoc3"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"TWb78n`08U_O0``05a_OM^`0Og_O1Y`0Kk_O5U`0Jl_O6T`0Hn_O8R`0FQ@9o?FR@:j`0Nfm^3"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"Yjg7a0]a01O000000000000000001N_VX3"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"ban7`0^a01N1000000001O000OScR3"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"ofX6?a0DW`0?i_OAR`0d0n_O\\OQ`0e0o_O[OQ`0d0P@\\OP`0d0P@\\OP`0c0Q@]OP`0a0Q@_OU`0;k_OEX`07\\^h4"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"noQ67`a0;n^OAY`0d0e_O]OV`0g0k_OYOU`0g0k_OYOU`0f0l_OZOT`0f0m_OYOS`0f0n_OZOS`0e0m_O[OX`0?i_OA[`0:ccn4"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"[\\l5j0Pa04K50O100O1O2N7I3MZhT5"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"X]l55ja00O00000001O00001NZgT5"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"miS4>^a06K2M2L4N11M3O012XOn^O`0Ya0O2MmVl6"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"SaZ4a0[a04L0M3013O1O2N10ONccf6"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"cT`4`0[a03N2M4I60O10010O6J2N5K=AlY_6"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"jkf46da0<_OBn^Oe0n`060001N1001O8H2M5BXUY6"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"bZk47fa0;F2OO01O00000000000000O2OYbS6"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"icR5?^a04M0000O01001O0000000000001NVgk5"}},
    {"image_id": 194875, "category_id": 44, "segmentation": {"size": [574, 640], "counts": b"[nT5<_a08B9O2O01O0O2O6K2M1N5K[Rk5"}},
    {"image_id": 197796, "category_id": 44, "segmentation": {"size": [478, 640], "counts": b"_jX44i>101O2N1O1O1O2bA5e=o0D4K2Ne0[Oa0_O5LO001O1O1\\MYDo1h;oM\\Dn1f;oM^Dn1\\<M9F:F_ef4"}},
    {"image_id": 197796, "category_id": 44, "segmentation": {"size": [478, 640], "counts": b"a3f07a0c<_O]Cc0`<^O`Cf0\\<[OcCh0Z<XOfCm0U<SOkCQ1Q<oNoCU1l;lNTDW1i;iNWDZ1f;fNZD\\1d;dN\\D]1c;cN]D]1d;bN\\D^1d;PN^D4Nl1e;lMcD5Ho1W<oMiCQ2X<nMhCR2Y<lMhCT2a<001O02N3N1O004L3M4L4L6I7H5L4L7H8I1N4LjXi8"}},
    {"image_id": 211042, "category_id": 44, "segmentation": {"size": [640, 458], "counts": b"WSW48fc0<E5K3N4L4L3M2N01N5oN^]O7_k`4"}},
    {"image_id": 229358, "category_id": 44, "segmentation": {"size": [423, 640], "counts": b"TYU32S=d0^O7H6K4L105J12M4M1N4L5J9H7H7IX^l4"}},
    {"image_id": 229358, "category_id": 44, "segmentation": {"size": [423, 640], "counts": b"^Uk11S=<F9F4Cb0G4N1O1O0O1010O00002N8H2M2O1O1N2O5J;]O[COkRT6"}},
    {"image_id": 238410, "category_id": 44, "segmentation": {"size": [480, 640], "counts": b"^Zg41V>n0G6K5L2M4L3N200O2N1O100001O002N3M3M4K5QOgBFPY[4"}},
    {"image_id": 262440, "category_id": 44, "segmentation": {"size": [640, 400], "counts": b"Y_g0`0Zc06O1000000001O2Mlll6"}},
    {"image_id": 279730, "category_id": 44, "segmentation": {"size": [333, 500], "counts": b"l[\\1d0h92M3N1N2K6F9M3N2O1O2N1O1O100O2O0O100O2O0O101N1O1O2N1O1N3L3M4K4hJ`Ma2c2PMmMm2T2fLYNY3i1ZLcNe3^1nKoNR4R1iKROW4o0fKSOZ4n0dKSO\\4n0cKRO^4P1]KROe4S1RKPO`5e23M1O1O0010O00010O01O010O1O010O1O2M6eKlIa35gLX6V1jI36aNT6W1mI1j6K[INk6[OPJ;Z6WOljP3"}},
    {"image_id": 279730, "category_id": 44, "segmentation": {"size": [333, 500], "counts": b"`4l5a40O100000000O10000N2I7E;I7M3N200O1001O001O3M8H8H6J5K1O00000000001O000000001O00001O001O1O2[J^K[5l4N1]K]KZ3d4bLaK\\3_4cLcK\\3^4bLdK]3]4aLfK]3[4aLiK\\3X4bLSLT3P4gLcLh2V6QMoGW2e8]O]i_4"}},
    {"image_id": 286907, "category_id": 44, "segmentation": {"size": [640, 480], "counts": b"^iX42ac0f0D5M4[OTOo]On0la0g0M2O1O11O0O1O4M2L3N4K7ITch4"}},
    {"image_id": 296231, "category_id": 44, "segmentation": {"size": [480, 640], "counts": b"afR5e0W>:G4H7N2O1O12N8H3M3L5Lc0\\OkUS4"}},
    {"image_id": 306733, "category_id": 44, "segmentation": {"size": [426, 640], "counts": b"Qfn02W=2O000O100000001O000WCL\\<7^CMa<`0N2N2N1O00[OgC9Z<BlC<b<O1N7Ha\\R7"}},
    {"image_id": 322163, "category_id": 44, "segmentation": {"size": [480, 640], "counts": b"eU[67c>7L4N101N1M3N2K500O11O1O<^OiXj2"}},
    {"image_id": 322163, "category_id": 44, "segmentation": {"size": [480, 640], "counts": b"Xi`64`0Ne=j0K400000O1ROaB9b[h2"}},
    {"image_id": 340697, "category_id": 44, "segmentation": {"size": [333, 500], "counts": b"Z^d08R:7CB`Fd0\\9:L3N2M3N3L3M4L3M3M4L2M3N1O1002N1O001O001O002N2N1O1O1O1O001O1O1O6J2N1O1O000O2O001N5L3L4L8H2N3L3N2NnVm3"}},
    {"image_id": 340697, "category_id": 44, "segmentation": {"size": [333, 500], "counts": b"][U18R:;E7J8H7J5L2M4M1N2N100O1O1O1N2O1N2O1O10000002N1O1O1O1O1O1O2N1O1O001O1O001O1O1O4L5K2M9H4L4L7I5G[c]3"}},
    {"image_id": 340697, "category_id": 44, "segmentation": {"size": [333, 500], "counts": b"j^k1:o9:H9H5J6K5J6I;G2O1O00000001O1O1O1O1O1O2N1O1O1O1O1O1O001O1O001O8H1O00001O00000O101N1O4K?]O[_h2"}},
    {"image_id": 340697, "category_id": 44, "segmentation": {"size": [333, 500], "counts": b"]e^28P:a0A;F2N2O1N2CmN_GT1_8>O1O100O1O1O101OO101O1O1O2N2N1O1O1O1O1O1O001O001O001O4L4L1O1O001O0O3Lg0ZO]cU2"}},
    {"image_id": 349480, "category_id": 44, "segmentation": {"size": [450, 640], "counts": b"`_j35j=6]OHSC=j<`0N2M3N001N110002N1N1000O10O1N101O0O2O1O002N3L4N1N4L2N3N2M2N3Kki_4"}},
    {"image_id": 350679, "category_id": 44, "segmentation": {"size": [428, 640], "counts": b"gSn52X=4nC7\\:KYE`0e:BjDn0V;e0]OTNbEo1V:g0O2M2N3N1O100O2O000O1L4N200O100O1000000O1O1N2N2M3N2O1O100001O002M=C2K5K4H9F:G8H:YN`DU1Q<E;F:Eg`h1"}},
    {"image_id": 360564, "category_id": 44, "segmentation": {"size": [427, 640], "counts": b"WRg4<m<3J5N20000006J2M5I[d_3"}},
    {"image_id": 389109, "category_id": 44, "segmentation": {"size": [640, 427], "counts": b"Tj`3g0Wc02N2N2N2N2SOm0O010000000000O101O8H8]Nk]Ok0gb0N1O1O2NmY\\4"}},
    {"image_id": 440184, "category_id": 44, "segmentation": {"size": [425, 640], "counts": b"YQ89n<2O2O01O5JoRo7"}},
    {"image_id": 446574, "category_id": 44, "segmentation": {"size": [640, 428], "counts": b"Wmg44k02Pb0T1K1O000011_O\\]O^Olb0>T]OBQc09P]OFSc07m\\OIkc0Jce\\3"}},
    {"image_id": 474786, "category_id": 44, "segmentation": {"size": [500, 375], "counts": b"ofa33`?2C=@`0N101N1O1D=M2O2O0O2O00001O00001O010O01YNcBU1o=0O01O2M5nN_hg1"}},
    {"image_id": 474786, "category_id": 44, "segmentation": {"size": [500, 375], "counts": b"oln3:`>k0G8N3O0O2O0CaNdBa1Z==O1O2O001O00001O0010O010oMjBb1h=L1O1N3E;VOha[1"}},
    {"image_id": 492362, "category_id": 44, "segmentation": {"size": [640, 427], "counts": b"]lU13jc03N2M3M3N2N2M3N2N2O1O10O01O1O0001M3N2N3L4M3L_df6"}},
    {"image_id": 541773, "category_id": 44, "segmentation": {"size": [480, 640], "counts": b"iaf475KX>c0K3E;N2000O3N;D4L5K7DXj_4"}},
    {"image_id": 551794, "category_id": 44, "segmentation": {"size": [480, 640], "counts": b"QUj33k>5J4M3M3N2N1O10O10O01M2O101O1O2CilY5"}},
    {"image_id": 551794, "category_id": 44, "segmentation": {"size": [480, 640], "counts": b"[e`45h>3L4N3O0000J7LPcg4"}},
    {"image_id": 579070, "category_id": 44, "segmentation": {"size": [427, 640], "counts": b"TbZ27S=9G:F4MOGXOoCj0o;90001eDlN^:T1bEmN^:R1bEPO\\:P1cERO]:m0cEUO\\:k0YEmNJ;l:g0XEDh:<YEDg:;YEEh:;YEoNH=P;c0YEmNJ?n:c0aE[O`:d0aE[O`:d0aE[O`:e0`EZOb:d0_E[Ob:d0aEYO`:g0S1O002N5N23I<D00O2M3M4M6ZO_C5T=GdP`5"}},
    #
    # "bowl"
    {"image_id": 14038, "category_id": 51, "segmentation": {"size": [427, 640], "counts": b"_\\65V=8H00000000000000000000000O100001O0000000000000000O1000O101O000000000O1N1O2O1N2N3O0Oiab7"}},
    {"image_id": 34873, "category_id": 51, "segmentation": {"size": [480, 640], "counts": b"XUP43m>2M3N3M100000O01O1O00100O0000MTR>MRnA6I2O01O0O0100000O1O1O001O1O1O1N2N2O2Mgl\\4"}},
    {"image_id": 52996, "category_id": 51, "segmentation": {"size": [426, 640], "counts": b"P:m0]<00000000000000000O01000000O100O100O101O0O00100O1O2N1N2M3N3M2N2O2N3LP\\k7"}},
    {"image_id": 86582, "category_id": 51, "segmentation": {"size": [427, 640], "counts": b"PZa75U=3N2N1N3N1O1O2N2M2O1O1O1O1O1O1O1N2O1O1O1O2N1O1O00000000001O0000000O1000000000000001O00000O1000000O1O1O1O1O1O100O1O1O1O1O1OkF"}},
    {"image_id": 96001, "category_id": 51, "segmentation": {"size": [426, 640], "counts": b"cYo26R=5L3N2M3NA[COO8e<GcC8h<000O100O1O10O01O100O1O001O001O00001O01O000000000000O10000000000000000O100O01000000O01000O010O00010O1O001N10O10OKBaC=`<53K6IgR_4"}},
    {"image_id": 171740, "category_id": 51, "segmentation": {"size": [480, 640], "counts": b"Xl^74l>1O2N1O1O001O1O00100O001O1O000000000000000000001OO100000000000000000000O10000O10O01000O01O1O1O2N1O3KiVU1"}},
    {"image_id": 175364, "category_id": 51, "segmentation": {"size": [461, 614], "counts": b"Tfn08T>4M1O001O0O10000000000000000000000000000000000000000000O1000001O001N7Gc`U7"}},
    {"image_id": 195165, "category_id": 51, "segmentation": {"size": [478, 640], "counts": b"PmV75g>2O10001O0000001O001O1O1OO2O0O1O2N2MXoj1"}},
    {"image_id": 195165, "category_id": 51, "segmentation": {"size": [478, 640], "counts": b"fdS762La>:N100O101O000000001O000001M2N3K4O2O2Mahm1"}},
    {"image_id": 195165, "category_id": 51, "segmentation": {"size": [478, 640], "counts": b"jW`74i>2N2O001O000000001O001O001O1O01O0O1N3M3Maf`1"}},
    {"image_id": 195165, "category_id": 51, "segmentation": {"size": [478, 640], "counts": b"odZ71k>3N10O01O1O10000O100000000000000001O0000010O001N2Ninc1"}},
    {"image_id": 195165, "category_id": 51, "segmentation": {"size": [478, 640], "counts": b"a`j74i>2N2O001O00000000001O00001O0010O001M2N3Mj]V1"}},
    {"image_id": 195165, "category_id": 51, "segmentation": {"size": [478, 640], "counts": b"_Zf71k>20000N3N1O2O1O1O5EBkA?T>BlA>T>BlA>U>@mA`0X>00000001O0000IAoA?Q>APB=Q>CoA:T>FlA9U>HjA6X>JgA3]>Mo[W1"}},
    {"image_id": 221872, "category_id": 51, "segmentation": {"size": [427, 640], "counts": b"T_2f0Y<>C=I6ZOf0E:F;B=]Oc0^Ob0SOm0TOcJWIP6a6a0N2M3N101O1O1O\\KfIY2Y6eMWJn1h5RN^Ji1a5WNeJd1[5[NkJ`1T5`NQK\\1o4cNTK[1l4bN]KX1b4iNcKR1]4nNiKl0W4TOjKk0V4VOjKi0U4YOlKe0T4ZOmKf0S4XOPLg0P4VOTLi0k3WOVLi0j3VOYLh0g3WO[Lh0e3WO]Lh0c3WO^Li0b3VO_Lj0a3UO`Lk0`3TOaLl0_3SOcLl0]3SOdLm0\\3SOeLl0[3TOfLk0Z3UOfLk0Z3UOgLj0Y3VOhLi0X3WOiLh0W3XOiLh0W3XOjLg0V3YOkLf0U3ZOmLd0S3\\OoLb0Q3^OPMa0P3_ORM?n2ASM>m2BSM>m2BTM=l2CUM<k2DVM;j2EWM:i2FWM:i2FXM9h2FYM:g2E[M:e2E]M:c2E^M;b2D`M;`2EaM:_2EbM;^2EcM:]2EdM;\\2EeM;Z2ChM=X2CiM<W2CjM=V2CkM<U2CmM<S2CnM=R2CnM=R2BoM>Q2BPN=P2BQN>P2APN?P2@RN?n1ARN?n1ASN>m1BSN>m1ATN?l1AUN>k1BUN>k1AWN>i1BWN>i1BWN>i1BWN=j1CVN=j1BXN=h1CXN=h1BYN>g1BYN>g1A[N>e1B[N>e1B\\N=d1C]N<c1D]N<c1D^N;b1E^N;b1E^N;b1E^N;b1E_N:a1F_N:a1F_N:a1F_N:a1F`N9`1G`N9`1G`N9`1GaN8_1HaN8_1HbN6_1JaN6_1JaN6_1JbN5^1KbN5^1KbN5^1KbN5^1KbN5^1KcN4]1LcN4]1LcN4]1LdN3\\1MdN3\\1NcN2]1NcN2]1NdN0]10cN0]10cN1\\1OdN0]10cN0]10dNO\\11dNO\\11eNN[13dNM\\13eNL[14eNL[14eNL[14eNL[14eNL[14fNKZ16eNJ[16fNIZ17fNIZ17fNIZ17gNHY19fNGZ19gNFY1:gNFY1:gNFY1;fNEZ1;fND[1<fNCZ1=fNCZ1=fNCZ1=fNCZ1>fNAZ1?fNAZ1`0eNAZ1?fNAZ1?fNAZ1?fN@[1a0eN^O[1b0eN^O[1b0eN^O[1c0dN]O\\1c0eN\\O[1d0eN\\OZ1f0fN[OX1e0hN[OX1e0hN[OX1e0hNZOY1f0hLcNoNh0X4e0iLdNnNg0Y4f0gLeNPOa0\\4j0dLeNPOa0\\4j0dLfNoN`0]4k0cLeNQO`0[4k0dLeNQOb0Y4i0fLeNQOb0Y4j0eLeNQOa0Z4j0eLeNRO`0Y4k0eLfNQO?Z4k0eLfNQO?Z4k0eLgNPO>[4l0dLfNQO>[4l0dLfNRO=Z4m0dLgNQO<[4m0dLgNQO<[4m0dLhNPO;\\4n0cLgNRO:[4o0cLhNQO9\\4o0cLhNQO9\\4P1bLgNRO9\\4P1cLgNPO9]4P1cLgNQO8\\4Q1cLhNPO7]4R1bLgNQO7]4R1bLhNPO6^4R1bLhNPO6^4R1cLhNnN6_4R1cLhNoN5]4T1dLgNoN5]4U1cLfNPO5]4U1cLfNPO5]4U1cLgNPO3]4V1cLgNPO3]4W1bLfNQO3]4W1bLgNPO2^4W1cLfNoN3^4X1bLeNQOMYNIT6e1bLfNPOLZNIT6e1bLfNPOL[NHS6f1cLfNoNJ\\NJR6f1cLfNoNJ\\NJR6g1bLeNPOKc4`1^LeNnNKd4`1^LeNnNKd4`1^LeNnNKd4a1]LdNoNKd4a1]LdNoNKd4a1]LeNnNIf4c1[LdNoNIf4c1\\LcNnNJf4c1\\LdNmNIg4c1]LcNlNKf4c1^LaNlNLf4c1^LaNlNL]NIT6k1cLaNkN0a4_1dLbNjNJ_NJS6j1eLaNiNK_NJS6k1dL`NjNK`NIR6l1dL`NjNK`NHS6m1dL_NiNLg4f1_L_NiNKh4f1_L_NiNJi4h1]L^NjNKh4g1^L^NjNKh4g1^L^NjNKh4h1]L^NjNJi4h1]L^NjNJi4h1^L]NiNKi4i1]L\\NjNKi4i1]L\\NjNKi4i1^L\\NhNJk4k1\\L[NiNJj4l1]LZNiNJj4l1]LZNiNJj4l1^LYNhNKj4l1^LZNgNJk4l1_LYNfNKk4m1_LXNeNKl4n1^LWNfNKl4n1^LWNfNKl4o1^LUNfNLl4o1_LUNdNLm4P2^LTNeNLm4P2^LTNeNLm4Q2]LSNfNLm4Q2^LRNeNMm4Q2_LQNdNNm4R2_LoMdNOm4R2_LoMdNOm4R2_LoMdN0k4S2aLkMeN1k4T2aLjMdN2k4U2TNkMl1V2SNjMm1V2SNjMm1W2RNiMn1W2RNiMn1W2RNiMn1X2QNhMn1Z2QNfMo1Z2QNfMo1[2PNeMP2[2PNeMP2\\2oMdMQ2\\2nMeMR2\\2nMcMR2]2nMcMR2^2mMbMS2^2mMbMS2_2lMaMT2_2kMbMU2_2jMaMV2_2jMaMU2a2jM_MV2a2jM_MV2b2iM^MW2b2iM^MW2c2hM]MX2d2gM\\MY2e2eM\\M[2e2dM[M\\2e2dM[M\\2f2cMZM]2g2bMYM^2h2aMXM_2h2aMXM_2i2`MWM`2i2_MXMa2i2^MWMa2j2_MVMa2k2^MUMb2l2]MTMc2l2]MTMc2m2\\MSMd2n2ZMSMf2n2YMRMg2o2XMQMh2o2WMRMi2o2UMRMk2n2TMRMm2P3QMPMo2Q3oLPMQ3R3mLnLS3S3kLnLT3T3kLlLU3U3iLlLW3T3hLmLX3T3fLmLZ3T3eLlL[3T3dLmL\\3T3cLlL]3U3bLkL^3V3`LkL`3V3_LjLa3W3^LiLb3X3]LhLc3Y3[LhLe3Y3ZLgLe3[3ZLeLf3\\3YLdLg3]3YLbLg3`3XL_Lh3b3YL\\Lg3e3YLZLg3g3XLYLh3g3ZLWLf3h3\\LWLd3S3UJgL\\25_3R3VMmLi2S3XMmLh2R3[MlLe2S3]MlLc2T3]MlLc2S3^MmLb2S3^MmLb2S3^MmLb2S3^MmLc2Q3_MnLa2R3_MnLa2S3^MmLb2S3^MmLc2R3]MnLc2R3]MnLc2S3\\MmLd2S3QLiLPO4P5S3lKmLSO0Q5T3hKPMVOLS5T3cKUMXOGU5V3`KUMZOEW5X3YKVM@BX5Z3PK[ME\\O\\5\\3iJ\\MIXO_5b3[J]M5POb5l3gI^Me0fNe5e5WJ\\Jj5i5jI]JX6Z64L5K:E<E:F>B:E>B:G8G=C:G9E:G8H<D<D:E:F<B`VQ3"}},
    {"image_id": 289415, "category_id": 51, "segmentation": {"size": [428, 640], "counts": b"lb`15V=:G2N1O0O2O0000000000000000000000000000O100000000O1000000000000O101O0000000000000O10001N100O1O1O2O0O100O2O001LT`S6"}},
    {"image_id": 397681, "category_id": 51, "segmentation": {"size": [640, 640], "counts": b"]do34jc05X\\Od0eb0>M3M2N2O000000O10000O100000000000000000000000000001N01000000000000000000000000010OO10001N1lN`]Oh0`b0UOj]Ob0Pc0[O`Sa7"}},
    {"image_id": 470773, "category_id": 51, "segmentation": {"size": [480, 640], "counts": b"^V^24g>6K4N1gADm=?RBDj==WBCg=>ZBCd=>[BCc=>]BD`==aBC^=>aBC^==bBD\\==eBCZ=>eBCZ==gBCX==hBCX==hBDW==iBCW=<iBEV=<jBDV=;jBFV=9jBGW=8jBHV=8jBHV=7jBJV=6jBJV=5jBKW=4jBLV=4iBMW=2jBMW=3hBNX=1hBOY=0hB0X=OhB1Y=OgB1Y=NgB3Y=MgB2Z=NeB3[=MeB2\\=NcB3\\=NcB2^=NbB1_=O`B2`=O^B1b=g00O1O1O010O001O1O0O2O000O2M2N2N3N1O1O2N101M:Gj]n5"}},
    {"image_id": 512330, "category_id": 51, "segmentation": {"size": [640, 426], "counts": b"j;1oc01Y\\O0Zc04d\\OM[c03c\\OO]c02a\\OO_c0:O00000O101O1O0O01001O00000000O1O100001O1O0000010O0000O100001O000000000000O1000000000000001O00O1000000000000001O00O100000O1000O11O1O00O10000000000O1000000O1O2O1OXTd6"}},
    {"image_id": 516871, "category_id": 51, "segmentation": {"size": [418, 640], "counts": b"[aX31o<3N2N2N3N1O1O00001O0O10O01001O0001O1O1N5LO100O2M2O1N200O001O100O101N10000O10000000000O100N200O100000000O`\\90acF6J1O1O1O00001O00001O01O0100O1O1XDAk:`0REDl:=REDo:=nDDS;>^DCM1h;P1000O2Jf0\\OiQc3"}},
    {"image_id": 526197, "category_id": 51, "segmentation": {"size": [640, 428], "counts": b"U6X1hb00O100000000O1000O100000000000000000000000O1000000000O100000000000000000O10000000O10001O00000000000000000O10001N100000000000000000000000001O0000000000000000001O00000000000000001O0000001O000O10001O0000001O0000001O001O0000001O0O10001O001O001O1O1M3Ehim5"}},
    {"image_id": 529966, "category_id": 51, "segmentation": {"size": [421, 640], "counts": b"^n]4`0`<;F8J4J7K4L5K4L4L4M3M3L6K5K4K6K5KQOWFgNe9X1_FhN^9W1eFkNW9U1lFkNQ9U1PGmNm8R1VGoNg8P1]GPO`8Q1`GQO]8o0fGQOW8n0kGTOR8l0PHUOm7k0THWOj7h0XHYOe7h0\\HYOa7g0bHXO\\7h0eHZOX7f0jHZOU7ZOnG9o0>P7VOYH8h0b0n6ROaH9b0e0k6QOgH7?j0g6nNoH5;m0d6mNUI29S1_6jN[I18U1\\6hNaIO5Y1X6hNeIM5\\1T6fNjIK3`1Q6eNiK[1U4eNmK[1R4dNPL\\1n3dNSL]1l3cNUL]1i3cNXL^1g3aN[L_1c3aN_L_1`3aN`L`1_3_NcLa1[3`NeLa1Z3^NhLa1W3`NiLa1V3^NlLb1S3^NmLc1Q3]NQMc1m2^NSMb1m2]NVMb1i2^NWMb1h2^NYMc1f2]NZMd1d2]N]Mb1c2^N]Mc1b2\\N`Md1^2]NbMc1^2]NbMd1]2\\NdMc1[2]NfMd1Y2\\NhMc1X2]NhMd1V2]NjMc1V2]NkMc1T2]NlMc1T2]NlMd1R2]NoMb1Q2^NoMb1Q2^NoMc1P2^NPNa1o1`NQNa1n1_NRNa1n1_NRNa1m1aNSN_1l1aNTN_1l1aNUN_1j1bNUN^1j1cNVN]1j1cNWN]1h1dNWN\\1i1eNVN[1j1eNVN[1j1fNUN[1j1fNVNY1i1hNWNX1i1iNVNX1i1hNWNX1i1iNVNW1j1jNVNU1i1mNVNT1i1mNVNS1j1nNUNR1k1oNUNP1k1QOTNo0l1SORNn0m1SORNm0n1TOQNl0o1WOoMh0Q2YOnMg0R2\\OkMe0S2^OkMb0U2@iM`0W2CfM=Z2EdM;\\2EeM:[2FeM:[2EfM;Z2DgM<Y2BiM>W2AjM`0U2_OlMa0T2^OmMb0S2]OnMc0R2\\OoMd0Q2[OPNe0P2ZOQNf0o1YORNg0n1YORNg0n1XOSNh0m1WOTNi0l1WOTNi0l1VOUNj0k1VOUNj0k1VOUNj0k1UOVNk0j1UOVNk0j1TOWNl0i1TOWNl0i1TOWNk0j1UOVNk0j1UOVNk0j1TOWNl0i1TOWNl0j1SOVNm0j1SOVNm0j1SOVNm0j1SOVNm0j1SOUNn0k1ROUNn0k1ROUNm0l1SOTNm0l1SOTNm0l1SOTNm0l1SOTNm0m1ROSNn0m1ROSNm0n1SORNm0n1SORNm0n1TOPNl0Q2TOoMl0R2SOnMm0R2SOnMm0R2SOnMl0S2TOmMl0S2UOlMk0T2UOkMk0W2UOhMk0X2UOhMk0X2VOfMk0Z2VOeMi0]2VOcMj0]2WObMh0_2XOaMh0_2ZO^Mg0c2XO]Mg0d2ZO[Mf0e2[OZMe0f2\\OXMd0j2\\OUMc0l2^OSMb0m2@PMa0Q3^OoLa0R3AlL?T3CjL<W3EgL<Z3EdL:]3GbL9^3J^L6d3KZL4g3OVL1j30TL0n30QL0o31PLNR41nKOR40nK0S40mKOU40jK0W4OjK1W4NhK2Y4MhK3X4MgK3[4LeK3]4LcK3^4LbK5^4KbK4`4K`K4a4LWKgN`M]1[7KTKkN^MZ1_7KRK<P5CPK<Q5DoJ;S5DlJ<V5CjJ<W5DiJ;Y5DgJ;Z5EeJ;]5EbJ:_5F`J:b5E^J9e5F[J9f5HXJ8j5GVJ8l5HRJ8P6GPJ8Q6ImI5W6JhI6Y6KfI3]6M`I4b6K^I3e6LZI3i6MVI1l60RIOQ71lH0V7OiH0Z70dHO^72`HNb71\\HOg72VHNl72QHOQ81lGNX82fGN\\82aGNb84YGMi84SGLQ95iFJ\\99YFLj9e13M3M4J6L3K6L4L4K5K5K6J5K7H8GcQ="}},
    #
    # "banana"
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"lTf58:I\\<d0O0O10000O1O101N1O2N1O1000001O00001O0010O01O0001O0010O01O001O1O010O1O1O1O1O0O2O1O2M3K7Fk[Q2"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"R_X6<h<8M10000O101O0O1O100O1O10000O100000O100000000000001O0O2O1K5M4L3N4J`dc1"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"fnd64c<0jC3U<NhC4W<0cC3]<=0000O01000000O100000000O10000000000O1000000O100O2O1O0O2O2M1N3GiZV1"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"TkS5<h<6O2N1O10001O010O0000010O00001O1O10O01O0001O01O0001O01O000001O00000000001O0000001O001O1O2M5L5GPCNW=NPPb2"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"fPi4<j<6L3O0O2^C]O[<c0dC_O[<a0eC_OZ<i00000000001OMhCUOW<k0kCTOT<l0500001O0010O10000O010M3N1BiCHY<3b0MfZT3"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"f`_67m<7K4J7L3N2O1O1O1O1O2N1N2O1O1O001O1O1O1O01O1O1O100O1O2N2N3M5K2O0O2M2O1N2N3L3N3N2O1O3KbkX1"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"V^S6:m<:G4L3M3N2N2M3N1O2N2O0O2O000O2O000O010001N101N101N2N2M3L4H9H7IY`i1"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"Td^53U=4L4N3L3N2N2N2N2N1O2N1O1O1O2N1O10O00010O00001O001N10001N1O2O001N101O010O001O1O010O1O00100O1O2N1N5HjiV2"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"o\\n46S=3L5M1M3N2N2N2N20000O00100O0100O0100O010O0010O01O01O00010O00001O01O0001O01O01O1O2O1N2N2N2N2N2N2N1O1O1O1N2O1O2Nd`d2"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"_iS54U=4K5L4K3N1O2N1N3N1O1O2O000010O1O010O2N101N2N1O2M3L4L4L4M3Mmni2"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"_[b58m<6J5K6L3N2N2N2O2M2O1O1O2N10001O001O000010O100O101N2N4M6I9UOj][2"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"Rkn5;l<5L3N2M3M3N1O2N2N1O1O0000O1O10000O2O0000000100O00100O0010O01O01N101O1O1O1N3N1O2M4L4M3LQTi1"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"hg[63V=1O1O2N2N2N2M3N2N2M3N2M3N100O010O01N101O001O10OO2O1O1O1O2N101M2N5KV\\`1"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"lk_62V=4L4M4L5K2N100O010O10O1000O0100000O10001O0001O1N2M4L8Fag^1"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"lWo57R=1N2O1N1O1O1O1O1N2M3O1O1000001O0000000O10001O00001O00001O000010O01O100O10000000O1O1O2N1O2N2N4L6J6HcWf1"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"VZg51T=6L4L3M3N2M3N2M3N3M2O2N2N2O3L4M5K7I5KO1L4N2L5L3M4N2M3L5K6K3M4I8IUWU2"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"obT59j<9K5M2M3O1N2N2O1N1O2O001N2O100O100O2O10O01O1O1O10O0100O01N2N2N2K6G9I6Iaef2"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"_Xh62W=1O2N100O1O1O1O1O1O1O1O1N2N1O2M3N2N2J61O002N6I4K6K4JahV1"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"]`S741Nl<>L2M3O0O101N100O2O000O10001O000000000O100000001O000000O10O10000O10000001N101O1N3M2N3M2N3L3M5Jghb0"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"R_b71X=2N2O1O001O2N2N2N1O2N2N2N2N2N1N2O1O2N001O1O0010O0000001O000O2O0O2O1N2O0O2N3M3M3M4K_Y6"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"UWR77S=4K4M;E1O1O010O0010O00001O001O001N2O001O00001O001O001O001O1O001N2O001N2M3N`Vh0"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"STU76R=3N101N2O001O001N101O001O001N101O00001O1O0O2O001O001O0O2O001O000O10O1000000O100O100O2O0O1O2O1M3M4L4KSm?"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"h]b71Y=1N100000000010O01O000001O0001]CNl;3QD0n;2nC0R<2iC1X<`00000010O000O101N100O101N100O1O01001N2O7I2MPh6"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"k^b71X=4M0O2O0O101N100O100O10000000000000O10000000000000O100O2O0O1O2O0O2O1O0O2O001O0OO101O100O1O1N2O1O1N2N2O2N3MeZ1"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"fSU77R=2M2N2O1N2O1O100N2O001O100O1O100O00100O1O100O10O0100O010O010O0100O01000O01000O1O001O100O100O2N1O1O2N1O2N2O1N4Gek="}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"icR71U=6L3L3N2O0O100O0010O10O10O01000000O1001O01O0000001O010O001O01O01O1O010O010O00100O0100O0100000O10001O0N2N3K4Kei`0"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"e]n63R=;Fd0\\O=C4M3N2M3N2O0OO2N2O2N1O2N101N3N1N2N2O2M2O2M3M2M4J6J8DQ\\o0"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"bUc65U=3L7J2N0000O100000000O2O00100O01iCG\\;9aD0Z;0bD4];OZD7f;g0001O1N3M1O2M:AQ][1"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"W`d72X=000O2N100O1O1O1O2N100O1O1O2O0000001O01O00010O001N2N2H]S:"}},
    {"image_id": 8844, "category_id": 52, "segmentation": {"size": [426, 640], "counts": b"\\]Q72V=3M4L3N1011N2O0M4M101N1Nc]S1"}},
    {"image_id": 28809, "category_id": 52, "segmentation": {"size": [500, 498], "counts": b"keP51c?1O001N101O001O001O00001O010O001O00001O00001O0000001O00001O00001O00001O0O101O0000001O00001O0000001O0000001O00000O101O0000001N10000O101O0L40000O11O01N1000000000001O000N20000O1O1000000O10O010O1O001O001O100O00001O001O001O1O1O0O110N2O1O1O001N2O0O2O0OO20O101O0O2O0O2O2N1O000O101O1N2N3M]e="}},
    {"image_id": 78959, "category_id": 52, "segmentation": {"size": [640, 384], "counts": b"]`Y47^c0=L4N3M1O1O2N1O1O0V]OQOcb0P1Z]OSOeb0U11N1O2N2N3N1N2N2N2N3N3L3M5L4K3Lhbe2"}},
    {"image_id": 78959, "category_id": 52, "segmentation": {"size": [640, 384], "counts": b"\\eY45jc02N2N1O2N1O2N2N100O101O0001N101O0O2O1O0O1000O010N10O10O0010O2O2MTga2"}},
    {"image_id": 78959, "category_id": 52, "segmentation": {"size": [640, 384], "counts": b"Pdh31oc02N1O1O2N1O2N1O1O1O2N1O1O2N1O1O0000O4M2N2O1N3M2N3L`SW3"}},
    {"image_id": 78959, "category_id": 52, "segmentation": {"size": [640, 384], "counts": b"VXP35ic08I2O2M21Oi\\ODjb0;T]OHlb0f00100O010O010O000010O00000000000O1000000O100O1O10O01000O01O1O001O001O00001O0O2BQ[b3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"feZ41kc07G7L4YOBf]Oc0ma0o0F:L4J5M4L3M4M2M3N2M3N2N1O1O010N11O01O01O0101N100O1O2O000O10001O0000000000001O000000O10001O0O101N101N2M3N2N2N2M3N3L3N3L3K6L3M4K4M4K5K4L5K5K5J7K5JVV`2"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"eSe5l0Pc0>B:E:G8H7I6J7I6K5Jg0VO9J5M4M2O0O2N1000001O00000000000000O2N1O1N2L5K4L4K6M2N3N2N2N2N2N2M4M3M3L4L5K5K5J6I:D?@ndd1"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"Ub`61nc03M3N3M3M2M4M3M4M5J;E]1cN4L3M3M3N1N2N2N2O0O2O0O1O2O1N2O1N6K4K2O1O0O10000O10O00100O1O1O1O1O1O1O2N1O2M2O2M3M3K5K6H8G9I7G:I7J7H8H;Ckkb0"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"_^[72nc02N1O1O2N101N1O2O1N2N2O1N3N2M3N3M2P_O\\O^>h0XA@g>d0o@Co>b0h@CX?c0]@Ca?k0i_O^OW`0V201O0O2O001O000010O01O101N2O1N100O10O1O0O2O1N2N1O2O2M2N4IP@"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"WX_27?1Yb0R1J5L4M2N3L3N2O1N2N2N2O0O2O0O1O10O00001O010O1001N10001O0O101O000O1000000000000O10O2O0O10000O100O2O0O1O1O1N3N1M4I6M3L5M2N3M2O2M2O2N2N101N1O2O1N2N101N2O1O1N2O001N2O1O1O2N1O1O1O1O2MfRT4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"ljU23hc07K4L5I6I6L4N3M2M3O001N2O000O10000000000000001O00001O10O01O0010O01O0010O00001fNf]Om0Zb0QOo]Oh0Rb0VOQ^Oh0db0O2N1N3N1O2N1O1O1N2O001O00001O00001O0001O0001O0000010O0010O01O010O01O010O010O00100O1O010O1O1O010O1O1O1O001O1O1O10000O20O001O010O1O1O1N2O1N3M3N2M4Mljm3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"oaj2=]c0<Fj0VO5L4L4L4L4L3N2N2L4N101N20O01O000000O001O1O0O20O010O01001N010OjMi^Of1Wa0VNR_Oe1n`0YNW_Od1i`0YNl_OU1ga0G8H6K5J4L5KSRf4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"Vin29ec04L3K4L5G8L5K4N2N2N2N2O0O2N100O2O000O1000001O000001O01O001O01O01O010O01O010O010O10O01O010O1O1O00100O1O001O1O1O001O1O1O1O100O1O10001N100000001O001O0O2O001N101N2N2N2N2N2O2M4L6JZhe3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"`lS22mc03O0O1CKi\\O:Tc0Jg\\O:Vc09N2M3O1N1O2O1N3M2O1N2O1N2O1O001O0001O01O0001O01O010O1O010O10O010O01000O010O10O0100O01000O1O1N1O2O1N2N2O1N2O1N2O1O1O001O1O2N1O1O1O100O2Ch\\OOfc0N3MiTh4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"dUP26gc05K4M3M3M2O2M2N2O1N2N1O2N1001O001O1O1O1O2M2O1O1O1O00001N11O000001O010O001O0010O01O1O010O1O010O010O010O1O0N3FPPY5"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"Smi14kc02M3N2M3M2O2M2N2N2N2N101N1002M9H2M4L3N2M2NYkS6"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"iVa12lc03M3N2M2M4M2N3L4L3M4M1O2N2N1000001O0O101O001OlN]]Ol0db0QOb]Ol0]b0ROh]Ok0hb0O1N10001N1O101N001N2M2J7L4MTZQ6"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"mPa32gc0b0F6I3N3L3N2N1N2O2M6J4L4K3N2M2N1O2N2N1O1N3M2O001O1N2O001O010O00N3I6J6M4M200N3N1L4N3K4M4M3ROohm3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"[bk4434jb0U1C8J5J6K4L4L4L5L2M1O1O1O1O1O100O1O1O1N2O1O1O1N2O1N2O1N2N2N2N2N2M3N2N2N2M3O11O;E:F7I6J4J5K4M4K4M3Le0[O5J4M4K4J6I7GgY\\2"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"`om54cc0=@b0A;M1000000001O0000000000O1O1O1N2M3L4L4L4M3N2N2O1O1O1O1N2O1N2N2N2N2O1M3M3N2O11O2N2N3M3M2N2N1O2N1O2N1O2N2K5K5I=CQZY1"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"noP72gc07bN0d^O8\\a0V1002N2N1O1O1O001O00001O00000000000000O100O100O1O1M3M3M3O1002N3ZNh]OM0_1ib0F:Fl\\c0"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"\\jf76hc0<F<Ff0YOO1O2N1O1O2N1O1O2N1O2N2N2N3M3M3M3M1O2N1O1O001O00001O001O4H="}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"TdT21jc08I5K5L3M3M4M2N3M2O2N10000O01O0O1H8L4O1N2N2O1O1O1O2N101N1O2N101N2N101N2N[i_5"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"Q\\i13jc05K4K4M4J6K5M2N2N2N2N2N100O2O00O101N2L;F5J5L5K4L3N3LlXQ6"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"`mZ25ec08A>I6K5L4O21nNg]O9Rc0N1O001O0000000O2N1O0O2N2O0O2N10O1N2O1O101O0O1001O0O2M3NYSZ5"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"UV\\5b0Wc0;B=L2M>B4K3M4L3M4K4M4M2N3N1N1O2O1N2O1O1O11N2O2L3M3M4K5L8H4M2N2N2N2N1O2M2O1O1N2N2N101N2N1N2O1O00O02O1N3L3N2N2M3L5L3La_j1"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"eda6a0\\c06J6K5K5L4K5J5L5K4L4K5K4M3M3M3M3O1O1O01000O010001N2O101N2N1O1O1N101N1O1O1O100O1O001N101O001N101N2N2_OR^OlNSb0n0d0K6I8H:Ehjf0"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"oh^487MPc0f0K4M4L3N1O2N1N2O2M2N2N2O2L3O001O00000O020N3N001O10O01O010O01O100O1O00100O1O100O1O001O1O1O001O1O1O001O1O001O1N101O001O001N101N101N1O2O1D=E:Kk\\`2"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"fRb3372Sc0c0I6L3L4M3N10100O0010O01O00100O001O1O001O1O001O1O001O1O0000000000000000O100O100O1O1O1O1O2hNc]O4M;\\c0K3N2M4L3LYbi3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"n^U44kc01N2O1O1N2O1O2M2N2O2M2N3M2N3M2N3M3M2N2N2OO2N2N2L4M4J7I7GWnc3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"kce5<]c0>G;F;F001O1N2O1N2M3M2M3M3N2O1O1O1O1O001O0O01O1O000001O1O2N1O2N1O1N3N1N3M2N2N2O2N1000O101O002N4K5L4L3L5K4M3L4L3M4M2M3M3M3M3M2N3M3M2N3M3M3M3M3M3L5K_eW1"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"Yim55kc07I7H2OO10O100O1O1O1O1N2N2N3M2O1O101N1O100O10O00000010O00000O2O0000000O10O0100O1O10O00010O00001OO2O00O10000O1O100000O010001N2N5I\\UU1"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"Xmi66gc09H5K6J7I5K3L4M2M4M2N3L3N3L3N3L3N3M30O4M5J4M0N3M3L4K4N3L3N2N2N2N2N2O2M3M3M3L4M3M2N1O1N3N1N3MfVd0"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"V[V7:8N`b0V1J5K2N2N2N2N1O2N1N2O1O1O1N2O1N3M3L5_O`0L4L3N1M4N1O1001O00001N101N2O1N1O2M3B>K5L4L4L4M3K5L8F=^Oei7"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"fTn74hc05M4K1O1N4M6I6H`0\\O>WOf000O11N200O1O002N2N1O4IaD"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"ZbY74jc02N2O2N00100O2O0001O01O000010OO2O001O10O01O010O00100O001O100O001O100O1O2N1O2O0O1O2O1N10010O001O001O1O1O0O11M[A"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"\\VQ36fc05K5O1N10100O0001O000O1O1N2O001O000010O0100O100O10O0100O1N2MSnf4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"iiQ37dc07H7L3N2N2M4M2N2O2M2N2O1N101O0O10001N2O0O2O1O1O1O1O001000O010O100O100O1O010O1O1O010O1O1O1O010O1O1O0O2O1O1O001O1O1O1O1O001O1O1O1O1O1O1O100O1O1O001N2N2N2O1N3N1N2O1N2N2N2N3NPPd3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"f]m27^c0<G8L5M2M2O10M3L5J6M2N3N2N2N1O2N101N1O2O001N2O002N`km4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"b\\c26fc05M3G9K4M3N2N2O2M2N200O03N3L4L2O0O2N2O0O10001N1000001O001N101O0O2O0O101N100O101N1O101N1O1O1O2NjSj4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"^_k26ic04L4L2N2O1N1O2M2O1O1O1O1O2O0O2O0O2N101N1O101N10000O2O000O2O000O10000O10001OO010oNf]O<Zb0Aj]O>Vb0@m]O?Rb0AQ^O=oa0BR^O>na0AT^O>la0BU^O=ja0CW^O=ia0BY^O=ga0A[^O>ga0_O\\^O`0bb001O0O2O001O1N101O1O000O2O001O000O10001O000000O0101O00000000000O1000Tlj3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"U_d35hc05K4N2N2O1N1O2O0N3N1N2N3N100O2N2N2O1N1O2O0O2O0O2O0O1O2O000O100O100O1O100O1000000000000000000000000001O0O100000001O0O10000000000\\Oj]O]OWb06X^OHha02_^OLba01b^OM`a0Od^OO]a00R[[3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"X_l44ac00a\\O7Tc0`0L4M3M3N2M2N2N2O1O1O001O1O1O0O2O1O1O1O1O1O1O1O00100O00100O10O10O0100O100O100O100O1O2N1O1O1O1O1O1O2N1O1O1O1O2N1O1O1N3N2N2M3N2M3N2M3L7ITnS2"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"kki5a0Yc08I7J5L5K4L5L3M9G4L3N2M3N1O2M2O1N2O0O2N2O1N110O01N2L4N2O100O101N1O1O1N2O1N2O2M2N2N2O2L3O2M2M4M3L5L3L6K4K6J7GXY_1"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"gbk62mc07[\\OMPc0e0M1N101N2N1O2N3L4K6I6N3L3N2N2N1O2N100O1O100O1O10O010O1O010O1000O100O2N0100O1O1O1O1O1O1O1O2N1O1O1N3M2N3G9I7L5J6I:FbP;"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"j\\c78hc05K8H9G1O001O001O001N101N2N2M3G8M4N2N200O1O10O100O1O100O2N2M2O2N1N3M4J5]Og0CS;"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"[V`71nc01O2N2O1O1O00100O1O1O1O1O101N1O1O2N1O101N2N2N3N2M4L6K`0_O2N100O10O0100O1000000O010O10O1OZI"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"^Pf57fc07J5K4L3M4L4L4K5M2M3M3N2N2N2O001O100O1O101N2N1O1O10O0001O00000000000000O1O1O1N2N3I9L5K5K5J6J6J6I`kf1"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"kUX64lc02N1O2N1O2M100O2N1O1N2L4M3N3N1N2O1N2M4K4J601O10000O1O101O1N10O1O1O1N2O0O1O1O2N1N4J6H9J7I9F`bV1"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"RQS76ic05K6J5J3N2N2N2N2M3N2M3N2N2M3M2N3M3N1O2N11O010O1O00100O001O1O1O1O1O001O1O1O1O1O2N00100O1O2N1N2O1N3M2N3L4Bm\\OInm7"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"US[74lc01O2M4M3L5L7H9H1N2O1O1N101N2O0O2O1O1O1O001O10O01O00100O0001O000000001O000O11O01O1O001O1O0O2O1N1O2M3N3LfL"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"hk`64jc06K5K4L6J5L2M4K5L1O2N2N1O2N1O2M3M3N2O1L3L51N1O01OO101O1N2O1N1O1O1N201N1O2M2O2N2N2M4L3N3K6K6J8FZdl0"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"[UW4:dc03N2N2N2M3L3M4N2N2N2O1N1O2O1N2O0O2O1O000O2O00000O2O000000000000000000000000010O00O100O2N1O1O1O1O1O2N1N2O1O2N1O100O1O2N2N1O2N2O1N2O1N2O2N3M1O2M3N2MdRf2"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"lQ[31kc08K2M3M3M3M2N3N1O101N1O1O1O101N1O101N101O1N10001N10001N100O100O100000000000O010O1O100O1VO_]O5ab0Fg]O6Zb0Ih]O6Xb0Hk]O6Vb0Ik]O7Ub0Gn]O7Sb0GP^O7Qb0FS^O9kb0N2O1N2O1O1O0OPbk3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"^Vj23kc05L3M2N2N2N1N2N2O1N2O1N2O1O1N200O1O1O1O2N100O10000000PO[]Oe0eb0YO`]Od0`b0ZOd]Oc0nb0O001O0O2O001N10001N1000001N101O000O2O1O000O2O000O2O0O1OcQ]4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"nbd22mc02N3M3M2N2N1O2N10000001N2O1N2O0O100O100O100O1O1O100O1O101N1OVaS5"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"jV`21mc04M2N2N2N2N1O1O1O1NO1010O1O0100Gg\\OLYc049000000O10000O2N2O1OTjY5"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"kTo26gc05L2L3N20O1O2N101O1O1O1O1O1O100O1O1O100O1O100Oe[m4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"SXm22mc04L3M2M2O2L4M2N2N2O001O1N2O1O1OZOX]O6gb0I]]O5bb0Ja]O5_b0He]O7Zb0Hh]O8Qc0O0000000000000O10000O10000O100O2O0O1O1Nocd4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"b\\i34dc0;J5H7N2N1O2M200N2O001N2O1O100O2N1O010O100O1O1001O3M3M1N2O001N2N101N1O100O2O0O10000O2O00000O10000O1O100O1O010O1O1O1N2O9CRP\\3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"eWW38fc03N3J5M2N2N3N100N2O1O001O1O1O1O1N3O0O1O100001O2N2N2N1O1N2O1O0O101N1O2N1O2N1O1N3N1O1O1O1O2N100O1O100O1O101Nf`R4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"P`o4;\\c0>I3M5K3N2M2O2M2N2N2N2N2O1O2N1O1O1O1O1O001O010O1O100000O100O100N2O1N3N1N2N2N3M2N2N2M3N2N3N2M;E7I5Kfh\\2"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"YcY48bc09K3M3M3N1N3N1O1O2N2N100O1O1O2N1O10000000000001O000000000O1000000O100N2N1O2O1N2O1N2O1N2O1M3N2O0O2O1O002N1O2M3N2M`Yn2"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"cVf3:ec02M4K5M2N2N1O1O2N1O2N1O2N101N1O100O2O000O1O100O100O100O1000O0N3M3N2N2N102N5J7J3M4L2O2M3M2N2Oamg3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"bm]48ec0:G5L4L2N3M2N3M2O0O1O2O0O101N100000001O000O1000000000O1000000O10000000O1000O101O001O1H^]OoNdb0l0;M4K5L5Hhnn2"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"ofY32lc05L2O0O10O00N2N2N2O1O10000000001O0000M202N1O1O10000001O0000000001K^\\OJcc04510M2OUX1OngN0S\\O2lc0NUnV4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"UfY33mc02N1O1O1N2O00000000O010O1O1O1O100O1O1NoYe4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"jUW36ic03L3M4L2O1N2N2O1N2O1N]OT]O5lb0JX]O4gb0L[]O3db0M^]O2bb0La]O3`b0Ic]O7Sc00000O01000000O10O1O1O100O1O1O1OWf_4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"aQ^36hc04L3M3N1K5N2N2N2N20OO2N2O1O1O10000001N101O1O0O2O1N1O2N1O1N2N2N2N2N2O1O2N2N1O2N3LQkS4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"j^m5=_c07J6L4K5L2N1O2O0O1O1O2N100O100O101O0O10000O100O10O1000001O001N101N1O2O0O2N2N2N2N2M3N3M3M3M4K6JWQ`1"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"`iV64ic07I6K3M3M3M3M3N2O0O2O1N101O0O101O1O0O2O001O001O00001O00000010O000O100O2O0O1O2O0O101N1N3N2M2N3M4J6Io^U1"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"T^Y55ic05J4M2L5J6J6N2N2O0O2O1O1O0O2O00001N1000001O000000O100O100O1O100O1O1O1O1O1O2N1O2N2N2N2N3L6H_ZU2"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"jhX53fc0=H3M4L4L3N3M1O2N1O100O100O01000O10O100000001O0000001O1O001O1O1O1O1O2N3M3M9GT[Z2"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"]Rl63lc01N3N101N3M3M3M2N3M2M4L4M2L4M2O2O0O1O101N100O10000O010000O101N101O0O2O1N2O0O2N2O1N2O1N2N2O2M3M4Jmi`0"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"ZmW7;dc0100O010O1O001O1O1N2O1N2O2N101N2O0O2O1O010O1O1O100O1O2N100O0001N2O1O1N2O1O1N2O1O1N3N2M2M3N2M4Kcb5"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"Udn56ic03L6J9I8H7I3M1O1O1O1O1OO100N2M3M3N2O1N2O1O1O1O10000O1000000O100000000O103L6Fm_d1"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"P\\f62nc03^\\O4jb0a001O000000001O0000001O00001O001O00001O1O1O1O1O2N2N1O0000O100O1O100O1N2O1N2N2N2N2N2N2Dj\\OLXc03;N2MSTg0"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"kjh73kc02O2ZO1R]O6nb0>01O0000001O01O3M2N2O1N3M3L^]7"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"SZP83mc02O1N2N3N3L=D2N00O0100O001O1O10O00fM"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"f^e3g0Pc0?F7M33M2NOO0O1O1O1O00001O00000000O1000000O1O1O1N2L4J6K5L4001OZ1fN9GZhP4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"YRS86ic05L3M3M3M1O1N3N2M3K6J5@a0c0YOiE"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"SY\\35ic05J4F:I6N2O01O00010O001O00010O01N110O0010]OX]ONgb0Lc]O0^b0Mg]O1Uc0O1N10R[^4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"XUo25jc03L3M3M3M3M2O1N2O1O1O1O1O001O100O1O100O1OCW]OEib08]]OEbb08d]OE\\b04_hl4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"ddl71oc01O0000001O1O001O1O1O1O1O001O1O0O100O2N3L3N11OaK"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"fPl71oc01O2N1O100^]OLVa05i^OLVa05i^OLWa04g^ONYa02e^OO\\a01b^O1^a00_^O1ba00Z^O3ea00i]OLK7]b0Q1000O01O0100O1000O02IPK"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"neS78fc02J61O1O1O1O002N100O010O1O10O010O01O1O000O101O0O1001O01O000000000001O00000000001O00000000001O00MX\\ONhc01Y\\OOaU9"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"eao31mc04L3L3O1N2N2O4L1O1O1O00100O10O01001O0O101O0O1I7N2N2O1O1O1O1O1O2MnZg3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"dlb4=`c05L3M2N2O1N1O2O1O1N110N20000000000000000000000000O10000000000000000N2F:I700O1O3L3N3Lmgm2"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"aPR48fc04L2O2M2N3L4M2O2M20001O001O001O0000001O00000000O100GW]OZOjb0`0>M3N2N2N2O1N2O1N2O1OQha3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"Ydc35ic04M2N2N2N2N1N3O001O001O001O1O1O001O00001O00O1ET]OBlb0<=N2O1M3N2O1N2NRlS4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"nTm71nc02N2O1O1N2O1O2S]OGna0;P^OFPb0<m]OFQb0<m]OESb0=j]OEUb0<h]OGVb0<e]OHZb0o001O0O2O00000001NYO"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"[`b72kc0:G7H3N3N10001O00001O00000000000000000000O100O10000O100O100O100O10000000000O1O1"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"`lT42nc02M2O0O2O1N200O1O101O002N1100N3L2N2M3N2Mm^i3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"]dR23lc04K4L3L4M3M3MEP]OKnb01X]ON_c0M4MXoQ6"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"PXZ32nc01O2N2N1O2N2N00001O00000000N2N2N2N2O1O10PTd4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"alZ35jc04L3M2N2O000O11O00001N101O0O2N2N2O1N3L]Sd4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"SeY33kc04M4L1O2OO001O1N2O10O01O1O1N2O1MWWg4"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"Wbg4>Xc0;N1O1O0001O010O1O1O00100N1Hj\\OFWc00i\\O0OM32Tc01k\\O04NRc02i\\O24LSc0=j\\ODTc0a0i\\O@Vc0e0O1k\\OXORc0j0100_Om\\O4Sc0;2O1_Ob0MajQ3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"\\Ro43jc04FLe\\O5[c09O0O1M3O100O0N21O00J[OS]Oc0mb0@Q]O`0ob071B>00001O000000O10000O0N3N2N3LWSi2"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"WjX47^c0V1SO<F6K5K00O1O1O1O1O001O00001O00000000O1O1O1O1O1N2O1O1O11OV1jN7I5K3M4L3M3M3MTlZ3"}},
    {"image_id": 161820, "category_id": 52, "segmentation": {"size": [640, 428], "counts": b"Pb^72mc01O2N100N200O12N1OO1O1O2O00001O00001O00001O0000010O000001O01O01O01O010O00101N100O1O00100O01OnA"}},
    {"image_id": 188906, "category_id": 52, "segmentation": {"size": [364, 500], "counts": b"jiP23W;7K2N1N2O1O010O001O001O00101N1O100O1O100O@_E6a:DeE<Z:DfE=Y:BiE=W:CiE>c:O01O10O10O10O01O001DBjE=T:ElE;S:EnE;Q:FoE:P:FQF9o9GQF9o9GQF9o9GQF:n9FSF9n9FSF9m9GSF9m9GTF8l9JSF5m9KTF4l9MSF3m9NSF2l90kEF55Q:6fEIi:>O1O0001O01O5K1O10O00000O1M4CcW3JmhL4M1O2L3M4M2M3N2M3M3O1000000000001O00010O001O010O1O00100O1O2OO01O1O00010O1O2N1O101N2N102M2O0O101N2N100O2N101N1O1O2O0O1O2O1N1O101N100O1O010O2N2O0O2N101N2N101N2N2O1N2SIfMcN_Oh5n2ZKVNe4l1UKXNj4l1hJ_NW5f1[JdNe5a300010O0010O010O1O1O1O1O2O0O1O1O1O1O100O00100O10O01O10O01O10O01O100O100O10O010O00010O0001O0001O01O0000000000000000000O010000000000000000001O000000000000001O00O20O001OO11O00001O00000000000000000000000000001O01O0000001O001O00001O00001O001O00001O001O00001O1O001N101O0O2O1N1O2O1N3N1O1N2O2N1N2O2M2O1N3N1N3N1N2MjI"}},
    {"image_id": 331799, "category_id": 52, "segmentation": {"size": [464, 640], "counts": b"llR7>m=8K4L4M3M2N2O001N01O2O001O002M2O1O4L5K3N1N2N2N101N2N1O1O100O1O0010O01O001O001O100OYQ\\1"}},
    {"image_id": 331799, "category_id": 52, "segmentation": {"size": [464, 640], "counts": b"Yal69T>4M3N2O001O001O000000O010O1O010O1O001O1N2O1N2M3O2M4M^Wi1"}},
    {"image_id": 349480, "category_id": 52, "segmentation": {"size": [450, 640], "counts": b"iY^41P>1O2O0O10001N10001O001O1O1O1O1O100O2N100O1O2O00001O1O1O1O00O1O100O2N1O2N2N3L4JT[i3"}},
    {"image_id": 349480, "category_id": 52, "segmentation": {"size": [450, 640], "counts": b"iVf41Q>1O00001O10O01O1O100O100O10001N1O2N1N3N2O1O1OO010O1O011M3N2N1N3M3LaRd3"}},
    {"image_id": 349480, "category_id": 52, "segmentation": {"size": [450, 640], "counts": b"UPo42o=2N2O1O0010O0001O2GHcB;]=501O000O10O1O2N1O1N3N5IUT`3"}},
    {"image_id": 349480, "category_id": 52, "segmentation": {"size": [450, 640], "counts": b"PZe41Q>2N001O001O00001O001O2O0O010O1000O01000O100O2000O2M1O010O01N101O^]e3"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"Xm^46h>3N2N3M2N1O2N1O100O2N100O100O101O0O10000O100O10O100000000000O100000O100000000000000000001N10001N100O2O0O2M2O2M2O2N2N2N2MR`P4"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"TgW51l>5N1N2N3M2N3N1N2N2O001N101O00001O00001O0000001O0000000000000O20O0O10001O00001N101N2N2N3M3L6EPX^3"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"U_m34k>2N2N2O2N2N101N2N2N1O2N1O1O1O2N1O100O1O1O2N3N1N1O2N10001N2O001O00001N1000000000O100O1O1O1O1O1O1N2O3M1O1N3N1N3N2M3N3K6Kb[b4"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"f^S59e>6L2M3M3N1N2O1O1O1O1O1O100O1O1O100O100O10O001O001O001O001O001O100O1N101O1O1O1O1O1O2M3M3Kj]c3"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"`eh41l>5M4JG_A:_>5O2L31OO2N1O1O1O100O1O001O1O010O0010O0^OSB1m=M]BKc=4e00O0O2O0100L\\AKg>2]h3NkdM0obN0O0[jl3"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"jlU45j>3N1N3N01O010O001000O001O1O100O001O100O100O10000O10O1000O1001O0101OO00010O02N1O2O2N7JN2M2M3N1O2M3L8HfT^4"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"bgZ34k>3L201O1O1O1O2N1O2N1O2N1O10O01O1O2N1O001O1O1O1O001O1O100O1O1O011N01O001O01O01O001O001O10O01O1O1O100O1O00100O1O002N100O3M2O1N2O1N4K]YR5"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"mdi44k>3M2N2O2N1O1O100O001O1O1O100O001O100O010O1O00100O10O010O015J100O2O00000000000O1O000O2O0O2O0O2O0O2N[lj3"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"Tcf21n>4M1N2N100O101O1O0O2O1O001O1O001O1O1O0O2O1N2O001O01O0000000000001O000000001O0000000010O0001O00001O001O001O001O1O100O1O010O1O1O1O001O1O1O1O0O2O1O1N\\fb5"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"Sdf22m>2L4N1O1O2O0O2O001N101O1O001O1O0O101N101N101O000000001O000000001O0000001O0000001O000001O01O000000000000000000O1N3M2O1N3_OjA4^Wi5"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"dlj221Oj>5O1N1O100O2N010O2N1N2O1N2O1O1O1O2N1O1O100O100000000O1000000O10000O010O1000O01000O010000O010O01000O01000O10O10000O01000O100O100O10000O1O101N1O2N1O2O1N3M3LUb\\5"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"fWS45a>=L2J5N3L3L4O1M300O1O1O100000000000O10O10O1O1N1O3M2O3K5K5J8FWXj4"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"mXR4=a>g0ZO10E_BWO`=h0=G9K4M400N101O0O2M30O1010N[YQ5"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"fSd44h>6L3L3O2M2O1O1N3M2O1O1O001O1O1O1O001N2O10O0100O01O10O01O1O100O00100O1O1O00100O2Na0_O3M2N2NiiR4"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"ma]42l>3M2N2O1M3M3L4K5M3N1010M2N3L3N3N2N2N2N2O1N2O2MRWc4"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"ngX51k>4N3N1N2M3J6N2N2O1M3O1O100O100O100O100O1O100O1O001O100O1O11O1M3L4L5K5IV]b3"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"mif52k>4L3M3\\OEZB0J?l=AVBh0P>14L4L3L```3"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"lbW31k>6L2N2N3N1N2O1O1O1O1O1O1N2O1O1O1N2O1O1O1O1O1N2O1O001O1O100O100O100O01O10O01O1O001O1O1O1oNYBh0R>L3N1O001O1O1N3N1N3M4LSVZ5"}},
    {"image_id": 389812, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"cn_34k>1O1N2O1N2FGkA:V>8001O001O1N2O2N1O1O1O1N2O1O010O1O1O1N_k_5"}},
    {"image_id": 400161, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"gnP83k>3M2N2N2O1N2O1O1O1N2O1O1O1N2N2M3O1N2N2O1O1N2O1N2O1O1O1N2O1O1O1N2O0O2O1O1O2N1O1O1O2N2N1O1O100O100O1O10O010000O1000O001N2O1O1N2O1N2N2O0O2O1N2N3M2O1N2M3M3N2N3L3M4J5K6K5K6J[X3"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"hnX22kc05L3N2M2N2M4K4M3M3N2O0O100O101O0O101O0O2O0O2O001O1N110O00001O001O000010O0001O0001O01O01O01O01O00100O001O100O1O2N3M3M4L4L4L2N3M3IkVi5"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"]Zd11mc05L2N2N2N2N001O1O010O1O1O1O1O1O1O1O1O1O100O1O1O1O1O100O1O10O0100O10O0100OO1O2M2M4M2N201N101N1O2O1O001N101N2O1O1N101O2N2NjZ`6"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"PlZ25ic03M3M2M3[OOW]O6fb0c0O1O0010O01O0001O001O0010O10O0100O010O010O0010O001O000010O0001O000O10001O00001O000O101O0O100O1O1O2N1N2N2N2M4M4M6GUbh5"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"j_Y35ec0<k\\OAWb0l0^]O[O[b0W1L5K4M4L3L3N3M2N3M1001O2O2N3M4L5K5K3M6aNc]OP1jb0L2N1N2N3N1N2O0O2N2N1O1OL4O11O0O2O2M5KUQW5"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"[Ub3g0Wc08I3N2M3N4K6J3L4He0_O2N3N1N2N3N001000O100N2K5M4M2O5K2M4M3M3M2M4L4L3L5J6J8Ek^Q5"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"ggX3c0Wc0:I7H6L4L3M3M4M4K6K4L2N2N10000008H2N1O1O0O1O2H7O1N2N2N2N2M3L3L6I8Ikh\\5"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"jom39ac0:J5O00001O1N2N2O00O01O001O10O10O2N2N2NO100O1O1O001O1O1O0O2K6I6L4M3M3MXWf4"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"T[m33jc06K5L4L3M4L3M3M2N3M2N2M3N2N2M4L3N4K3M4L3N2O1O1O10O01O1O100O0101O00101N4L3L3N2M3M3L4M3L5K5\\OY]OFPc0JZ]O3\\c0M`[_4"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"eRe46hc06J5L4L4L4M4L3M5K6K3L2N100O1O1O1O10O01O2N1000001O000000000000000001N11OO2O000O101J6M2O101N100O2O001N101N101O001N2O1O1N2N3M4K9H2L4M3LWg[3"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"YbQ53hc09K2M3N2N2N2O001O1N2O2N1O2N1O1O1O2N1O1O1O001O00010O001O010O0010O00010O01O010O10O01O010O010O01O01O010O01O010O0010O01O010O1O1O010O1O1O1O100O001O1O1O1O1O1O1O1O1O1O1O2O1N2O1N3M2N1O1O1O0O3L4L_\\^2"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"Wo_53mc02N101N100O2O0O2N101N101N2O0O2O1N2O2M2O0O01O010O010O01O010O000010O01O010O00010O0000010O000000001O00000000001O0001O0000101N101N2O1N2N3M3M2N2M5I`g]2"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"QRm53lc0101N1N3I60001O1O001O0010O01O00100O00100O1O100O010O100O100O100O1O10000O10001O0O2O2N1O1O1OO1000001O02OO1N2N101N1O2O0O2O1N2N3M2M3N2L3M4KeTS2"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"jfS46hc0a0_O8H7I6I5J7I6I7F;J7L4M1O0000O100O1O1O1N2O1N2L4I7J6L4M3M3N2M3M3L4L4L4L7Fcm_4"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"caZ42mc03N1O1O1O2N1N2O1N2L4J6L4M3L4M3N2N2O1O1N101O1O1O10000O10O1000000000000O100O01001N011O000O2O00001O1O001O1O1O002N1O2M4L5K;D4L2N3MQUh3"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"h^P52nc02N10001OO02O00000_NKU_O6j`0KV_O5i`0LW_O4h`0NW_O2i`0NW_O2i`0OV_O2h`00W_O0i`01V_OOj`02U_ONk`03T_OMl`04T_OKl`06R_OKn`07o^OIRa09k^OHUa0=e^OD[a0f0Y^O[Oha0f0V^O[Oja0f0S^O[Ooa0e0m]O^OSb0W1101N100O2O0O2O1N2O1N2O1N2O2N1O2M4L7J7G3N2M3M2N3MY`X3"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"Y`i43=Nlb0;P]OHmb0;P]OFPc0<l\\OGUc0b000O10000000O100000001O0000001O0O100O1O10000O10O1001N2N7I2M2NfZk3"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"kP[51oc0001O2M2O001O0010O0100O01000O01O10O0100O10O01O0010N101VO3^]ONcb03Z]ONfb04W]OMib05S]OMnb0b0010O1O1O2N2O1N3M3M101N1N101N2N2MoRQ3"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"`QR27fc03N10010O01O010O10O01O010O010O10O0100O1O010O100O100O10000O100O101O001O20gba6"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"Uik16ic02N2N1O101N1O0O20O100O101N10000O2O0O100O101N1000000O2O000O10001O00000000000Oobf6"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"\\dc15jc03N1N101O000O2O03M3N0O100O101N100O1OXW[7"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"Xgi25ic04M2N1O1O1O2N1O1N101O1O1N101O1O1O2N1O1O1O100O1O001ON3M2O1O1O100O2O00001O1O1O=C5K\\]g5"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"]o[25gc05F:L3N3O00O100O1O2N1O1O100O100O01000O010N1N3O1O001O1O001O1N2O001O001O1N2O\\QW6"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"hRU24kc02N2O1N2N2M2O1N101N101N101N1000Hk\\OFUc09P]ODob0;<N1O1N2N101O1NR]ONSb02n]ONQc02OO10O1001NXQa6"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"bf_24jc04L3L4L4L3N2M3N2O1O001M201O0O2O1O1O1N2O1O001O1O1O001O001O1O00001O010O00001O01O000010O0001O010O001O1O001O1O1O1N1N3M3M3N3M3M3L4M4M3L5KRWa5"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"eYl16ic02N2N3L4M2M3M3M2N2O1N2O001O00001O1O1O1O1O100O001O1O010O00100O01O010O0100O010O01O10O010O01O1N2O4L2N3M1N3N1O1O1O0010O01O1O1O001O1O1O1O100O1O1O100O1O1O100O100O010O10O1000O10000O10akf5"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"[Xj25ic03M3N2M2M4M2N101N101O1O001O1O100O1O1O1O100O1O100O1O100O1O1O010000O100O1000000O100N2I7K5M3M3N2N2N2O1N2O2M3Nfh^5"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"YP_23kc04K5M2M2N2N2O001O001O001O0O2M3M2O1O1O10O001O2N2N1O2O1N2O1O1O1O1O1O101N1O1O2N100O2N101N100O2N1O2OgTm5"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"RRb3=_c08I7I?A5L2N3M2N3M2N2O1O1N2000O100N2N1O2N2O1O001OO100000000001O0O100O2N2N2N3N1N3L4M4L3M4K5L5K6Gkfj4"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"k_l43lc08I7I4L4L3N2M4L3M4L2N1O101N1O2N1O1O2O0O1O100001O00001N100O101N1O101N1O101N2N1O2O1N2N2O0O2O1N3M2O2M3L4M3L2N3M3MYV[3"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"n_[52nc01O2M2O2N1O1O1N3N1O1N2O2M3M2O2N1O3M1O2M3N1O1O0010O010O010O10O0100O010O00100O010O0010O01O10O01O001O1O00100O1O001O1O001O100O1O001O2N1O1O101N2N1O2N1O001N2O0N3M5KmV]2"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"\\_g44kc03M2N2N2I7D<N2O0O2O0O101O00001O01O0000001O00010O00001O0010O01O00001O001O1O0O2O1O0O2O1N101N2O1N2O1O1O1O1O1N2O00000O2M4Ldh]3"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"V`d3;_c09J5K5K4M3M4M3M3M2M4M2N1O100O1O10O0100O01N101O1O100O2N2N2N2M2N3L4M3N2M2N2O2M2N3M2M3M4K4MbTj4"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"eV[24jc04N1N2O0O101O0O100O1O100O1O2O0O1O2O0O2O001N101N100O2OO10O10000OFP]OFPc06X]OFhb08\\]OEdb0:b0O001O1N110O1O001O10O0100O010O010O100000O0100000000O101O00001O000O2OQjc5"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"kU[25jc02N3M2N1O1O1O1O1O1O100O1O1O100001O0010O0001O00001O0000001O000O10001N100O10001O0O100O2O000O101O0O100O101O001N101NWnk5"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"QQ]26jc02M2O1O0O2O000O1O2O0O101N100O2O001N101O000O2O00000O2O^OU]OOkb00V]O0ib01X]ONhb01Z]ONfb02Z]ONfb02[]ONdb02\\]ONdb02]]OMcb02_]OMab03`]OL_b04b]OM^b02c]OM]b02e]OM[b03e]ONZb01h]ONXb02i]OMWb02k]OMUb03k]OMVb02j]ONVb01m000O10Y_n5"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"Qmm28gc02O1N101O1O001N2O0O2O1N2O0O2O0O2O0O2O001O1N10001O001O001O00001O00001O00001O001O010O001O00010O0001O01O01O0010O01O0010O0010O00100O1N2N2M4Dn\\OCVc07>Lh^P5"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"cQY4;cc06J3M3N1O1O1O1O100O2N100O1O2O0O1O2O001O001O01O001N1O101N1O2N2N2N1O3M2O1M5LbnY4"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"XUP55jc05K:F2O0N2O101N100O2O00000O10010O001O000010O001O00001O1O1O001O2N1N3M5IdRd3"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"eRW51nc02N1O2O001N101O0O2O001O1O001O001O1O001O1O1O1O001O1O100O1O1O010O001R]OYOab0i0[]OYOfb0Q1O000001O01O01O001O000010O0001O001O001O010O00001O1O00001O1O001O1O001O1O1O1O1O1O1O1O1O1O1O1O1O001N2O0O2M3M`d\\2"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"]Z]52lc03N1N2O100O1O1O100O1O100O100O10000O2O000O101O0O10001O000O2O00001O0O101O001O00001N101O00001O001O001N101O00000000000000O100000000O10000000000O1000000O2O00001N2N101N101N101N1O2O0O2N1O1O2O0O100O100O2N2N3LlYn1"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"o]e51lc03E;0O01001N0100000O1000000O1000O10000O010O100O10000M2O21O00001O00001N101O001O2F]\\O3jc0M3NY^j2"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"Rea52mc01O2N2O1O2M3N3M2N1O000001O00000O100000000000001N10000O100O101N101MPkS3"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"lPf52mc0100O1O1O1O2O0O100O100O1000000O101O00000000001O0O101O00000000O100O2O0O100O2N3N3KYSk2"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"jkn52nc0001O1O00100O001O001O001O10O01O001O1O00001O00000000000000000000001O0000000000001\\OEa]O;`b0E_]O;ab0E_]O;bb0E]]O;cb0F\\]O:db0F[]O;eb0FY]O;hb0DV]O>jb0CT]O>mb0:001O001O001O1N101O1N2O1O1O1O1O001O1O000O2N1O1MXdm1"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"YX]61nc02O1O1O001O100O001O1O1O1O2N1O2O1N101OO10000O011Og\\OBob0>m\\OETc0c01O1O2N1O2O1N2N2N001O0O2O0O2M3MnVS2"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"Qaj55lc02M3N2M3M100O10O001O010O001O01O01O0001O01O01O00001O01O01O001O001O0010O0001O00001O01O0000000O1000001O2N3M1O1N2M\\V]2"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"Z`h61oc01O1O1O1O1O1O1O1O1O2N1O2N2O1O001O00O2N2O1O4K4M1N3MmnQ2"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"Z`Y519:Qc0Hl\\O:Sc0Gl\\O;Tc0Dk\\O=Vc0Aj\\O`0Zc01N201O001O01O001N2N2M4Iccf3"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"QaV41nc03N1N2O2N2M4MO100O001O1O2N100O2O0O1O2O1MQSg4"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"ejo28ec04M3N2N2N2N1O1O2N1O2O0O2N100O2O0O2O000O101O000O100000000O100000000000000000000001O00000000001O00000O101N100O2O0_OZ]OGhb04d0N3N2MjiT5"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"ejR47ec08J4L4M2M4M2N2O1N2N2N101O1N10001O0010O0000001O000O2O001N1O2O001N1O2O2M3M4K6F`a_4"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"mZ`61oc0001O0O1000001N10001O00001N10001O001N101O01000O0100O1O011O0O2O1O0O101NglS2"}},
    {"image_id": 407574, "category_id": 52, "segmentation": {"size": [640, 478], "counts": b"nZ`62nc0010O1O1O002N00100O100O00010O00010O010O01O10O010O10O010O01000O10O100000000001N101N1O2OQd0OTPm1"}},
    {"image_id": 465806, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"cSX14i>5M3M3N2M2O1O1O1O001O0O2O1O000010O000001O00000001O00001O00000000001O00000001O00000000000000O0100000000O01000O010O010O010O001OF3AoA;T>27N2M3O2O1N2O1NneQ7"}},
    {"image_id": 465806, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"h`j03m>1N110O01ON6K4L3N1O1N2O1O001O1O001O00001O00001O00000100O2N1O3M101N2N1O001O001O1O001O001O0000001O000000001O0O100000O10O1000000O10000O10O0100O100O10000O1000il\\7"}},
    {"image_id": 465806, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"_Qj01m>5M3L2O001O0O01O1O100O10O100000000000000001O00001O00001O0N2Od]S8"}},
    {"image_id": 465806, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"jTW14k>1O2O001O00000001O000000O101N4M2N1O1O1O1O001O1O001O00001O0000001N1001O000001O000O100000000000O10000000000O01000O10000O1O010O1GjAGW>89O1L5N2N[`T7"}},
    {"image_id": 465806, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"iji21l>4N2N1O2O0IHeA:Y>701O000O2O0O1O2O000O101O000O10001O000000000000000000000001N101N103L2N1O1O2N2N2LdTl5"}},
    {"image_id": 465806, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"]\\_33l>:G0O2M3O0O100H^ORBb0m=_ORBb0m=_OSBa0m=@QBa0o=_ORB`0n=@RB?n=BRB>n=BRB>n=BRB=o=DQB;o=EQB:P>FPB:Q>EoA:R>GnA7S>InA5T>JmAOKNZ>3lANY>1;11Mo__5"}},
    {"image_id": 465806, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"l^f2>b>1O2N1O2O3N3L2N10O00000O1O1O1O00001O001O00001O001O001O00001O001O001O001O001O00001O000O101O00000000000O2O0000000O10000O010O10000O010O0O200001O1N10000O100000O10000O100000000O1000001N2O]\\Z5"}},
    {"image_id": 465806, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"knm22n>1O000000000000O11N100000000O1O100O1O1O1O1O100O1N200O1O1O1O010000O101O0O101O0O2O000O2O0O2O0O2N2N^Rg5"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"Wdh12k>5L3N2O1N3M101N2O000O2O00001O1O001N101O0001O01O000000001OO100O100O1O1DjAMW>2lAKU>4oAHR>7<O2O0O1O100O1O10O0100N20S_k6"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"iem23l>2M3M3N2N1O2N1O100O101N10000O100O100O100O100O100O10O010O0\\ORB8n=GTB7l=JTB6l=IVB5j=LVB4i=MWB2j=MXB1h=0XB0g=1ZBMg=2ZBMf=4[BJe=6]BIc=7b0001O001O001O001O000O2N2O0O2N1O1E@TBd0k=82N1O2N3M2M4L5K5Ik_^5"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"]mj24i>3M2N2O1O1O101N1O100O100000000000000000000000001O000001O000000001O00001O0010O0001O00001O001O001O1O001N2O1O1O1O2N1NYne5"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"_g^21l>6L2N101N2N100O2N1O1O100O2O0O100O1O100O010OO20OO2N1M4M2N3M2O2M201N10Yl\\6"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"eme38e>4M3M2N2O1N100O1000O100O2O0000000O2O0000001O0O101O00001O0010O01O001O1O001O00100O00100O1O010O10O01O10000O10O01000000O100000000O10000000000000000000b]c4"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"\\Xa32l>4L3N2N2M3N1O1O01O0O101O1N2K5KVXc5"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"jRd35g>5L4M2O1N2O10O2O2N1N2O0O1O100O3HYA1U]`5"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"Vjg38e>5K4M3M2O1O1N2N2O0000000O1000001O0000001N1001O0001O000000000000000010O000010O0001O001O00010O001O001O1O1O1O001O1O00100O1O10O01O100O100O10000O1000000000001O01O0001O001N101O001N101O0O2O1O1N2O1NWWW4"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"]WQ44j>3M2M4K5K5L3M4L4L4L4M3M4K4M2O1N1O100O00100O1O10O10O1000N2M2M5M2N2O0O2O2N1O100O101N10001M2O2O0O2O1O1N101N2O1O1N2O1O2N1O1O1O1N2N2N1O200O010O1O01000O010O10001N2MS[U4"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"fbk32j>7L1O1O1N11N10000O100O2O01O01O00001O010O000010O01O1O001O1NS\\R5"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"PPm36f>5M3M2O1N2O1N3N1O001O00O2L3N3L3N3N1M4M2O101OPR>1nmA2N2O001N2O001N2O001N2O001O1O010000O1O1O2M2O2M2O2M2O[aY4"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"SY_46g>4M2M2O2N1O1O1O1O101O0000O2O001O1O001N101O1N101N2O001O1O0O2N2Nmg]4"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"QhX41k>8J5K100O10001O000000000001O00000O1000000001O001O1O1O2M3N1O2N2N2M3N2M3N1O1N10O1O010O10O0O1010O001O001O001O1O001O1O1N3N1O1N2N10O00O2N3N3L4L4M4M3MiSQ4"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"laj44j>3M2O2M3N1N3M3N1N3M3M3M3M3M3M3M2N3M2N1N3N1N2O0O2N2N1O2M2N3N2N2N1000010L3L4011M3N3M2N3jM[Cm1m<N2N3M2M4L4L4L5K5J8YOoVh3"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"hnZ56h>3M4L3M2N3M2N2N3M2N2N2M3M3M3N2M3M201O10O3M2O2M3M2L3N3M4L2M4M2N1O2N2N101N10N101O0O2N1M4M3M3N2O1O101O00000000010O01O010O10O0100O10O10O100O100O10000O100O101N101N100O2N101N2O1N2N2O1N2O00001O001O002MVUc2"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"dX^56f>4M4L3M4N1O2O001O001N1O10@?L4NRXf3"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"^[d5b0Z>5L3K6M2M4M3M2M4M2N3M3M2N2N2N2O0O2OO010O010O1O1O1O1O1N2N2O1N2N3M2O1O1O1O2SOcB5^=JeB3]=KeB3\\=MeB2\\=MeB1\\=NfB1[=OfBN[=2fBM[=2fBM[=2fBMZ=3gBK[=4i0O010O1O100O100O10e`l2"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"QeU66g>3O2M2O1O1O2N1O1O1O1O100O1O1O100O100O100O1O001000O01O10O01O01O010O010O010O00100O<D3N0O101N100O00100O10O0100O1O010O10O01000O010O010O0100O1LjaU2"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"Skh6;b>4L4N1N2O1O1O1O1O1O010O1O100O010O10O010O010O10O10O10O10O10O01O1N2O1N2O001O1O1O1O100O2N100O100O2N100O2O0O2O001N2O001O_`g1"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"`oU71k>9H4N2M3M2O1N2O2N1O1O10O01O1O01O010O00001O010O00100O00100O10O0100O100O10000O1000001N10000O101O00000O2O001O1O1O1O1N7J2NmlY1"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"PWZ76i>2M2O2N2N2N2N1O1O1O1O100O001O100O10O0100O100O010O10O01000O010000O010000O01000O1000O10O10000O100O1O100O1O1O100O2O0O2N2N2N2N1O2N1O2O0O2McmQ1"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"P_o66i>4L3L3O0O1N200O1O2N1O100O1O101N100O0100O001O010O1O001O1O010O001O1O10O01O1O1O001O1O1O001O1O100O0O200O001O1O001O1O010O1O1O1N10mP_1"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"^d^61l>5L4M1N3M3N1N2O001O0O1000010N1001OO1000M30001O0001O00LfACZ>=hABW>>51O1O1O010O10O4M2M2O001N100O1O1O100O1O1O101MdPU2"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"VoQ64i>5K4M2N3M2O1N3N1O1O1N101O1O1O1O001O001O1O001O00001O0000001O0000000O10O100000O10000O1002N2N2N1O2N1O2N2N1O100O1O1O1O1O2N1O1O1L3O2N2O1O1O1O0O2O1O]ZX2"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"cSQ25i>4M2M3N1O1O1O00010O0001O010O0010O0101N100O1O100O101N100O1O100O100O1O010O100O1O010OmVg6"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"R_k14k>3M2N1N3N2N1O2N1O1O10N2O2N1M300O101N100O100MZhU7"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"n_k18e>4N2N1N2O1N2O1N2M2O1O00AQB0o=OUBMl=3VBKj=4YBIi=6`00001O0010O01O2N101NnkS7"}},
    {"image_id": 560256, "category_id": 52, "segmentation": {"size": [480, 640], "counts": b"_UX21o>1N10000O10000O100O100N2001N1MiZl6"}},
    #
    # "apple"
    {"image_id": 2149, "category_id": 53, "segmentation": {"size": [427, 640], "counts": b"RT]41h<R1\\O;F8E:G8J6J5K5L4K6K5L2M5K4M3L5L3M3L3N3M3M2N3L3N3M3M2O2M2N3M2N3M2N2N2N2N2O1N2N2N2N2O1N2N2N2O1N2O1N1O2O1N2N2N2O1N2N1O2O1N2N101N2O0O2O1N101N101N101O1N101N101O0O2O0O2O000O2O001N101O00000O1000001O0O100000000O1000000000000O10000000000000000O100000000000000000000000000000O10000000000000000O1000001O0O1000000O10001O0O10000O2O000O2O0O10001N100O2O0O2O000O1O2O0O2O0O2N101N100O2N101N1O2O0O2O0O2O1N1O2O1N2O0O2N2N2O1N1O2N2O1N2N2O1N2N2N2N2N2N2N2N3M2N2N2N3M2M4M3M2N3M3L4M3L3N3L4L4L5K4L5K4K6I6K6I7I8H;C>Bh0XOPhf0"}},
    {"image_id": 2149, "category_id": 53, "segmentation": {"size": [427, 640], "counts": b"lVk63W=100O100O010O100O1O010O1O100O1O1O100O1O1O10O01O10OO2O1N2O1O1O1O1O1O1O1O1O1N2O1O2N1N2O1O1N2N2O1N20001O01O001O1O1O010O1O1O1O1O100O1O1O100O1O1O100O1O1O100O1O100O1O100O1O100O1O2O0O2O0O2O1N2N2O0O2N2O1N3M]n5"}},
    {"image_id": 2149, "category_id": 53, "segmentation": {"size": [427, 640], "counts": b"\\hj56S=3M3M4L3M3N2M2N2N2N2N2O1N2O1O1N2O1O1O1O0O200O1O1O1O1O1O1O10O01O1O100O1O100O1O1O00100O1O1O100O1O100O010O1O1O100O10O0100O100O100O10O0100O1000000O1O100O1000O01O100NdMUE\\2k:1100000000cMTE[2k:eMVEZ2n:0MfMUEZ2k:33M1OO010000000O10O10O100O10O10O100001O0O1000000000001O0O10000000000O1000001O00000O10001O00000O101O0000000O2O000000001O000O2O00001O00001O00001N101N10001O001N10001N101O0O101O0O2O1O000O2O001O1N101N2O001N10kE"}},
    {"image_id": 2149, "category_id": 53, "segmentation": {"size": [427, 640], "counts": b"[SQ17n<9H;bC[Of;i1ZO:G9G9G6K3M3N1O2M2O1O1O2N1O1O1OmNWGeMj8U2X1L5K4L4N3L3N3M2N3N1O2N1O2N1O2N1O2O0O1O2O000O2O00001O0000001O00000000000010O00000010O0000010O01O0010O01O010O1O010O00100O010O1O10O01O10O010000O01000O10O1000O10O10000O1000000O10000O1000000O1000001N1000000O2O0000001N10001O001O0O101O000O2O001O001O0O2O001O001O001N101O1N2O001O1N2OdnW5"}},
    {"image_id": 2149, "category_id": 53, "segmentation": {"size": [427, 640], "counts": b"\\_Q35V=2M4M1O2M3N2N2M4M2N4L5J4M5K7I;D6K1O0O10O1O1O010O1O001O1O010O1O001O1O1O010O1O001O10O01O100O010O0010O01O01O010O01O10O0100O010O0100O010O00100O00100O00100O0010O1000O1000O1000000O100000000O10000000O10O101O00000O100000000000001N100000000000001O001O000O101O000000000000001O000000001O0000001O0000001O00001O0010O0001O001O010O001O10O01O1O010O1O10O01O1O010O1O010O100O1O010O2O0O1O102M2O1N2N3N1N2N2O0O2N3M5Hfif2"}},
    {"image_id": 2149, "category_id": 53, "segmentation": {"size": [427, 640], "counts": b"nfZ31X=3N1O2N1O1O100O2N1O1O1O100O1O1O1O100O1O100O1O100O1O100O1O100O2O0O1O100O100O100O100O100O100O10000O10000O10000O1000000O10000000O01000000O100000000O100000000O010000000O10000000000000000000000O10000000O1000000000000000000000000000000000000000000000000000001O0000000000001O00000O2O00001O0000001O00001O00001O00001O001O000O2O001O001O001O001O001O1O0O2O001O1O001O1O1O001O1N2O001O1O1O1O1O1O1O1N3N1O2Ml]^2"}},
    {"image_id": 2149, "category_id": 53, "segmentation": {"size": [427, 640], "counts": b"e8Q3Z:0N2O2N1O1O1O2O0O1O1O1O2N100O100O2N1O100O1O2O0O1O100O1O2O0O1O100O100O2N100O100O100O2O000O100O101O0O100O10000O2O00000O10000O2O000O10000000001O0000000000000000001O00000000001O000001O00000000000010O000001O0000001O0000001O000010O01O00001O001O001O010O1O001O00001O001O001O0010O01O1O001O001O1O1O001O001O010O001O1O001O001O001O001O001O1O010O001O001O001O1O001O1O001O001O1O001O00100O1O001O1O1O1O1O001O1O1O1O1O1O1O1O1O1O1O1O1O1O1O1O1O1O2N1O101N1O1O1O1O2N1O1O1O2N1O1O2N1O1O2N1O1O2N2N2N2N2N2N2M4M4L5K5K4K6H]`S5"}},
    {"image_id": 76416, "category_id": 53, "segmentation": {"size": [480, 640], "counts": b"miQ6:d>5L2O1O0O10000N2N2O1005K0O2BfA3e>MneR3"}},
    {"image_id": 246968, "category_id": 53, "segmentation": {"size": [428, 640], "counts": b"Tn]41S=1SCOl<3SCOj<2UCOj<2VCOi<1WC0h<0XC2e<0ZC1e<N\\C2c<O]C1c<0\\C0e<O\\C0d<0]COc<1]CNe<1[CNg<1ZCLj<2VCMl<2TCNm<18OaVe3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"n\\T83T=5L5K4N1N2N2O1O1N10001O01O00eC"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"VoS83V=2M4M2O0000O1O10000O1000000000nC"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Sko72W=2O0O100O1000000O100000000001O00000000001O001O1O00"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Zhh75P=5M4N1O101N101N101O001O1O010O1O10O1O001N2O001N2O1O1N2O2N2N3M3M^U4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"_Zh74U=3M4L10O10O01O10O01000000001O000010O010O01O10O10O10000000M4JjP5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"ZP[73V=2N2N2O1O1O1N2O1O1O1O1O2N1O1O1O1O1O100O010O01O001O0O2O1N2N2N2N5J4MhRa0"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"lTi75T=1O001O00100O1O0100000001O00010O00100O010O10O0100O1N3MY^5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"[ke73W=1N2O2N002N1O1O000001O001O00001O001O1O1O1O1O1Om\\:"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"UnS86S=4L2M3N1M4N1O2O000000000001O00TE"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"fPl75T=4K4N2M1O1O1000001O00001O001O1O10O001N2O1M4M3L5K]j3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"TTi77Q=4L3O0O1O100O100O100000000000010O0001O001O1O1O2M4MfY6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"b^b75S=4M2N1O1O10001O00001O001O1O100O10O1N101N2N2N3N3L`\\="}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Q][73U=3N2N1O010O100000000O100000000001O001O001O0O2O1O1O1Oacc0"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"mY^73U=3N1O1O100O011N100000001O001O1O00100O2O0O10O1N101N3Glf`0"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"UoU73V=2N2N2N2O1N3N3M3M2N001O0001O001O0O2O1N1O2M3N2N2N4Lb^i0"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"\\Rn63U=2O2N101N100O2O1O1O1O1O2N2O2M01O001O001O1O1O2N1N3M5KnmP1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Vi[72U=8J2N101O001N2O1O01O01O01O01OO2N2M2O2N3LYge0"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"k`d73V=1O10000O10000O101O001O001O010O10O0O1N3N2O0OPU<"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"^mS82X=1O2N1O2N3N1N0001O1O1O001O2N2MZE"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"XV\\75T=1O001N110O1000000O101O000010O01O0101O1N2Mlld0"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"iiQ73U=5L1O2N1O101N101O00O1O1O001O2O0O101O1O2N1O2NQln0"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"X\\Q77Q=2O0001N110O1O10000O1000001O00100O1O10_aP1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"mZj72W=3M1O010O1000O100000000O101O0001O2N12N2N]U7"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"edh61W=200O2O001N2O1O101N:G0O01O1N2N2O1N2N2L4MekX1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Sjb64S=5M2N2M200O1000O0100000O100O1O2O0O101O1O001O1Nb^]1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"jkg55R=5L3M3N1O2O0O1O100O100000000000000001O001O001O1O001O1O1O1O1O2N3MjdT2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"hbP6134m<6O1N101O1N2O1N2O1O2M3N2N001O00010O01N101O1O1O1O1O1N2N2O1M5K[hl1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"]`d53U=4M3N4K4L3N1N2O2N0O2O0000O1O100O2O0O2O001O001N200O2M3ImRZ2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"]gY66R=3N2N2N1O2O2M2O3M5J3N0010O0000001O001O1N101N2N2N2N2M4M3L^^d1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"\\P[62W=2N1O1N2O1N11O010001O001O1O0000000000000001O001O001O002N1O3MnZb1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"a_l62X=1N100O100O100O10000001O0000001O001O1O002NacT1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"WdZ71W=2O1O100O100O100000000000000000000001O0000001O001O00001Oiac0"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"jTd64U=1N3M3K5K5O1O2M2O3M1O0000010O0001O0O2O1N2N2O0O2O1N2O1N2N3LmcY1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"VWP71R=8N101O00010O010O00100O0010O001O1O2N1O2N2MjkP1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"\\YR74d<1gC1Y<a0N10001O001O000001O000000001O1N2M4M3L_Wo0"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"k[`6:n<3M3N2N1O2O1N2O1O1O1O1O1O1O01O00001O001O001O1N2N2N2M4L4LQj]1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"nVf61X=1000O100000N200O101N1O2M2O3L3O001O001O1O1O10001N10O0O3N1N4K5IUgV1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"TUf5152i<OSC9j<40000O10O10O10000O10001O001O0010O10000001OO1O1N<CTkX2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"d\\Q69o<5L2N3M2O1N2O1O0O10000000000000001OO2N1N3N2M3N101N3M3N3KWil1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"eVW63U=3M2O1O1O2M201N2O1N101N3N1O4L2N000001O1O0L4L5L4N2N2N3M3M\\of1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"^`n68P=5L2O1O1O001O1O0O101O000001O0000001O1O1O1N3M3M5JaZQ1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"ami69o<4M3M101N1O2O00000000O2N1O101O001O1O1N2O1O2M3MkZV1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"le^61W=3N2N100O2O1N2O1O1O2N4L1O000001O001O1O100O1O1O1O2Mmg`1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"kYe54S=7J4M2N2N2O1N1O10000O10000001O00001O1O0O2O1N2N3M2MUTZ2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"UU\\59o<4M3L2O2N2O0O2O1N101O001O000001O001O1N2O1O3L5H6JPfc2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"jQn53V=2N1O3M2H8O1O1OO1O1O1O1O101N101O1N2O1O4Kg^S2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"PYo57Q=4M3M2N1O100O2O0O1000001O001O10O001O001O1O1N2O1O1N2N4LUZo1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"\\g[52W=3L6K2M200O010O0100O10000000001O010O100O100N3M4JjSd2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"[Ye57Q=4M1O1O10O00100O10000O101O001O10O02N1O2NQW\\2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"feY63V=3M4L5K3N000O11O0000001N2N1O1O2N101N101O1N3NPPg1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"[md61X=2O1O001N2O1O100O1O2O0O10N2N1O2O1N3Mb]]1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"`jb66S=3M2N1O100O01000O1000000O100001000O010O0100O2LR^]1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"dji3;m<5L2M3O1N100O1000000O1001O0000000001O01O001O0O2O1N2N3L6JX[T4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"[Sk38P=8I3M3N1N2O1O1O0O1000000000O1000000000001O0O2N2N2N6HWmS4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"WT\\49o<5L3M2O0O2O1N2O0O2O000O2O000000O2O001O001N2N101N2O1N2M4IjQb3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"oWT42V=3M3N3L4M3M10O001O1O1O1O100O1000001O001O1O001O1O1N1O2O\\[j3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"QnU43k<<M3N1000000000010O0100O100O1000001O00001O1O100O2O1NoRi3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Rec46Q=5L4M2M3N2N101N101N101O0001O001N101N2O0O2O1O0O2O1O001N2N3M4IYfY3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"d[V43S=9H4M3N100O1O100O1O100O10000000000000000001O001O1N2O1O1O1N3N4Dfbf3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"mjg45S=2N2O1O100O1O1O100O1000000O10000001O001O001O1O1O1O2N1O2N2NemU3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"dTP57Q=3N2N2N2N2N2O2N2N1N3N1O010O0001O00001O0O2O2G8M4L4M4Kjkn2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"nYY57Q=3M2O100O100O100O10000O100O10000000000000000001O001O001O1O1O2N1O2M3MS\\b2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"ZYY51V=7J3M4N1N3L3O0O1O10O01000O0100000O2O000010O01O1O001O1N3M3M__d2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"fVR57Q=4M1O1O1O0100001O0O101O0001O000O2N1N3M3N2N2NV_n2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"`SP54T=3N3L4M4M2M2O0O1000O10000O10001O0000001O1O1O1O1N4K]Zo2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Wge41S=8L2O0010O0100O1O2O0O2O0O2O1O0O2O10O01O001O100000O1O1N3L7HcQX3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Wig46R=2O1O10O100O100O1000000O20O01O001O1OkaZ3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"YPn49o<4M3M2N2N2O1N1O01O0010000O1000001O00001O1O100O1O1N4KZPQ3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"jPi46S=2N1O1O10000O101O000102M3N1O0O101M[gY3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"kd^43W=1N2O1N3N2N;E000001O0O2I7M3M3M3Nh`d3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Y\\l34T=3L2N3O10O100001O0O1000000000000001O0000100O006Io^S4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"gba41X=2O2N2N=D01N1O1O100N101O1M3N3KQPb3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"ZQ_35R=6L3M3M2N2N2O0O2O000000000000N3GlTd4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"ac^35R=5L4M2N001O0100O100O1000000000000O3FPhc4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"RRU34T=3M3N3M2N2O0O10O010000000001O00001O0100O1O0O2N3M4Kl[j4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"gRU35Q=5L4N1N200O100O100000000001O00001O1O001O1O1N3M3Lchj4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Uhl27Q=4M2N1O1O100O100O10000O10001O0010O000O2M3K6L4K``S5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"g`k21W=2O1O100O100O10000000000000000001O00001O1O1O2NigT5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"eiX21W=200O1O100O100O1000000000000001O001O001O2N`Yh5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Yhb2:m<6L2M3N2N1O100O100000000O10000000000001N1O2N3M2M4L5H_X\\5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"bom25S=3M4M3M1O010O1O0100000000000000O2N1N3M3N2N2N]fR5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"QWo28P=2O1O1O001O01000O100000001O0000100O10O100N2N3MaQQ5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"PaW32U=5M3N1N4L3N1O0O2O0000000001O0O2N3GfWk4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"iW`27Q=3N1O1O100O100O1000001O0010O001O001N2O2N3LZk`5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"km\\23S=7L2N1O1O1O1O100000000O10O1L5M2N2O1N3N10lbd5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"]f[26Q=5L3N1O1O10000O10001O001O0000O2M6K4L3M2NPje5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"f[b26S=1N2O100O1O10000000000000000000000O1001O1O1M3N3Mb_]5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"_WV2:n<4M2N2N1O2N2N100O1000000O02O00000O2O001N2N2N2M4Lkci5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Q`R21V=6K3N2N3M2N2O1O06K1N1N2O1N2N2MmRQ6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"_[i16R=3N1O1N3N101N1O2O1O0O2O1O1O0000000001N101N2N2N2N2M5HYeU6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"[Tc14T=5J3O2N1O1O2O0O101O0O101O1O0000O1L5M2N2O2N1O2O1N2N2O\\l[6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"cjd12V=3M2O1O1O1O1O1O1O100O100O100O100000000000000001N1N3L3M4Mh[Y6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"lVj18o<4N3M1O1O1O1O100O10001O0O101O00O1N2N3L3N3M2N2N4KddU6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"ihd16Q=4M2O2N101N1O2O1N2OO1M3N2O1O1O1O2N1O2O0O2O2MWm[6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"aPa14Q=8L3M1O2N100O1O10000O01O1O100O1O10000O2O1O1O1O2N3Ja]^6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"l`Y12V=2O2N100O2O1N2O1O2N2N1O01O0O101O001NZjh6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"WlR18P=4M2N2N100O1O101N10000O10O100O100N3N1O1O2N2N2N2O2Mhal6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"lg]18P=3M3M4M2N3M101N10000O100000000000M3N3M2O1O2N1O1O2N2N2O1NX^`6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"UnR13V=1N2O100O1O1O100O10000O1000000000000001O001O001O1O1O1O1O3M^jj6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Zl\\15S=2N2O2N100O101N101O001N2O001OO1O1M4N1O1O101N1O2O1O1N2OQga6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"VeV16Q=3N3N1O2N1O2N2O1N2O1N2O00000000O1N2N2O1N2O2N1O2O0O2O1N2O1OdSg6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"caY15R=7K2N2N2N1O1O10L3N3N10100O1O10000O10000O2O001O002N1OU_e6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"k_m05S=3M2O1N3O0O1O100O2O00001O1O2N2N0001O0O100O2N1O2N2M3Mn`Q7"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Qam01R=;J2O1N2O1O1O1O10000O10O1N2O1O001O1O1O2N100O101O0O2O001O1O1Oejo6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"dkf02T=7K3L4M3N1N2O1O101N100O100000O100M3O1N2O1O1O1O1O2O0O101O1O2M4LgRV7"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Ude03W=0O1O1O100O100O100000000000000001O00Qg\\7"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"PX=6Q=6K3N2N2N1O000100O010O10000O100000001O001N2O1NhPc7"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"`oe16S=2N2M6L0O1O2O000O100000000001O001N2O1N2N3L4I]fZ6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"l^m14U=2O1N3N2N1O1O0O02N1N2O1O2O0O2O0OkfU6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"XnY24U=101N2O2M4M1O00100O0001N1O2M4Lhdi5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"hkm17Q=4M2N2O0O100000001O0000000001N1O3L3L^_T6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"R_h14T=2O1O010O10000000001O00N2O4K\\a[6"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"`nT21V=4N1O00100O100000000000N3O001Nfdn5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"gZ_25S=4M3M2N2O0O2OO10000O1O1O2M2N3M3NSkc5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"nmT21W=4M4L3M2O1N1000001O00000000O2O001N2N3Lmol5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"[[Z21Y=001N3M1O2N1O1000001O000020O000O1N1O1N1O3Llgf5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"f_R36Q=4M3N1O2O0O2O1N1000000001O001N101N2N3LW^o4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"SoY33U=4M4M3L2N2O0000000000000001O0O2M4K]ih4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"iWl25S=5L4L2N101O0O100000000001O0O1M4J6N2N\\SV5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"_^\\38P=4M1O1O101O0O1000000001N2O1N2NdTg4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"YWQ32V=3N1O2N101O1O1O1OO10001O0O200O2M^nQ5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"hXg22W=1O1O1O1O1000000O100001O00001O1O2Lg_[5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"SSh26R=2O001O001000000O11O002N2O0O1O0NeR[5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Vhn25S=3O0O10000O10000010O010N2O0O3LkjT5"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"cW[33U=5L1O100O1000000000000001N1N4M2NUng4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"]la34U=2M2O100O10000O100001O0Minb4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"QQk37Q=5L2N3M2O1N10001O00000000O1O2N1O2N2N2M3N4KSRV4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"mkP41W=4M3L3N1N2O1N200O10000000000001O00001O0O2O1O2M2M`on3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"SSW44R=4N3N1O2O0O2O1N2O2N1O0001O0O2N2O0O3M2Njjj3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"obc45S=3N1O10000O10000000000001O001O001O1O2MiZ^3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"^]_49P=2N1O101N101O1N2O01M2O1O2N101O1N2O1O3KX`b3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"VUh42W=2N1O101O1O1O1N3RCEi<?O01O001O1O1O1O3KTcZ3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"TVj31V=6L3L3N01O010O10O01000001O001O101N1O101N4LllV4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"flf47Q=5L2N1O2O1O1O0000000001O1O001O2M2N2N3MoP[3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Tbm42W=2M3M4J9J3N01N10001N2N3L4LekV3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"[bc43W=001N101O1O0020O100O0O1N2NRk`3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"YXl36S=001O1O10O11N1000001O100O1000O1O1NT`V4"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"PhS47o<5N2N1O1O101O001O0001O0O2O1N2N2Mk]o3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"WjZ4;n<2O0O101N101O0010O00001O0O2O1M4K_[h3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"_WV45T=1O10000O2O001O1O001O10N101N2O1NWnl3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"aah43S=7M1N1O10000000O1O1000001O001O3M4KiVZ3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Vlf45l<MUC9i<5O1O00M4O1O100O10001O00001O1O2N_l[3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Zd`48Q=3M2O1N2O0000000O10O101O000O101N4GWTb3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"UZb46T=KmB4P=MQC4m<5O1O1O010O1000O1M4M2O2N3MoXa3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"\\`P66R=4K4N1O1O10000O100000000000000001O001O001O1O1O2M3Lbmn1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"fkd56R=4M1O1O0O110O0100000000000100O010O100O2M4J_W\\2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"dc^55T=3M2M3O1N2N2O0O2O00000O11O0O1O2N2N2M4M2N4L__b2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"\\Pd51W=3L4N2N2N2O1N3N2N1O0000000000O2O0O2N2O1N3L5K`e\\2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"`YV57Q=4M3M2O1N2O000O100000000001O001O1O1O2N2M3M2M4Mjni2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"_nR54U=4K5L2N2O1N100O2O0000O101N100O2N2N2N2N4KPbn2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Ybm59P=3M2O1N100O010000O100000001N2O1O2MSVU2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Z_k56S=7I2O1O00O002N1O100O2O001O1N3MdSX2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"bbc57R=4L2N10O010O1O100O1000001O1O001O101M_h^2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"^Xj52W=2N1O2O1N1O3M3N3M3M10O001O4L1G9LYmX2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Yeo52W=2O4K2O1OO011N1O0100O1000000001O0000100O100O2NTcP2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"cSR53V=4K3N01O001O100O100O10001O00010O001NbWP3"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"_`\\53U=200O010O10000000001O00100O1O1O03LnWf2"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Z\\b66S=6J0100N200O2O001N2O2Nkkb1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"jki66R=5L2O1N2O1N100000O0O2O1O1O2O0O2O1O1O2MoQX1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"]`Z73U=101O1O001O010O1000001O001O1O1O100O01O1O1N2NaUf0"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"fZ[75S=3M20O0010O10O101O0000001O00101NQkg0"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"oeY73V=2N2N1O100O100O10O1O100O101O1N2O1O1NUeh0"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"Pdm63U=3M2O100O100000O1N2O1O10001N20O000`TU1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"mUR72V=4M2N00100O1000000001O001000000O3M]bP1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"_Qd61X=1O101N1O2N2N3N2M20O001O002DXC1g[`1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"V^S71X=1O2O001O2N1O1O1O10O001N2O1ORbP1"}},
    {"image_id": 303566, "category_id": 53, "segmentation": {"size": [426, 640], "counts": b"oQZ62V=3N3M2O1N2O1O00000001O002N1N]ni1"}},
    {"image_id": 331799, "category_id": 53, "segmentation": {"size": [464, 640], "counts": b"Ui`62[>4N2N1kAHR>=N2N3NO01O01O001O1N4M001O3MeQY2"}},
    {"image_id": 331799, "category_id": 53, "segmentation": {"size": [464, 640], "counts": b"aoY66Y>4L2O001O3M2N2O00O2N1O2N2N2N1O1O1N2O2NPn^2"}},
    {"image_id": 331799, "category_id": 53, "segmentation": {"size": [464, 640], "counts": b"_c]61_>2nAOa=3\\BNd=4ZBLf=7VBJMMj=:YBLf=4YBLh=3YBMf=O^B2b=M`B1a=NbB0_=OcBN_=0b`^2"}},
    {"image_id": 363461, "category_id": 53, "segmentation": {"size": [478, 640], "counts": b"chb37e>3N2N1O100O01000N101O1O1O01O1O4L2GaAOZQ`5"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"PaQ44fc09K4M2N2N2N2O001O1O0000O100O1O10O10O100AP]OMQc00V]OKkb04nkj4"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"lP^48ec06L4L2N2N2O1N101N2O00001O000000000001N101O1N101N101N1O2N3L6DY[Y4"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"o\\Q5:bc05N3M2N2N2O0O2N2O0O1O2O0O10010O0001N101O0O2O1N1O2N2N2M5JVWg3"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"bUW4;cc04M3N1N2N2O0O2O0O2O001N11O001O1O1N2N1O2N101N100O1O2N5I]Rb4"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"^UR4?`c04M2M20O010O001^Oo\\O3bc0L2NPfQ5"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"Y^S4;cc05L2N2O1O1N2O1N1000010O01O001O001O0O2@k\\O3Vc0HP]O5`c0N2MWmh4"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"aYi4?ac01N10001N1O2O0O2N2O0000000001O1O001O1O0O2N1M4M2N2N3M3M^no3"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"RRW54hc08J3N2M3N1N3M3N101O0O2O000000000001O001O0O2O1N2N101N2M3N3L5JTZ`3"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"`Qa51lc04M2]OLW]O8gb0a0O200O1O01000O010O01O00001O000O101N1O2N2L3N4K4LQWX3"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"l\\o51oc02M102M3M:GO101N3L3N3LSkS3"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"e]o51lc04M201O1O0100001N3N10M[jS3"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"jlR45ic05L3N1002N0O1O100O1O0010O0000O1O1N2NQok4"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"Zm\\41kc06L4L4M2N3M2O1N101O1O0O10010O0000O10001N101L4K4M4M3M2NoZ\\4"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"o`V57gc03M3L3M4M3N2N101O1O1N1001O001O1O0O2O001N101N101N1O2N2N2M3MW_a3"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"aYk48ec05L3N3L2O2M3N2O0O100000000001O001O1O001O1O0O2N2N2N2M3Mdnm3"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"Tf[47gc02O1O1O1O011N2O1N2O001O001O001O000000O1O101O0O2O1N2N3L5Jnm\\4"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"`]Z45hc08I4N001002M1O2N1N2O1O1N2O001O00000O101OO1001O00Wf`4"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"[UT48fc05K3O1O1O1O10O01O01O0Bm\\OOTc0NV_n4"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"QjT48fc04M3M101N10O100O101M2J6N3NSVm4"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"Xif51nc02M3M2J7N2N2O1O2N2N0010N100O2O1O0O2N2N2N3L5JmbU3"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"la[54ic03L6H601N2O1O001N10000O100O100O10O10001N101N2M3N2M4M3Jaf]3"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"Qni54kc07H3N1L4K500O10O10O01N3M2O2N2N4I\\VV3"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"\\f^56dc07O001O1O001O00000O0100O1O001O1O1O2MmU`3"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"Wjm49ec04L3N2N2O001O1O001O00000000000000O10O0100O1O2N2N2N2M5Jl]k3"}},
    {"image_id": 386210, "category_id": 53, "segmentation": {"size": [640, 478], "counts": b"gjh45ic03L4M4M4M1O0100O1N2O1N2O0O2O0O2O0O2N2LZ]U4"}},
    {"image_id": 405249, "category_id": 53, "segmentation": {"size": [375, 500], "counts": b"dY77^;4N1N2N2O001O00001O001O0O1K5O2N1001O1O2M5K3AmD5\\;O3LadV5"}},
    {"image_id": 405249, "category_id": 53, "segmentation": {"size": [375, 500], "counts": b"Tfc04b;4L2O1O000O101O01N100O1O2O1N2Nham4"}},
    {"image_id": 405249, "category_id": 53, "segmentation": {"size": [375, 500], "counts": b"a9`0W;00N2O1N3O0O101N2O1Nkhb5"}},
    {"image_id": 405249, "category_id": 53, "segmentation": {"size": [375, 500], "counts": b"h[51d;4M2N1O1O2O0O1000000000O10O010001N1O100M4NQfY5"}},
    {"image_id": 405249, "category_id": 53, "segmentation": {"size": [375, 500], "counts": b"o64b;2N101N1O100O100O10O10O010000O101N1O1O2O1O2Mo^^5"}},
    {"image_id": 405249, "category_id": 53, "segmentation": {"size": [375, 500], "counts": b"gfd12d;1A7nDKP;`0M2O1O1O100O10O10000O010O100N2O1O2N1O10001N101O0O2O1O002N000O01000O1O100O100N2O\\eb3"}},
    {"image_id": 405249, "category_id": 53, "segmentation": {"size": [375, 500], "counts": b"Sbd44b;2N2O1N2O00001O00000000000001N10001N1O2L3O`_j0"}},
    {"image_id": 473406, "category_id": 53, "segmentation": {"size": [640, 480], "counts": b"e\\d67gc04L4L3N1O2O1N1O101N100000O001O1O1O1000O10O10001N100O1O1O1O10000001O01O00000000000000001O00000000000000001M2K5N3Meoc1"}},
    {"image_id": 473406, "category_id": 53, "segmentation": {"size": [640, 480], "counts": b"dTf76hc03M3M3N1O2O0O2N100O1O1O100O010O01O001O1O010O01000O10O10O1000O0100O10O01000000O1000000O1000O010000O1000O10O100O1O1O2N100O2N2O1N2N3Mmc<"}},
    {"image_id": 473406, "category_id": 53, "segmentation": {"size": [640, 480], "counts": b"dRm65hc04M3L4L4M2N3M3N2M3N1O2O0016Ia0_OZmT2"}},
    {"image_id": 473406, "category_id": 53, "segmentation": {"size": [640, 480], "counts": b"a^V76fc0;G5K4M2N1O2O0O2N1000001O01O2O2M4L3M2N3N1N2M3N2N2N3M3LkPd1"}},
    {"image_id": 473406, "category_id": 53, "segmentation": {"size": [640, 480], "counts": b"YRa75kc03L4M2N3M101O101O1N1001N3M2Mj\\OBkb0>=O100O100O1N2N1N3NcX[1"}},
    {"image_id": 473406, "category_id": 53, "segmentation": {"size": [640, 480], "counts": b"Qnb73mc02N2N1O1O2N2O1N2O2M3N2M2O001O1N100000N3N1N2O2N2M4L:ETUX1"}},
    {"image_id": 473406, "category_id": 53, "segmentation": {"size": [640, 480], "counts": b"egY68fc03N3N1O1O001O0010O0010O01O10O00001O001O00001O01O01O01O00000O10O100O10O010000O10000O01O1N2O001O10O1000O10O10000O10000O010000000001N3L4K`hg1"}},
    {"image_id": 473406, "category_id": 53, "segmentation": {"size": [640, 480], "counts": b"nZd65jc05J5L3M2O2M3N1O1O1O2N001O01O1O1N2O1N101O1O1N2O001N101O000O2O000O2O001N1000000O101O0O101O00000010O1O2M;F1OO100O2N1O101M201O2M2N2McP_1"}},
    {"image_id": 473406, "category_id": 53, "segmentation": {"size": [640, 480], "counts": b"VXU71mc03N2N1O1000000O2O000000000000000O2O0000000O1000000O1O101N1O1O100O010O01O00100O010O1O010O0100O010O10O010000O02O00001N2O2N2M6JV\\o0"}},
    {"image_id": 473406, "category_id": 53, "segmentation": {"size": [640, 480], "counts": b"Vkn73lc03M3N3L3N0O1N2O00010O0101O00010O01O101O1O3L3N0000O>B1O1O1O1N3N1O2NTlg0"}},
    {"image_id": 482719, "category_id": 53, "segmentation": {"size": [480, 640], "counts": b"iXR33m>1O1N101O1O1O1O1O1O001O1O001O001O001O1O1O1O100O1O1O1O001O0010O01O0001O01O00010O0010O01O010O01O010O0100O010O100O010O10O010O1O01000O010O10O01O10O0100O10000O100000O100000O2O0000001O001O001O000O2O001O1N1O3N1N3MYmh4"}},
    {"image_id": 482719, "category_id": 53, "segmentation": {"size": [480, 640], "counts": b"XVa44k>3M4L3N3L5K4M3L2O2M2O0O2O1N1O2O0O2O0O101N100O2N1O2N1O1N3M2O101N1O2N1O101O0O2O001O001O001O001O001O1O001O001O001O1O001O10O01O1O010O001O10O01O010O1O1O100O1O1O100O1O10O01O10O01O010O10O01O100O00100O010O010O0100O00100O001O1O010O1O10O0100O1O100O100O1O100O1O100O100O100O2N100O101N1O2O0O2N2N2N2L5J5K6I9]Od0FZmd2"}},
    {"image_id": 482719, "category_id": 53, "segmentation": {"size": [480, 640], "counts": b"Rge68e>4N2M3N1O2N1N3N1O2N2N1O2N2O1N1O2N2N2N1O2O0O2N2N101N2O0O2O1N2O000O100O10000O10000O100000000O1000000000000O1000000000000000000000000001O00000000001O00000000001O0000001O000000001O0000001O00001O00001O00001O001O001O1O001O1O001O1O001O1O001O1O1O001O1O1O1O1O1O1O1O1O1O1O1O1O1O1O1O2N1O1O1O2N1O1O2N1O1O2N1O2N2N1O2N2NSR>"}},
    {"image_id": 509131, "category_id": 53, "segmentation": {"size": [425, 640], "counts": b"gaX36P=;F;F1N01O1N2O1O101N101N101O001O001O00100O001O100O1O100O101N2O2M3N1Mlab4"}},
    {"image_id": 553664, "category_id": 53, "segmentation": {"size": [414, 640], "counts": b"[]T48e<5K4K3O2N2O01O000O1O3M5K3M2N4JTkg3"}},
    #
    # "sandwich"
    {"image_id": 226903, "category_id": 54, "segmentation": {"size": [480, 640], "counts": b"lYo71n>2L3O101N1O100O2O0O100O101O0O100000000O101N100O11O0000000000001O000000001O001O1O001O001O1O002N001O00O1007HR\\c0"}},
    {"image_id": 530146, "category_id": 54, "segmentation": {"size": [640, 640], "counts": b"[Zn58gc02M4N1O1N2O1N3M3M6K4K2N3M3L3eNiNk_OY1Q`0ZO]_Oh0``0^O\\_Od0``0CX_Ob0d`0`1L4L5K4L3L5L4L3M3N3L3M4L4M2M4M3L4M3M2M3N3M3M2O1N3M2N3L4M2N2N3M3M2N3M2N2O2M3M2N2N1O2O1N3M2N102M2N2N2O0O2O1N2O1N1N3O1N101N2O1N101O1N2O1M3O1N2N2N2M3N2N2O1N2O1N2O1N3N1N2N2N3M2N3M3N1O1N2O1O1N2O1O1M3N2N101O00001O001N2O1O0O10000O10001N1000oEcF^9^9`FdF`9\\9_FeFa9[9^FfFb9[9]FdFd9k910000O1O1O100001N101O1N101O001N10001O001O001N101O001O001N101O0O2O0000000O10001O000O10001O3M2N0O101O0O101O0O101N2O1N101N101N2O0O2O1N1O2O001N101N2N2N2O2M3M3L3N2M2O1N3M2O2M2N3N2N3L3N1O2M3M2O1N3M3N2M2N3M3M3N3L3M4M3M3M3M2M4M4K4M3L4L4L3M3M3M2O1M4M2N3N1N3L3N3M2O2N3L5L5J6J6I5L3\\Ob^ObNba0Mf^Oc05WOYa01k^O?Pb0[OW^O3hlS1"}},
    {"image_id": 530146, "category_id": 54, "segmentation": {"size": [640, 640], "counts": b"^UQ25ec0;F9@c0C`0@:F8H8I6J6L4L5J6K5J7K6J5K5K4L4L4L4L4L4L4L4L4M2BdJUB^5h=eJWB\\5f=a0N2M4L3N3K4M3N2L4M3L3O2M2N3N1O2N100O2O0O2O0O2O000O2O0O1O2N1N3M2N2O2N1O2O000O2O001N10001O00001O00001O0010O0001O0000001O00001O00001O0000001O00000O2O00000O101O000O2O001N10000O2O000O10001O0O1000000000000000000001O00000000001O01O01O0000000000000000000000001O00001O001O0000001O0O2O001O001O00001O0O2O1O1O1O1O1N2O1O001N2O001N101N2O0O2N1O2O0O2N100O2N2O1N2N2N1O2N2N1N3N2O1M2O2N1N3N2N1O2M3M3M3N2L4N2M4L3M3N2M4J5K6L3N2O1N3N1N3N1N3M2O1N2N3M2M3N2N2N2M3N2M4L3M3M4K5L5K4K5K4I8H8G;G`0^O`0C:TOS]O2lVY5"}},
    #
    # "orange"
    {"image_id": 18575, "category_id": 55, "segmentation": {"size": [480, 640], "counts": b"ekg76f>=D7I6I7K4L4L4M2M4M3M2N3M2O1N2N1N3N2O1N2N1O2N2N2N101N101N2O001O001N101N101O0O10001O000100O001O1O0001O000O100000000O1000000000O100000000O100O1O2O001O2N1N3N2N2N2M2O000O2O0O101N1O101N101N1O2N2L4I7N2N2N2N3SO_B5d=GaB6e=A`B<U>L3M5Jon1"}},
    {"image_id": 50896, "category_id": 55, "segmentation": {"size": [640, 640], "counts": b"][o32nc01N10001N10000O101N100O100O1O100O100O100O10000O100O100O100O1O1O1O1O1O001O1O1O0O2O001N2O0O2OO0O2K4O10010OO20O102M4M5K3L5L4KfmY7"}},
    {"image_id": 184791, "category_id": 55, "segmentation": {"size": [500, 640], "counts": b"iTk41Y?c0E5L4K5K4L4M3M2N3M2N2N2M2O2N2N2N101O001O0001O0001O0001O000000000000000000000000000000000000000O0100000000O010000000O10O101M2O1M4N1O2N2O1M3N2M4M3L3O2K5K6K4L5JbYf3"}},
    {"image_id": 184791, "category_id": 55, "segmentation": {"size": [500, 640], "counts": b"ici6b0i>=F8K4M4M2N2N2O1N2N101N101N100O10001O01O00001O000000000000001O0000O100000000000O100000O100000000O0100000001O001N2O1O1N101O1N2N2O1N3N1K6L3N3L4K5K?@mgj1"}},
    {"image_id": 186929, "category_id": 55, "segmentation": {"size": [500, 333], "counts": b"Tgc33a?2N2N1O1O1O001O1O001O001O1O001O1O001O001O001O1O001O1O001O001O1O001O001O001O001O001O0000O10000000000O100O10000O100O1O1O100N200000000O1O1O11O00001O0000O1001O001O0000000000001O1O1O1O00001O1O00O1"}},
    {"image_id": 280891, "category_id": 55, "segmentation": {"size": [640, 427], "counts": b"lTc03lc03L4M2N3\\]OH[a0;_^OJ_a0:Y^OLfa09n]OMRb0Q10O001000O10O10O1000O0100O101O0O2O1O002N1O002N1O1O1O00000001O0O100O2O001N101O0O2O001N2M3L4M3N2M3N3M3M3M3M4L5K9Faf_6"}},
    {"image_id": 280891, "category_id": 55, "segmentation": {"size": [640, 427], "counts": b"]go13mc01O001N3N001N2O2N1O1O1N3N1O2N000001O0000000000001O0000001O00001O001O002IdPd5"}},
    {"image_id": 366711, "category_id": 55, "segmentation": {"size": [640, 427], "counts": b"ibe3;bc05M3M2N2N2M2O1O10000000O101O00000000100O10O01O1O001N3L4M3JYaR4"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"hWY35l94M3M2N3M2O2N1O1O2N1O2O0O2N2OO001N2M2O2N2O1N200O1O1O100O2O0O10000O100O101O0O1000001O001O1O1Nlb`0"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"_Ye38j93L4M3N1N2O2N1O2O0O2N1O2O1N2O0O2O1N2O1N2O1O1OO0N3M3N2M3N2N2O1N2O1O1O1O101N1O100O1O10000O2O0O101O001O0O2O001O0O3Mk[1"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"TZ^34m95K4M4L4M2N2N1O2N1O2O1N101N2O001N2O1O1N2ON2M2O2N2N2N2O1O1O1O1O1O2O0O1O100O2O0O101O0O2O0O2O001O1O001O1O1O1O1O1O1O2MjP8"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"njb2<e95L3M8I3L4M2N2N2N2N2N2N101N100O100O10N1D=M3M3O1N101O1O1N200O2N2N5L6I3N1N2O1N\\`Y1"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"PVi2?a98J4L5L3L4M2N3M2N2N2N2OK4M4M2N3N1O2O1N2N101O1O1O100O1O1O2O1N3N3L4M3M1N3N1O1NXUS1"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"aPm23j9:J3M3O1N2N2N2O1O1O1O1O1O1O1O100O100O100O10000O10000000O1O1O100O1O1O3M3M6K3L4M1N3N1N3N2MU^m0"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"ZVV31R:2N1O100O1O1O1O1O100O10000O100O10000O100000000O100002N6J2N3Lkeh0"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"jTW25k99H6K4L4M2N1O2N2N2N100ON2N3N1O2N2O001O1O1O1O101N4L4M2M3N1O1N101O1N2O1OjTf1"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"mnZ28h98J3M6J3N2N1O2N1O2O1N1O01L3O2N1O2O1O001N20OO200O1O2O5J4L3N1N2O1O1N2O1OgZb1"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"SS_24m94M2O1N2O1O1O1O001O1O1O100O101N100O1000000O10000000000000000002N3M3M2N2N2N1O2N1O1O1N3N[e[1"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"WRT11R:1O1O100O100O1000000O10000000000O1000000001O000000001O00001O001O1O001OZWi2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"\\[a13n94N1N2O1O1O1O1O100O1O10000O100O100001O4L3M2N2N1O1O1O1O1OnT^2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"oZg1:g98I5J5M2N3M2N2N1O2N10N1I7N3O1N101O001O0010O01O100O1O10000O100000001N101O001O00100O001O1O100O1O1O2N4LiVQ2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"Rkj15i96M4M2O1O1O1N2O1O100O10O01O10O00100O010O100O100O10000O10000000001O0O1001O01O001O001O1O1O00100O2N2MRQn1"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"Rco12Q:100O100O100O100O10000O1000000000000O100001O00000000000000001O000000001O1O00001O001O001OZkj1"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"h6k0X910O010O0100O1000O10O1000000000000000000010O0O10001O000O2O1O1ZOdFb0_9O10000O2O2N2M:Fhik3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"Y6?d90100O0010000O10O10O100000000000001O0000001O010O1O00100O10O02O1N[Qn3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"l5<h90O10O10O010000000000000000000001O0001O01O10O0100O10O100001N3Nh[n3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"a5:j9000O01000000000000000000000000001O01O01O0100O0100000O101O3LWfn3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"Y58l9000O0100000O10000000000001O0000000010O00010000O10000000002Lafn3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"m4<h900O01000000O01000000000000001O0001O01O01O01000000000O2O1NRQo3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"ia<4n9:AFdF<X9FhF:W9GiF9V9HjF8U9IkF7T9JmF5R9LoF3P9MTGOl82WGIk87`0100O10001N100000001O0O100010O0000000000001N101O001O001N2O3L]k^3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"bn:=e93N1O1N2O1O01M2O2O001O001O001O010O100O01000O10000000000O10000010O01O001O00100O011N1O2O1Nl__3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"Sd:9i94K110000000O10000010O010O1O10O01000000O10000000000000001O00001O010O10O0100O010O10001O1L^j_3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"Vo99i92O00O100001O000001O0010O000100O100O1000000000000000001O010O0001001N10`Zc3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"fP?2o94N1O1O1O10000O1O10000O2O001O000000K5N2O1N2O2MeRb3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"ofd06k95M3M3L5L3M2N3N1N1O100O01N2O1N2O010O1JjF]OW9b062NO1M3G9N2N3MPT[3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"hkh07j95L4M1N010000O10001O010O00100O001O1O1O1O100O100O100O100000001O0000001O001O1O1OcUS3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"jYl0;g96J5K4M2N3L3N2N1O100O100O1O101N100O1000000O2O00010O0001O0K5M4L3O1N3N2M2O2O0O2N3M2N2O2M4LfTn2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"W`U15j98K3M2O2M2O1O2N1O1O2O0O1O100O100O10000O100000000O10000000000001J5L4O2N1N2O2N101N2N102M101N3N2NTPd2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"]nX13Q:1O2M2O3M4M1N0000O1O2M2O1O2O0010O01O1N3MiRi2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"nWS11R:10001O00001O00001O001O010O001O010O01N101O2MRUn2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"``Z17j96J4M4M3M2M3N1O2O0O1O2O0O10000OO2O1N2N2O1O1N2O1N2N2O2N1N2L5L301O001O1O1N2OSUb2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"Shb18i96K2O2M2O1O2N1O1O10F:N1O1O2N2N101O1O1O1O010O101O0O100OnR]2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"^me1<e94M2O2M3M2O1O1O1O0010O001O10O10O010O1000000O10000N2M3N2N2O2M2O2N1O2O1N1O2NXhV2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"cfo15k95N2N1O2N2N2O1N2O0O100O100O1000O10000N1N3N2O1O1O1O100O100O101N10000O2O1O001O1O1O1O\\fk1"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"WgU23o92N2O1O1O1O100O100O01000O010O01O100O1O1O2O000O101O0O2O001NZ_i1"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"PUZ21S:0N101O0010O01000OhF0]81bG0^8ObG3]8MbG4^8LaG5^8KbG5_8KaG4`8L^G5c8K\\G6d8I]G6d8J[G7e8IZG7g8IXG7j8HUG7m8IQG8]9O10000000000O101N101O2NbTc1"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"eR[22P:3N2N2N2O1N101N3N1N2O001O00L4O1O1N2O1N2O2N1O2O0O2O1NTRe1"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"g`_23P:2M3N1N2O1N2O100O2O0O1O10001N101O00001O00000000O100000001N1O1O2N1O2N101N2O1O1O1O2NUl[1"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"aTf27k92N2N2O001O001O100O01O010001O001O0O01O1O1O101N1O101N10001N2O1O1O1O^iW1"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"U]T32Q:2N2N2N2M3M3L3M3L4000FkFEU97?M2O2N1O2NScn0"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"haW32R:1O001O001O001O00000000O10000000O10000O100O100O10O0O1010O1O100N3M2O10O2O2N5Kaid0"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"ek97i99J101O00O010000O1N1100O1O2N101N2O001N101N3N1O2MWmf3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"^k94o910O010O0100O010000O2O00001O001O_^i3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"W\\<4o91O1000001O01O000MeTi3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"hk?2Q:3N1M3N3M2O3L2O00O1O10000O010010O0010O001O1N2N3KWm`3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"[m>2P:3M200O00O101O001O010O10000000001O001O\\^c3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"V`f02Q:2O2O3TFId9:1HZF0ib`3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"]Tg02P:2O1O000010O01000O10000O10001O001O`k[3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"lRh04n93N1O01O001O1O00100O10000O10000O2O00mbZ3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"fZ>5m94L3N2O1N101N100000001OO100O2N2O2M1O9GfPd3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"^bd11o99J3M2N1O1O1000O100O2N100O2O0O2O001O1N3MQ_]2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"UPV12Q:2N2N1O1O1O01N2O010O100O1000001O001O1O_[l2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"g[\\11Q:3O0O1O2O0O101O1O001O0000N3L3N_Xg2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"Rj_19i94M2N100O2O0O100000001O01O001N1O2N2M4M_ab2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"hc]13Q:3L4K3N1O10000O10010O0000O10000O2O00001N3NaSd2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"QRi03o95L3M2N2O1N100O101O0000001O000001N1O2N2N1O3MV[X3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"jZP14n96J3N2O0O1O10000O2O00010O000000O2O1N2N2M5K`\\Q3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"c^n07k94M2N1O100O100O101O0000000001N100O2O1N2O2MgXS3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"^ll03P:3M2N2N1O10O100000000O1N2N3N1NhgV3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"gUg08j94M2N2N3M100001O1O1O00001O01O000001O0N3N2N4LZWZ3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"[YW1:i93M2N100O1000001O0O1000O2O000O2O0O2N2N4L4Li]j2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"W]U16l95L2N2N1O10K5M201O1O1N2O2O0OTan2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"mX]14o92N2N3N3L2O1O1OGaFIc966O1O1N200O2O1OQQf2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"Ze\\11R:2M4M2NO1O011O1O2N2O1N\\Wh2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"olW13P:1O2N2O2M6K1O00001N11OO2O01O001N2N2N2N3M\\Tj2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"eaX13P:00100001O00001O00Sol2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"Xnj06n91N2N2N100O100O2O0O10001O1O000001O0O2N2N3M4Kl^V3"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"klQ15n94K4M2N100O10001O0000001O001O00O1O1O2N2N1O3L3NWVo2"}},
    {"image_id": 498919, "category_id": 55, "segmentation": {"size": [324, 432], "counts": b"PZP14P:3L2N2O1N2OM2O2N2O1O100O2O001O1OmoR3"}},
    {"image_id": 529966, "category_id": 55, "segmentation": {"size": [421, 640], "counts": b"]ok5=e<7I4M2N2O1N101N2O001O1O001O1O1O1O010O1O100O101O0O10000O10001O000O10001O001O001O001O1O001O1O100O1O1O100O1O101N3N1N2OO001M3I6L5L4M3M3N2M3N2M3N3M2N3M3M2N3M3M4M3LRXZ1"}},
    {"image_id": 529966, "category_id": 55, "segmentation": {"size": [421, 640], "counts": b"QSe6b0]<;H5L4L4L4M2M3N2N2N1N2O1O2N100O1O2N101N101N1O2O1N101N2O1O0O2O1O1O0O101O00O10000000000O2O000O2O0O101N101N1O2O1N1O2N101N2N1O2M3N1O2M3N2N3L3N3L4L4K6H=@bVc0"}},
    {"image_id": 529966, "category_id": 55, "segmentation": {"size": [421, 640], "counts": b"oS]22S=1N2O1O2N1N2O2]DDY:=dEFZ:=aEF_:<[EHd:<UEHk:>iDHV;T100O00100<D6I4M2N1O2M2O2N1O1N2O1O1N2O1O0O2O1O0O2O001N100O2O000O2O0O100O100O100O1O10[[S5"}},
    {"image_id": 529966, "category_id": 55, "segmentation": {"size": [421, 640], "counts": b"jeh41l<?D6L5L3M2N3N2M3N2N2N1O2N2N1O2N2N2N101N2N2N101N101O1N101O001O0O2O001O001O001O001N101O01O0000000O101N1O101N100O2O001N101N1O2O1N1O2N2N2N2N3M2N3M2M3N2L4N3K5K5K6JUb]2"}},
    {"image_id": 529966, "category_id": 55, "segmentation": {"size": [421, 640], "counts": b"g_g54P=3L4L4mCFV;>dDFZ;T1N2N1O1O010O1O1O10000O100O10001N1000000O2O001O00001O001O1O001O1O1O10O01O000001N10000O2O0O2O1N101N2N101N2N2N2N2N2N2M4M2N3L5J6J9EXXc1"}},
    {"image_id": 529966, "category_id": 55, "segmentation": {"size": [421, 640], "counts": b"gg_53o<3O2M2O2O0O1O1O2N1O1O2N1O1N2O2N1O1O1O101O0O10000O101O0000000O1000000001O01O0000000001O001O00001O001O001O1O1O001O1O1O2N1O1O2N1O3M2N4Kijk1"}},
    {"image_id": 529966, "category_id": 55, "segmentation": {"size": [421, 640], "counts": b"XdY63P=4M4L4M8G2N2N1O010O1O100O1O1O100O00100000000O010000000O01000000O10001O0O10001N10000O101O0O2O001N101O0O2O1N101O1N2O1N2O1N3N1O2MgUS1"}},
    #
    # "carrot"
    {"image_id": 460494, "category_id": 57, "segmentation": {"size": [426, 640], "counts": b"m\\h23W=1N2O1O0O2O1O002N1O1O2N1O2N2N3M1O1O1O10O01OO101N2M3N3M3L4M2N2Ll`T5"}},
    {"image_id": 460494, "category_id": 57, "segmentation": {"size": [426, 640], "counts": b"QWS33V=3L4M2N2N10O010O0O2O001N110O2N101O1N2Nnfn4"}},
    {"image_id": 460494, "category_id": 57, "segmentation": {"size": [426, 640], "counts": b"mS[32W=2N2N2N100O100000O100O100000001O000O1O100O2NQbe4"}},
    {"image_id": 460494, "category_id": 57, "segmentation": {"size": [426, 640], "counts": b"Xjc21X=3N1N2N2N2N2O00000O10O10O010000O101O001O1O1O2M4MlP\\5"}},
    {"image_id": 460494, "category_id": 57, "segmentation": {"size": [426, 640], "counts": b"Y\\m23V=4K5M1N1O1O1O1O1O101N10000O10O1O1O001O10O0100O100O100000001O01O10O101N2M4M3Jddl4"}},
    {"image_id": 460494, "category_id": 57, "segmentation": {"size": [426, 640], "counts": b"mnb23S=6M2M4M2N2N2M3N2N2N2N2O0O1O100000000O10001O0000000O01O1O1O1O2N1O101N2N2O1N3N2N1N3N1O2M2M4LkTT5"}},
    {"image_id": 460494, "category_id": 57, "segmentation": {"size": [426, 640], "counts": b"[SV33V=1O1O10000O10000O2O000O2O1O2N2N3L3N1O000O10O1O2K5N2N2N101N3N1N2OZ]f4"}},
    {"image_id": 460494, "category_id": 57, "segmentation": {"size": [426, 640], "counts": b"VS`34T=4M1O2O1N2O1N100O0100O1O1O2O1N2O1N2O1N2MZ]a4"}},
    {"image_id": 460494, "category_id": 57, "segmentation": {"size": [426, 640], "counts": b"`]h31W=2O1O100O1O1O100O101O3L2O00000O0100O1000O1001O01O1O10O1O001N1O2N1O2N2N2OQ^R4"}},
    {"image_id": 460494, "category_id": 57, "segmentation": {"size": [426, 640], "counts": b"Xe_33V=1O2M3O001O1N2O1N2O1N2O0O101O1O1O1O1O010O000001O0O1O2O0O1O100O1O2O0N3N1N3M3N2MZnY4"}},
    {"image_id": 460494, "category_id": 57, "segmentation": {"size": [426, 640], "counts": b"nl`34S=3L4M3N11O001000000O100000000010O01O1O1O1O010O0001O0001O1O2N_^\\4"}},
    {"image_id": 460494, "category_id": 57, "segmentation": {"size": [426, 640], "counts": b"]fZ48P=3N2N1O00100O100O1O1000000010O01O0001O0O100O100O101O1O001O1O001O100N2N[b`3"}},
    {"image_id": 460494, "category_id": 57, "segmentation": {"size": [426, 640], "counts": b"jiW44U=9G2N2N2N3M2N1O01O010000O1000O1O1000010O010O001O1N2O1N2N2M2M6JXTe3"}},
    {"image_id": 460494, "category_id": 57, "segmentation": {"size": [426, 640], "counts": b"]Vb41X=2N2O1N2O1N4M2N001N110O1O1O100O01O100O1O2N3N1M2N3MUW]3"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"WeR31Wc08Q]O2hb0o0D4N2N001OO100000001O001O1O1O1N2O1O2O1N4L001O0O101O0N2M4M3L4M2O3LS[b4"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"gXU2:fc03L3N1N3M3N1N2N101O1O1O1N1N2O100O00010O1O010O010O1N2O010O01O00001O1O100O3N1N2O1O3M2M3N1N3M3M3M6JWoV5"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"R`g13ic08I5M3M3M2O0O101O1O1O1O01O01O000O10O0100O1O1O100O1O10O000010O1O00100N1O20O010O1O100O1O1O2N101N2N1O100O100O1O1O2N2N3M3M4L^X]5"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"_>n0Rc00O2N1O1O100O1O1O100O1O00O2OO1000001O010O0010O01O00001O0100O1O2N102M2N2N2N3M2O1N2O1N2O1N3M2O2M3M3MbU[7"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"\\<i0Wc01O2M2O001O0000O1O10O0100O1O2O000O2N2N2N3N2L5L3L[kj7"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"d\\?4lc04L0O01O1O10O10O100O010O10000O10O1000O10000000000000010O00001O00001N^cU7"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"lS]26fc05M2N1O1O110O01O1N3M2O1O2O0O2O1N^Tc5"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"e_U39dc04N100O1000001O00000000000000000000000O10000000O01000O10000O1O1N2O1O1O2O001O002M_h[4"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"mRQ35jc03M3N1N3N1O1O1O2N1O1O00000001O000O100O1O1O1O2N1O2O1N2O1N2N2O002MmTe4"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"igZ16hc07I3N2O1N2O1O0010O1O01O0O1K6K4N3N10001N100001O001O1O2N1O2N1N101N2O1N2N2O1N2O1N2N2O1O1N2N2N2NRhR6"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"Rg_13mc01N2O0000001O00000001O00001O0010O10001N10000O10O1000O101O000O1000000001O001O1O0O1N3MTXP6"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"aUf08fc02M3N3ML50010O01O10001N101N2O1N11N1N2L5M3LonV7"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"Z`;3kc06K3M9F3O0O2O00001O00010O01O01O01O0010O0010O0010O0000O1M4M2O1O100O1O1N2M3N2O101O2MdSU7"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"hZ=3mc01O1O1O0O2O001O1N101N2O001N101N100O2O000O1000O1O001O001O1O2N101N2N2O2M2OZ]V7"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"le2<bc04J4K6I6M3O2O0O2O0000001O01O00001O0000001N101N1O1O1O1N3K4M3M4K5J6Lenb7"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"deP15jc03M4M2M2O1N2N4L2M2O2N1O1O001O00010000O100O1O100O1O1O1O2N1O100O1O1O2O0O:FaRc6"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"^bW18cc06N1O1O0010O1O1O0100O1O00Hc\\OO]c00900100O10O102M2MQnd6"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"[bU23kc04M2O0^\\OH[c0:b\\OKZc0?O0O2O01O2O1N1OO1O1CAX]O`0gb0BX]O>gb0CX]O>hb0BX]O>hb0CW]O=ib0>OO1000000TOW]Oa0jb0]OX]Ob0ib0\\OX]Od0Rc00000O10O1O010O1O010O1O0001O1O2M2O2M2N3M4KoeV5"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"eVT33lc02N1_O1o\\O1mb05o\\OLPc08m\\OIQc0c001ON30O2O003L101O001O00001O0O10O100000O01O0G:M2N3N2L4N4Iaj`4"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"cij25ic03M3N1N3M2O2N2N2O1N2O10O0100O01O1N1O2L3N3M2O2N1O2O001N101O1Mafl4"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"TYk33`00ib01T]O3kb0b0N101O00O1M3O1O100O10001N2O1O2N1O1O2M3N3LaVQ4"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"[ie24hc06K4M2O1O100O000001O1O1N101O1O010O010O00100O1O100O1O2N2NVoR5"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"Zlc2=ac06K4L4M2N0O01O1O1O100O100O2O1O1N3N2M3M4IckY5"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"ZXR36ic01N3N1O2M2O2M2O2M2O2M2N2O2N1O1000O0HW]OYOkb0e08N300001N1000000000O1N2O2N1O101N2M]`a4"}},
    {"image_id": 465585, "category_id": 57, "segmentation": {"size": [640, 427], "counts": b"io`05ic05L4L2M3N100O1O1O1O010O1O10O0100O10O10O010O0010O01O010O10O1O1O1O1O2N2O0O1O2N2N2O0O2N1O1O2MgTm6"}},
    {"image_id": 567898, "category_id": 57, "segmentation": {"size": [454, 640], "counts": b"Yla44Q>2G9N1O2O001O10000O0O100O01O1O1O1O2O1O7I1N2N^eo3"}},
    {"image_id": 567898, "category_id": 57, "segmentation": {"size": [454, 640], "counts": b"cSU33Q>2N4M2O1N1O2O1O100010O000O1O1O1N2N3N1N2NYZ]5"}},
    #
    # "pizza"
    {"image_id": 127476, "category_id": 59, "segmentation": {"size": [640, 480], "counts": b"PTc22nc06J9G5K2N001O1O2N1O1O1O004L001O002N2N001O00001O1O1O1O1O1O00001O1O0000001O000000001O0000001OO1O10000001O00001O00000000000000O10000O100O10000O1O100O100O1O100O100O100O100O1O100O1O1O1O100O1O10000O1O1000000O10000O10000O100O100O100O10000O1O1O100O1O1O1O1O100O10000O100O100O100O100O10000000000000000000000000000000000O1000000O1000000O10000O1O1NRX_3"}},
    {"image_id": 535253, "category_id": 59, "segmentation": {"size": [612, 612], "counts": b"f[V37mb03M4K4M4M3L3M5K1O1O00000000000000O101O0O3N3L3M4M4K;DgWg7"}},
    {"image_id": 535253, "category_id": 59, "segmentation": {"size": [612, 612], "counts": b"VQX38gb05K5K5L4M3O100O010000O10000O100O100O1O1N3L3M3K6KPjf7"}},
    {"image_id": 535253, "category_id": 59, "segmentation": {"size": [612, 612], "counts": b"RVe33lb06I6K5L3L5N2O1000O10000O10000O100O100O1O1M3L5K4J[eY7"}},
    #
    # "donut"
    {"image_id": 34417, "category_id": 60, "segmentation": {"size": [375, 500], "counts": b"[Rd45a;101O00000000000000O100O2NPmm0"}},
    {"image_id": 34417, "category_id": 60, "segmentation": {"size": [375, 500], "counts": b"gkl42d;2N2O00000O100001N10jVf0"}},
    {"image_id": 163640, "category_id": 60, "segmentation": {"size": [457, 640], "counts": b"noQ65Q>3O1000001O0001O00001O00001O00000000001O001O1NYm`2"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"i_f06]=>D5K4L4L3M2N2O1O001N101O001O1O00100O1O010O1O100O0100000O100000O0100000000O1000001O00000O100001O00O2O000001O000001O0000001O01O01O000010O000001O010O001O010O01O010O001O0O2O0O2N2N1N3L5L3L5L3N3L3M4M3L6KcPa6"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"Sc`1=W=4L3N2N2O1O2M2O1O1O2O0O1O1O2O0O1O2O0O2O0O2O0O2O001N101O1N2O1O1N3N1O2M2O2N2N2M2O1O001O0000000000000000000000000000O1000000O101O0000000O2O00001O000O2O001N1O2N1O2M3L3M4K5L4M3M3M3N2M4M2N3N3K6JiQi5"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"oUY2>U=6H7L3M3N2N2O1O1N2O1O2N1O100O1O2N1O10001N100O2O000O2O0O2O000O2O001N101O0O2O1O1O1O0O2O1O1O1O1N2O001O1O1O1O1O1O1N2O1O1O100O1O1O2N001O0001O0001O0001O00000000001O000O101O001O000O101O000O10001O0O101O0O101N1O100O2N2L4F9I8K5L4L4M3M2N3M3M4L3N3L4M3M5Keld4"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"ZYY34`=9I1O2K4I7O1O2N1N2N3N100O2N1O100O2N1O1O101N100O2O0O10001N101O1O0O2O1O1O1O1O1O001O2M2O2N1O2N3M3M2N1O000001N10000O10000O1000000O2O00000000000O101O0000001O001N101O001N101O001O001O0010O01O001O1O001O1N2O1N2N2O1N2N2N3M2I7I7J6J7J`Ri3"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"gcg48[=9H5H7H9M1N3N2N1O2N1O2N101N2O0O2N101N2O0O2O001N2O1N2O1O1N2O1O1O1O1N2O1O1O1O000O2O0000000000000O1000000000O1O101N1O100O100O100O101N10000O2O000O2O000O101O0O101O000O2O00001O001O00001O00001O00100O001N2O1O0O2N2N2N2N2M3N3L3M3L4K5K6K5JP_Y2"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"SkQ5;1FR=h0G6L3N2N1N2N2O1O1O100O00100O1O100O10O010000O100O1000000O1000000O100000001O0O100000001O0000001O00001O0000001O01O01O00001O000010O01O01O01O010O010O10O0100000O010O100O1N2O1O2M2O1N3M2N3M3L4K4J7J7IYnV2"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"ScZ69Y=8I5D<M4M2N2N2N2N2O0O2N100O100O010O1000O01000O0100000O01000000000000000000000000O1000000000001O0000001O0000001O01O0001O0010O0000010O01O010O0100O01000O0100O011N100O01O1N101N2O1N3M2N2N2N3M2N3L4M4I7J;ARml0"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"Qco26Z=8L3N2N3N001N2O1O1N2O1O1O1N2O1O1O1O1O1O100O1O1O1O100O1O100O1O1O100O100O10000O10000000000O100O1000000O10000000000O10000000000000000000000000000000000000000001O0000001O00001O00001O00001O001O001O1O001O1O001O1O1O1O1O001O1O1O1O1O1O2N1O1O2N1O1O2N2N2N3M4L5Iahl3"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"jlf45`=2O1O1O100O1O1O1O100O1O100O100O100O100O10000O10000O100000000O10000000000000001N100000000000000000000000000000000000000000000000000001O00000000001O000000001O00001O00001O00001O001O00001O001O001O001O001O1O001O001O001O1O1O001O1O1N101O00PZY2"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"`fY58V==]Oa0K6K4M2N3L3N3L4M2N2N3M2N2N2O1N2O1N2O1N2O1N2O0O2O000O10001N10000O2O00000O2O00001O001O00001O001O001O00001O001O0010O0001O01O0001O0001O0000001O01O01O0O101O00001N10001N10001N101N101N101N2O001N2O1N2O1N2N2O1M3N2N3M2N2N2O1N3L3M4L3N3L4M4K4L4M4K4L6Ii[d1"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"he\\6:Y=8I6K5L3L4M2N2N3M2N101N1O010O1O10O01000O010000000O0100000000O100000000000000000O1000000000000001O000000000000001O00010O00000010O01O0010O01O1O001O010O001O1O010O001000O000O2O1N2O0O2O0O2O1N2M3N2N2H9L3L4N2M4L5K`Si0"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"Xhc55`=4K5K4M2N2O1O1O1O1O1O2N100O1O100O100O101N100O100O2O00001N10001O00001N101O00001O001O001O00100O001O1O100O00100O1O100O2N10O001O001O001O00001N101O1O0O2O1N1O2N2M3M3N2N2N2M3M4K4M4K8Gj^h1"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"`kb58X=9J5M4K4K6N2L3O0O2O1O0O101O0O0100O10O010000O100O100O01000O10000000000O10000000001OO10000000000001O00010O001O0000010O00010O01O1O010O02N010O1O1O2M3M2N5I4L9EcRn1"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"iUT4c0Q=:H6I4M2N1O1O1O100O001O100O100O100O1000000O10000000000O100000001O000000000010O0000010O0001O01O01O01O0001O010O00100O00100O0010O10O10O1N101N1O2O1N2N2M3N2N2L5I6K6J6IWQ[3"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"bo\\36^=4L3M3N2N2O2N1O1O1O1O1O1O100O100O10000O2O0O101O000O101O000O2O00001O00001N10001O00001O001O1O00100O1O1O2N2O1N3M100O1OO101N100O2N100O2N1O2N101N2N1O2N2N2N2N2N2N3M3M4L5IniQ4"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"bWZ2;Z=3M2N3N1N2O1O100O1O1O1O100O100O1O2O0O100O100O101N1000000O2O00001O001O001O1O001O1O1O001O1O1O001O101N1O1O2O0O1O10N10001O0O101O0O2O000O2O001N101O1O1O1N2N2N2N2M4M3L6J7H7JjST5"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"emg25]=6M2O1O1O1O1N2O1O1O100O1O100O100O101O000O10001O00001N101O00001O001O000O2O001O1O1O1O001O100O1O2N1O4M2M1O01O0000001O001N101N101N1O2O0O2N101N1O2M3N2N2M3M3M3J7K5LoTh4"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"WSh34`=4L3K6L3N1O2O1O1O100O100O100O10000O100000000O101O0000000O2O0000001O00001O000010O0001O00100O001O100O1O100O2O000O10O1O1N101N2O1N1N3H8H8L4M3LlXl3"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"SWh65Z=;J4M2M3N2O1O1N200O010O100O100O100O10000O100O1O101O0000000000000000001O0000001O0000001O0001O01O0000010O0000010O0010O0100O01000O0100O0100O10001O0O100O10O1O1N2O1N2M3N2M3N2N3L4M5J4IXbc0"}},
    {"image_id": 238866, "category_id": 60, "segmentation": {"size": [439, 640], "counts": b"YZd62Y==L5K4N2M3N2N2O1N2N2N3N2M3N1N2L31N100O100O010O100O10000O10000O10O0101O0000O100000000001O00000000001O001O1O000001O01O000001O000000010O001O01000O0010O2fNlCn0_<O1M3M3M4L3L5JW_j0"}},
    {"image_id": 405432, "category_id": 60, "segmentation": {"size": [375, 500], "counts": b"nR\\1=V;9H5L4M3L3N2N2N2N2M2O2N2N2N101N1O2N1O2N1O2N100O2N1O1O101N1O1O1O2O0O1O100O100O2N100O100O1O2O000O1O100O100O10000O10000O1O10000O100O10000O10000O10O10O10001N1000000O2O000O100000O100000O2O00000001O0000000000O01000000O1000000O101O001N2O1N100O2O0O100O2N100O1O100O2N1O1O1O2N1O1O1UNhFU1Z9kNfFb0n9[OTFb0o9\\OTF`0P:^OXFJJOR:6S1M2O3Line2"}},
    {"image_id": 405432, "category_id": 60, "segmentation": {"size": [375, 500], "counts": b"bcm17_;2N2N2N1O1O1O100O001O001O10O01O01000O0100O01000O10000O01000O1000000O101O001O1N101O2N1O2MhPY3"}},
    {"image_id": 405432, "category_id": 60, "segmentation": {"size": [375, 500], "counts": b"Rm_15_;9G6L3L4L3N1N3N2N2N100O001O1O00100O0100O10O0100O010O1O1O101N1O3M2N2N2M3\\O\\E2X;KQYi3"}},
    {"image_id": 405432, "category_id": 60, "segmentation": {"size": [375, 500], "counts": b"bS`01e;1O10000O100O1O1O100O1O1000000O10000O10000O10001O0O10000O100O10000O100000000O10000000000000000000000000000000000001O00000000001O0000001O001O001O001O001O1O1O001O1O1O2N1NikW4"}},
    {"image_id": 405432, "category_id": 60, "segmentation": {"size": [375, 500], "counts": b"Wck13a;5K5G8L4UECX:R1E9K5L3L5Ib0B3M2O1O1O2N1O2M4M2N1N2O2mGfLf7[3WHhLh7c31N110N101O1O1O001O1O1O1O001N2O0O2O1004L2M2O1OO100O1000000010O0000TOmGTNT8j1nGTNT8j1nGdMN6U8T2]HfMf7X2m0O2N1O2000O02M100O1N2O01NWOcF[O^9b0eF]O[9b0hF]OX9`0kF_OX9C_F<`00c:M2N101N001O1N3Lodk2"}},
    {"image_id": 405432, "category_id": 60, "segmentation": {"size": [375, 500], "counts": b"g_:1b;=D6L3M2M4M1N2O1O001O001O001O00010O0000010O01O10O10O100O100O100O1000001O001O001O1O1O3M2M3L6H\\]k4"}},
    {"image_id": 561465, "category_id": 60, "segmentation": {"size": [612, 612], "counts": b"]5a0cb0010O1O1O1O010O1O1O10O01O1O010O1O0010O0001O010O001O0010O01O00010O00001O01O01O00001O01O01O001O01O01O0001O01O00000010O0001O000001O01O0001O01O0000001O00000000001O0001O0001N1000000010O0000O100000001O00000000000000000000000000000O1000O1000000000000O1000O10O1000000O10000O101N101O0O2O1N2O0O2O1N2N2O2M2M5L`mc8"}},
    {"image_id": 561465, "category_id": 60, "segmentation": {"size": [612, 612], "counts": b"]]m27lb05K3N1N3N1O2N1O1O1O1O1O1O1O00100O001O1O0010O01O001O001O010O00001O001O010O00001O01O01O00001O00010O0000001O0000010O0000001O0001O01O0000010O0001O0001O01O010O00000010O0001O0010O01O0001O01O000010O0001O00000010O000001O0000001O000000001O0000001O0000001O000000001O0000000O2O00001N101O1N2O1N2N2N4L4L4Ka^h5"}},
    {"image_id": 561465, "category_id": 60, "segmentation": {"size": [612, 612], "counts": b"`Rm5:eb09K2O1N101O001O1O00001N101O1O001O001O001O001O001O00010O00001O00001O00001O00010O0000001O0000001O000001O000001O0000000000001O0000000001O01O0000000000001O0000000000000000000010O0000000000000000000000000000000000000000000000000000000O2O00000000000O10000000000O100000000O101O000O10000O1O1O2N100O1N2O1O2N1N3N2M6Hedd2"}},
    #
    # "cake"
    {"image_id": 242060, "category_id": 61, "segmentation": {"size": [459, 640], "counts": b"`Xc4<m=3F4^BA_=b0dB[OX=i0hBWOT=n004K5]Od0M2O2N2N1O2N1O2N101N10000O101OO0O2L3L5K4N3M3N2N2O1O00100O1O1O100O010O10000O101O000O2O00000O1000001O00010O001O0010O01O001O1O2N2N4L7I:F6JVbY3"}},
    {"image_id": 242060, "category_id": 61, "segmentation": {"size": [459, 640], "counts": b"Uk[58l=7J6M3N3O0O2N101N1O2O0O2O0O2O2N2M4M5K;E6J5J4M1O1N1000001O00000001O000001N10001O01O01OO2O1O0O1O2L3M3L5L3L5L3M4M2N3M3O1N2O1N3M2O3L4L=C8HSad2"}},
    {"image_id": 242060, "category_id": 61, "segmentation": {"size": [459, 640], "counts": b"oo[74T>6K<D3M3M2M4M2N3M2N3H6L3M2ON4N3O1O1O10O2O00010O01O10O01O100O1000O100000O01001O00000O10000001O00000000001O0001O001O00010O0001O001O01O0000100O1O0010O010O1000O102M2O4L8Gc0]OPi<"}},
    {"image_id": 242060, "category_id": 61, "segmentation": {"size": [459, 640], "counts": b"_na6<_=a0M2O1O1O2O0O101N100O1O100O10001O001N101O0O2O00001N2O001O010O001O1O2N1O2N7I=C1O1O00O2O00001O00001O00001O00001N2O1N2N2M3M3L4M3Mg0YO7I4L5K5H\\o]1"}},
    {"image_id": 376322, "category_id": 61, "segmentation": {"size": [640, 478], "counts": b"dT^15jc03M3M3M3N2M1O2O1N100O100O1O1O100O1O100O1O10O01O100O1O00100O10O01000O100O101N1O100O1O100O2N1N200O1O1N3M2O1M3O2M2N2O2Mogg6"}},
    {"image_id": 376322, "category_id": 61, "segmentation": {"size": [640, 478], "counts": b"kbf33gc08L5K4M3M1O2O1O0O2O01O0000010O010O01O10O0100O100O100O010O01O001O010O0O2O001O0O1O2N1O2N101M3N2N2M4KQmd4"}},
    {"image_id": 376322, "category_id": 61, "segmentation": {"size": [640, 478], "counts": b"_j`49fc04K3M2O2N2O1O3L5L1O0O10000O10000O10O100000O1001O0O1000001O2M3N3M2N2M4M5J4KWUR4"}},
    {"image_id": 376322, "category_id": 61, "segmentation": {"size": [640, 478], "counts": b"mbX56gc03O2L3O1N2N2O1N3K4O100O2O000O1O101O0O100000001O0O100000001O01O0000010O0O1I7O2N1O2N2K5J6KiQV3"}},
    {"image_id": 376322, "category_id": 61, "segmentation": {"size": [640, 478], "counts": b"_[Z63lc04L4M2M10001N1000001N10000O101O0O1000000O2O00001N101O0O010000000000O1000000O101O0O2O001N2N2O1N3M3L4La`P2"}},
    {"image_id": 376322, "category_id": 61, "segmentation": {"size": [640, 478], "counts": b"Rlh5;dc03M2O000O2O0O100O100O101O0O10001O0O10000000001O00000000001O010O001O000001O000000001O0000000O2O000O101O0O2O2M5K6IgW^2"}},
    {"image_id": 397681, "category_id": 61, "segmentation": {"size": [640, 640], "counts": b"eeP531n0gb09M1N2N2O1O10O2O001O0O101N101N101N1O1O2N1M4L4M2M5L3L5K[jm6"}},
    {"image_id": 397681, "category_id": 61, "segmentation": {"size": [640, 640], "counts": b"mmm61jc0:J3L5L3N2M4L3N3L2O2M2O1O1N101N101O001O0O101O000O1J6:cNa]O01H\\UQ5"}},
    {"image_id": 419312, "category_id": 61, "segmentation": {"size": [500, 375], "counts": b"icj1=U?4M4L3N4K3N2M3N2M3M2N2O1O1N101O00001N1O10000O101O0O1000000001O0000000000001N10000L5M2N2N2M3L5N2N3N3M1O1O01O1O0001O1N3L3L5L4MQgm2"}},
    {"image_id": 419312, "category_id": 61, "segmentation": {"size": [500, 375], "counts": b"mmg24^?4L3M5M3L3M3N2N2N2N4L1O1O0001O00000000000000000000O010000O1000000000010N100000000000000000000O01001O0O102N2N2M2O1O2M3M2N3L3M4MUmo1"}},
    {"image_id": 419312, "category_id": 61, "segmentation": {"size": [500, 375], "counts": b"fd_25]?2N3K5N3L4M4M2N102N1O2M2N3M2N2O0O2O1001N1O100O100O2O1N01O0O1O1O001O000000000000000000O1O0100O100001O000O1000O10000000O10001O00O0100000000O10001O001O001O2N3L3N2N2N2N6I4M1N102M2O2MR_k1"}},
    {"image_id": 435081, "category_id": 61, "segmentation": {"size": [500, 500], "counts": b"eb_49Y?5L5J4M3M2O1N2O1N101N101N1000001O0000000000O101O001N101N1O2O1N2N2M3L4K6Kj_b2"}},
    {"image_id": 435081, "category_id": 61, "segmentation": {"size": [500, 500], "counts": b"Qcj3l0g>3N00000001O1O1N2O2M5L4K6JVfb3"}},
    {"image_id": 435081, "category_id": 61, "segmentation": {"size": [500, 500], "counts": b"mQW56\\?3N2N2N3N1N2O1O1O1O1O1O001O000000O2O2L7J5JgZR2"}},
    {"image_id": 435081, "category_id": 61, "segmentation": {"size": [500, 500], "counts": b"Zj`55^?6h@Jh>c0N1O001O00O101N2N3Md^m1"}},
    {"image_id": 435081, "category_id": 61, "segmentation": {"size": [500, 500], "counts": b"ToY55]?5L3N0O100O100000000001O1N3M3L][R2"}},
    {"image_id": 435081, "category_id": 61, "segmentation": {"size": [500, 500], "counts": b"PZX44^?4L3N1O2N1O101N101O0010O00010O001O000O2N1O2M3N1N3M3Nfdn2"}},
    {"image_id": 482275, "category_id": 61, "segmentation": {"size": [480, 640], "counts": b"aSe71k>5L4`AKR>7jA5l=c0L2N2O01O00001O0000002N1O2N7I1O001O1O1N4K6GVfZ1"}},
    {"image_id": 482275, "category_id": 61, "segmentation": {"size": [480, 640], "counts": b"k`j524`0Q>:N100O2O0O100O1000000M3L4N2O10000O10O2O1O0SO[B?g=]OdB7`=GdB3a=IcB3ofU3"}},
    #
    # "dining table"
    {"image_id": 1425, "category_id": 67, "segmentation": {"size": [512, 640], "counts": b"g=X2h=000001O00001O0000001O0000001O0000001O0000001O0000001O00001O00000000001O00001O000000001O0000001O0000001O000000001O000000001O00000000001O000000001O0000001O0000000000001O0000001O000000000000001O0000001O00000000001O0000000000001O00000000001O000000000000001O0000001O000000001O00000000001O000000001O00000000001O00000000001O00000000001O000000000000001O00000000001O00000000000000001O000000000000001O00000000001O000000000000000000001O000000000000001O0000000000000000000000001O000000000000000000001O00000000000000000000001O0000000000000000000000000000000000001O0000000000000000000000000000000000000000001O00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000O1000000000000000000000000000000000000000000000000000000O1000000000000000000000000000000000000000000O100000000000000000000O100000000000000000000O1000000000000000000000000O10000000000000000O100000000000000000000O100000000O100000000000000O10000000000000000O10000000000O100000000000000O10000000000O10000000000O10000000000O1000000000000O10000000000000000O1000000O10000000000O100000000O10000000000O100000000O100000000O100000000O10000000000O10000000000O10000000000O1000000O100000000O10000000000O1000000O100000000000000O100000000O1000000O10000O1000000O100QB"}},
    {"image_id": 15335, "category_id": 67, "segmentation": {"size": [480, 640], "counts": b"U;e0R2?T9@lF`0U9_OkFa0V9]OkFc0V9\\OjFd0V9[OlFd0U9[OkFe0V9YOkFg0W9UOkFk0Z9oNfFR1d;000O1O100O100O100O100O100O10000O100O10000O10000O100O100000000O1hNdNlD\\1S;gNkDY1T;hNlDX1S;iNmDW1Q;jNoDW1Q;hNPEX1o:iNQEW1o:iNQEW1o:iNPEX1P;iNoDW1Q;iNoDW1Q;jNnDV1Q;kNoDU1P;lNPET1P;kNQEU1n:lNRET1n:kNSEU1m:kNSEU1m:kNSEU1l:kNTEV1l:jNTEV1l:hNWEW1i:iNWEW1i:iNWEW1i:iNWEW1h:jNWEW1i:hNXEX1h:hNXEX1h:hNWEY1i:fNXEZ1h:fNXEZ1h:eNYE[1g:eNYE[1g:eNYE[1g:eNZEZ1f:fNYE[1g:eNYE[1g:eNYE[1g:dNYE]1g:cNYE\\1h:dNXE\\1h:dNXE\\1h:dNXE\\1h:dNYE[1g:eNZEZ1f:gNYEY1g:gNZEW1f:jNREITO^1j;kNoD]1Q;eNlD[1V;bNmDJUOX1R<mNREP1P;POQEo0o:QOREn0n:ROREm0o:SOTEi0m:WOWEc0k:^OVE>l:DSE8P;IQEH];3hDJ];0m1MUW41jhK2N1O2N1000000O1O1N2O1O2O0O1O101N11O00001O001O0010O0001O2N1O00001N2O010O010O1N11O01O001O00001O1O1O1OnPn07W`QOI^>a0M01N2N1O4L2N3N11N5N3I12M2N114J1O1Oa]a3MWb^L1eAO[>2dAN]>1cA0[>1fAOY>2fAOY>1hANX>2hANX>3gAMY>3bAM0O_>3aA3_>L`A6`>JbA4_>KbA4^>M`A4_>700001O004MO0001O00O10L[AMf>2ZANg>0ZA0f>0[ANg>0Z[g1"}},
    {"image_id": 69224, "category_id": 67, "segmentation": {"size": [375, 500], "counts": b"Wme12e;1N10001N101O000O101O00001O0O10001O000O101O000000001N10001O0O10001O000O101O000000001N10001N1000001O000000001N1000001O01O00000000000O10000O2N1K5O1O2N1FS\\U3"}},
    {"image_id": 92939, "category_id": 67, "segmentation": {"size": [640, 424], "counts": b"PW1>=Ebb0P1M1O1O1O1O100O100O1O100O1O1O100O1O100O1O100O100O1O100O1O1O100O1O100O1O1O100O1O100O1O1O1O100O1O1O100O100O1O1O100O100O100O100O1O1O100000000O100O100N20000O100O1O10ZNk^Oa0Ua0\\OS_O?l`0@Y_O=f`0C\\_O<c`0Ca_O;_`0Dc_O;]`0Cg_O;Y`0Eh_O:W`0Ek_O;U`0AQ@=n?BT@>l?@W@?i?@Y@?i?^OX@b0h?]OY@c0h?[OZ@d0f?\\O[@c0i?XOX@h0i?WOW@i0k?TOW@k0_a00001O001O00000000gMXO[Ag0e>ZOZAf0e>_OWAa0i>@VA`0j>@VA`0j>]OV_ONn1d0l>_OV_OLn1e0k>AYA?g>CW_OGl1f0m>JPA6o>KQA5o>KQA5n>LRA4m>LTA4l>LTA4l>KUA5j>LVA4j>KXA4h>LWA5h>LXA4h>I[_OAm1f0g>K[A5e>K[A5e>J\\A6c>J^A6b>J^A6a>J`A6`>J`A6`>J`A6`>J`A6_>K`A6`>J`A6`>J`A6_>KaA5_>KaA5_>JbA6^>JaA7^>JbA6^>JbA6]>JdA6\\>JcA7\\>IeA7[>IeA7[>IeA7Z>JeA7[>HfA8Z>HfA8Y>IgA7Y>IfA8Z>HfA8Z>GgA9X>HgA9Y>GgA9X>HgA9Y>GgA9X>HhA8X>HgA9X>GhA:X>GgA9X>HgA9Y>GgA9Y>HeA9Z>IdA8\\>IcA7]>JaA7_>Ln_OXOR1m0o>;n@FR?:m@GR?;l@FT?;j@FU?<i@EX?;f@FZ?;d@F\\?<`@F`?<\\@ROL[Oh?d1Z@nN7YO_?k1T@oNe`0M\\_OU1d`0iNb_OS1^`0mNe_OP1[`0POg_On0Z`0QOh_Om0Y`0SOj_ODD>a`0Ng@NZ?2h@KY?4j@JU?7m@FT?9o@EQ?;QABP?>QAAo>>TA_Om>a0TA^Ol>a0Z2N2N1O2O100O100O010000O10000000O1000O100000000000000O101O001O001O0O10O100O1O1O1O001O1O1O1O100O001O1O100O2N1OUh?1jW@11O000000000000000000000000000000000000O1000000000000fKMgD3Y;NfD2Y;OfD2Z;0dD0\\;1cDO];2bDN_;2`DNa;2^DNb;3\\DNb;5]DKb;8c@Dd34i;=WDCi;>VDBj;>UDCk;>TDBl;?SDAm;a0QD_Oo;e0mC[OS<h0iCYOW<i0gCWOY<k0eCUO[<o0`CRO`<o0_CQOa<P1^CPOb<Q1\\CPOd<Q1[CoNe<R1ZCnNf<S1YCmNg<T1WCmNi<T1VClNj<T1VClNj<T1VClNj<T1UCmNk<T1TClNl<T1SCmNm<T1QCmNn<T1RClNn<T1RClNn<U1PClNP=T1PClNP=T1oBmNQ=S1oBmNQ=S1nBnNR=S1lBnNT=S1kBmNU=S1jBnNV=R1iBoNW=R1hBnNX=S1fBnNZ=R1eBoN[=Q1eBoN[=R1cBoN]=Q1aBQO_=o0`BRO`=n0_BSOa=n0]BSOc=n0[BSOe=n0YBSOg=P1j@SNQ1n0U>[1gAgNY>Z1eAgN[>Z1aAiN_>W1_AkNb>V1XAnNh>a1c@eN]?o20000O11O00000000O100000000000000000000000000000TMPAh0P?oN[Ao0e>mN`AR1`>jNdAV1\\>hNfAX1[>eNgA[1o>nMSAQ2R?iMo@W2^`0O001O0000001O000000001O00002MU2"}},
    {"image_id": 99039, "category_id": 67, "segmentation": {"size": [480, 640], "counts": b"S=l1S=1O1O1O1O1O1O1O1O1O1O1O100N200O1O1O1O1O1O1O1O1O1O1O100O1O1O1O1O100O1N2O1O100O1O100N2O100O1O1O1O00100O2N1O1O1O1O1O1O1O1O100N200N2O1O100O1N2O100O1O1N2O100N2O1O1O100O1O1O1O1O1O001O1O100O1O1O1O2N1O010O1O1O100O1O1O100O100O100O1O1000000O]KTFT4l9kKVFT4j9kKXFT4h9kKZFT4f9kK\\FT4d9kK^FT4b9lK^FT4b9kK_FU4a9kK`FT4`9jKbFV4^9jKcFU4]9jKdFn0AR2l9oLdFj0GT2\\:kMfET2[:jMgEU2Z:jMgEU2Z:iMgEW2Y:hMhEX2X:hMhEX2Y:fMiEY2X:fMhE[2X:cMiE\\2Y:cMgE]2Y:bMhE^2Y:aMfEa2Y:^MhEb2Y:]MgEc2Y:\\MgEe2Y:[MgEe2Z:ZMfEf2Z:YMfEh2Z:WMfEj2Z:VMdEk2^:SMbEn2^:QMbEP3^:PMbEP3^:nLcES3]:lLcEU3T;0O100O100O100O100O100O1O10000O100O100O2N100O1O100O001O100O101O000O10000O0100000O100000000000000000000010O000O100000000000000000000000000000000000000000000000000000000000O100000000000000000000O10000000000000000000000000000001WLnDb3Z;N1O1O1O1O001O000000001O0001O01O0O10001O000000000000010O00000O10000001O000000000000O10O1000000001O2N1O1O2N1O2N002N10O00000000O]NTMTGl2k8VMTGj2l8VMTGj2j8XMVGh2i8YMWGh2h8XMXGh2h8XMXGh2h8XMXGh2h8XMXGg2f8\\MZGd2e8\\M\\Gd2c8]M]Gc2c8]M]Gc2c8]M]Gc2c8]M]Gc2c8]M]Gd2b8]M]Gc2c8\\M^Gd2b8\\M^Gd2b8\\M^Gc2c8]M]Gc2b8^M^Gb2b8^M^Gc2a8]M_Gc2a8]M_Gc2a8]M^Gd2b8\\M^Gd2b8\\M^Gd2b8\\M^Gd2b8\\M^Gd2b8\\M^Gd2c8SMlE5a1h2g8WMYGh2j8VMVGj2k8UMUGl2`:O004L4L2M2O3M2N3M4L3M3M2N3N1N2M3N101NmM^NiFa1T9cNlF\\1R9fNPGW1P9jNQGU1l8nNVGP1h8ROYGm0g8SOZGl0f8TO[Gk0d8VO]Gi0c8WO^Gi0a8WO`Gg0a8YO`Gf0`8ZOaGe0_8[ObGd0^8\\OcGc0\\8]OeGc0[8]OfGb0Z8^OgGa0Y8_OgGb0X8^OiGa0W8_OjG`0V8@jG`0W8_OjG`0W8_OjG`0Z8\\OfGd0\\8YOfGf0[8YOeGf0]8XOeGg0[;0O0001O001O001O00001O00001O00000000001O0000000000000000000000000000000000000000O1000000000000000000000000O1000000000000O100000000000000O100000000O10000000000001O=C3M3LVQS2"}},
    {"image_id": 116208, "category_id": 67, "segmentation": {"size": [480, 640], "counts": b"YWd76h>4M2N102M101N10000O1000001N10000O1000001O000000001O00001O001O2N2N1O1O0000001O001O0000001O0000001O00000000001O0000001O000000001O00000000O1N2D<DZi3NRWL3O00001O000001N101MSW43khK2O000000000001N2KTV4"}},
    {"image_id": 156278, "category_id": 67, "segmentation": {"size": [425, 640], "counts": b"^`n44S=2O2N3N4L4XCJT<g0O000000000O101O00000000000000000000000000000000000000000000000000000OYOSD4m;KUD4k;KWD4i;KYD4g;HcD2];LjDOV;0nDLS;4mDLS;4Q10000O2O0OZRh00fmWO101O0000000000000000001O00001O1O1O1O1O1O00000000001O001O1O1O1O1O1O1O1O1O1O1O<D5K0000000O1000000000000000000000000000000O100000000O100OnNZDc0f;[O^Dc0b;\\O`Dc0`;\\ObDc0^;\\OdDc0\\;]OeDb0[;]OgDb0Y;^OhDa0X;_OiD`0P<01O001O1O001O1O001O00001O001O001O001O00001O00001O00001O00001O00001O00001O0O101O00eV;"}},
    {"image_id": 172571, "category_id": 67, "segmentation": {"size": [361, 640], "counts": b"mhP16i::J7F9J6J6L4N200O100001O1O1O1O1O1O1O1O002N0000TKRO^Om0=XODg02CO<JJ76DN>1[O5g0JQO=P1CgNe0[1ZO_Nj0d1UOVNP1l1oNoMU1S2jNfM\\1\\2cNaM_1`2aN_M`1a2`N_M_1c2`N]M_1d2aN\\M^1f2aNYM`1h2_NXM`1i2`NWM_1k2`NUM`1k2`NUM_1m2`NSM_1n2aNRM_1o2`NQM_1Q3`NoL`1R3_NnL`1S3`NmL`1S3`NmL_1U3`NkL_1W3`NiL`1W3`NiL_1X3aNhL_1Y3`NgL_1Z3aNfL_1Z3aNfL^1\\3aNdL_1\\3aNdL^1^3aNbL^1_3bNaL]1a3bN_L^1a3bN_L]1c3bN]L]1d3cN\\L\\1f3cNZL\\1g3dNYL\\1g3dNYL\\1h3cNXL]1h3cNXL]1i3bNWL^1i3bNWL^1i3bNVL_1k3`NUL_1m3`NSL`1m3`NSL`1m3`NSL_1n3aNRL_1n3aNRL_1n3aNRL^1P4aNPL_1P4aNPL_1P4aNPL_1Q4`NoK`1Q4`NoK`1R4_NnKa1R4^NoKb1Q4^NPLa1Q4^NoKa1R4_NQL^1o3bNaLm0a3RORM;n2FUM6k2IWM6j2IWM5j2KXM3i2LYM1h2OXM1i2NXM0i20XMOh21X40`]h0j0eaWO2O000001O001O001O001O00_OWOcFh0\\9ZOcFf0]9[OcFc0^9]OcFb0]9_ObFa0^9_OcF`0]9AbF>_9CaF<_9EaF:_9G`F9`9H`F7_9JbF5^9LbF2_9O`F1`90`FO`92`FM`93`FM`94`FJa96_FJa97_FHa99_FFa9;_FDa9=_FBa9>aF@_9a0aF]O`9d0`F[O`9e0b01O1O1O1O001^FYOWOMT9j0ZGKd86ZGKf86ZGJe86[GJe87[GHe89[GFe8:[GFe8;\\GCd8>\\GAd8?]G@c8a0\\G_Od8a0\\G_Od8b0\\G]Od8c0]G\\Oc8e0]GZOc8f0^GYOb8h0^GWOb8j0^GUOb8l0^GTOa8m0_GROa8n0`GQO`8P1_GPOa8P1`GnNa8S1^GmNb8S1_GkNb8U1^GjNc8W1g01O1O1N101O010O001O0O2O1O1O00001O001O0000N2O1L4N2N2N2L4M3N2N2N2M4L3N2M3M3M3N2M4M]Y4OcfK5L4K4M3L3N3L4M3M3M2M4M2M4M2M4M2N2M3N2N3M2O2N11O010O001O1O0010O01O1O10O01O0010O010O01O01O01O001O01O01O01O1bLRN`Mm1_2TNaMm1^2SNbMm1]2TNdMk1\\2VNcMj1]2UNeMj1Z2WNfMj1Y2VNgMj1X2WNhMi1X2XNhMh1W2XNiMh1W2XNjMg1U2ZNkMf1U2ZNkMg1T2YNmMf1R2[NnMe1R2ZNPNe1P2[NPNd1P2^NPN`1Q2`NPN]1Q2dNoMZ1S2fNnMW1S2jNmMT1U2lNlMR1U2nNkMP1W2POjMn0W2ROiMm0W2TOjMj0V2WOjMh0W2XOiMg0X2YOiMe0W2\\OiMc0X2]OiMb0V2_OjM`0W2@jM?U2BkM>U2BkM>U2BkM>T2CmM=Q2DoM<Q2DoM=P2CQN<n1ERN<m1DSN=k1DUN=j1CWN=g1DYN=f1CZN=f1CZN?c1B^N=a1D_N=`1C`N>^1CbN=^1CcN<\\1EdN;[1FeN9\\1GdN9[1HeN8Z1IgN5Z1KfN5Y1LgN4X1MhN3W1NjN1V1OjN1V1OjN1U10kN0T11lNOT11lNOS12mNNR13oNLP15POKP15POKo05ROKm06SOJl07UOHk08UOGk0;TODl0=TOAm0`0SO^On0c0RO[Oo0f0QOWOQ1j0POQOkMFT1Z1Q1kNPNKn0[1S1cNUN3f0[1b3fN\\L[1c3hNZLY1f3hNXLY1h3hNVLY1j3hNTLY1m3hNPLY1P4hNnKY1R4hNkKZ1U4hNhKY1X4hNfKY1Z4iNcKX1]4iN`KY1`4iN\\KY1d4iNYKX1c2`NTM97X1^2iNXM24X1b2iNYM02Y1e2hNXM1OY1i2gNWM3JY1o2dNWM5FY1S3cNVM:\\OX1^3^NVM>SOY1g3YNUMf3k2ZLUMf3k2ZLUMf3k2[LTMe3l2[LTMe3l2[LTMe3l2[LTMe3l2\\LSMd3m2\\LSMd3m2\\LSMd3m2]LRMc3n2]LRMc3n2^LQMb3o2^LQMb3n2_LRMa3n2`LQM`3o2`LPMa3P3_LPMa3P3`LoL`3Q3`LnLa3R3`LmL`3S3`LmL`3S3aLkL`3U3`LkL`3U3aLjL_3V3bLhL_3X3aLhL_3W3cLhL]3X3dLfL]3Z3dLdL]3\\3dLcL\\3]3dLbL]3^3dL`L]3`3dL^L]3a3fL\\L[3d3fLXL]3h3fLSL\\3m3P2O100000000000000O1000000000000000O1000O100000001O000O10O11O0000000O1000000000000O1000000O100000000O100VL"}},
    {"image_id": 194940, "category_id": 67, "segmentation": {"size": [375, 500], "counts": b"0e;20001O9G<D3M1O1O1O00001O0000O10000O11O4L3M3M1O2N2N1O2N1O2N1O1O2N2N1O2N1O1O1O1O2N1O001O1O1O1O001O1O001O001O0000001O1O1O2N2N1O2N2N3M2N3M1O3M2N2N1O2N2N3M1O3M2N7I4L2N3M2N2N2N1O2N2N1O1O2N1O1O1O1O1O1O1O1O1O1O1O1O001O001O1O001O001O00001O1O00001O00001O0000001O001O0000001O00000000001O00000000000000000000O1000cJoJT4Q5fK\\KS4d4hKfKS4Z4jKmKR4R4lKTLQ4l3mKWLR4i3lK]LP4c3nKaLP4_3mKfLQ4Y3oKjLo3V3oKnLo3_5N2N2N4L2N2N2N2N1O1O2N2N1O1O2N1O1O1O1O1O001O1O1O1O001O1O001O1O001O001O0000]K[M5d2I^M7b2cKdMd3Mj0^2aKgMa3Nn0[2aKgM`3Oo0Z2aKfM^32R1X2`KfMZ36V1T2`KeMS2OdN<i3P2`KdMT24ZN=R4k1`KdMT2_1]2m0_KcMV2_1\\2m0^KcMW2`1[2m0^KbMY2`1Y2n0^KbMZ2_1X2o0^KbM[2]1X2Q1]KaM\\2^1W2Q1]K`M^2^1U2R1]K`M_2]1T2S1]K_M`2^1T2R1\\K`Ma2]1S2S1\\K_Mb2^1R2S1\\K_Mb2^1R2S1UNlNk1T1UNlNk1T1UNlNk1T1VNkNk1T1UNkNl1U1TNlNk1T1VNkNj1U1VNkNj1U1VNkNj1U1WNjNi1V1WNjNi1V1WNjNj1U1WNjNi1V1WNjNi1V1WNjNi1V1WNjNi1V1WNjNi1V1WNkNh1U1YNjNg1V1YNjNg1V1YNjNg1V1YNjNf1W1ZNjNe1V1[NjNe1V1[NjNd1W1\\NjNc1V1]NjNb1W1^NiNb1W1^NiNb1W1^NjN`1W1`NiN`1W1`NiN`1W1`NjN^1W1aNjN^1W1bNjN]1V1cNjN\\1W1dNjN[1V1eNjNZ1W1eNjN[1V1gKXMj2d1]1U1iKWMj2e1[1U1kKVMj2e1Z1V1lKVMi2e1Z1U1mKWMg2e1[1U1nKVMg2f1Y1U1PLVMf2e1Z1U1PLVMe2g1Y1T1RLVMd2g1X1T1TLUMc2i1W1S1VLUMb2h1W1T1WLTMa2j1V1S1YLSMa2k1T1S1\\LRM_2k1T1T1]LQM^2m1S1S1_LQM]2m1Q1T1bLoL\\2o1P1S1dLoLZ2P2o0S1gLmLY2R2n0R1iLmLX2R2m0R1kLlLW2[1PNjNk2R3nLiLW2W1XNkN`2W3QMgLV2S1eNgNQ2c3TMdLT2o0i1a2SL`LS2m0j1f2SL]LR2l0k1i2SL\\LP2j0m1l2SLZLo1i0n1o2SLXLm1j0o1P3TLVLl1i0Q2R3SLULk1i0Q2T3TLTLh1h0T2V3TLRL3GY1R1`2W3TLPL3HV1R1b2X3ULnK3KQ1n0h2[3TLlK3Mk0n0m2\\3ULiK3Of0m0P3_3WLeK40b0l0P2QOmMc4]OaK33;k0Z2_4XMcJ372j0f2[4UMdJ3l1j2NbMh0A^M3j1l2KkMg0VOdM3i1n2HoMh0POgM3h1P3DVNh0gNlM4f1Q3CYNh0bNoM4f1R3@]Nh0]NSN3d1U3^O_Ni0YNUN3c1W3[OaNl0UNVN3b1Y3ZObNl0RNXN3a1[3XOdNm0nMZN3`1]3WOdNn0lM[N3`1^3TOgNo0hM]N3_1_3TOhNo0fM^N4]1`3TOhNP1dM`N3\\1b3ROjNP1aMbN3[1c3QOlNQ1^McN3[1d3oNmNR1\\MdN3Z1e3oNnNR1ZMeN3Z1f3mNoNS1XMfN3Y1h3kNQOT1TMhN3X1j3kNPOT1SMiN3X1j3jNROT1QMjN3W1k3jNSOT1oLkN3W1l3hNTOU1mLlN3W1l3gNUOV1lLlN3V1n3fNUOW1jLmN3V1n3eNWOW1hLnN3V1o3dNWOW1gLoN4T1P4dNWOX1eLPO4T1P4cNXOY1dLPO4T1Q4aNYOZ1bLQO4T1Q4aNYOZ1bLQO4S1R4aNZOZ1`LRO4S1i7JSHSO4S1i7JSHSO4S1j7IRHTO4R1k7JQHSO5S1k7IPHTO5S1k7IPHTO5S1l7HoGUO5S1l7HoGUO5S1m7GnGVO5S1m7GnGVO5R1o7GlGWO5R1P8FkGXO5R1P8FkGXO5R1P8FkGXO5R1P8FkGXO5R1Q8EjGYO5R1Q8EjGYO5R1R8DiGZO5R1R8DiGZO5R1R8DiGZO5R1S8ChG[O5R1S8ChG\\O4Q1T8ChG\\O4Q1T8ChG\\O5P1S8DhG\\O5Q1S8BhG]O5Q1S8BhG]O5Q1S8BhG]O6P1R8ChG]O6P1R8ChG]O6P1R8ChG]O6Q1Q8BiG^O5P1R8BiG^O5P1R8BiG^O5P1R8BiG^O6o0Q8CiG^O6o0R8BhG@5o0R8AiG@5o0Q8BjG_O5P1P8AkG_O6o0o7BkG_O6o0o7BkG@5n0P8BkG@5n0P8BkG@5o0o7AlGA4n0P8AlGA4o0o7@mGA5n0n7AmGA5n0n7AmGA5o0m7@nGB4n0n7@nGB5n0l7@oGB5n0k7APHA5o0j7@QHB4n0k7@QHB4n0k7@QHB4o0j7_ORHB4P1e3]N5R1RLA5o0c3`N5P1SLA5P1a3`N7o0SLB4o0a3bN6n0ULA4P1`3bN6m0VLB3P1_3bN7m0WLA3P1_3cN6l0XLA3Q1]3cN8k0XLA3R1\\3bN9k0XLA4Q1Z3dN9k0YL@4R1X3eN:i0ZL@4S1V3fN:h0\\L_O4T1U3eN:i0]L^O4U1S3fN:h0_L]O4V1Q3gN;f0`L^O3U1Q3hN;f0aL]O3V1P3hN;e0bL]O4V1m2iN<e0cL\\O4W1k2jN<d0eL[O4X1h2lN>a0fL[O4Z1e2lN?`0hLZO4[1c2mN`0>iLZO4\\1`2nNb0=jLYO4]1^2oNb0<lLXO5]1[2QOa0<oLVO5^1X2SOc09PMWO4^1V2UOd07RMVO4`1R2WOe04UMUO4b1o1VOg04VMTO4c1l1XOh02XMSO4e1h1ZOj0NZMSO4g1a1^On0J]MQO4i1\\1@Q1G_MPO4k1X1AR1FbMnN4l1U1DR1CeMmN4Q2k0EZ1^OgMlN4S2g0GZ1\\OlMiN3Y2?F`1YOnMhN3^23Ji1QOQNgN3j5g1bKVNdN3l5d1aKXNdN4m5_1bK]NaN4o5Z1cKbN^N4S6S1bKiN[N4U6o0bKmNXN5Z6e0cKVOSN5a60hHKn20iM5l9KTF5l9KTF5l9KTF5l9KTF5l9KTF5l9KTF5l9KTF5l9LSF4m9LSF4m9KTF5l9KTF5l9LSF4m9LSF4m9LSF4m9LSF4m9LSF4m9LSF4m9KTF5l9KTF5l9KTF5l9KTF5l9KTF5l9KTF5l9KTF5l9KUF4k9LUF5j9KVF5j9KVF5j9KVF5j9KVF5j9KWF4i9LWF4i9LWF5h9KXF5h9KYF4g9LYF4g9LYF4g9LYF4g9LYF5f9KZF5f9K[F4e9L[F4e9L[F4e9L[F4e9L[F4e9L\\F4c9L]F4c9L]F4c9L]F4c9L]F4c9L^F3b9M^F3b9M^F4a9L_F4a9L`F3`9M`F3`9M`F3`9M`F3`9M`F3`9M`F3`9M`F3`9M`F3`9L"}},
    {"image_id": 232489, "category_id": 67, "segmentation": {"size": [640, 640], "counts": b"la0T2la0000O1001O001O001O1O00000000001O00001O1O1O001O00001O00001O2N1O0000001O001O001O1O001O0000001O00001OY^OaNm`0_1Q_OcNPa0\\1o^OeNRa0Z1m^OgNSa0Y1l^OhNTa0X1k^OiNVa0V1i^OjNXa0V1f^OmNYa0S1c^OQO^a0h1000O2O01OO101O1O001N10000000000O2O00001N10001N101O001O00001O0O2O001O001O1O000000000O2O00001O001O001O00001O000O1000001O00001O0O1000001O00001O000O2O0000000@V]OJjb06W]OIjb06X]OHhb08Z]OFfb0:[]OEeb0;\\]OCeb0=\\]OBdb0>]]OAcb0?^]O@cb0??01O00001O001O00000000001O00001O000000001O1O00000000001O000000001O00000000001O000000001O00O1001O000000001O00000000000000001O000000000000000000001O00001O00001O0000001Ohhb02TW]O3N1O101N1O1N3O0N2M4K4N2N2O2O0O1000001O0000001O000000001O0000001O00001O00001O00001O0000001O001O00001O0000001O00001O000000001O001O00001O0000001O001O00001O1O0000001O00001O001O000000001O1O00001O00001O001O00001O1O0O2N1000001O0O2O00001N101O000O2O001O000O2O001O001O0O101O001N101O001O000O2O1N10001O001O001N10aMl^OS2Sa0mMn^OR2Qa0oMQ_OP2n`0PNU_Om1k`0SN[_Og1d`0ZN__Od1``0\\Na_Oc1_`0]Nb_Oc1]`0]Nd_Ob1\\`0^Ne_Ob1Y`0_Ni_O`1V`0`Nk_O_1U`0aNl_O_1R`0bNo_O]1Q`0cNP@]1o?cNR@]1m?cNT@\\1k?eNU@[1k?eNV@[1i?eNX@Z1g?gNY@Z1f?fN[@Z1c?gN]@Y1c?gN^@Y1`?hN`@X1`?hNa@X1]?iNc@W1]?iNd@V1\\?jNd@W1[?iNe@W1[?iNf@W1X?jNh@W1V?jNk@U1U?kNk@V1S?kNn@T1R?lNn@U1P?lNQAT1n>lNRAT1n>lNRAU1m>kNTAT1k>mNUAT1j>lNWAS1i>mNWAT1g>mNYAS1g>mNZAS1e>mN[AT1c>mN^AS1a>mN_AS1`>nNaAQ1_>oNaAQ1_>oNaAR1]>oNcAQ1\\>POdAP1\\>POdAP1\\>POeAo0[>QOeAo0Z>ROfAn0Z>ROfAo0X>ROhAP1V>POjAR1S>oNmAR1Q>oNPBQ1o=oNQBQ1n=PORBQ1m=oNSBQ1l=POTBQ1j=POVBP1j=POVBQ1h=POYBo0f=ROZBo0e=QO[Bo0d=RO\\Bn0c=SO]Bn0a=SO_Bm0`=TO`Bm0^=TObBl0]=UOcBl0\\=TOdBl0[=UOeBl0Y=UOgBk0X=VOiBi0V=XOjBi0T=XOlBh0T=XOlBh0S=YOmBh0Q=YOoBg0P=ZOPCg0o<YOQCg0n<ZORCf0n<ZORCg0l<ZOTCf0k<[OUCe0j<\\OVCe0h<\\OXCd0g<]OYCd0e<]O[Cc0e<]O[Cc0d<^O[Cd0c<]O]Cc0b<^O^Cb0a<_O_Ca0`<@`Ca0^<@bC`0]<AbC`0]<AcC`0[<AdC`0[<AeC`0Z<@eCa0Z<@fC`0Y<AeCb0Y<_OfCb0X<@gCa0X<@gCa0X<@gCb0W<_OhCb0W<_OhCb0W<_OhCb0W<_OhCc0V<^OhCd0W<]OgCe0X<\\OfCf0X<\\OfCg0X<ZOgCg0X<ZOfCh0Y<YOeCj0Y<WOeCk0[<UOdCm0Z<TOdCn0[<SOcCo0\\<ROaCR1]<oNaCS1^<nN^CW1`<jN^CX1a<iN]CZ1a<S3O2N1O2O0O1N2N3N1O1O2M3N1O2N2N1N3M2O2M3N1O2N1O2N1O2M2O2M2O2N2N1O2N1N3O0O2L4N1N3N2N1N3M3N1O2N2M3O0010000O0100O01[HoEZ5P:eJRF\\5m9bJUF_5i9`JYFb5e9[J^Fi5^9UJdFm5Y9RJjFm5V9QJmFm5T9oIPGP6P9nITGP6m8lIYGQ6h8kI]GS6c8kI`GT6a8jIbGT6_8jIcGU6]8jIfGU6Z8hIjGV6W8gImGW6S8fIRHW6P8gIRHX6o7fIUHW6l7gIYHU6i7hIZHV6h7hI\\HT6f7iI]HT6h7gI\\HV6f7gI_HU6c7gIaHV6h:M3M4L3L10O1O1O1N1O2O1N2O1aF"}},
    {"image_id": 245026, "category_id": 67, "segmentation": {"size": [424, 640], "counts": b"hk>3T=100O100O101N100O100O100O100O100O100O100O100O100O100O10000O100O100O10000O100O100O10000O100O10000O100O100O1000000O10000O100O10000O10000O10000O10000O1000000O100O10000O1000000O1000000O10000O10O1001N10000O1000000O1000000O100000000O10000O100000000O100000000O1000000O10000000000O100000O0O2M3M3M3N1N3N2M3M3M3M3M\\EAe8:[GLc82\\G2d8K]G7d8CaG=e:0000000000000000000001O0000000000000000001O0000000000000000000000000000000000000000001O000000000000000000000000000000000000000000000000000000000000001O0000000000000000000000000000000000000000000000000000001O00000000000000000000000000000000000000001O000000000000000000000000000000000000000000001O0000000000000000000000000000000000000000000000001O0000000000000000000000000000000000000000000000000000001O000000000000000000000000000000000000000000000000000000001O00000000000000000000^MLPH4n7<dGD\\8j0VGVOj8W1iFiNW9g1XFZNi9S2hEnMX:a200000000001O0000000000001O0000000000001O000000001O000mNdEZO\\:d0jEXOV:h0nETOS:k0nETOR:l0oESOQ:l0RFROn9n0UFoNk9Q1WFmNi9S1YFkNh9T1ZFiNg9W1\\FfNd9Z1U1O101O000000001O0000001O0000001O00000O2O000000001O0000001O00000O2O0000001O0000001N1000001M2ZOiC9g<L3M4JTk^1"}},
    {"image_id": 245651, "category_id": 67, "segmentation": {"size": [500, 375], "counts": b"_a01j1W1_2e0jKRO0RO23M:OG=;CH2JY1^1;L\\2U5YLPKX1N_2R5ZLaIE[1_14d2n4]LmJm06h2l4YLPKn05k2i4SLeIG]1Y16o2g4QLWKm05T3b4oKZKj04Z3a4lK[Kh04_3`4iK\\Kf04d3_4fK]Kd03k3^4aK`Ka02Q4]4_KaK=2X4[4ZKeK;0^4Z4WKgK8Nf4Y4RKjK4Nn4V4nJlK2OR5T4lJnKN0X5Q4kJoKKO]5Q4iJoKIOb5P4fJQLD1i5l3cJmM`5R2_JoMc5o1]JoMf5P2ZJoMh5P2YJnMj5P2[JjMg5U2UJnMn5P2QJoMR6P2nIPNS6o1mIPNV6n1jIPNY6o1gIPN\\6n1eIPN]6o1cIPN_6o1aIoMc6o1]IoMf6P2ZIoMi6o1WIPNk6o1UIPNm6o1SIPNo6o1QIQNP7n1PIQNS7m1mHSNT7l1lHTNU7k1kHUNW7i1iHWNX7h1hHWNZ7h1fHXN[7g1eHYN]7e1cH[N^7d1bH\\N_7c1aH\\Na7c1_H]Nc7a1^H]Nd7b1\\H^Ne7a1[H^Ng7a1YH_Ni7_1WH`Nk7_1UH`Nm7_1SHaNn7^1SHaNo7]1QHbNQ8]1oGbNS8]1mGcNT8\\1lGdNV8Z1jGeNX8Z1hGeNZ8Z1fGfN[8Y1eGgN]8W1cGhN_8W1bGhN_8W1aGhNa8W1_GiNb8V1^GiNe8U1[GjNg8U1YGkNh8T1XGlNi8S1WGlNl8R1TGnNl8R1TGmNo8Q1QGoNP9P1QGoNP9P1PGoNR9P1nFPOS9o0mFPOU9o0kFQOV9n0jFQOY9m0gFSOZ9l0gFRO[9m0eFSO]9k0cFUO]9k0cFTO_9k0aFUOa9i0_FWOb9h0^FWOd9h0]FWOd9h0\\FXOf9f0[FXOg9g0YFYOh9f0oE_MJj1Y:f0mEaMIi1[:e0lEbMIi1\\:d0kEcMIi1]:c0jEcMJi1^:c0hEeMJg1_:c0gEfMJf1a:c0eEgMJf1b:b0cEmMH`1f:b0bEoMG^1h:c0aEoMG^1i:b0`EPNG\\1l:c0]EQNG[1n:c0[ERNGW1R;g0XEQNFLMV1X;l0UERNGJ0S1V;Q1SERNNk0Q;R1QESNLk0V;Q1nDTNLj0W;R1mDTNLh0Y;T1nDQNJi0Z;U1hDPNE29h0\\;U1fDWNNc0];V1fDUN1ND<g;`1dDVN1MF;g;a1dDUNN1D:k;`1dDUNMOE;l;`1bDVN57Z;c1bDUN3N\\O8Q<d1`DWN08a;a1_DWN61\\;h1^DXN6O\\;i1^DXN6N^;i1[DZN6N_;h1RDXNJNO5d0Mb;h1lCiNa0_Od;`2\\D_Mf;`2YD`Mh;a2WD_Mi;h1gCWN1`0?Ai;h1gCWN1`0?Ai;h1gCWN0a0`0@j;g1fCXN0a0?@l;g1eCXN0a0?@l;g1eCXN0a0?@l;g1eCXNOb0?_On;g1dCXN00O>?BP<g1bCYN4OM;n<]1QCYN8:g<]1QCYN;7d<`1QCXN::e<^1]CcNc<]1ZCfNf<Z1UCkNk<U1RCnNn<R1QCPOn<P1TCnNl<R1UCmNk<S1WCXNJa0o<W1YCiNg<W1ZChNf<X1ZChNf<X1ZChNf<X1ZChNf<X1ZChNf<X1[CgNd<Z1^CdNb<\\1^CdNb<\\1^CdNb<\\1^CdNa<]1_CdN`<\\1`CdN`<\\1aCcN_<]1aCWNC:k<_1eCaNZ<`1gC_NY<a1hC^NX<b1hC^NW<c1hC]NY<c1hC]NW<c1jC\\NU<e1lCZNT<f1lCZNS<g1mCYNS<g1mCYNR<h1oCWNQ<i1oCWNP<j1PDWNo;i1PDXNo;i1oCZNo;g1PDZNP<f1lC^NS<c1iCaNW<_1iCaNV<`1iCbNV<^1fCfNY<[1dChN[<Y1gCfNX<Z1hCfNW<[1fChNZ<Y2O1O101N1O100O100O2N100O100N200O101N100O1O101N1O100O1O100O2N100O100O1O101N1O1O100O100O1O2N10000O2N1O100O1O100O1O2O0O1O2O0O1O1O100O1O100O2N100O1O100O2N1O100O1O1O1O101N1O1O1O101N100O1O100O2N1O2O0O100O1O1O100O2N100O1O2N1O100O1O1O1O2N1O100O2N1O1O100O1O100O1O1O100O2N100OXNZGdLe8T3dGlL[8P3jGQMT8n2nGRMa2]NX2`4YKTM^2_NU2]4^KTM^2aNQ2Z4bKUMZ2gNP2T4gKUMY2hNn1S4jKUMY2gNl1U4kKUMY2eNl1U4lKVMZ2bNj1Y4lKUM\\2`NmLIe4b4SLUM]2[NiL5d4\\4VLTM_2XNjL7_4^4XLSMd2`NR1^4ZLRMd2aNQ1]4[LRMe2aNn0^4]LQMf2`NaLKU4e4dLQMf2hNa0X4iLPMh2jN:W4nLoLj2kN\\L]Oe3j4UMnLk2SOIP4\\MmLm2VOBm3aMmLo2XO[Ol3fMlLQ3WOWOn3hMlLQ3VOUOo3jMkLS3UOQOQ4lMjLU3TOmNS4nMiLW3SOiNV4oMgLY3SOgNV4PNgLZ3ROeNX4QNfLZ3SOcNX4SNeLZ3UO`NW4VNdLZ3UO`NW4WNcLY3WO^NW4YNbLY3XO\\NW4\\N`LY3YOYNX4dNgJTO10080E3O1U4l0WNX4\\4jJXIh0\\2\\4R>"}},
    {"image_id": 285047, "category_id": 67, "segmentation": {"size": [640, 427], "counts": b"]V1Y15lNWb0_1O1O100O100O1000000O1000000O10000O100O10000O10000O1000000O100000000001O00001O00001O001O1O1O001O1O001O001O1O001O001O001O001O001O1O001O001O0000001O001O000000000000001O00001O001O001O1O1O001O1O001O001O001O001O00001O00001O001O1O1O1O2N001O1O1O1O001O1O1O00001O001O1O00001O0000001O0000001O00000000001O0000000000000000O10000O100000000O1lMFb@:^?Ga@9_?Ga@9^?I`@8`?I^@8a?K]@5c?K\\@6d?LY@5g?KY@5g?LW@5i?KV@6j?JU@7k?JS@7m?IS@7l?MQ@3o?NP@2P`0On_O2R`0Nn_O2R`0Om_O1S`01j_O0V`00j_O0V`0Ml_O4T`0Jm_O7S`0Gn_O:Q`0EP@<P`0CP@>P`0AQ@?o?_OR@b0P`0XOT@h0ba0000001O0000000000O100O1O1HTOZ]On0cb09O100000000001O00001O0000001O000000000000001O00000000000000000000O10000000000O1000000O10000O1000000O10000O1lNiN__OW1a`0iN^_OX1b`0iN]_OW1c`0iN\\_OX1d`0iN[_OW1e`0jNY_OW1g`0jNW_OW1i`0jNV_OV1j`0jNU_OW1k`0jNT_OV1l`0jNS_OW1m`0jNQ_OW1o`0jNo^OW1Qa0jNn^OV1Ra0kNk^OW1Ua0kNg^OW1Ya0h01O001O0000001O00000000001O000000000000001O00000000001O000000001O001O0000000000000000001O00000000001O00001O0000001O00001O000000001O000000001O00001O000000001O00001O0000001O000000001O00001O00001O00001O0000001O0000001O00001O00001O001O0000001O00001O00001O001O001O001O0000001O002N00O11O0kN[]Oo0mb0ROT]Od0Uc0O005Kdd0"}},
    {"image_id": 321214, "category_id": 67, "segmentation": {"size": [480, 640], "counts": b"]Sh24:0S>2jA0U>2iAOV>4fANZ><O1O100O1O100O1O100O1O1O1O1O1O100O1O1O1O100O1O1O1O100O1O1O1O1O1O1O1O1O100O1O1N2O1O1O1O1O100O1O1O1O1000000000O2N100O1O100O01O001O010O1O1O1O100O101O00000000001O01O00000O1O2VOPCAQ==SCAm<>UC@l<>WC@k<>WCAo<8SCFS=3PCJU=1oBLW=LQU_3Nok`L4_OLoA8n=?N2O1O0010O01O1O1O1O2N1O1O0000000001O0000000000000000000000000000001O00000000000000000000000000000000000000001O0000000000000000000000000000000000001O0000000000000000000000000000000000000000001O000000000000000000000000000000000000oA"}},
    {"image_id": 334483, "category_id": 67, "segmentation": {"size": [640, 480], "counts": b"kod22kc0301M2O02OO1N1002O001O010O00000O2O0000000O10O10O0N21UO0`]O6_b0N\\]O5bb00X]O2hb0c0O1O100O1O001O1O1N2N2N2N1N3O001O01O1O2O1NZOfNh^OX1Xa0kNh^OS1Ta0ROm^Om0Ra0TOo^Oj0Sa0VOm^Oh0Ta0XOn^Oe0Ta0\\OV^OEb0k0Za0Fe^O9\\a0Gd^O7^a0Ic^O4^a04[^OIga09X^OEja0<V^OBka0>U^O@la0a0U^O\\Oma0d0T^OYOma0i0R^OUOPb0k0b02N100O1O101N10O00000O1O100O2O0O101N10gLSO_Cl0a<UO_Ck0a<VO^Ci0c<XO\\Ch0c<ZO]Ce0b<]O]Cb0d<_O[Ca0e<@ZC?f<CYC=g<DXC<h<EWC:i<IUC7k<JTC6l<LRC4m<OQC0P=8hBHW=:hBFX=<fBDY=?eB@\\=b0bB^O^=d0`B\\O_=7^@_OP2:a=6a@Am19b=5b@Bl18b=5d@Cj18b=4e@Di18a=5e@Dj17a=4f@Ei16a=6f@Di16`=5h@Fg16_=5k@Ef16_=4l@Fe16^=3o@Gc16`=KTAN\\17b=GWAOW1:c=EYAOT1;e=D\\AMn0`0h=_O_ANi0c0V?\\Oj@d0Ya00O10000000000PNZOe@g0[?YOe@g0[?YOe@g0Z?[Oe@e0[?[Od@f0\\?[Oc@e0]?[Oc@e0]?[Oc@e0f=YOPANc05e0e0f=]Om@Me02h0d0e=0aA\\Oj0d0d=3_A[Ol0b0d=4`AZOk0c0c<VOgBm0LZOi0c0d<WOeBl0OZOg0d0c<XOfBk01XOf0e0b<ZOXBJOo0a0YOe0d0b<[OYBJLP1d0WOe0d0b<[OXBKLo0e0XOd0d0b<[OYBKJo0f0YOc0d0d<YOXBU1`0oNd0c0d<YOXBU1?POd0c0g;POgC9]OU1?ROe0`0h;QOfC8^OV1<SOg0?h;QOgC7_O8M3;2i0;i;QOgC8^O35516k0:j;POgC9]O196K8m09j;oNhC:\\OO>6C;Q17i;QOhC8]OMa08]O>R15j;QOiC7]OLd0]1;@j;QOiC6_OKe0^17Al;QOgC5BJf0_13Cl;POhC4DIg0_11Dk;QOiC3DHi0`1MEl;QOjC1EHj0`1KFl;ROhC0HHj0`1HGn;QOhC0HGl0a1DIo;oNhC1IFl0b1BIQ<nNhC1IFm0b1^OKT<lNhC1IEo0c1ZOLV<lNfC1LCn0e1XOMW<jNgC1Z1Y1eNMZ<iNgC2Z1X1cNN\\<iNeC3ABf1f1cNOa<fNeC7X1V3R;dLeC7X1U3S;eLdC6Z1T3S;eLbCKF0e1a3R;eL`CMHMg1a3P;fL_CMJLh1`3P;[MYCUOg1`3P;[MYCVOf1_3Q;[MYCVOg1_3P;YMZCXOf1_3P;YM[CVOg1a3n:UMcEk2]:QMhEo2W:PMjEP3V:nLlES3S:lLnEU3Q:kLPFT3P:kLQFU3o9kLQFV3n9jLSFV3l9jLTFV3l9jLUFV3j9jLVFW3i9iLWFX3h9hLXFY3h9eLZF[3e9eL[F[3f9eLYF\\3f9dL[F\\3e9bL\\F_3c9aL]F`3c9_L]Fb3b9^L_Fb3`9]LaFe3]9[LcFf3]9YLcFh3\\9XLdFf1UMKU<_NgFb1YMNP<_NgF`1^M1i;_NiF_1aM3d;\\NlF_1cM6_;YNPG`1dM<V;QNYGa1cMg0j:gMdGb1cMf0j:fMdGc1dMf0h:gMdGb1eMg0h:eMeGc1dMg0S>XOnAFTOEn>e0oA^O@Ga>j0PB]OEE[>m0RB[OGFX>n0RBYOJGT>o0TBWOKIQ>P1TBVONHn=Q1VBTOOJk=R1WBRO1Jh=T1WBQO3Jf=U1XBoN4Kd=V1YBmN5Lc=V1XBmN7La=V1YBnN7K`=W1ZBlN8L^=W1[BlN9L\\=W1]BkN9MZ=W1^BkN9NY=U1aBkN9NV=U1cBlN\\?S1f@lN[?R1j1O1O1O10000O100O1000000O100O1001O00001O0000001O00001O0RLTOhDn0U;UOiDk0W;VOhDk0W;UOiDm0U;SOkDm0U;SOkDn0T;ROlDn0T;ROlDo0S;QOmDo0S;QOmDo0S;QOmDo0S;ROlDo0S;QOmDo0S;QOmDo0S;QOmDo0S;QOmDo0R;SOmDm0S;SOmDn0R;ROnDn0R;ROnDn0S;QOmDo0S;QOmDo0T;QOkDo0U;QOkDn0V;ROjDn0];iNdDX1R?O100001O001O1O0O2OC=M3O1O1O1O1O1O0010i]O[OSa0d0n^O^OGM^`0d0m_O_OCO^`0b0Q@_O_O1_`0`0R@BZO0d`0>R@DUO1i`0:T@;k?EV@:i?GX@8h?GZ@9e?G[@9e?F]@9c?G]@9W=XObC?WO:U=[O`C<\\O8S=A]C6A9R=A]C6B9o<B^C6C8n<C_C4E8i<GbC1F7b<OgCJG8V<:QD_OI7T<<SD]OJ6R<?SD[OK6S<>RD[OL7R<?QDZON6Xd0"}},
    {"image_id": 335427, "category_id": 67, "segmentation": {"size": [448, 640], "counts": b"_V2b04AZ1N72]NOS2Z1PNPO1i31PLJ5c0Q4]1g2`NZMa1f2]NZMd1f2]NYMg1c2[NZMh1e2XNYMk1e2VNYMl1f2TNZMm1e2UNXMo1e2SNYMo1e2SNXMP2f2QNYMQ2e2PNZMQ2e2oM[MS2c2QNXMR2f2PNXMQ2g2PNXMQ2g2PNXMR2f2XMkI7_3c2d2VMmI8]3d2e2TMoIENa0\\3g2f2TMSJ5V3i2e2SMUJ4U3j2e2RMVJ4U3k2d2QMWJ6S3k2d2oL[JBK`0T3P3e2mLaJ3k2P3c2lLeJNBHU3^3d2lLbJED92HS3`3c2jLdJ1FFR3a3b2hLfJ1GEQ3b3b2hLfJDG012O2P3`3b2iLkJCK5g2_3c2iLWKJU2_3b2hLSKOZ2Z3b2gLSK2Y2X3c2eLTK5X2W3c2cLVK6W2W3c2cLVKD[O:0Ik2g3c2bL]KKVOLa2Q4j2XL`KJVOM_2Q4k2YLcKESO2_2P4j2YLkKH[1n3j2ZLiKK]1k3i2ZLfK0`1f3j2ZLeKKROL^2o3j2YLgKLQOLT2NQNQ4R5YLiKHoNM31P23QNP4R5WLmKFTO0l15nMo3U5VL[LF`0_4U3kK\\LE?a4T3jK]LF>`4U3jK]LH=]4V3lK\\LG>]4V3mKTLCgN8h1IWNa4U5kKUL1;Z4`3dKVL29[4a3cKXLDeN3NOc1h4a3aK`LF^N0a1i4a3aKbLD_N1]1i4b3bKbLD_N1]1j4a3aKjLGCh4c3bKiLHCe4d3cKiLIBd4e3dKgLJ]OLiNf4S5dKeLD\\N1Q1n4n3\\KgLFYN0Q1n4o3\\KiLEWN0Q1o4o3[KjLFWNNQ1Q5n3[KZNe4e1[K\\Nd4d1\\K]Nc4c1^K\\Nb4d1^K]Na4c1_K_N_4a1aK`N^4`1bKaN]4_1bKdN\\4\\1dKeN[4[1eKfNZ4Z1fKgNY4Y1gKhNX4X1hKiNW4W1jKiNV4V1jKkNV4T1jKnNU4Q1kKPOU4o0jKSOU4m0kKTOU4k0kKVOU4i0kKZOS4e0mK[OT4d0lK]OT4b0lK_OT4`0mKAR4>nKDR4:nKHQ47nKKR44nKMR42mK1S4MmK5R4JnK7R4HoK8Q4GoK:l2[KiMZ4[O>e2`KPNn3[Oc0b2dKRNg3[Oh0^2hKTN_3^Oj0[2jKVN\\3^Ol0Z2jKXNY3^Oo0W2kKZNU3_OQ1V2mKZNP3@U1T2lK]Nm2_OX1S2mK\\Nk2AY1S2lK]Ni2@]1Q2mK^Nd2A:GoLY24^Nb2B;GPMX24_N`2B<IoLU26aN]2A>KnLS28aNZ2Ae0GiLV29bNX2Af0GkLT28eNU2@i0GjLS29fNS2@j0KgLn1>fNP2Al0JgLo1=fNo1AbLFX44lLn1<hNk1Cn0GfKNS1m1`0kNg1@T1NeLg1`0kNf1@V1NdLf1b0kNc1A\\1J`Li1a0lNb1A_1I^Lj1a0lNa1Aa1I^Lh1b0nN]1Ad1J\\Lg1c0nN\\1Ae1MZLd1f0nNY1Ag1M[Ld1e0nNX1Ag1O]Lc1c0nNV1@j11^L_1c0oNT1Ak13]L]1c0POT1@m1IXK5T1d1a0nNU1@k1K]K6P1`1d0oNR1@n1H_K8o0`1c0POo0Ao1GaK0L1T1f1a0ROm0_OQ2IaKOK4U1b1`0TOm0^OR2HfK8j0]1a0UOl0^OS2HgK7k09iNa0f1Hk0Af2ITL3SOd0Y1Oh0Ah2HiJNT2g0E2c0_Ol21lL=E4a0^On23lL:E5`0^Oo23mL;B4b0^OQ3HgJ0Y2g0]O3`0^OT3FgJ210S2e0B4>_OT3GoJ2n1d0@5=^OU3HoJ5n1?A6<^O`30cL<A6;^Oa31dL<_O69]Od33dL:^O78\\Oe35eL9^O57]Of37dL7_O65\\Oh37eL7^O64\\Ok3GbJ3LNS2e0@91ZOX4HUJ0T2e0^O80[OY4HUJ2S2c0@7N\\OY4IVJ2S2b0_O8N[OZ4IVJ3T2a0]O8N[O\\4HUJ5T2b0\\O8KYO`4HUJ8S2>^O:GXOb4IUJ:S2<^O9GXOb4=YL1^O9GYOc4JVJ9S2<\\O8GYOP5FiI2Y2h0VO8FXOV5HfI0S2g0\\O:BWOZ5FeI4S2e0[O<AUO`5MdKa0[O=@UO`5OeKa0YO;AUOa51eK`0XO;_OTOc54fK=WO=]OROe55iK;VO=[OSOf57hK8XO?XOROh57iK9VO>XOROk5GcI7V2b0SO>XOROW6ITI0X2g0TO`0VOPOY60]Ka0SO?VOPOZ62\\K?TO`0TOoN\\62^K?QOa0SOnN^65\\K>RO?ROnNa65\\K>PO`0QOmNa68^K;QO?oNnNb6;\\K9RO?nNmNd6;]K9QO`0kNmNR71RKa0QOP1n5_NRKb0oNm0n5cNSK`0nNm0n5YNmH5W2e0nNl0o5YNmH5W2h0kNi0S6WNlH70JS2P1mNf0Y6_NfHNU2m0kNe0Z6aNdHOW2l0jNc0X6nNnJ?jNb0Y6\\NgH`0V2c0iN`0`6^NbH1O2V2o0iN>g6_N[H5V2n0gN>k6fN^Jl0fN=l6iN]Jk0fN;l6kN_Jk0dN9m6PO]Jh0dN7T3_OnND[Of0bN6j29kNlNIf0aN4f2`0oNgNJf0`N2a2m0oNmMkM5W2P1]N0S2gNYMh2\\2XM1X1WN0P2j1W2XNgKMP2T2S2PNlKKP2X2S2mMnKJi1b2V2gMnKFc1S3Z2WMRLFa1W3\\2UMQLC`1_3\\2nLTLB_1c3\\2mLSL_O]1k3^2fLTL_O\\1R4YNPKn3a1ZL^O\\1Z4Y2ZLXL[O]1^4\\2ZLSLWOa1`4]2[M`Mi2`2UM\\MW3^2hL`M\\3`2bL^M`3c2_L\\Mc3d2]LZMj3a2VL[Mo3d2PLZMS4b0[Ia0^2mNY4;XIkN2m1\\2lN\\4:XIlN1n1Z2kN`49UImN3o1W2gNh4:oHnN4Q2T2fNm48kHQO7P2o1cNfM^OZ7m0YIR1f1bNV5:VIT1c1aNZ5:RIV1c1ZNkMEg7P1`HS1n1VNi5g0WHROKl1T2[Nj5e0`HP1d1]Nk5c0cHo0c1ZNn5e0`HQ1c1VNP6h0_HQ1m9nNUFP1k9nNVFT1i9jNYFV1h9hNXFY1j9hN]E\\O601m1[:]N]E`03T1b:YN[E64G6f1Z:]N\\E64G6g1^:WNYE:4F9g1Y:YNZE<2D>e1V:ZNZE>2@a0h1R:ZN[E=i0[1k9VN]E>j0\\1l9eNPFAYOk1f:jNjE[1V:QNYEm04S1e:mN[EXOMc1g:jN[EC2N0c1c:mNZEA3N1e1a:nNYE^Oa0e1V:lNZE\\Ob00@c1c:_N\\E1N3o0^1f9]N]E022l0b1j9[N[E4k0a1k9[NWE8l0]1l9[NXE;3H=b1V:[NZE;4G=c1U:ZNYE=5F>d1Q:[N[E?1Cd0d1n9UOlEUOCh1^:SOoEVOFS2k9gN_FWOFQ2l9gN_FYOCQ2n9eN^F]OAo1S:dNPFWO1a2P:W11O001O2N001O001O0WNfEL\\:1hELX:AeEROO13\\1Z:^OgESOO20[1\\:AcERO21O\\1]:AaERO31M_1^:^OcEQO2N13LX1_:EbEQO4M05LW1_:CWFUO[OW1_:CVFVO\\OV1_:A]EWO<2H4MQ1b:A^EYO92J3NP1b:B]EXO93J3On0b:DjE[OE30m0b:HeEXOI13o0_:HdEYOIM9P1[:HdE[O;k0R:IdEYO<n0P:GgEXO<P1n9HeEXO=P1o9IaEYOE110`0k0[:L\\ED9>]:NYED;=\\:OYED<<[:5TE_Ob0<Y:6SEAc08Z:7SEBd05Z:7TEBd06X:6VEBe07V:7TED:CIa0j:U1RE]N3>m:]1VE`Nj:`1WE_Ni:`1YE_Nh:`1YE_Ng:a1REQN1=m:a1REWNM8R;]1UEXNL:P;\\1UEZNM8o:]1SE]NM6Q;b1kD[N32R;n1oDQNQ;n1REPNo:o1REPNn:P2SEoMn:P2SEoMm:Q2TEmMn:R2`001O16J0O1O0001O10OO2O1O02O0O000020N01O0000001O01N101O00000000001O000N3N2000O01O0000000cNSDg0n;XOSDf0n;ZOTDd0l;]OTDb0m;@QD?P<APD?o;@SD>m;CTD<l;ESD;m;GRD8n;ISD5n;KRD4n;MRD1P<NRD1m;3QDKo;5RDJn;6RDJn;6SDIn;7RDHn;9SDEm;>PDCo;=QDCo;=QDCo;>oCDP<W1O010O000000000001O0ARDlNo;R1RDnNn;P1TDPOl;P1SDQOm;o0SDQOn;R1oCmNQ<S1oCmNQ<S1PDlNP<T1PDlNP<T1QDkNP<S1RDlNn;T1SDkNl;V1TDjNl;V1VDhNj;Y1UDgNk;Z1UDeNk;[1VDcNk;^1;100O1O1O0000001O3M0000000000000000M3O1O1001O001O00001O1O001O0000000000000000001N11N100000O1001O01N1O01001O0O010O10001O0000000O01O1N21O2N1O0O02O0000O2N1000O0011O000O10000000O1N2N1100001O0^OlCUOV<k0jCUOU<m0kCSOS<n0nCROR<k0RDSOo;l0TDROk;o0UDQOk;o0UDQOIMi;R1^DkNN5c;P1jDROT;n0kDTOT;m0jDTOV;l0iDUOW;k0hDVOX;j0hDWOU;B]DU1=ZOV;B\\DS1>\\OU;i0jDXOV;o0bDQO^;R1`DnN`;S1_DmNa;S1^DoNa;h100O1000OO2O1O100O101O00O10O1O100O1000000O1O100O1O1O1O1O10001N10O01O10000O10000N3N10OO20000O1O1O2O0O100O100O0O2O1O100O1N200000UMcES2]:mMdER2\\:nMhEn1X:QNjEn1V:oMmEQ2R:oMoER2l9]MjEb07R2o9TNmEo1S:QNmEo1X:lMhES2_:YMPFd2ee5"}},
    {"image_id": 336356, "category_id": 67, "segmentation": {"size": [640, 427], "counts": b"WVQ27fc03N3M2M4M2N3M2M3O2L3N2N2O1O1O100000000000000O1000O2M3L8I5XOi\\O=fc0EWZf5"}},
    {"image_id": 346703, "category_id": 67, "segmentation": {"size": [640, 550], "counts": b"[?b0eb0_Od]O0O1Kb0Ub0T1N20O3N1N2N2OO00010001N101N100O100O10000O2gNb]On0nb0I3N2N2M2O1O1O1N101O001N2O001NUOMk]O3Vb0Lj]O4Vb00e]O0\\b04]]OOcb07R]ONnb0b00000000000000000O1000O101O00000000lMQOWAo0g>UOYAi0g>XOVAj0i>WOVAj0j>VOUAk0k>VOSAk0m>UOSAk0m>UOSAj0n>VORAj0n>VORAj0m>WORAj0n>WOQAi0o>WOQAi0o>WOQAi0o>XOPAh0o>YOQAg0o>YOPAh0P?XOPAh0P?XOPAh0P?YOn@h0Q?YOo@g0Q?YOn@i0Q?WOo@i0Q?XOo@g0Q?YOo@g0P?[On@f0R?ZOm@g0S?YOm@g0S?ZOk@g0T?ZOl@f0T?[Oj@f0V?[Oh@g0W?YOh@h0X?YOg@f0Z?ZOe@g0Z?[Od@g0[?YOd@h0\\?YOc@g0]?YOb@h0^?YOa@g0_?YO`@i0^?YO_@i0a?UO`@l0`?ROb@n0]?ROb@Q1]?mNd@T1\\?jNd@X1\\?fNe@[1[?dNf@]1X?dNh@\\1X?cNn@DiNd04HU`0OYB0f=N^B0b=O`B0`=0aBO_=0bB1^=MdB2\\=NdB2\\=MfB2Z=NgB2X=NhB2X=MjB2V=NjB3U=MkB3U=MlB2T=NlB3T=LlB4T=LlB4T=LlB4T=LlB3U=MkB1W=OiB0X=0hBOZ=0eB0\\=0dBOSMNQ`02mBNRM2P`00nBLSM6n?NWC3i<MWC4h<LXC5g<KXC6h<KVC7i<IWC8h<HWC9i<HVC8j<HVC5m<LRC1Q=0_31O0Z^O3Y?N^@:b?FX@?i?BU@>l?CS@<n?FP@9J^Ol>9YA8BKS?N[A4A5P?G_A3A8o>E`A1A<o>D_AOB?n>C`AM_Od0P?@`AL^Oh0P?]OaAK]On0n>YOcAI]OR1o>TOdAJ[OV1o>QOfAIYOX1P?POfAIWOZ1R?mNgAIUO\\1T?kNgAJRO^1V?hNhAJPOd06\\OR?6hAQ1]OeNk>:iAm0CfNd>;jAe00gNW^Z7"}},
    {"image_id": 346703, "category_id": 67, "segmentation": {"size": [640, 550], "counts": b"dU\\7>h1Hl?;l_OJT`07k_OIU`07k_OIV`06i_OKW`05i_OKW`06g_OKZ`04f_OLZ`03f_ON[`01e_OO\\`01b_O0``0N`_O2a`0M^_O4c`0L\\_O4f`0KX_O6i`0JV_O6k`0JS_O7n`0HR_O8o`0GP_O:Pa0Gm^O;Ua0Dh^O>Xa0Bh^O>Ya0Be^O?\\a0Ab^O`0^a0Aa^O?`a0A^^O`0ba0B[^O?ga0@X^O`0ia0@V^O`0ja0BS^O?na0AQ^O?oa0AQ^O?oa0AP^O`0Qb0_Oo]Oa0Qb0_Oo]Oa0Qb0_Oo]Oa0Rb0]On]Od0Rb0\\On]Od0Sb0[Om]Oe0Sb0[Om]Oe0Tb0ZOk]Og0Vb0WOk]Oi0Ub0WOk]Oi0Ub0XOi]Oi0Wb0WOi]Oi0Xb0UOi]Ok0Yb0SOf]On0Zb0QOf]OP1Zb0POe]OQ1db0100O100O1O100O1O100O1O10000O100000000O10000001O1O1O00001O001O00000000001O000000000000000000001O0000000000000K5L4M3O1L5N1O1O001N2N101O1O1O1O100O1O1O100O01N11JX\\O4jc0O01O01O100000000000O0100000000O010000000000O100O10001N10000O101O000O101O0WNGh_O<W`0Hf_O9Z`0IY^O2k06l`0HX^O3k02UOEha0c0S_OCVOH02ga0d0R_O]OWON0O11ga05Y^O7W1Chc0"}},
    {"image_id": 360393, "category_id": 67, "segmentation": {"size": [427, 640], "counts": b"j2Z2P;3M6J4M3M3M2O200N4M01OO3O1O000O1O1N2M4M1O1N4L3M3M2O2M3M3M5K2N2N4L3M3M3M2M4M4L4L2N2N3L3N4L`NgHQMV7e2_IRM_6g2nIVMn5g2ZJWMd5f2aJ^MY5_2mJ`MQ5\\2WKaMh4]2]KdM^4[2eKfMY4W2mKkMn3S2ULnMi3P2\\LoMb3o1bLSNZ3k1jLVNS3h1PM^Ni2`1[M_Nc2`1aM_N^2_1fMcNV2\\1lMeNQ2Z1RNjNi1U1YNlNe1R1_NmN`1R1bNQOZ1m0jNTOS1k0oNZOj0f0XO[Of0c0]O]Ob0b0A@:?IB5=MGN75JI5:JE5<N@2c0OZOOi06QOJo08oNFU19jNFW1<fND]1=`NBa1a0\\N^Of1c0WN]Ol1d0QN[OP2g0nMXOU2g0jMXOW2k0eMUO]2j0cMUO_2k0`MTOb2k0^MTOd2k0[MUOf2k0ZMTOh2k0XMTOj2k0VMTOl2k0TMTOn2k0QMUOQ3j0oLVOQ3j0oLUOS3j0mLUOU3i0kLWOW3h0iLWOX3i0gLWO[3i0dLVO^3i0bLVO`3h0aLWO`3i0`LWOa3h0_LWOc3h0\\LXOf3g0ZLYOf3g0YLYOi3f0WLYOj3g0VLXOl3h0SLXOm3h0SLWOo3h0PLXOR4f0oKZOQ4f0oKYOS4g0lKXOU4h0jKXOX4f0iKZOW4f0iKYOY4f0fKZO[4g0dKYO]4f0cKYO_4f0`KZOa4f0_KYOc4f0]KZOc4f0\\KZOf4e0ZK[Of4d0[K[Og4d0XK\\Oi4d0WK\\Oj4c0UK]Ol4c0TK\\On4c0QK]OP5c0PK]OP5c0PK\\OQ5d0nJ]OR5c0mJ]OT5c0lJ\\OV5c0jJ]OV5c0jJ\\OW5d0hJ]OY5b0gJ]OZ5c0fJ]O[5b0dJ^O]5b0cJ]O_5b0aJ^O_5b0`J^Ob5a0^J_Ob5a0^J^Oc5b0\\J^Oe5b0[J^Of5a0ZJ^Og5b0XJ_Oi5`0WJ_Oj5a0VJ_Oj5a0VJ^Ok5b0UJ^Ol5a0SJ_On5a0RJ_On5a0RJ^OP6a0PJ_OP6a0oI_OS6`0mI@S6`0mI@S6`0mI_OT6a0kI@U6`0kI_OW6`0iI_OX6a0hI_OY6`0gI_OZ6a0eI_O\\6a0dI^O^6a0bI^O_6b0`I^Oa6b0_I^Ob6a0^I^Oc6b0]I]Od6c0[I^Of6a0ZI^Og6b0YI^Og6b0YI^Og6b0XI^Oj6a0VI_Oj6a0VI_Oj6a0VI^Ol6a0SI@m6`0SI@m6`0SIAl6?SIBm6>SIAo6>QIBo6>QIBo6>PIBR7=nHCR7=nHCR7=nHBS7>mHBS7>lHBU7>kHBV7=jHCV7=jHBW7>hHCX7=hHBZ7=fHCZ7=fHCZ7=fHCZ7=eHC\\7=dHC]7<cHC^7=bHC^7=bHC^7=bHB_7>`HC`7=`HCa7<_HCb7=^HCb7=]HDc7<]HCe7<[HDe7<[HDe7<[HCf7=ZHCf7=ZHCf7=ZHBg7>YHBh7=XHCh7=XHCh7=WHCj7=VHCj7=VHCj7=VHBk7>UHBl7=THBm7>SHBm7>SHBm7>SHBm7>SHAn7?QHBo7>QHBo7>QHAP8?PHAP8?oGBR8=nGCR8=nGCR8=nGBS8>mGBS8>lGCT8=lGBU8>kGBU8>kGBU8>jGBW8>iGBW8>iGBX8=hGCX8=hGCX8=gGCZ8=fGCZ8=fGCZ8=fGCZ8=eGD[8<eGC\\8=dGC\\8=dGC]8<bGD_8<aGD_8<aGD_8<aGD_8<aGD_8<`GDa8<_GDa8<_GDa8<_GCb8=^GCb8=^GCb8=]GDc8<]GDc8<]GCd8=\\GCd8=\\GCd8=[GDe8<[GDe8<[GCf8=ZGCf8=YGDg8<YGCh8=XGCh8=XGCh8=WGDi8<WGDi8<WGDi8<WGCj8=VGCj8=UGDk8<UGDk8<UGDk8<TGEl8;TGDm8<SGDm8<SGDm8<RGEn8;RGEn8;RGEn8;RGEn8;QGEP9;PGEP9;oFFQ9:`E\\OX1:X9:^E_OX18Z99^EAV16\\99_EAS17^98_ECQ15`98_EDo05b97_EFm02e98^EJh0Oj97^ELe0Nm96^ENb0MP:5^E0?LS:4^E2;LW:2^E65J]:0^ET1b:mN^ES1b:mN^ES1b:mN^ES1c:lN]ET1b:mN^ES1b:mN_ER1a:nN_EQ1b:oN^EQ1b:oN^EQ1b:oN^EQ1b:oN^EQ1a:PO_EP1b:oN^EQ1b:oN^EQ1b:oN^EQ1a:PO_EP1a:PO_EP1a:PO_Eo0b:QO^Eo0b:QO^Eo0b:QO^Eo0b:QO^Eo0b:QO^Eo0b:QO^Eo0b:QO^Eo0b:QO^Eo0b:QO^Eo0a:RO_En0a:RO_En0a:RO_Em0b:SO^Em0b:SO^Em0b:SO^Em0b:SO^Em0b:SO^Em0b:SO^Em0b:SO^Em0a:TO_El0a:TO_El0a:TO_El0a:TO_El0a:TO_El0a:TO_El0a:TO_El0a:TO_El0a:TO_El0a:TO_El0`:UO`Ek0`:UO`Ek0`:UO`Ek0`:UO`Ek0_:VOaEj0_:VOaEj0_:VOaEi0`:WO`Ej0_:VOaEj0_:VOaEi0`:WO`Ei0`:WO`Ej0^:WObEi0^:WObEi0^:WObEi0^:WObEi0]:XOcEh0]:XOcEh0]:XOcEh0]:XOcEh0]:XOcEh0]:XOcEh0\\:YOdEg0\\:YOdEg0\\:YOdEg0\\:YOdEg0\\:YOdEg0[:ZOeEf0[:ZOeEf0[:ZOeEf0[:ZOeEf0[:ZOeEf0Z:[OfEe0Z:[OfEe0Z:[OfEe0Z:[OfEe0Y:\\OgEd0Y:\\OgEd0Y:\\OgEd0Y:\\OgEd0Y:\\OgEd0Y:\\OgEd0X:]OhEc0X:]OhEc0X:]OhEc0W:^OiEb0W:^OiEb0W:^OiEb0W:^OiEc0V:]OjEc0V:]OjEc0U:^OkEb0U:^OkEb0T:_OlEa0T:_OlEa0T:_OlEa0T:_OlEa0S:@mE`0S:@mE`0S:@mE`0S:@mEa0Q:@oE`0Q:@oE`0Q:@oE`0P:APF?P:APF?P:APF?P:APF?o9BQF?n9ARF?n9ARF?n9ARF?n9ARF?m9BSF?k9BUF>k9BUF>k9BUF>k9BUF>j9CVF=j9CVF=j9CVF=i9DWF<i9DWF<i9DWF<h9EXF<g9DYF<g9DYF<g9DXF=g9DYF<g9DYF=f9CZF=f9CZF=e9D[F<d9E\\F;d9E\\F;d9E\\F<b9E^F;b9E^F;b9E^FRONb0c9=_FPO0b0a9>_FoN1d0_9=`FnN2e0^9=`FmN3f0\\9>aFlN3g0[9=bFlN3g0Z9>cFlN3e0Z9?bFmN4d0Y9`0cFmN3c0Z9`0cFmN3c0Z9`0dFlN3c0X9b0gFiN1f0W9a0lFeNMj0V9b0PGbNIl0W9b0RG`NGn0V9c0TG^NFP1U9b0WG\\NDR1U9b0XG[NCS1T9c0ZGYNCS1S9d0[GXNBU1Q9d0]GWNBU1Q9d0^GWN@U1Q9e0`GUN_OV1Q9e0`GUN@V1o8e0bGSN@X1m8g0bGRN@W1o8e0bGTN_OX1n8d0kG\\OV8c0jG]OY8`0aGWN\\OY1l9GhFPO\\OZ1n9CfFTOZOZ1T:]OdFg0`9UO`Fl0b9QO^Fo0f9lN[FT1g9iNZFW1i9fNWF[1k9`NWF`1j:001O00001O00010O0000001O00001O001N10001O001O00001O001N101O001N10001O0O2O000O2O1O0O2O001N100O2O0O2O0O2O1N1O2N101M2O2N1O2N2N1N3NdMnE726n9ATF726h9B[F408e9C^F20:a9BeFOL?^9@lFKId0[9^OPHb0o7\\OTHd0k7YOXHg0k7SOYHm0S:01OO02O0000O10O1000O1O11OO10O10001O1O2N4L3M2N2N4L2MSo5LmPJ5M2N2O1J6M3M3N2N1L5I7L4O1_O`010fI"}},
    {"image_id": 402720, "category_id": 67, "segmentation": {"size": [612, 612], "counts": b"Rjl1;<Gla0>P^ONca09W^OKfa0l0I6J7L4H6J7J6L5M2O1O10_NP@Om?OX@Og?0\\@Nd?0_@0`?Ob@2]?Le@4Z?Kh@8T?Fo@9Q?FQA9P?FQA:n>ESA<l>CVA>h>UOW@KR1P1g>TOX@KS1n0h>UOX@JQ1P1h>VOX@IQ1o0h>YOX@EQ1R1g>YOdAf0\\>ZOdA>e>A\\A=e>C[A=e>DZA=e>C\\A=c>C]A=d>C[A=e>C[A=e>C[A<f>EYA;g>EZA8h>HXA6j>JVA5k>KUA4l>LTA3m>LTA3m>MTA1m>OSA0n>OSA1m>OSA0n>0RAOo>1QANP?1QANP?2PAMQ?3o@LQ?4PAKQ?5o@JR?6o@HQ?9o@FR?9l1100O100O1O00100O100EHj]O8Ub0<O10000O01000O1000000O11N3M3M1L5L4K5M2N20002MUc03i\\O1N2O002M2W_OGe>:YAHf>9YAHf>9XAHh>9WAHh>9VAIh>9VAHj>7WAIi>7WAJh>5YAKf>6YAKg>4ZAKf>5[AKd>6[AGg>;YABi>>o1O2N3LS\\5F[QJ1k01h`0O[^O6g0Ol`0K]^O7f07c`0O]_O2b`0N__O2_`0N__O6``0J`_O7]`0Ie_O8Z`0Hf_O9Y`0Fh_O=T`0Bo_Og0g?XO[@k0a?SOc@n0Z?POj@T1o>kNTA\\1d>bN_Af1X>XNkAQ2k=nMVBX2W?22N23LN2N5K6KdMRNbCl1^<TNeCi1[<WNYA0[2e1_<]NbCa1a<aN]C\\1d<hNYCV1h<nNVCo0k<TOSCj0o<YOnBe0S=]OlBa0U=@kB?Y=mNh@;P2f0`=ROgBm0[=POfBP1Z=POgBn0Z=ROgBl0Y=UOgBk0Y=UOhBi0Y=WOhBf0Z=ZOhB1k=Oe21N100O02O00001O^_Oe0[=[OdBh0\\=UOeBl0h?2O0O2O0O2N1O1O2N1O2N1OEa^ORO_a0m0;1O1O1O1O21N2O0O2O1N2O1O1N4L3K[\\5LlcJ2N1O1M32M005L8H1OO01Oe]ONea01Z^O1fa00W^O1ia01S^O2ma0NQ^O2Qb00i]O3Wb0=0000000O101O000O1N20000O00100O100O001O010O1000O0O2O0M3J_Og]Oe0da0g0^Ob0J7O10O0WOY_OWOg`0h0[_OVOf`0i0[_OVOe`0i0]_OVOd`0j0\\_OVOc`0i0__OVOb`0i0^_OXOf`0c0[_O\\Oh`0a0Y_O_Oi`0>X_OAj`0>V_OBk`0<V_OCl`0;V_OCl`0<T_OCn`0;T_ODl`0;U_ODm`0;S_OEo`08R_OGPa08Q_OFQa08P_OHPa08Q_OFQa08P_OHPa08P_OGRa07o^OIRa06o^OHSa07n0N2N2O]kk3"}},
    {"image_id": 415238, "category_id": 67, "segmentation": {"size": [474, 640], "counts": b"oXd0P11UO\\=\\1E9H7J5M4L3N2N3N1O2N2N1O2N1O1O2O0O2N100O2N100O2O0O1O101N101N100O2O000O2O1N10001VEcLT:^3mEaLS:`3mE_LS:a3mE`LQ:b3nE^LR:b3nE^LQ:c3oE]LQ:c3PF\\LP:d3PF]Ln9d3RF\\Ln9e3QF[Ln9f3RFZLn9f3RFZLn9g3QFXLo9i3QFWLo9i3QFVLP:j3PFWLn9k3QFULo9k3QFVLn9k3QFULn9l3RFULm9k3SFULm9k3TFTLk9m3VFRLj9n3VFSLi9m3WFSLi9m3XFRLg9o3b000000O100000000000001O000O101O1O000O101O0000001O0O101O001O000O2O1O001O00000O2O001O1O00000O10001OO010001O000O100000001O1O00001O0O10O100002N00001O000000O10O10001O00000000O1000000O10000000000000000O1001O0000000000000000O100000O10O10000O1_MbFD`9:hFTOd9k0bFhNf9W1eFRNh9m1c100O1O100O1000000O10000O2O0O4M7I5K3L4M2N2N]CBk:=oDh0T:VOiEP1V:nNiET1X:jNgEW1[:gNdEZ1]:eNbE\\1_:cNaE]1a:aN_E`1a:_N_Ea1b:^N^Eb1c:]N]Ec1d:\\N\\Ed1e:[N[Ee1e:[N[Ee1f:ZNZEf1f:ZNZEf1g:XN[Ef1f:ZNZEf1f:ZNZEe1h:ZNYEd1h:\\NYEb1h:^N]EU1k:kN\\E7\\;Hk100O1000000000000O1000kB7Y;IWDR1^;nN`D\\1X;dNgDb1T;^NlDg1o:YNREh1l:XNTEh1l:XNTEh1l:XNTEh1l:XNTEh1l:XNTEh1l:XNTEi1k:WNUEi1k:WNUEi1k:XNTEh1l:XNSEi1m:WNTEg1m:YNSEg1m:YNSEf1n:ZNREe1o:[NQEe1n:\\NREd1n:\\NREc1o:]NRE`1P;`NTEb0f;^Ok100000O1000001O00000hBD@c0Y;HlD`1m:aNREb1l:^NTEc1j:^NUEc1k:]NUEc1j:^NWEa1g:aNYE_1e:cN[E]1c:eN]E[1a:gN_EY1_:iNaEV1^:lNbET1]:mNcES1[:oNeEQ1Y:QOhEm0V:VOjEi0U:YOkEe0T:^OlE5_:MbEN_:5bEF_:=cEoNl:T1XEdNj:_1V12O1000000O10000aD[NeNKO9a:a1[FI[97aFO]91bF1]9ObF2^9NbF1_9OaF1_9OaF1_9OaF1_9OaF1_9ObFO_91aFLb94^FIe97\\FDh9<YF@j9`0XFXOn9i0SFdN^:\\1hESNc:m1U10000001O00001O010O001O001O1O100O001O1O101N5eDZNX9e3O1O1O00O2O00000000001O0O10000000000000001O0O1000001O00000000000O2O0000000000000000001O000000000O1000001N1000001O00001N101O000O101N1000001O0O10001N101O0O101O0O2O001N1000001O000O101O0O2O0O1O2O001N10001O001N101O001O1N101O0O2O001N101O0O2O0000001O0O1O2O001N2O0O2N101OeCeMX<Y2iCgMW<X2jChMX<V2gCkM[<S2dCnM_<U27CXCZNn<_1UC_NT=W1nBhN^=k0g0@RY_1"}},
    {"image_id": 458992, "category_id": 67, "segmentation": {"size": [640, 480], "counts": b"U>?]2`2h;`MXD`2h;`MYD_2g;aMZD^2f;aM\\D^2d;`M`D^2`;aMbD^2^;aMdD^2\\;bMfD\\2Z;cMhD\\2X;cMjD\\2V;cMlD\\2T;dMmD[2S;eMnDZ2R;fMPEX2P;gMREX2n:hMSEW2m:iMUEU2k:jMWEU2i:kMXET2i:jMYEU2Z>O1O1O1O1O1O1O1O001O1O1O1O001O1O1O1O001O001O001O1O1O001O001O001O1O001O001O1O001O1O1O001O1O1O1O1O00001O001O001O1O001O001O00001O1O1O1O001O00001O00001O1O1O001O000000001O0000001O00000000001O00000000000000O100000000000000000000000000001O00000000001O0000001O0000001O00000000001O00000000001O00001O00001O0000000000001O00001O00001O00001O0000001O00000000000000001O00001O00000000000000000000000000001O001Oog=1PXB000O10000000000O1000000O10000000000O10000000000O10000000000000000000000000000O1000000001O00000000001O000000000000000000O10000O1O100O10000O100O1O1O100O1000000O100000000000000001O000000O1000000000000000000000000000000O1000000000000000000O1O100000000O1000000O100000000O10000000000O100O10000O1000000O100000000O10000O10000O100O100O10000O1000000O100O1O1M3O1O100O10000O1O100O10N2F:H8G9K8IlKNZ41N2O1O1O1O1O1O1O1O1O1O1O2N1O2N1O2N1O1O2N1O1O2N2N2N2N001O00O100O100O100O1000000O1000000O100O2_OQB"}},
    {"image_id": 468332, "category_id": 67, "segmentation": {"size": [424, 640], "counts": b"VP\\26P=4J9I9I0000_OhCN\\<1>01O000O100000000000000000000000000000000O1O10010O0001O0O10001OO1000010O0000000001N10000O0O20000I7N2L4O0O2O10O0100O010000O10000O01N20OJUOPDl0P<VOnC8N6T<NQDNP<LkCK69o;KmCK49P<KmCK4:o;JnCL3:o;JnCM29P<JnCM28Q<KWD4j;LVD4j;LVD4j;LWD2k;MUD3m;KSD5n;JSD5n;JSD5a<O1O0O2N]Wk10chTN1M3K5L4M12O0O1O2O100O1O1O1O0OG0]COd<6500O1O1M3N3Mi[W12SdhN5M2N2O1N2N2L4N20000001O0000bD]OX:c0eE_O[:a0aED^:<aEF_:9]EJd:6QE5P;JkD;U;FjD:V;GiD9W;HfD9\\;i00O10000O2M2O1O10000010O001O001O0000000000000000O10OSO]D]O<OE6c;>]D[Oa05S;a0oD_OQ;`0k01O0100000EZOTDf0l;\\ORDd0n;]OPDd0o;@lCb0T<900000001O00O0100000000000000000O1000000000000001OO1000000001O000000000UI"}},
    {"image_id": 488673, "category_id": 67, "segmentation": {"size": [640, 480], "counts": b"jXh07gc04M3M3M5J4M1O1O1N2O1N2N2N101N2N2HgNf]O\\1Yb0510O1000O101O008G5L3L2O2N2M2O1O1O1O1N2O1O0O101O1N101O000O2O000O101O000O1000001N100000000O2O000O101O000Ooo90RPF001N100000000O100000000O10000O10000O2O0O100O10001N100O1O1O1O100O2N1O1N2O1N2N3L3ASOh]OP1na0f0O1N3O00001O0O10001O001O0O2O00001N10001O00000O1000000O101O000O2O001O001O00001O001O10O01O1O010O0000WOe^OmN\\a0o0j^OoNUa0o0n^OPORa0o0Q_OPOn`0o0U_OPOk`0m0X_OROh`0m0Z_OSOf`0k0\\_OUOc`0k0]_OUOc`0j0__OVO``0j0a_OVO^`0i0c_OXO]`0g0d_OYO[`0f0g_OZOX`0e0i_O\\OW`0c0j_O]OU`0c0k_O^OV`0?l_OBW`09i_OGd`0K^_O6d`0F\\_O<f`0_O\\_Oa0Qb01O10O00000O2O0O101O0O101N1000000O101O000O1000001N1000001NR`7Oo_H10001O00000000000O10001O00000O1000001O0O1000001N10000O1000N2L4Lih3J`WL2N101N2O1N2O0O2O1N2O1O1O1[]O_Oha0d0T^O_Oka0d0o]OAoa0a0k]ODTb0U10O01001O0000O001N2O1O1O0O2O04]Nb^O=cb0O0N1O1O1O001O001O001O001O000000001O0000000000000000000000000000O100O100O1O1N2N2K5]Oc0ZOf0G9C=O10000O10fMm^Og1Ra0XNT_Od1k`0\\NX_Ob1h`0]NZ_Ob1e`0^N^_O`1b`0_Nb_O^1^`0aNe_O]1Z`0dNh_OZ1X`0eNj_OZ1U`0gNm_OW1S`0hNo_OW1P`0jNQ@U1n?lNS@S1i?POY@o0e?SO\\@l0c?UO^@j0c?UO^@j0b?VO^@j0b?UO`@j0`?VO`@j0`?VOa@i0_?WOa@i0_?WOb@h0^?XOb@h0^?XOc@g0]?YOc@g0]?YOd@f0\\?ZOd@f0\\?[Oc@e0]?[Oc@e0]?[Od@d0\\?\\Od@d0\\?]Od@b0\\?^Od@b0\\?^Od@b0\\?^Od@b0]?^Ob@b0^?^Ob@b0^?^Ob@b0^?^Ob@b0_?]Oa@c0_?]Ob@b0_?]Oa@c0`?]O_@c0a?]O_@c0c?[O]@e0d?ZO[@g0f?XOZ@h0h?VOX@j0j?TOU@m0_a0000O10000O100O100O100O1O1N2N2O1N2O1N2O1N2O1O1O1N20000O11O00k1"}},
    {"image_id": 492110, "category_id": 67, "segmentation": {"size": [427, 640], "counts": b"X;R2Y;0O10000O10000O100000000O10000O10000O10000000000O10000O100000000O10000O1000000O1000000O1000000O100000000O100O10000O100000000O1000000O100000000O10000O10000O1000000O1000000O100000000O100O100000000O10000O1000000O100000000O10000O10000O1000000O1000000O10000000000001O2N6J8H1O2N6J3M1O001M2O2N1O2N1O2N1O2O0O2N1O2O0O1O2N2O001N1ZOSDMn;0bDAa;=h0M2O2N1O1O2N2O0O2MXWW10ihhN3N2M2O1N3N1N10001N2O1N100O2O001N100O2O000O2O0O100O1000000O1O100O100O100O10000O1O2O0O1O100O10000O100O100O100O2O0O10001N10000O10000O100OiN`De0`;ZObDe0^;[OcDd0];[OeDd0Z;]OfDd0Y;\\OhDc0X;\\OiDd0W;\\OjDc0V;]OjDc0W;[OkDd0U;\\OkDd0U;[OmDd0T;[OlDe0T;ZOnDf0Q;ZOoDf0Q;ZOPEe0P;ZOREe0n:[OREe0n:[OREf0l:ZOVEe0j:[OVEf0i:ZOXEf0f:[OZEe0f:ZO\\Ee0c:\\O]Ed0c:\\O]Ed0b:\\O`Ec0`:]O`Ec0_:^OaEb0_:^ObEa0^:^OcEb0\\:_OcEb0]:^OcEb0]:]OdEc0\\:]OdEc0\\:]OdEc0\\:\\OdEe0\\:[OdEe0\\:[OdEe0\\:[OdEe0\\:ZOdEg0\\:YOdEg0\\:XOeEh0^;100O100000000O100O100O100O100O100O10000O10000O100O1SOmNbES1]:nNcER1]:oNaER1_:nNaER1_:oN`EQ1`:oN`EQ1`:PO^EQ1a:PO_EP1a:QO]EP1d:oN\\EQ1d:oN\\EQ1d:POZEQ1g:nNYER1g:oNWER1i:nNWER1i:oNUER1l:mNTES1l:mNTES1l:nNRES1n:mNRES1o:mNPES1P;mNoDT1Q;mNmDT1T;lNkDT1U;mNhDU1X;?001O00001O00001O000000001O001O0000001O0000001O00001O00001O0000001O00001N1O1O2N100O2O0O1O101N1O2N2N2N2LU[R2"}},
    {"image_id": 533206, "category_id": 67, "segmentation": {"size": [427, 640], "counts": b"c5f7e5000O10000001O000000O`JaJV3_5iLcJV3]5iLdJW3\\5hLfJW3Z5hLgJX3Y5hLhJW3X5hLiJX3W5hLiJX3W5hLjJW3V5iLjJW3U5jLlJU3T5kLlJU3T5kLlJU3T5kLlJU3T5kLmJT3R5nLmJR3S5nLmJR3S5nLmJR3S5nLmJR3S5nLmJR3R5PMnJo2R5QMnJo2R5QMnJo2R5QMnJo2Q5RMPKm2P5TMPKk2P5UMPKk2P5UMPKk2o4VMQKj2o4VMQKj2o4VMQKj2n4XMRKg2n4YMRKg2n4YMRKg2m4ZMTKe2l4\\MSKd2l4]MTKc2l4]MTKc2k4^MUKb2k4^MVKa2j4_MVKa2i4aMVK_2j4aMVK_2i4bMWK^2h4dMXK[2h4eMXK[2g4fMYKZ2;VK[3a2ZLY2:`KR3Y2dLV2:eKm2V2iLU29iKk2R2lLU29oKd2m1SMT29TL^2i1ZMR28]LU2b1cMQ28hLj1V1oMR27mLd1Q1VNR26oLa1m0]NS22SM]1g0eNV2N[MU1=oNX2LaMn05YOZ2JeMf0JIa2@lM:F;]2[OVNM^Ok0\\2XOZ1i0fNWOX1l0gNUOW1P1eNPOZ1W1`NiN_1\\1]NdNb1_1\\NaNd1a1ZN_Nd1d1[N[Nf1g1XNYNg1i1XNWNh1j1WNVNh1l1WNUNg1m1XNSNg1o1XNQNg1P2YNPNg1Q2XNoMg1T2WNkMj1V2UNjMj1X2UNhMj1Z2UNfMk1[2TNeMk1\\2UNdMj1^2UNbMk1_2TNaMk1`2UN`Mk1a2TN_Ml1b2SN^Ml1d2SN\\Mm1d2SN\\Ml1e2TN[Ml1f2SNZMl1h2SNXMm1i2RNWMm1j2SNVMm1k2RNUMn1l2QNTMn1n2QNRMo1o2PNQMP2P3oMPMP2R3oMnLQ2S3nMmLR2T3mMlLR2V3mMjLS2W3lMiLT2X3kMhLT2[3jMeLV2\\3iMdLW2]3hMcLW2_3hMaLX2a3fM_LZ2b3eM^LZ2d3eM\\L[2e3dM[L[2h3cMXLZ2l3eMTLX2P4gMPLV2T4iMlKT2X4kMhKS2[4lMeKQ2_4nMaKn1d4QN\\Kl1g4TNYK\\1\\OYL_5Z2UK[1_OXL_5\\2RKZ1BXL^5]2PKZ1`5eN`JZ1a5fN_JX1c5hN]JR1XOcL]6Z2[JQ1[OcL[6\\2ZJP1m5POSJn0P6QOPJn0Q6ROoIm0S6ROmIm0T6SOlIl0V6SOjIl0W6TOiIl0X6SOhIl0Y6TOgIl0Z6SOfIm0Z6SOfIm0Z6SOfIm0[6ROeIn0[6ROeIo0[6POeIP1[6POeIP1[6POeIQ1[6nNeIR1[6nNeIR1[6nNeIS1Z6mNfIS1[6lNeIT1[6lNeIT1\\6kNdIV1[6jNeIW1Z6iNfIW1Z6iNfIX1Z6gNfIY1Z6gNfIZ1Y6fNgIZ1Z6eNfI\\1Y6dNgI\\1Y6dNgI\\1Y6dNgI\\1Y6dNgI]1Y6bNgI^1Y6bNgI^1Y6bNgI_1X6aNhI_1X6aNhI_1X6aNhI`1W6`NiI`1W6`NiI`1W6`NiI`1X6_NhIb1W6^NiIb1W6^NiIc1V6]NjId1U6\\NkIe1T6[NlIe1T6[NlIf1S6ZNmIf1S6WNPJj1o5SNTJm1l5PNWJP2i5mMZJT2f5gM^JY2b5`MeJ`2[5]MhJc2X5XMmJh2S5UMPKk2P5TMQKl2o4PMUKP3k4nLWKR3j4gL\\KY3d4cL`K]3b4\\LcKd3R7O1000000O10000000000000000O1000000000000000000000iNhL[HX3^7PMaHP3W7XMiHh2U7ZMkHf2T7[MlHe2S7\\MmHd2S7]MlHc2T7]MlHc2S7^MmHb2R7_MnHa2Q7`MoH`2n6cMRI]2f6kMZIU2c6mM^IS2a6nM_IR2a6nM_IR2a6nM_IS2_6nMaIR2_6nMaIR2_6nMaIR2_6nMaIS2^6mMbIS2_6lMaIT2_6lMaIT2_6lMaIT2`6kM`IU2`6kM`IU2`6kM`IU2a6jM_IW2`6iM`IW2`6iM`IW2a6hM_IX2a6hM_IX2a6hM_IX2a6hM_IX2b6gM^IZ2a6fM_IZ2a6fM_IZ2a6fM_IZ2a6fM_IZ2a6fM_IZ2a6fM_IZ2a6fM_IZ2a6fM_I[2`6eM`I[2`6eM`I[2`6eM`I[2`6eM`I[2`6eM`I\\2_6dMaI\\2_6dMaI\\2_6dMaI\\2^6eMbI[2^6eMcI[2\\6eMeI[2Z6eMfI?^ODl6MgI<AFg6NiI9DGc60kI5EK^61nI2GK[63nI1IKY64PJNINV64QJMJOT65SJJK0R66TJHL1P67UJGL2n57WJFK3n57WJFL3k58ZJCL5j58ZJCM5h58\\JAM7g58]J@M8e58^J@M8e58^J@M9d57_J_OO9b58`J^ON;a57aJ^ON<`56cJ]OM>^56eJ[OO?[56gJZONa0Z55hJYOOb0Y55hJYOOc0Y53iJYONf0W51kJYOOf0U51mJWOOh0V5OlJWOOk0V5LlJWOOn0U5JnJTOOS1R5ISM6n2IRM8m2HSM8l2ITM7l2ITM8k2HUM8j2IWM7f2KZM5d2M\\M4b2M^M3b2M^M4a2L_McNdLP1m5<`MaNgLR1h5=aM^NmLS1a5?YNBe1>]NAb1?_NA`1?aNA^1?cNB[1>eNDY1<hNEV1;kNFS1:mNGR19oNGP19POHP17QOIn07ROJm06TOJk06UOKj05VOMh03YOMf03ZONe02[ONe02\\OMc04]OMb03^OMb03_OLa04_OM`03@M`03@N?2AO=2DM<3DN;2EN;2EN:3FN92HM83HM74IL74IM54KL54KL45LK45LL34ML25NL14OL050LO41LN52KN52LL54KL54KL54KL54LK45LK45MI47LI47MH38OF1:1DO;WO^K]OV4\\1<TOdK@m3\\1?QOjKAf3^1`0oNQL_O^3b1a0mNVLDS3_1g0kNYLEP3`1f0kN\\LEm2`1g0iNaLEf2c1i0hNcLCd2e1i0gNeLCb2f1h0fNjLC\\2h1j0dNmLBY2j1j0cNPMBU2k1TOZNYN9b4^1TM[NYN7b4_1UM[NXN5d4`1TM[NWN5f4`1RM]NWN3f4a1SM\\NVN3h4a1SM[NUN3h4c1SMZNTN4h4c1TMYNTN3i4d1SMZNRN3j4d1TMYNRN2j4f1TMXNQN3k4e1TMXNQN2k4g1TMXNoM1m4h1SMYNnM0m4i1UMYNkMOo4i1VMYNiMNP5k1VMYNgMNR5j1WMYNeMMS5l1XMXNcMMT5l1ZMXN^MNV5l1\\MXNYMN[5k1\\M[Oc2f0]MYOb2i0^MWOa2j0^MWO`2k0`MTO_2n0aMRO^2o0bMQO]2P1cMoN]2R1cMnN\\2S1eMlNZ2U1fMkNY2V1gMiNZ2W1fMiNY2X1fMiNX2Y1hMgNW2Z1iMeNW2\\1iMdNV2]1jMcNV1YNdLU3V2bNT1_N`LQ3\\2_NU1cN[Lo2`2^NU1fNVLn2e2\\NV1jNmKm2m2YNV1_2jNaMV1_2iNbMX1]2hNbMY1^2gNbMY1^2gNbMZ1]2fNcMZ1]2gNbMZ1]2fNcMZ1]2eNdM[1\\2eNdM\\1[2dNeM\\1[2dNdM]1\\2cNdM]1\\2cNdM^1[2bNeM^1[2bNeM^1[2bNeM^1[2bNeM^1[2bNeM_1Z2aNfM_1Z2aNfM_1Z2aNfM_1Z2aNfM_1Z2aNfM_1Z2aNfM_1Z2aNfM_1Z2aNfM_1Z2aNfM_1Z2`NgM`1Y2`NgM`1Y2`NgM`1Y2`NgM`1Y2`NgM`1Y2`NhM_1X2aNhM_1X2aNhM^1Y2bNgM^1Y2bNgM^1Y2bNgM^1Y2bNgM^1Y2bNgM]1Z2cNfM]1Z2cNfM]1Z2cNgM\\1Y2dNgM\\1Y2dNgM[1Z2eNfM[1Z2eNfM[1Z2eNfMZ1[2fNfMY1Z2gNfMX1[2hNeMX1[2hNeMX1[2hNfMV1[2jNeMV1[2jNeMU1\\2kNdMU1\\2kNdMT1]2lNcMS1^2mNbMS1^2mNbMR1_2nNbMP1_2POaMo0`2QO`Mn0a2RO_Mm0b2SO_Mj0c2UO^Mi0d2WO]Md0g2\\OYM`0k2@VM=l2DSM9P3GPM8Q3InL7R3IoL5R3KnL4S3MmL2S3OlL0U31jLOV32iLNW32jLLW38eLG\\3;cLD]3?`L@a3f0ZLYOf3V1kKiNV4[1gKdNY4_1dK`N]4b1bK]N^4c1bK\\N_4d1bK[N^4e1bKZN_4g1aKWN`4i1`KVNa4j1`KUN`4k1`KTNa4l1`KRNa4n1`KPNa4P2_KoMb4Q2_KmMb4S2_KkMb4U2^KjMc4V2^KgMd4Y2]KeMd4[2]KcMd4]2\\KaMf4_2\\K]Mf4c2[K[Mf4e2[KXMg4h2YKWMh4i2YKUMh4k2ZKQMh4o2YKnLi4R3XKlLi4T3YKiLh4W3YKeLj4[3XKaLj4_3XK]Lj4c3XKYLj4g3YKSLj4m3\\KhKi4X4U200000000000000000000000000000000001]GeKE0\\8[4kGoKR8Q4lGSLR8e4N1O1O1O1O001O1O001O1O1O00001O00001O0000001O00001bHaJn6_5PIdJo6\\5PIfJo6[5oHfJQ7Z5oHgJP7Y5nHkJP7U5oHXKe6i4ZI[Kb6e4]I_K`6a4`IaK^6_4bIbK]6i5M3M2N1O2N1O1O2N2N1OdH"}},
    #
    # "laptop"
    {"image_id": 39956, "category_id": 73, "segmentation": {"size": [427, 640], "counts": b"_V`13X=1N2O1O1O000O100000000O10000O10000O100001O0O103Ln_2OT`M000000O100000000000000000000000000000V]U6"}},
    {"image_id": 325838, "category_id": 73, "segmentation": {"size": [480, 640], "counts": b"Vkn09d>6K3N2L5L2N3N2M2O2L301O0010O001O1O100O001O1O010O1O10O01O1O001O1O100O1O10O01O100O001O00100O1O1O001O1O100O1O1O1O001O100O1O001O1O1O0010OO2O00[AIb>7\\AJe>8010O001O001O010O001OO1001N10001O0000000000O100O100O1O100O1N200N200O10O0100O01OO20O1O1N1HaA0^>1dAM]>570[[e6"}},
    {"image_id": 325838, "category_id": 73, "segmentation": {"size": [480, 640], "counts": b"XS`21n>100XAOa>2^ANa>3_AM`>4`AL_>5aAK^>6bAJ^>7aAI]>9cAH[>9dAHZ>:fAGV>=iACn=f0RBZOl=h0TBXOk=i0TBXOk=i0UBXOj=h0VBWOi=k0WBUOi=Q1O1O1O1O1O101N1O1O1O00M4O01O1O00O1100O1O00OkNgNgDV1];iNbDU1a;lN]DS1e;mNZDQ1i;oNWDm0n;SOPDl0Q<VOmCg0W<ZOgCd0\\<]ObCa0a<@]C?e<BZC;i<EVC7P=HPC5S=KmB1X=NiBM\\=2j0O2NVZP6"}},
    {"image_id": 325838, "category_id": 73, "segmentation": {"size": [480, 640], "counts": b"odY13l>5L2N2N103L01M3O10O00102M01O010O0000000010O000000000010O0000001O0001O0001O000000010N1000000001O01O0000000001O01O0000000001O1O0001O00000000000010O00000000000001O000010O0000000010O0000000000001O0O1000000O100O01000O10O01O10O0001O1O00100000OO2OecY6"}},
    {"image_id": 325838, "category_id": 73, "segmentation": {"size": [480, 640], "counts": b"ZR[11P?4K2O00000O010O10O10O010O0001O01O0000010O0000000010O00000001O00000001O01O0O100001O000001O00000000010O0001O000010O000001O01O000000001O0000000000010O00000000001O01O000001O01O00000001O00000O100000O0100O10O10O10O010OO11O010O00O11N1O2M3MbRZ6"}},
    {"image_id": 448076, "category_id": 73, "segmentation": {"size": [480, 640], "counts": b"d]n61o>1O000O101O00000000000000000000000000000JO\\A2b>7N2M3N2M3N1001N2L4M3M3O1N3JVgl1"}},
    {"image_id": 465822, "category_id": 73, "segmentation": {"size": [375, 500], "counts": b"`lU52c;2N2O1N2N2N2O1N2N2O1M3N2O1O1N2O1N2N2O1N2N2N2N2N2L4M3N2O1M3O1N2N2M3N2O1O1N2O1N2N2N2N2N2N2O1M3O1SG"}},
    #
    # "remote"
    {"image_id": 404839, "category_id": 75, "segmentation": {"size": [640, 427], "counts": b"]h_17hc03`\\OJRc06m\\OKSc05m\\OKSc05l\\OMTc03j\\OOUc01k\\OLMKYc0:h\\OJ]c06b\\OI`c0:3M4M2MgW1L^hN000dk_6"}},
    {"image_id": 494913, "category_id": 75, "segmentation": {"size": [428, 640], "counts": b"ib_63W=2O2M2O1O100O01O1O2M2Oolf1"}},
    #
    # "keyboard"
    {"image_id": 13659, "category_id": 76, "segmentation": {"size": [480, 640], "counts": b"Ven11n>2N1O1O2M2N2O1O1O1O2N001O1O100O1O1N2O1O10001O00000000000001O00000000000O1O1O1O1N2O2N1N2N2O1O1O1O1N3M_^e6"}},
    {"image_id": 13659, "category_id": 76, "segmentation": {"size": [480, 640], "counts": b"lke13k>2N2O1N2N2O2N1N2N2O1N2N2N3N1N2O1N2O1O1N3M2N2O1N200O101O0001O000001O000001O00000N2XOdBJ^=1hBMY=1iBMY=2hBLZ=3hBJZ=5iBGZ=8g0O1O100O1O100O2O0000001OWQj6"}},
    {"image_id": 32610, "category_id": 76, "segmentation": {"size": [427, 640], "counts": b"ZmT12V=3N3N1N2N2N2N101M3O1N3M2N2N1O2O1O0100O100O1000O1000O100000000O10000O1000000000001O0000000000001O00O1001N10000000000O100000001OO1000000000000000001O0000000O10000000000000000001O01N11O0001O000000001O0000000000000001O00000O100O1O1O100O10000O10000O100000000000000M3L4M3N3KYf]5"}},
    {"image_id": 32610, "category_id": 76, "segmentation": {"size": [427, 640], "counts": b"W\\o3;n<4N1O1O1O1O1O1O1O2N1O2N1O01O01O0000000000000000001O000000000000O1000000000000001O000000O1000000000000001O00O2O000000000000000001O0000000000000000000000000000001O00000000000000000000001O0000O1000000000000001OO100000000000000000001O003Kf0ZOVki2"}},
    {"image_id": 32610, "category_id": 76, "segmentation": {"size": [427, 640], "counts": b"b]a5=m<=D001OO100000001O0O10000000000001O00O10000000001L7_O]V^2"}},
    {"image_id": 32610, "category_id": 76, "segmentation": {"size": [427, 640], "counts": b"PlX34T=3K5M3000O1000O010000O10000O1000001N1000000000000O101OO100000000000000001O0000O02O0001O0000000001O0O1O^Z\\4"}},
    {"image_id": 32610, "category_id": 76, "segmentation": {"size": [427, 640], "counts": b"b[S3b0h<:G1O001O0000000000000001O004EQkP5"}},
    {"image_id": 35279, "category_id": 76, "segmentation": {"size": [463, 640], "counts": b"Xmb25l=M[B9b=<M2M3_OVOWCP1`<POZC_1e<6N3N1O1O1000000O100000000000001O00000001O00000000000000000000000000001O00000000000001O0000000000O11O00000001O0000000000001O0000000000000001O0000000000010O001O00O0100000000001O0001O00000000000000000001O0000O100000000001O0000000000000000000010O00000000000001O00000000000000000000000000000000000000000001O0001O0000000000000001O001O00001O000000010O000000000000000000000000000000000000000000000010N01001G9TOk0BaP`3"}},
    {"image_id": 51610, "category_id": 76, "segmentation": {"size": [427, 640], "counts": b"dRd13W=1O1O1O1O1O1O1O1O1O1O1O1O1O1O1O2N001O100N2O1O101N1O1O1O1O1O1O1O1O1O001O2N1O1O1O1O2N100N200O1000O100001O0000000000000000000000O100001O0000000001OO100000000000O1O2M2N2N2O1N2N2O1M3O1O1O1N2O1N2N3N1N2M3O1O1N101N2O1N3NnVZ5"}},
    {"image_id": 63602, "category_id": 76, "segmentation": {"size": [425, 640], "counts": b"fZT32Q=6J7K4K5L4K5O100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001O0000O1000000001O01O0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001O0000001O3M6J:F_`^3"}},
    {"image_id": 77595, "category_id": 76, "segmentation": {"size": [425, 640], "counts": b"[9i3`90O10O100000000000O10O100000O100000000O10O10000000O10000000O1000000000O1000O10000000O10O10000000000O010000000O100000O010000000000O010000000O1000O1000O1000000000O01000000000000O010000000O10O1000000000O0100000000O01000000O0100000O10O1000O1000O100000O10O11OO10O100000000O01001O00O1O010O10000000O100000O1000O010000000O100000000O10O10O0100000O1000000000O010001OO100O02O0000000000000O100000000O1000000000O010000000000O100000O1O01000000O100000O010O1O1001N1000001O00001O2M3N001O2N3M6J0O3N2N4K3N2N1O1bMXEY2o:L4M1O3M2N2N3L;F3M3M2N2N3M3L5L1O3L3N5J6Ja^j4"}},
    {"image_id": 80949, "category_id": 76, "segmentation": {"size": [438, 640], "counts": b"jcm31c=3N1O10000O101N10000O10000O100O100N2O1O1O10000O1000000O011O00000O10000000O1O11O0000O100001OO1000000000000000O11O0000000000O100O10001O0000000000000000000001OO100000000000000O100O100O10000O1O100O100O100O10000O1O1000000000000000000001O00001O0000001O00001O000000001O00001O1O00001O001O00001O0000000000000000000000001O0000000000001O00000000001O001O1O001O0000000000000000000000001O00000000000000000000001O00001O2N1O2N3L`Ra02^m^O5K2O2N2N4L3M2O1N1O2N1O100O1O1O110O01N2N1O2N2N2N1O2N1O2N2N2N2N1O2M3N^`k0"}},
    {"image_id": 86582, "category_id": 76, "segmentation": {"size": [427, 640], "counts": b"`\\X51Y=2N2N101M2N2O2^OGnC;R<?00001O000O100000001O0O10000000001O000O101O0000001N1000000000001O0O100000000O2O000000000O10001O001N1000000000000O1000001O000O10000000001O000O100000001O0O1000000000000O2O0000001N10jVi1"}},
    {"image_id": 89648, "category_id": 76, "segmentation": {"size": [427, 640], "counts": b"^o^63W=5L3M2N6J2N8I1N001O00000000000001O3M3M3M2N3M2N2N1O2N3M3Mgh_1"}},
    {"image_id": 111609, "category_id": 76, "segmentation": {"size": [429, 640], "counts": b"kPe76V=5L3M3M3M4L3M3M4L5L2M4L3M3M1O2N2N10O0000000000000000000000001O000000000000000000010O000000001O0000001O00000000"}},
    {"image_id": 112798, "category_id": 76, "segmentation": {"size": [359, 640], "counts": b"b5a0f:0000O10000000O1000000000000000000000000000000000000000000000000000000000O1000000000O1000000000000000000000000000000000000000O1000000000000000000000000000000000000O1O1L4M3MbfQ6"}},
    {"image_id": 135872, "category_id": 76, "segmentation": {"size": [427, 640], "counts": b"eak24W=2N2N2N2N1O1O1N2O2N3M2N2N1O1O1O0000000000000000000000000001O1O1O1O2N2M2O2N1O1O1O002N1O2N1O1O2N1N2O]^j4"}},
    {"image_id": 172595, "category_id": 76, "segmentation": {"size": [360, 640], "counts": b"^fh22U;1O1O1N2O2N1O1N2O1O1N201N1000000000000010O0000000000010O000000000001O01O000001O000001O0000000001O01O0000000000001N1O1O1O1N2O1O2M2O1N2O2NbQ`3"}},
    {"image_id": 195918, "category_id": 76, "segmentation": {"size": [428, 640], "counts": b"U[Z72Z=1O0O2O000O2O00001O0O2O00000O2O00001N100000001N10001O0O10001O0000001O000010O001O01O01O01O01O01O00000010O0001O01O01O00010O01O01O010O00010O01O0001O01O010O001O01cF"}},
    {"image_id": 248631, "category_id": 76, "segmentation": {"size": [480, 640], "counts": b"Tcj04j>3N1N2O1N2L400N2O1O1O1N2N2N1N3N2O1N2N101O1O0N3N3M2N2O1N2M3O1N2O1N2M3N1O2O1O10000O100000O100000000000000000000000O1000000000000O10O10001O0O1000O10000O10000000000000000000000000O0100000O10O01001O0000000000000O100O010000000000000000O1000O1000000000000000000000O100000000000000000O1000O1000000000000000000000000O11OO10O10000000000000000000000000O10O10O010000000000000O100000000000O100000000000000000O100000000000O10000000000000000O10O10000000000000O01O10000O10000000000000O10000000000000000O10000000O10000000000O10000000000000O1001O000000O1000000000O11N10O10000O2O000000O1000000000O100000O100O02O000000000001N01000O10000000O10001O1O1N4M2M200O7I2N4L5K2N4L1O4L2N2M2O00001@jA3`Ze3"}},
    {"image_id": 321118, "category_id": 76, "segmentation": {"size": [426, 640], "counts": b"nST13U=3M3N1N2N2O1O1O1O1N3N1N2000O4M7I8GVdY10j[fN2O0O2O1N2O1O1O0O2O1O001N2O0O2O0O2O1N101O0O101O0O2O001N100O2N1O2O0O2M200O2N100N3[MbNeG6c0Y1f7hN]G7h0T1j7SOmFN=^O7d1_8?RGFn8[2O2O0000001O0000000010O00000001O00000000001O000000000000001O00000000000000000000000001O000000000000000000000000000000000000000000000O1000000000001O000O10000000000O10000000000O1000000O1000000O1000000O1bMlFf0T9YOoFe0Q9TOVGk0k8SOXGTONk0j80YGRO3k0d83YGQO5j0c84ZGPO6j0`86ZGmN:l0\\87[GjN<m0Z88^HHb74cHJ^72fHNZ71hHMY73iHKW74kHKU75kHJV77iHIW77iHHX78hHHY77hHGY79gHGX7:hHEZ7;fHDZ7<fHC[7=fHBZ7>fHAZ7`0fH_O[7a0fH^O[7a0eH^O\\7a0eH_O[7a0eH^O\\7a0fH]O[7b0fH]O[7b0gH]OY7c0gH\\OZ7d0fH[O[7d0gHZOZ7f0fHYO[7g0d2O100O1000000O1000001N0100000000001N100000000000000000000000001O0001O001O1O001O000000000000000000000000001O00000\\EYOe8h0YGZOf8f0YG[Og8f0WG[Oi8f0TG\\Ol8d0SG]Om8c0RG^On8c0PG^OQ9a0nF@Q9a0mFAS9?lFCS9=lFDT9<hFHX99dFJ\\96bFL^94`FN`93]FOc92[FOe94WFMi94UFMk9:lEHT::hEHX:e1000000O100000000000000000000O10O100001O0000000000000000000000000001O0000001O002N1O2N3M1O1O2N2N2N2N2N3M1O2N2N1O3M1O1O2N3M2N2N1O1O3M2N1O2N2N3M1O2N2N2N2N1O2N1O2N1O2N2N1N3N3K_eT1"}},
    {"image_id": 367095, "category_id": 76, "segmentation": {"size": [427, 640], "counts": b"eU_31Y=100O1O100O2O0O100O100O2O000O100O101O0O101O01O00000000001O01O000001O0000001O01O0000001O0000000001O0000000001O01O000001O00000000N3N10000O101O0O101O0O2O1O1N`Uk3"}},
    {"image_id": 370478, "category_id": 76, "segmentation": {"size": [480, 640], "counts": b"o\\k12m>2O2M2O1N2N2O2M102M2O1N2O2M2N2O1O1N2N10O10O001O01O10O0010O010O010O000010O1O01O01O000100O010O0010O010O010O001O01O01O01O010O10O0100O0010O00010O010O0100O1O100O2O0O2N2O1N1O2O1N2O1O1N3N1N2N2N3N0OkcS6"}},
    {"image_id": 376264, "category_id": 76, "segmentation": {"size": [481, 640], "counts": b"fo^61n>4M2N3M2N2N2O1N2N2O0O2N2M3N2N2N3N1N2N1O2N2N3L3N2N2N3M2O0O2O1N2M4M2N2O1N2O1N2M3N2M3N2N2N3M2O1O1N2N2N2N101N2N2M3O1N2O0O2M3N2N3L3M3O1N2O1O1N201N1O101N110O0000010O001N1O100010O00000001O000001O001O001N20O000001O10O000001O001O6J00O2N1O2N1O2]EiKX:a4O1O2N100O1000000000000000O10000000O0100O2O0O1O2N1O1O1O2N1O1N2O1N2N2O1N2N3M2N4L2N2N3M3M2N2N2N2N2N2N2N3M4K3N2N2N2N3M2N1O2O2M2N2M3O0O2N3M2N2N2O2M3M2G802N1N2O2N1O1O0ObC"}},
    {"image_id": 397303, "category_id": 76, "segmentation": {"size": [480, 640], "counts": b"Pbh13m>4L3M2N1OO2O0001O01O000O100000001O000001ON20001O00000O11O01O0N2O2O000O10jRR7"}},
    {"image_id": 425361, "category_id": 76, "segmentation": {"size": [491, 640], "counts": b"[Sj71Y?4M1O1N2O1O1O1O1O1O1N2O1O001O1O1O1O1O2M2O3M2N5K4L2N2N2N1O1N2O00001O000000000000O100O01000O100000000O10001O002N1O2N2N1O2N1O2N1N3N1O001O001N10001O1N2O001O1O1O001O1O1O1O1O1O0O2O1O1O2N1O1O2MYe;"}},
    {"image_id": 433103, "category_id": 76, "segmentation": {"size": [425, 640], "counts": b"b^e11X=0O1O2O0O100O100O101O0O100O2O000O2O001N100O2O0O101O1N101N3N1O2M2O1N2O0O2O000O010O0100O0100O0100O010O010O10O0100O0100O010O0100O010O10O010O01O1O1O00100O1000000000O1O1O1O1O010O010O0100O001O100O2O0O2O1N101N2O1O1N2O0O2O1N2O0O2O0O2O1N2O1N2NnVS5"}},
    {"image_id": 433103, "category_id": 76, "segmentation": {"size": [425, 640], "counts": b"\\nU32W=1N2O1O1N2O001O1N2O1O0O2O1O1O1N101O1O0O2OO1O00100O10O01O1O010O1O10O01O1O1O1O010O1O1O1O1O100O00100O100O1O1O1O2O0OoP\\4"}},
    {"image_id": 433192, "category_id": 76, "segmentation": {"size": [375, 500], "counts": b"bZi13c;2O000O101O001N101O1O0O2O1O001N2O00O1K5GUSf3"}},
    {"image_id": 450303, "category_id": 76, "segmentation": {"size": [480, 640], "counts": b"bmX63m>000O10001N1000000O2O000O10O100000O0100O1000cYh2"}},
    {"image_id": 459153, "category_id": 76, "segmentation": {"size": [640, 427], "counts": b"bjT41nc02O1N2O1O2N1O2O1N01O0N2N3N2N101NjT81VkG0O100O101O0O3M1K7N1O1000O001O100O1O1O1O1O100O1O10000O1O1O1O1O1O1O00V\\m2"}},
    {"image_id": 465822, "category_id": 76, "segmentation": {"size": [375, 500], "counts": b"[kV31e;3N1_DL];9N2N1O1O1O1O001O0000000000000000O10000000000000001O00100O1O1O001O1O1N101O1O1O001O1O1O1OjPo1"}},
    {"image_id": 479126, "category_id": 76, "segmentation": {"size": [427, 640], "counts": b"gW[4?\\<`0O2O000000010O00000000000001O00O2O000000000000000001O00000000000001O000000000001O001O6J4L4L4M2M4KhhZ3"}},
    {"image_id": 513688, "category_id": 76, "segmentation": {"size": [480, 640], "counts": b"WbU6=X>;I7I7F:J6H8K5O1O10000000001O0001O00000000000000000000001O00000000000000000010O00000000000001O00O100000000000000000000000000010O1O0O2Oj0QNfTV2"}},
    {"image_id": 546717, "category_id": 76, "segmentation": {"size": [640, 471], "counts": b"hke44kc02N2N3N1N3N1N2O2M2O2M2N3N1N3M2O1N3M3N1N3N1N2N2O1N3M3M2O2N1N3M2N2O1N3M3N2M2O2M2O1N2O1N2N2O2M3M2N2O2M2N2O0O100O0010O01O01O001N11O10O01O01O01O01O001O010O000010O0010O00010O000010O0001O000010O010O0001O01O01O00010O00001O010O01O01O000010O0001O01O01O010O00001O010O0000001O01O010OO1010O010O000010O00001O0010O0010O00010O001O010O1O1O101N2N2N2N2O1N2N2N2N2N2N2O1N2N2O1N2N2O1N2N2O0O2N2N3M2N2O0O3L201N2O1N2O2M2N2N2N2O1N2N101N3N1N2N2N1O2N2N2O1N2O1Nim8"}},
    {"image_id": 553788, "category_id": 76, "segmentation": {"size": [363, 640], "counts": b"_bY31Z;00000O010O2O001N100O1000000O2O0000001N1O1000000O10001O000O10000O10000O2O00000O100000000O100000001O000000000O10000000000000001N100000000O10000O1000O11N1000000O0100000000O2O0000000O1000000O2O00000O1000000O101O00000O1000000O1000000O2O0000000O10000O101N1O100O1N2O1O1OYUZ2"}},
    #
    # "sink"
    {"image_id": 59920, "category_id": 81, "segmentation": {"size": [640, 427], "counts": b"_<W1ib0O1O1O2N1O2M2O2N1N3M3M3K5L5LZSQ8"}},
    {"image_id": 178028, "category_id": 81, "segmentation": {"size": [500, 375], "counts": b"a8b0Q?101N100O100O101N10000O@[A3h>EfA1\\Z56]TK0O101l@1a>O^A2b>0[A1d>`00O1000O010000O010K5N2O100O10O010000O1000O1000000000O1000000O10000O0100000000000001O1O000000O10000O2O000O10000O10000O2ORmZ4"}},
    {"image_id": 287347, "category_id": 81, "segmentation": {"size": [640, 478], "counts": b"fnZ54ic05N3N2M102M1O010O0001O5J6KUc5Ko\\J3N001O2N1O2N1O1O1O2N1O1O1O1O1O1O1O001O100O10001O0N2N3M2O1O1O001O1O01O0000000000000000100000O0N2O100000000000O100O1WO`]OOcb0Mj0M4N1O1ORX`02mg_O1Ol0TO00O2^OQ]ODRQf1"}},
    {"image_id": 306733, "category_id": 81, "segmentation": {"size": [426, 640], "counts": b"cSY11X=102M2O0O2O00O0010O01O0O20O01001N6K4L2M3N0O2O00O10O1000O1000O10O10O10O100000O1000O10O100000O1000O1000O10000O0100000O1000000000O01000001N103M3M2M2O2N2M__2Me`M1O2M2O1O1O1O1O2O0O1O1OO10000000000O2O0000000O10001O0O10001O0O10001O0O101N[W_5"}},
    {"image_id": 368940, "category_id": 81, "segmentation": {"size": [480, 640], "counts": b"f2n0R>00O0100000O10O1000O0100000O10O1000O10O1000O10O1000O10O100000O01000O1000O1000O10O1000O100O0100000O001O100O10O10000000ZOlA`0\\>N001N2N2N1O2N100O2O1O@JYB2g=0d01O001N101O001N2O1O1O2N1O1O2M2O2N1O1O1N10000000O11N10000000O010O1M3N20O100000000O2O00000O0100O10O01O100O0100000O1000O10O10000001O10O000010O01N2O00001O001O1N101O001N2O001O0O2O0O2O002MhQo6"}},
    {"image_id": 429598, "category_id": 81, "segmentation": {"size": [480, 640], "counts": b"Q]k84k>3M2O0O101O000O10001O0O1000001O0O101O00000O2O0000001O0O10001O000000[OiAb0V>^OkA00<\\5"}},
    {"image_id": 474786, "category_id": 81, "segmentation": {"size": [500, 375], "counts": b"dhi4=U?5K4M2N2N2N2N1O2O0O2N2O0O2N2N10001N10001O0O1000O01000O10O2O001O0O3N2N3M1O1O001N2O0000O1L4M3F:O1O1N101O1N2N2N2O1N2N2O1N3M[B"}},
    {"image_id": 489091, "category_id": 81, "segmentation": {"size": [448, 336], "counts": b"hP[31o=1O001O001O000O2N10001O001O000O101O000000N2O1O10000O100000000000000001^BKW=5hBLY=4fBMY=4eBM[=5bBL^=<O000010O0001O001O10O0001O00001O0M301O010O00010O00WOmBe0W=1M20001O00YOkBO2?T=APC?o<ARC>n<BRC>n<BRC?W=001O00001O00010N1O101O0O1O2N1;DfF"}},
    #
    # "refrigerator"
    {"image_id": 31296, "category_id": 82, "segmentation": {"size": [425, 640], "counts": b"eTT1;m<<E8H6J0000000>B=CWX1GRhN2M2O3M6J1O000000000000000000O100O100O1OjN;l0=B2O00000000001O001O1O2N103L4L1O00001O001O10O01O001O100O001O1O00100O10_NnDi0T<Fd0YOSTW6"}},
    {"image_id": 175364, "category_id": 82, "segmentation": {"size": [461, 614], "counts": b"[9Q5\\900000O10000000000O100000000000000O10000000000O1000000000000O10000000000O10000000000O01000000000O1000O1000000O0100000O1000O10O10000O1000O01000000O1000O010000O10000O10O1000O2O1O?@`0A;E;E;D:G=C9F=D<D:F:E;F\\RV7"}},
    {"image_id": 194724, "category_id": 82, "segmentation": {"size": [480, 640], "counts": b"hWb52b>=^OFSBd0Y=k0F:A`0C<E;E;H9L3O1O100000000000001O00000000000000000000000000000000001O0000000000000000000000O1L4J6L4B>C=K5N2N2N2M3N2N2N2O1N2O1N2O1O1N2O1O1O1N2O1O1N2O1O1N2O1N2O1M3O1N2O1N2N2_OSBLP>1a0N5KgP?7Qo@7K6J2M3_O\\OaBg0^=>00QEoNo7Q1mGTOR8l0iGYOW8g0gG[OY8e0dG^O\\8b0[GfNUNl0`:>RFgN<5POf0c:?gEfNE:k0k0j9V1jEPOV:m20O100O10000O10000000000O100000000000000000000000000000000000000000000000000000000001O000000000000001O00000000001O00000000001O0000001O0000001O00001O001O00001O001O001O000000O1O1O1O1F_ETLb:l3_EQLc:n3800O1O1L4M3L4H8O1N2L4M3J6L4@jCUNW<i1lCUNU<j1nCoMW<Q2<O100N2M3M3M3M3L4O1"}},
    {"image_id": 435880, "category_id": 82, "segmentation": {"size": [480, 640], "counts": b"g\\g37h><De0\\Oc0\\Oe0\\Of0ZO`0_Oa0@4L1O000O10000O1000000O1000000O1000000O1000000O10000O1000000O1000000O10000O100000000O10000O1000000O1000000O10000O1000000O1000000O1000000O10000O10000O1000000O1000000O1000000O1000000O1000000O1000000O1000000O1000000O10000O10000O100000000O10000O100000000O1000000O11O0000000000001O000000001O00000000001O00000000001O000000001O00000000001O00000000001O000000001O00000000001O00000000001O00000000001O0000000O2O0O100O1O1O2N1I7_Nb1bN^1bN\\_^2"}},
    {"image_id": 459954, "category_id": 82, "segmentation": {"size": [375, 500], "counts": b"clc45b;1N3M2EITE8S1HY84aF5i05d8HbF4?>n8_ObF6:?S9Y1001hMeFR2b9N2N000000O1000000000000O10000000000000000000000O10000001O0000000000O100000000O100000000000000001O2Nb0\\O4K4L4J5G;_O]17hN3G9E;I7000000000000000O1O2K4K5L4K5J6L6HTo2"}},
    {"image_id": 462629, "category_id": 82, "segmentation": {"size": [426, 640], "counts": b"b\\\\47l<a0D2OYOh00O00101kBa1];7O7I5K5L00O000O1L400O10000000000O2C<@`0O2N1O1O1O2M2O2N10001N101N=C]i\\3"}},
    {"image_id": 554838, "category_id": 82, "segmentation": {"size": [640, 480], "counts": b"_oR8>Pc0S1TOc0_O`0A=D?C;H5L101O0O10000000001^@XMj=k2PBlN\\<m5_Nj0VOf1ZNd1\\N[1eN0O1000000000000000000000000O100000000000000000000000000O10000O10000O1000000O100001O2SG]3"}},
    #
    # "clock"
    {"image_id": 33638, "category_id": 85, "segmentation": {"size": [640, 425], "counts": b"nRh49dc03O1N200O1000006KO002N1N4KTiX3"}},
    {"image_id": 72795, "category_id": 85, "segmentation": {"size": [480, 640], "counts": b"Q]`4?`>1000000000000000000000000000000O1000000000000000000000O10000000000000003D_A1aWZ4"}},
    {"image_id": 84270, "category_id": 85, "segmentation": {"size": [480, 640], "counts": b"hVZ48g>3N1N100O1O010N3N1N2O1O100O1O100O100O1O1000000001O1O1O001O001O1O1O1O1N2O1O1O1N2N4KYS^4"}},
    {"image_id": 84270, "category_id": 85, "segmentation": {"size": [480, 640], "counts": b"UST4<b>3FDkA?U>70O1O0O100O00100O100000000000000001OO10000O1O100O1O100O100O1O2MV`g4"}},
    {"image_id": 84270, "category_id": 85, "segmentation": {"size": [480, 640], "counts": b"lac46j>3L2O1O1O001O1O001O1O001O1O1O1O2N1O1N2O001O1O000000O1N2O1O100O1O100O10000O11O00O10000010O02N1O00100O1O1O1N101O1O1O0O2MkYl3"}},
    {"image_id": 84270, "category_id": 85, "segmentation": {"size": [480, 640], "counts": b"nlm44g>5O100N2N2O1O1O100O100O1000000000000O1001O000000001O00000000000000O100000000000O2Na]j3"}},
    {"image_id": 92939, "category_id": 85, "segmentation": {"size": [640, 424], "counts": b"lYY44kc03M2N2O1O1O1O1N100O2O0O1O1O00O1O1N2O1O10001O2N1O2N2M3N`V^3"}},
    {"image_id": 234366, "category_id": 85, "segmentation": {"size": [640, 480], "counts": b"[k_5>bc04L5L06LO03L0N5HU`f3"}},
    {"image_id": 268378, "category_id": 85, "segmentation": {"size": [359, 640], "counts": b"hYY46P;2M3L3O1000O2O0Namc2"}},
    {"image_id": 268378, "category_id": 85, "segmentation": {"size": [359, 640], "counts": b"^io46P;3M2I6O2O0000000002M8GP\\l1"}},
    {"image_id": 273712, "category_id": 85, "segmentation": {"size": [640, 480], "counts": b"aPV8<bc04L4M2N2N2N2N2O001i0UOoRo0"}},
    {"image_id": 376322, "category_id": 85, "segmentation": {"size": [640, 478], "counts": b"nmZ55kc01N2N1O1O01N2NXjj3"}},
    {"image_id": 376322, "category_id": 85, "segmentation": {"size": [640, 478], "counts": b"mU[87ic02M10O100O10000O0100000000O10O100000000O10001O002LUZ?"}},
    {"image_id": 388927, "category_id": 85, "segmentation": {"size": [640, 480], "counts": b"WWh41nc01H8L3N3M3N4i\\O\\Okb0o0M2N2ON21K6L4M2L4N3L4L3N2M2O101O1O1O2M2O2O1O00001O10O01O10O001O00001O0O1N2N2O2O00100O001O0000000001O00KW^OSNia0l1600010O000O12O1000N010N1O3M11O3MO0N30O1PNT^OQ2ha0mMY^OT2ia0M3O1OMQNW^Om1ga074L3J6K2N3O2L3K6N1O1N2NKPO^]On0db0RO]]Oj0gb0UOY]Oh0jb0XOV]Og0kb0YOU]Oc0Pc0]Oo\\O`0Tc0Ak\\O=Xc0Cf\\O<]c012H9N3M\\f_2"}},
    {"image_id": 532761, "category_id": 85, "segmentation": {"size": [480, 640], "counts": b"b_T69d>6J5L4L4M2N2N2N2N2N1O2O1N101N10000O2O00000000000000O1000001N101N101N1O2O0O2N2N3M2M3N3L4K7Icna2"}},
    {"image_id": 562207, "category_id": 85, "segmentation": {"size": [425, 640], "counts": b"]n]15T=1N101O00O101O0O1O010OYff6"}},
    #
    # "vase"
    {"image_id": 25394, "category_id": 86, "segmentation": {"size": [640, 480], "counts": b"iZW77fc06Lg0ZO1O00001O0000001N1000010O0001O1O1O1O2M4D=^O\\ee1"}},
    {"image_id": 89045, "category_id": 86, "segmentation": {"size": [425, 640], "counts": b"_WY23V=c0\\O2O001bCXOY<m0OO100000000O100N2O2N1NjZi5"}},
    {"image_id": 175443, "category_id": 86, "segmentation": {"size": [640, 480], "counts": b"Ui63jc06K3N2N1O1N2O1cL_OZCb0e<CVC>j<FQC;o<KjB5W=2aBN_=9[BDh=f0\\AmNmN8l?S37N2O1O11O004L<D3MaNT@jNl?S1X@mNg?Q1\\@nNd?R1]@kNe?T1]@jNd?U1_@hNb?W1`@hN`?W1g@cNY?V1WA`Nj>9^BFd=DQC:]`0M2N4IV_]8"}},
    {"image_id": 189310, "category_id": 86, "segmentation": {"size": [480, 640], "counts": b"h\\h27f>4_Oa0J6O000O01O100O1O2GRB\\OP^^6"}},
    {"image_id": 268378, "category_id": 86, "segmentation": {"size": [359, 640], "counts": b"]Yg6371b::O100001O1O00M210O100001A`E4T`4"}},
    {"image_id": 268378, "category_id": 86, "segmentation": {"size": [359, 640], "counts": b"T\\Y59m:2O1O00001O000000Ni_c1"}},
    {"image_id": 313034, "category_id": 86, "segmentation": {"size": [480, 640], "counts": b"Yae25h>5E:mA]Og=f0RBEf=n0M1O2N1OO1N3^Og0G5L3N3Lj]_6"}},
    {"image_id": 313034, "category_id": 86, "segmentation": {"size": [480, 640], "counts": b"W]e33f>;L8G=E00O001N2O2[Od0M3Mkn`5"}},
    {"image_id": 370042, "category_id": 86, "segmentation": {"size": [356, 640], "counts": b"d[k12P;3N2N1O2aEJm97PFNk96RFMk96TFKi9j0O2dFjNg8V1WGkNl8S1PGPOR9o0kFSOU9n0iFSOX9m0gFSOZ9l0eFUO\\9Y1000dNhFl0Y9SOiFk0W9UOjFj0X9TOiFk0X9SOiFl0i9L4M3M3M4L3LTQi4"}},
    {"image_id": 370042, "category_id": 86, "segmentation": {"size": [356, 640], "counts": b"[d33P;2lENT92jF3S9MmF8n8JoF9o8L^FG5?]9l00000000000O10000000000000000000hNdFg0]9WOQG=P9ASG=m8CTG<j9O2O1O0O2N2M4Ka[_6"}},
    {"image_id": 370042, "category_id": 86, "segmentation": {"size": [356, 640], "counts": b"b_?7k:6K1nNFZG:e8HYG9g8GXG:h8FXG:h8GVG:i8KcFH6>W9P100000001O0000VOcFM]93cFM]92eFM[93fFLZ94hFJX96iFIW97kF]OH0^9c0j001_OjE1W:N`0O2NPoT6"}},
    {"image_id": 370042, "category_id": 86, "segmentation": {"size": [356, 640], "counts": b"Qfd01R;2O1O1O1O2N1O2[EG[:g0I2O000000001O00001O1O1O00000000O100^Ob0N3M2O100O2NlZn5"}},
    {"image_id": 370042, "category_id": 86, "segmentation": {"size": [356, 640], "counts": b"Tgm03=1G0R:1UF<f9FYF;f9GWF<f9FYF;f9FYF;f9GYF9f9d0EfNiF]1U9eNiF^1S9cNlF`1R9:O1O0000O1O0SOlFKU94nFIS96oFHR98oFGQ99PGEQ9;PGCQ9=QG^OR9b0oFUOE1^9j0f0000000000000000001XOjE`0V:^OmEa0S:^OoEa0Z:01O0000jECFNi9`0_FJ`96_FKb94[FOf90YF0i9e06J7I3M6ITQ_5"}},
    {"image_id": 370042, "category_id": 86, "segmentation": {"size": [356, 640], "counts": b"ZoR11R;1QO0iF2U91hF0W92gFOY92fFNZ93dFM]94`FN`93]FOc92ZFOg9b0500000000O10000000000000000001O^OWFHj96c0N2N2Omh`5"}},
    {"image_id": 370042, "category_id": 86, "segmentation": {"size": [356, 640], "counts": b"WVa13o:2N3M2O2N2O1O2jE@d9Q1O00000O1000001O00000000000001N1]ORFIMNR:6_FFd96g0M3NYWS5"}},
    {"image_id": 370042, "category_id": 86, "segmentation": {"size": [356, 640], "counts": b"XSo13P;2O1N<E2N5K001O001O00001O0000000000O100ZOlE4\\:KgE0]:OY]g4"}},
    {"image_id": 415238, "category_id": 86, "segmentation": {"size": [474, 640], "counts": b"lmW3b0T>8I5L4N2M2M4M2N2N101M3N101N101N101N2N100O103L2O0O2\\ClM5<g;e2J3L3N2N2N1N3N2N2N2N1O1O1O1O1O1O1O10O012M10O0010O00000001O0000000000000000000O100O1000000000000001O001O1O5K2N1N3N1O3M00O1O1O1O1O1O1O001N2L4O1O10O10O1O010O010OO1N2O3N1N2O2M2N2N2M3O1M3M3N2M3L4YOoCbNT<[1SD\\NR<d1SDUNP<j1`0O2N101N101N2N101N2O1N2N2O2L3M4M2N4K5L3M7G_gl3"}},
    {"image_id": 419653, "category_id": 86, "segmentation": {"size": [480, 640], "counts": b"SW_3<a>8J3M1O1N2O100000000001N1O3K4I7MSjd5"}},
    {"image_id": 419653, "category_id": 86, "segmentation": {"size": [480, 640], "counts": b"kSh3i0S>5M2O100000000O^OZBLf=1`BL`=2dBK^=3eBK[=4n0JXZ]5"}},
    {"image_id": 467315, "category_id": 86, "segmentation": {"size": [426, 640], "counts": b"nh]2?f<5M4L3N2N2O1N2N2O1O1O1O1O1O1O1O100O1O1J6000000001O000000001O00000000000000000000000000001OO11O000000000000000000000000O10000000000000000000000000000O10000000000O10000000000O17I1O001O001O1O1O001O1O2N1O1O1O2N2N3M2N3M3M7Hcf^4"}},
    {"image_id": 470173, "category_id": 86, "segmentation": {"size": [640, 446], "counts": b"lbj3>]c0:G6L3N2N2N2N2N1O2N2`N_1O2O10O1O2O1N3N0O1O2N1O1O2N2N1O1O1O00O100O1O1O1N2N2O1M3O1N101O1OdMj_OP1U`0mNo_OR1R`0lNQ@S1T`0eNo_OZ1]a0M3M3N2N2N2N00M3L4001M5[Of0I6KeQf3"}},
    {"image_id": 479248, "category_id": 86, "segmentation": {"size": [480, 640], "counts": b"[``24j>3O1N1O2N4L3M3I5O1O2O0O10O2O001O5J3M2L4M2O2O0O2Mih_6"}},
    {"image_id": 479248, "category_id": 86, "segmentation": {"size": [480, 640], "counts": b"jTl66i>2N2N2O0N2H9M20000000O1000001O1N4_OcA8nkW2"}},
    {"image_id": 571718, "category_id": 86, "segmentation": {"size": [427, 640], "counts": b"YPY21X=4L3N2N1O1G901O01N1O1O1K5G:NQdk5"}},
    #
    # "scissors"
    {"image_id": 340930, "category_id": 87, "segmentation": {"size": [480, 640], "counts": b"idY48e>9G7I7H7J6J6J6I7H8H7H9lMaMYGi2b8cMkFi2Q9e1M3M2O000O101O00O1O1M3H8I7K4H7K6I7J5L5J6K5K5K5K5J6L5K5J6K5I8J5J7G9J5L5J6I8H]TZ4"}},
    {"image_id": 456292, "category_id": 87, "segmentation": {"size": [640, 480], "counts": b"bYf3:ec09Ha0k]OnN[`0[1Z_OgNe`0l1c^OZN\\a0V20O01O10O01O010O01O01O010O00010O010O001O0100O100O010O01N2O001O001O001N1O1O1O010O00010O00010O00010O0001O01O0001O01000O5Ke0\\O;D;F;D:UOf\\O=bc0L5L2M1OV\\W4"}},
    #
    # "teddy bear"
    {"image_id": 72813, "category_id": 88, "segmentation": {"size": [480, 640], "counts": b"jP\\32n>2N1N2O1O1N3N1O1O1O1N102N001O001O1N2M3N2N3M2N2O1N2O1N3N1011OO1O2N2N01O2OO1N10101OO00000O1BfBTO[=e0d0N3M2N3M2O0O101N8I1O2MYhT5"}},
    {"image_id": 94185, "category_id": 88, "segmentation": {"size": [480, 640], "counts": b"SUm256<k=?O2O7H<D6K0O10O0O1UOkBJV=3UC[OGNV=7[1N3O1NlZW6"}},
    {"image_id": 94185, "category_id": 88, "segmentation": {"size": [480, 640], "counts": b"QRQ55j>4L2J6M2O100O2O00001O000000000O10000mAYOn=f0RB\\Ol=d0TB^Oj=MVB>0Fi=K_B8HNX>0hA1X>NhA3X>LhA7U>IkA9T>EmA=Z>3N0017DVmk3"}},
    {"image_id": 94185, "category_id": 88, "segmentation": {"size": [480, 640], "counts": b"XfT2e0[>:E;F1O1O01O01OO10001N101O1O2XOVB6m=@^B;[>I3M1Odlm6"}},
    {"image_id": 150417, "category_id": 88, "segmentation": {"size": [480, 640], "counts": b"^j`65j>1N3K4M3gNKZCJE=P=MQC0J5T=NnBc0S=e0001N4M3M3L5L3NO01O00O1O1O1N2OoNbBb0]=^OfBa0W=@mB=R=BRCHC>Z=I\\C6d<I^C6b<HbC6^<HjC2V<LmC3`=01NcW[2"}},
    {"image_id": 309964, "category_id": 88, "segmentation": {"size": [427, 640], "counts": b"U_V34n<OWC2h<OWC3h<NWC2h<OWC2b<M^C102a<a0O000O2aCXOX<o0N3N1O1OFQDWOP<i0b0G3M1O100GVC0j<NZCNVdk4"}},
    {"image_id": 355610, "category_id": 88, "segmentation": {"size": [427, 640], "counts": b"[m49o<5M4L3M3M3L4M2O1N2N1O2M3O1N2M3N2N1O1O2O0O1O1O1N2O1O1O1N2O1O1O1O1O1O1O001TJVN7j1@bN<_1BeN;[1DhN:Y1EkN7U1ImN5S1JoN5R1JPO4P1KSO3n0LTO2l0NVODhNhKS2c4XO@V1`0kN^OV1c0kN[OU1e0lNZOT1f0nNXOR1i0POTOP1l0ROROm0o0UOPOk0o0WOoNi0R1WOnNi0Q1ZOlNf0T1\\OkNc0V1^OiNb0V1@iN?W1BhN>hMZMV2Z21<iMZMV2[20:kM_MP2Y248gM[MmN7V3X255gMkMQ2Q274eMPNQ2o181aMZNS2g1:O`MaNR2f18IcMhNP2i15_OdMPOU2d14]OaMWOX2_14`1JgN1Y1NjNOW1OmNNT11nNNQ12QOLo04SOJm05VOIk06XOGh09ZODg0<\\O@e0`0^O[Od0e0@UOb0k0BPO?P1BnN?R1EhN=X13kMjJ3U5R2i50001O0001O000000001O00001O001O1O001O1O1O1O1O1O1N101O1O0000000001N1O100O100O10000O100O100O10000O100O10000O10000O10000O100O1000000O100000000001O000000000000000000000000O1000000O1000000O1000000001O00000000001O0000000000001O00000000001O00O100000000O1N2N2O1N2O1N2O1O1O1O100O10000O100O1000000O1000000O10000O100000000000000000000000000000000001O000000001O00001O0YN\\NgGd1R8eNlG\\1f7SOXHn0a7YO^Hg0]7@aHa0T7JkH7j65TIKl5W1RJjNk5Y1TJhNa0ZNY3S3SLcNc0\\NW3U3TL`Nc0^NU3U3WL^Na0aNT3U3YLZNb0dNP3W3\\LVNb0fNl2Z3`LPNb0kNi2Y3cLmMa0oNi2V3dLlMa0ROe2PORLU4e0iMc0VOb2V3jLfM`0XOd2V3gLdMb0ZOd2U3hLdM`0[Oe2T3gLeM`0ZOe2j5WMZJf2j5RM^Jj2h5nL^Jo2S8L7I8H2N0O2O0M4N2N2L4O1N2O1O1O1N2O1O2K:H9DjCROW<n04OfCROX<P10M4O001N101N101O0N3N101O0O2O1O1N2O1N2O1O2M2MZYh3"}},
    {"image_id": 355610, "category_id": 88, "segmentation": {"size": [427, 640], "counts": b"X[f3g0]<9I8H6J7G9K4VOUNoEP2i9m0L5L3N4K4K5L4L3N4M2M4L4K6K4M2M3M2O0O10001N100O1O1O1O1N2O100`LlJgNV5W1nJfNS5Y1XK\\Ni4b1]KYNd4f1_KWNb4h1aKUN`4j1bKUN^4k1dKRN]4m1eKQN\\4m1gKQNZ4o1fKQNZ4m1iKQNX4n1jKQNV4o1kKoMV4P2kKoMW4o1kKoMV4P2kKoMV4P2lKoMT4Q2lKnMU4Q2mKnMS4R2mKmMT4R2nKmMR4S2nKlMS4S2nKlMS4T2mKlMS4S2oKkMR4U2nKkMR4U2nKjMS4U2oKjMQ4V2oKiMR4W2nKiMR4V2oKjMQ4V2PLiMP4W2PLiMP4V2QLhMQ4X2PLjLUN1n5T3nKfLQ5W3SKcLR5[3`2O1O1O1O1000000O100O11O000000001O001O001O000XFiL\\9d3O1O001O0000001O0000001O0000000000000000O100O1O1O1O1O1O1O1N2O1O1O1O1O1O1O100O1O10000O10000O10000O10000O100000000O1000000000000000000000000O10000000000000000001O000000000000001O0000001O00001O0000001O001O001O1O1O001O00001O0000001O0000000000001O0000001O1O1O1O1O1O1O001O1O1N101O001O1BULZGl3d8UL\\Gl3b8UL^Gl3_8VLaGl3[8VLeGl3W8VLiGk3U8VLkGk3P8YLPHh3d7cL\\H^3T7QMlHP3S7PMmHQ3S7nLmHR3S7nLmHS3T7kLlHV3T7iLlHX3U7fLkH[3U7dLkH^3g5^K]KS1lNa3a5`KgKk0hNf3Z5fKoKb0gNj3o4mK\\L7eNm3e4VKYKk0]11dNo3e4WLhLHcNS4g4RLhLI`NV4i4PLiLk4W3TKmL]O[Nl4i4fKaMU4^2mKaMS4`2lK`MT4`2mK^MV4_2kK`MZ4\\2gKbM[4]2eKbM\\4a2aK^M`4e2^KYMc4i2\\KUMd4l2\\KSMe4m2\\KQMd4P3\\KoLd4R3]KlLd4S3_KjLa4V3`KiL`4V3cKhL]4X3fKeL[4Z3fKeLZ4[3jKaLV4^3lKaLU4^3nK_LS4`3oK^L]4V3gKfL[4X3hKeL[4X3gKeL^4W3hKcL]4X3gKdL]4Y3gK`L]4^3j20O2NN3L4M4K4M2M3N2L4L5D=J6K7J6Ie0\\O5L3K5K5\\OXXa0"}},
    {"image_id": 370900, "category_id": 88, "segmentation": {"size": [478, 640], "counts": b"Qic41l>3M102`MP1nDUOl:m0SESOl:P1REROj:R1TEoNj:V1REjNl:Y1SEhNi:[1VEfNWO@^;k1\\EdNVOBZ;m1`EbNUOAV;S2eE[NTOGi0g0a8X1cGXNUOM?k0c8Q1oGoMRO76o0f8k0RHPNQO90R1j8f0UHoMQOQ2i80UHPNROR2g8NXHoMPOX2c8J]HnMPO\\2_8FaHnMPO^2[8I\\HdMYO4Oi2P8EnG^Me0^3Y7ZOfHh0W7YOiHi0T7XOlHh0S7XOnHi0P7YOnHh0Q7YOoHh0n6[OQIe0m6]OSIc0l6^OSId0l6AfHh0Z7_3N101O001O1N110`IdH\\5\\7`JlH[5V7`JoH_5Q7\\JVIb5n6UJYIj5o7N1O1N2O3H7M3L3N4L2K6K4E<M2N2N101M2O1O2O0O1N2O100O100O1O101OO010001N100O010O100O100O1O100O100O1I7N2O1N2O1N2O1O1O1ESDeMm;Z2VDdMj;Z2YDeMg;Z2\\DcMe;\\2?0000O100O1O1O1N2K5J6O10000O1000000001O001O1O00001O001O1O0O101O001O00000O2O1N2O2M2M3M2L4K5M3J7L3L4M3K5L4L4M3K5N101N10001O010O1O1O100O01000O10000O100O100O2N2M4K4M4M2N2N2O1N2O1N3M2O2MN3O00010000O1O100O2O0O2O0O2O0O2O0O2O1N2N101N100O2O0O1O100O101N3M2O000O2N101N1O2O1N101N1O1iIdIl3\\6XLcIc3`6]LcI\\3`6cLfIT3^6kLjIi2\\6nLnHVNn0n1QOSN0a2U7WORJMVOb0n6AnI@_Ol0f6BRJSOAW1b6DmK6Y4HgK7\\4FgK8[4EhK9\\4_OjK?Z4XOlKg0W4VOiKj0Y4QOlKl0W4mNPLQ1R4eNXLY1h8O1N1G_BROe=l08O0N3M2K8^OeA2]\\i0"}},
    {"image_id": 370900, "category_id": 88, "segmentation": {"size": [478, 640], "counts": b"]UU49a>7I6J5L3[NZOoDj0n:[OlDi0Q;@nC[Od0X1Z;J_D8^;N]D4a;1ZD1d;2XD3d;d1O2M2cDhLQ;e3L3H9I7I7L4M3O001VIXK]3h4\\LcK`3]4]LgKb3X4\\LlKc3T4ZLPLd3P4ZLSLf3m3VLXLh3i3[JWK0O7T1]5f3[JYKN0@2;T1j5a3ZJaK@G0b08i0l5_3YJcLG1o5]3WJUKi07mNZ1Q6[3YJSKk0Q2j4m2YJSKm0P2k4l2WJUKn0P2l4j2SJYKP1n1l4i2RJ[KR1m1l4h2PJ\\KT1m1k4U3UKlLj4T3WKkLj4T3VKlLj4g2PJ[K_1f1a4j2QLTMP4k2QLSMQ4l2QLQMR4m2oKQMS4n2nKPMT4o2mKoLU4P3lKnLV4P3lKnLV4P3lKoLU4Q3mKkLU4U3mKfLV4Y3mKdLT4\\3nKaLS4^3nKaLT4]3nK`LS4a3mK^LT4b3lK\\LV4c3kK\\LV4b3mK[LV4b3mK\\LT4c3QLWLR4h3QLTLP4l3QLQLQ4n3`3O100HTE]Lo:Z3SEaL24l:Y3[EdLg:\\3>0O4MN1O3O0O1O000O2G8M4L5J5M2O1O1O2O0O4M2M2N101N3M2N1O100O001O10O1000O100O100O1O100O2O0O2O0O2O0O1O1N3I6N2N2O1N2O0O2F:O1N2O1N2O101O1N3N1N2Nj]R3"}},
    {"image_id": 489764, "category_id": 88, "segmentation": {"size": [538, 640], "counts": b"S\\U97b`08H2N3N1N2O1O001O01O010O1O010OO101O1N1O2O1O1O2N1O1O100O20O2N3M1N3ZOR@;W`00O1O010O1O010000O2O1Dl_OO``0OVeb0"}},
    {"image_id": 521405, "category_id": 88, "segmentation": {"size": [640, 426], "counts": b"Ya1W1W2VOl=m0QBVOm=k0RBVOm=j0RBXOm=i0RBXOm=h0SBYOl=h0SBYOl=g0TBYOl=g0TBZOk=f0VBZOi=f0WBZOi=g0WBYOi=g0WBXOi=h0XBVOi=j0WBVOj=j0UBWOj=i0WBWOi=h0VBYOj=g0VBYOj=h0UBXOm9\\OZD?f0b08;k0XOh8\\3ZF[Mo0YOc8c3ZFUMR1XOc8h3WFPMW1WOa8n3TFlL[1UO`8S4SFgL^1VO]8V4SFeL`1UO[8Z4RFbLb1TO[8]4RF^Lc1UOZ8`4QF[Le1UOX8d4QFXLf1UOW8e4SFVLe1UOW8h4RFTLf1UOU8k4SFQLh1SOS8o4TFoKi1QOQ8T5UFkKi1ROo7V5XFhKi1QOm7Z5YFeKk1POj7T7UHlHi7W7WHiHg7Y7XHgHg7[7YHdHf7]7ZHcHf7^7YHbHf7`7YH`Hg7a7XH`Hf7b7YH^Hg7b7ZH]Hf7d7ZHZHg7g7XHYHh7h7WHXHi7h7XHWHi7i7VHWHj7j7VHUHj7k7WHUHi7k7VHUHj7l7VHSHj7n7VHPHl7o7THQHl7P8THnGn7R8RHlGo7U8PHjGR8U8QHfGQ8[8j1O10O10000O01000RLQHjKP8j3bHPL]7h3RIQLo6k3YIQLg6ZOQIk0>Ha6UO_Ik06L[6SOnIf0K4W6UOTJa0J7R6UO[J>G;n5UOcJ8C`0k5WOiJ1Ae0f5YOmJMAh0a5[ORKI_Oj0`5\\OUKF^Ol0]5^OXKB]Oo0Z5_OaKZOXOU1W5AlKnNoN`1U5APLkNnNa1S5DRLfNnNe1o4EULdNoNe1l4FWLcNoNf1j4GWLaNROf1h4HO70J15OJ35MK52KN71IO80G0;OE0=ND2=MC2?M@4a0J@6`0J_O6c0I]O6e0I[O7f0GZO9g0GYO8i0GWO9i0FXO9j0FUO;l0DTO;m0DTO<l0DTO;m0ESO;m0DSO<n0DRO<n0DQO<P1CQO=o0CQO<P1DPO<P1DPO<P1CQO<P1DPO;Q1EoN;Q1DoN<R1DmN=S1CmN<T1DlN<T1ClN=U1CkN=U1CkN<V1DiN=W1CiN<X1DhN<X1DhN;Y1EfN<Z1DfN;[1EeN;[1EdN;]1FbN:^1FbN9_1G`N9VMmNlNk0m38VMnNmNj0m38VMnNmNk0l36YMoNjNl0k35\\MoNiNm0j33_MPOfNn0j32`MPOfNQ1f30dMPOeNQ1f3NgMPOcNT1c3LkMRO`NP1g3NiMRO`Nl0k31fMTO^Ng0P45bMUO]Nb0T49`MVO[N?W4:_MXOYN=X4<_MXOXN;Z4=^MYOWN9\\4=_MZOTN8]4?_MZOSN6_4?^M]ORN3`4`0_M^OPN1b4a0^M_OoMOc4b0`M@kMMf4c0_MAjMKg4d0_MDhMGi4f0_MDgMFj4e0aMEbMGn4c0aMG`MFn4d0bMG^MEQ5c0bMJZMDS5b0dMLVMBV5c0dMLTMBX5b0dMMRMAZ4KYIg0\\5OnL@X40\\Ib0^50jL_OX46^I:a52gL_OV49aI6c54bL^OX4<bI2d56^L^OZ4=bIOg58ZL\\O]4>aIOh59VL\\Oa4=`IMj5=PLZOf4=_IMk5>lKZOj4<]ILn5`0fK[Oo4:[ILP6d0]KYOY58XIKS6h0VKWO`57UIJU6k0PKWOe56SIIY6P1dJUOP6W1\\OKVJUO\\6Q1_Oh1b0XN^Oh1a0XN@h1?YNAg1=[NCe1=ZNDf1;[NEe1;ZNFf1:ZNFf1:ZNFf1:YNFh1:XNFh1:XNFh19XNHh18XNHh17XNJh16XNIi14ZNLf13[NMe12[NOe10\\NOe11[NOe10[N1e1O[N1e1O[N1e1OZN1g1NZN2f1L\\N4d1K\\N5e1J\\N6d1I\\N8d1G]N8d1H[N9e1G[N9e1F\\N:d1E\\N<d1C\\N=e1C[N=e1DZN<f1DYN=g1CYN<h1DWN=i1CVN>j1AWN?i1@XN?i1@WNa0i1^OWNc0i1\\OXNc0i1]OVNd0j1\\OUNe0k1[OUNd0l1\\OSNe0m1[OSNe0m1[OSNe0m1[ORNe0o1[OPNf0P2ZOoMg0Q2XOoMh0R2XOnMh0R2WOnMj0R2VOnMj0R2UOnMk0S2TOmMm0S2ROnMn0R2QOnMP1R2nNoMR1R2kNPNV1P2gNSNX1n1fNSN[1m1cNTN^1l1`NVN_1k1^NWNc1i1[NXNe1i1XNYNi1g1UN[Nj1f1SN\\Nn1d1gLXK_MW3j5b1fL\\KWMW3R6^1iL_KjLW3^6Z1hLAX3`0iL^OX3b0iL]OV3d0jL[OV3f0kLYOU3g0kLXOU3i0nLSOR3n0oLPOQ3S1nLlNQ3U1PMiNP3Y1PMeNQ3[1QMbNo2`1QM^No2d1QM`LXLHf6i3SM]LYLHe6l3SMZLYLHd6P4SMVL_LD^6W4TMTL`LB\\6\\4TMQLbL@[6`4SMoKcL@Y6b4UMmKbL@Y6e4UMjKbLAX6g4VMgKcL_OX6l4UMdKcL_OX6n4VMbKbL_OX6Q5VM_KcL^OV6V5WM\\KcL\\OV6Z5WMYKdL[OU6^5VMWKfLXOU6c5UMTKhLVOS6h5VMPKhLVOR6l5VMmJkLQOQ6S6UMlJR4U5nKjJQ4X5oKgJP4[5PLdJo3^5QLbJm3a5RL^Jm3c5TL]Jj3e5VLZJi3i5VLVJh3m5YLRJe3P6[LoId3S6\\LmIb3U6^LjIa3Y6^LgI`3[6aLcI^3_6aLbI]3`6cL_I\\3c6dL]IZ3f6eLYIZ3i6fLWIX3k6hLTIW3o6gLRIW3P7iLoHV3T7iLlHU3V7jLkHT3W7lLiHR3Z7lLgHR3[7mLeHR3^7mLbHQ3`7nL`HR3a7nL_HP3d7nL\\HQ3f7nL[HP3h7oLXHP3i7oLWHP3l7oLTHo2n7PMSHo2n7PMRHo2Q8PMoGo2S8oLnGo2T8PMmGo2U8oLlGo2W8oLiGP3Z8nLgGP3\\8nLdGQ3_8mLbGQ3a8mL`GQ3c8mL^GQ3e8mL[GQ3i8mLXGQ3k8lLWGQ3m8mLTGR3n8lLSGS3P9iLQGW3R9fLoFY3S9dLoF[3T9bLmF^3T9_LnF`3U9\\LmFd3T9YLmFh3T9ULnFj3T9SLnFo1YNUNk:HnFR2XNVNk:EnFT2YNVNk:BoFW2WNWNk:^OQGZ2UNXNl:ZOPG]2UNZNl:UORG`2RN[No:oNSGe2oM\\NQ;iNRGk2mM\\NU;aNRGS3jM\\NQ>c1oA^NP>b1PB^NQ>a1oA`NP>a1oA`NQ>_1oAaNQ>_1PBaNP>_1oAaNQ>_1oAaNR>_1mAbNR>^1nAcNR>\\1nAdNS>[1mAeNS>\\1lAeNT>Z1mAeNS>\\1lAeNT>[1kAeNU>[1kAfNU>Y1lAfNT>Z1lAgNT>X1lAhNU>X1kAhNT>X1lAhNT>Y1lAfNU>Y1kAhNU>W1kAiNU>W1kAjNU>U1lAjNU>U1kAkNV>T1kAlNU>S1kAmNU>S1kAnNU>Q1kAoNV>P1jAQOU>o0lAPOU>o0kAROU>m0lAROU>m0kASOV>k0kAVOT>j0lAVOU>i0kAWOW>g0jAYOV>f0jAZOW>d0jA\\OW>c0iA]OX>a0jA^OW>`0kA_OV>?kAAV>>jAA[>8iACji0"}},
]
# fmt: on
