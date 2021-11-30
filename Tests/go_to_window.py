import pygetwindow as gw

# lista = ''
# lista = gw.getAllTitles()
# print(lista)

oknoPodpisu = gw.getWindowsWithTitle('new 1 - Notepad++')[0]
oknoPodpisu.activate()
oknoPodpisu.send_keys('test')

#
# gw.getAllWindows()
#
# gw.getWindowsWithTitle('Untitled')
#
# gw.getActiveWindow()
#
# gw.getActiveWindow().title

# gw.getWindowsAt(10, 10)
