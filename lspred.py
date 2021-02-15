
#!/usr/bin/python

import pandas as pd
import glob
import os
import sys
import tensorflow as tf
from tensorflow import keras

t = sys.argv[1:]

classes = ["saprotroph","necrotroph","hemibiotroph","biotroph"]

l=[]
for i in t:
    t = pd.read_csv(i,"\t",usecols=["step_name","step_value"])
    name = i.split("TABLE_")[-1].split(".")[0]
    t.columns = ["name",name]
    t.set_index("name",inplace=True)
    l.append(t)

Xt = pd.concat(l,axis=1)
Xt = Xt.transpose()
model = tf.keras.models.load_model('lspred_15_2_21.h5')

pred = model.predict(Xt)

p = pd.DataFrame(pred)
p.columns = classes
p.index = Xt.index

print(p)
