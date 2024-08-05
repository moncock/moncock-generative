import random
from config import config
from pprint import pprint as pp

# collection config
total_supply = 100

# common
def shuffle_data(data, times=99):
    for rnd in range(0, times):
        random.shuffle(data)

# check config percent
print('\n# check config percent\n')
for cfg in config:
    zum = sum([ c[2] for c in cfg ])
    print(cfg[0][0], ':', zum)
    if abs(zum - 100) > 1:
        exit()

# calc trait qty from supply
for cfg in config:
    for info in cfg:
        pct = info[2]
        qty = round(total_supply * pct / 100)
        info.append(qty)

# adjust trait qty
#config[0][1][3] -= 1 # left wing cyborg
#config[0][6][3] -= 1 # left wing robot
#config[1][1][3] -= 1 # leg cyborg
#config[1][6][3] -= 1 # leg robot
#config[2][1][3] += 1 # eye big
#config[2][2][3] += 1 # eye big cute
#config[2][3][3] += 1 # eye big smile
#config[2][9][3] += 1 # eye funny
#config[3][1][3] -= 1 # body cyborg
#config[3][6][3] -= 1 # body robot
#config[4][5][3] += 1 # feather red
#config[5][1][3] -= 1 # right wing cyborg
#config[5][6][3] -= 1 # right wing robot
#config[6][1][3] -= 1 # tail cyborg
#config[6][6][3] -= 1 # tail robot
#config[7][0][3] += 1 # ambient blank
#config[8][1][3] += 1 # bg grass
#config[8][3][3] += 1 # bg ocean
#pp(config)

# check each trait supply
print('\n# check each trait supply\n')
for cfg in config:
    zum = sum(tt[3] for tt in cfg)
    print(cfg[0][0], zum)
    if zum != total_supply:
        exit()

# gen trait by qty
traits = []
for cfg in config:
    xss = [ [ v ] * qty for (_, v, _, qty) in cfg ]
    traits.append([ x for xs in xss for x in xs ]) # flatten and append to traits

# shuffle each trait
for tt in traits:
    shuffle_data(tt)
#for tt in traits: print(len(tt), tt)

# craft NFT from traits
nfts = []
for i in range(0, total_supply):
    nfts.append([ tt[i] for tt in traits ])
shuffle_data(nfts)

# print genesis data
print('\n# print genesis data\n')
print('genesis = [')
for n in nfts: print('  {},'.format(n))
print(']')
