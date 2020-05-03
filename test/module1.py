from rosreestr2coord import Area

# Area("38:06:144003:4723")

# 47:01:1706001:6679

area = Area("47:01:1706001:13") # дополнительные аргументы coord_out="EPSG:3857", area_type=1, media-path=MEDIA,
area.to_geojson()
feature = area.to_geojson_poly()
area.get_coord() # [[[area1_xy], [hole1_xy], [hole2_xy]], [[area2_xyl]]]
area.get_attrs()
f = open("C:\TEMP\TEST.JSON", 'w')
f.write(feature)
f.close()

