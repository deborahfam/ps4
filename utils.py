#------------------------------
# Libraries
#------------------------------
import pandas as pd
import numpy as np
import math

#------------------------------
# Data Imported
#------------------------------
data = pd.read_csv('database.csv')
rows = data.shape
names = data[['nombre']].values

#------------------------------
# Data Returned
#------------------------------
ret = pd.DataFrame(columns=('Trabajador',''))