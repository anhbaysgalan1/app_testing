import pandas as pd
import numpy as np
import streamlit as st


# test = input()


for i in range(int(15)):
    print(i)


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)