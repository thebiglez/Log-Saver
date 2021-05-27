from pywebcopy import save_webpage
import urllib.request

download_folder = 'C:\\Users\\Mike Nolan\\Documents\\Documents\\Logbot'
kwargs = {'bypass_robots': True, 'project_name': 'Logs'}


dpm = [31, 28, 31, 30, 31, 31, 31, 31, 30, 31, 30, 31]
year0 = 2021
month0 = 4
day0 = 18
end = False

for year in range(year0, 2022):
    if year % 4 == 0:
        dpm[1] = 29
    else:
        dpm[1] = 28

    for month in range(month0, 13):
        for day in range(day0, dpm[month - 1] + 1):
            urlDate = str(year)

            if month < 10:
                urlDate += '0'
            urlDate += str(month)

            if day < 10:
                urlDate += '0'
            urlDate += str(day)

            if urlDate == '20210525':
                end = True
                break

            url = 'https://freenode.logbot.info/grapheneos-offtopic/' + urlDate
            print(url)
            # urllib.request.urlretrieve(url, 'OT' + urlDate + '.html')
            save_webpage(url, download_folder, **kwargs)

        if end:
            break
        day0 = 1

    if end:
        break
    month0 = 1
