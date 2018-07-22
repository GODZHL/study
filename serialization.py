import pickle

d = dict(url='index.html',title='首页',content='首页')
d_serialza = pickle.dumps(d)
print(d_serialza)

d_reserialza = pickle.loads(d_serialza)
print(d_reserialza)
