import folium
import pandas as pd
import json

with open('./source/TL_SCCO_CTPRVN.json', 'rt', encoding='UTF8') as cnt:

    korea_geo = json.load(cnt)


df = pd.read_excel('./source/mt_100.xlsx', index_col=0)
# print(df.index)

mt_map = folium.Map(location=[35.82, 128.12], zoom_start=13)

for id, name, lat, lot, addr, ht in zip(df.index, df.iloc[:,0], df.iloc[:,2], df.iloc[:,3], df.iloc[:,4], df.iloc[:,5]):
    folium.Marker([lat, lot],
                    popup=f'<table width="200"><tr><th>이름</th><td><button class ="btn btn-outline-success" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight" id="mt_id" value={id} onclick="checkMtId({id});">{name}</button></td></tr><tr><th>높이</th><td>{ht}m</td></tr><tr><th>주소</th><td>{addr}</td></tr></table>',
                    tooltip=f'{name}',
                    icon=folium.Icon(color='darkgreen', icon='flag')
                  ).add_to(mt_map)

folium.GeoJson(korea_geo).add_to(mt_map)

mt_map.save('source/mt_map_zoom_2.html')