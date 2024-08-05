import glob
from pprint import pformat as pf

# load raw config from dir
chunk = []
for path in glob.glob('./traits/*/*.PNG'):
    (_, _, tt, tv) = path.split('/')
    # # skip 1/1 folder
    # if tt == 's1s1':
    #     continue
    chunk.append((tt, tv))
chunk.sort(key=lambda x: (x[0], x[1]))

# craft ordered key config
config = []
prev_tt = None
for (tt, tv) in chunk:
    if prev_tt != tt:
        config.append([[ tt, tv, 0 ]])
        prev_tt = tt
    else:
        config[-1].append([ tt, tv, 0 ])

out = pf(config)
print('config = ', out)
