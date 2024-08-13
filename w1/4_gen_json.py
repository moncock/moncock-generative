import json
from genesis import genesis
from pprint import pprint as pp
from meta import *

#pp(sorted(set([ x for xs in genesis for x in xs ])))
#exit()

json_dir = '../../w10/docs/json/{}.json'
ipfs_url = 'https://moncock.github.io/w1{}/{}.png'

# save json
for (idx, info) in enumerate(genesis):
    token_id = idx + 1
    dest = json_dir.format(token_id)

    # craft data
    metadata = {
      'name'        : '{} #{}'.format(title, token_id),
      'description' : desc,
      'image'       : ipfs_url.format(int(idx/1000), token_id),
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
