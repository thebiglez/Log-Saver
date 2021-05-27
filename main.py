from pywebcopy import save_webpage
# import urllib.request

download_folder = 'C:\\Users\\Mike Nolan\\Documents\\Documents\\Logbot'
kwargs = {'bypass_robots': True, 'project_name': 'Logs'}


dpm = [31, 28, 31, 30, 31, 31, 31, 31, 30, 31, 30, 31] # days per month
year0 = 2021 # starting year
month0 = 4 # starting month
day0 = 18 # starting day
end = False # program finished?

for year in range(year0, 2022): # cycles year
    if year % 4 == 0: # check leap year
        dpm[1] = 29
    else:
        dpm[1] = 28

    for month in range(month0, 13): # cycles month
        for day in range(day0, dpm[month - 1] + 1): # cycles day
            urlDate = str(year) # append year to string

            if month < 10: # check for zero
                urlDate += '0'
            urlDate += str(month) # add month to string

            if day < 10: # check for zero
                urlDate += '0'
            urlDate += str(day) # add day to string

            if urlDate == '20210525': # check if final day
                end = True
                break

            url = 'https://freenode.logbot.info/grapheneos-offtopic/' + urlDate # create URL
            print(url)
            # urllib.request.urlretrieve(url, 'OT' + urlDate + '.html')
            save_webpage(url, download_folder, **kwargs) # save full webpage to download folder

        if end:
            break
        day0 = 1

    if end:
        break
    month0 = 1
