import pandas as pd
import struct
data = pd.read_csv('data.csv',encoding='utf-8').fillna(0).astype(str)
print ("BEFORE:",data.head())
abcd = 1

def get_value(col):
	out=col.copy()
	i=0
	for d in col:
		d=eval(d)
		packed = struct.pack('L',d)
		unpacked = struct.unpack('L',packed)[0]
		out[i] = unpacked
		i+=1
	return out
	
data['col1'] = get_value(data['col1'].values)
data['col2'] = get_value(data['col2'].values)
data['col3'] = get_value(data['col3'].values)
print('AFTER:',data)	

sample=['1234','abcd', '0x12cd']
print(sample,'CONVERTED TO:',get_value(sample))