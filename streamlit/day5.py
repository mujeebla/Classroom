import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)


# import altair as alt
# from vega_datasets import data

# source = data.cars()

# brush = alt.selection_interval()

# points = alt.Chart(source).mark_point().encode(
#     x='Horsepower',
#     y='Miles_per_Gallon',
#     color=alt.condition(brush, 'Origin', alt.value('lightgray'))
# ).add_params(
#     brush
# )

# bars = alt.Chart(source).mark_bar().encode(
#     y='Origin',
#     color='Origin',
#     x='count(Origin)'
# ).transform_filter(
#     brush
# )
# st.write(points & bars)
# points & bars

# source