#%%
import timeit
import random
import string
import hashlib
import pandas as pd
import plotly.express as px


i=1
data = []
while i < 3000:
    text = ''.join(random.choices(string.ascii_lowercase + string.digits, k=i)).encode()
    setup="""
import hashlib
text = {}
""".format(text)

    t = timeit.timeit(stmt='hashlib.sha256(text).hexdigest()', setup=setup)

    data.append([i,t])

    i += 100


df = pd.DataFrame(data, columns=['Ilosc_znakow', 'Czas'])

barchart = px.bar(
    df,
    x = 'Ilosc_znakow',
    y = 'Czas',
    title = 'Szybkość generowania hashy',
    labels = {
        'Ilosc_znakow' : 'Ilość losowych znaków',
        'Czas' : 'Czas hashowania'
    }
)

barchart.show()

