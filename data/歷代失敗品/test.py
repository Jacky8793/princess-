ls = ['綾音(聖誕節)','千歌(聖誕節)','綾音(聖誕節)']

re = False
for l in ls:
    if l == '綾音(聖誕節)':
        if re == True:
            continue
        re = True
    print(l)