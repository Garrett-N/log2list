import csv

# i want to get a set of packages that i can remove from the history.log
# history log will look like this:
# xfburn:amd64 (0.6.2-1), xfce4-pulseaudio-plugin:amd64 (0.4.3-0ubuntu1), ...
# and i want this
# xfburn xfce4-pulseaudio-plugin ...
# so i can do "sudo apt-get remove xfburn xfce4-pulseaudio-plugin"

# read the whole file
with open("history.log", "r") as f:
    csv_list = csv.reader(f, delimiter=',')

    # each item will be like:
    # 'xfburn:amd64 (0.6.2-1)'
    # and we need:
    # xfburn
    package_list = []
    for item in csv_list:
        for raw_package in item:
            package = raw_package.split(':')
            package_list.append(package[0])

    # convert list to space delimited string
    space = " "
    package_string = space.join(package_list)

    print(package_string)
