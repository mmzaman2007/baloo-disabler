# baloo-disabler
Many KDE Plasma users often find Baloo FIle Indexer using so much resources that they literally have to wait until file indexing has been completed. Although it's possible to disable the file indexer from System Settings, some might fail to do so because of bugs or not knowing where to find the option in the first place. So I wrote a simple python3 program to ease the process.

This program creates a shell script, which will auto-start on login and disable Baloo FIle Indexer in the background.

You can always undo it by running the following command in the terminal.

$ rm ~/.config/autostart-scripts/baloo-disabler.sh
