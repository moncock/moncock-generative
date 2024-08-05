import json
from genesis import genesis
from pprint import pprint as pp
from meta import *

#pp(sorted(set([ x for xs in genesis for x in xs ])))
#exit()

json_dir = '../gen-sample/json/{}.json' # TODO
ipfs_url = 'ipfs://xxxxx/{}.png'        # TODO

# save json
for (idx, info) in enumerate(genesis):
    token_id = idx + 1
    dest = json_dir.format(token_id)

    # craft data
    metadata = {
      'name'        : '{} #{}'.format(title, token_id),
      'description' : desc,
      'image'       : ipfs_url.format(token_id),
      'attributes'  : [],
    }

    # update traits
    for (i, v) in enumerate(info):
        tt = trait_types[i]
        tv = trait_mapper[v]
        metadata['attributes'].append({ 'trait_type': tt, 'value': tv })

    # write file
    print(dest)
    #pp(metadata)
    with open(dest, "w") as f:
        json.dump(metadata, f)
