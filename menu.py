import pygame
import pygame.gfxdraw
import time


def set_cursor(s):  # Sorry Debbie
    THE_DRIVE = (  # sized 48x72
        "  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠀⠒⠀⠀⠀⠈⠔⣻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⣾⡏⠀⠀⠠⠀⠀⠀⢠⡼⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       ",
        "⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣾⣿⣯⣿⣿⣾⡶⣶⣬⣤⣤⣽⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⢻⡿⡛⠳⠿⠟⣿⠆⢙⣿⣟⡿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⣿⣸⢭⠀⢀⣴⢺⣬⣲⣼⣽⡗⠈⣁⢛⣅⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⣿⣟⡅⣇⠞⡵⣚⣿⣟⡿⣿⣼⡤⣶⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣾⣿⣿⢸⣿⣞⣯⣝⣛⣛⢻⣿⡏⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⢸⣏⡏⣀⣺⣿⠿⢿⣿⣿⣿⡟⣿⣽⡟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⢀⠤⠒⠒⢺⣷⣶⣖⢽⣣⣾⣿⣱⡯⡛⣿⣤⡻⠀⣸⡿⡵⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡞⠁⠀⠀⠀⢸⣿⣿⠏⢹⣿⣿⣯⣾⢧⢇⣿⣿⣿⣿⣿⡿⣹⣿⣵⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀  ",
        "⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠃⢀⠀⠀⠀⠀⢸⣿⣿⡷⢻⣿⡿⣿⢿⣾⣟⣎⠉⠉⣙⣽⣽⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⣀⣤⠺⢻⣯⢭⢋⠜⠀⠀⠀⠀⠘⣿⢿⡏⢡⣷⠹⢎⡙⣿⣿⣿⣷⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣟⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀⠀⠀⠀⠀⠀  ⠀⠀⢀⡴⠾⠛⠳⢇⣝⣯⠾⢇⠀⠀⠀⠂⠀⡲⣿⣿⣿⠀⢧⡩⡠⠽⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⡯⣸⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "  ⠀⠀⠀⠀⠀⠀⠀⣴⠏⠀⠀⢀⠤⣞⡟⣿⣄⡐⠓⠜⢶⡖⡍⠖⣿⣯⣿⣇⠕⡉⢀⢂⣪⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣱⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀⠀  ⠀⠀⠀⠀⣾⣣⠁⠠⠀⠀⠐⠘⠋⣫⣿⣧⠀⠀⡿⡔⢕⡄⢿⣿⣿⣿⡶⡙⠊⠋⢿⣿⣿⠿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣫⣿⣏⣿⣿⢿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "  ⠀⠀⠀⠀⠀⢰⡟⠒⢓⠊⠒⠀⠀⠀⠀⢋⡄⣈⠄⣼⣕⣯⣿⡧⢸⣿⣿⣿⣿⡜⢦⣤⣾⣿⣇⢀⣾⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⢛⣽⣿⣻⣿⣿⢿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀  ⠀⠀⠀⠀⢸⣧⠄⠂⠀⠀⠀⠠⠄⠀⢘⣧⠏⢠⡫⣽⣿⣿⠃⢸⣿⣿⣿⣿⣿⡄⠙⠛⣝⠙⣿⣻⡿⢉⣿⣷⣿⣿⣿⣿⣿⡾⣾⣿⣽⣿⣿⣿⡿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀⠀  ⠀⠀⠀⢸⣧⣥⣤⣄⡨⣈⡂⠔⠆⣽⣵⣿⣷⣿⣿⣷⣯⣄⣿⣿⣿⣿⣿⣿⣿⣦⣼⣿⣼⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣻⣿⣷⣾⣟⣿⢿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀     ",
        "  ⠀⠀⠀⠀⡰⠿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⢿⣿⣿⣯⣿⣿⣾⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠻⢿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀     ",
        "  ⠀⠀⢀⠼⠁⣼⣿⣿⣵⣿⡿⡋⠀⢀⡕⠀⠈⢿⣿⢿⣟⡋⣽⣿⣿⣿⢿⣿⣿⡿⡋⠉⠉⠉⠹⠋⠈⣿⣿⠿⢄⣀⡀⣦⣀⣌⣙⣿⣿⣿⡟⣛⣽⣽⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀     ",
        "  ⠀⢀⣞⠀⠀⠈⠙⢋⣡⠴⢣⡄⣠⠅⠇⠀⠠⣬⣗⠀⢙⣿⣿⣿⣿⣿⣿⣿⣿⣇⠇⠀⠀⠀⠀⢂⣰⠏⢷⣤⠀⣬⡉⠙⣪⣾⣷⢽⡏⢛⣷⣼⢷⣛⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀     ",
        "  ⠀⣼⠈⠈⠀⠐⠶⣾⣒⡚⡿⣇⢏⠈⣠⣌⣜⣿⣗⣴⣿⣿⣿⣿⣿⣿⣾⣿⡿⠠⣰⣴⠠⠂⢈⢈⣀⣤⣼⢾⣈⠹⣧⣾⣋⡾⣿⣿⣇⠀⠈⢾⣿⣿⣻⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀     ",
        "  ⠀⡏⠀⠀⡀⣺⠟⠉⠉⠛⠛⠻⠾⢿⣯⣖⣽⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠋⠁⠀⠀⠙⠺⣝⣷⢟⣿⣯⣯⣗⢿⣿⣫⡝⠛⡴⣿⣿⢻⡧⣆⠀⠉⢿⣿⣿⠿⣩⠉⠉⠙⣿⣷⡀⠀     ",
        "  ⢸⠀⠠⠴⠚⠢⡳⣀⣐⣂⠤⣠⣄⣀⣀⣀⡝⣛⢙⣋⢹⣿⣮⣅⡀⣢⣀⢈⠋⠁⢔⣬⣼⠧⣖⣥⡻⡽⣟⣿⠟⠻⣿⣵⣔⣨⣿⣽⣿⡿⢿⣿⣖⡼⣿⣷⡿⠯⠴⠔⠒⠾⣿⣇⠀     ",
        "  ⠈⠘⠀⠂⡷⡿⣦⡆⢀⠠⠂⠅⡀⣰⢷⣺⣿⠟⡑⠝⢍⣷⣡⣉⣋⡛⣿⣭⣻⠿⣿⡗⣾⣿⠃⠀⢴⣾⣿⣿⣦⣄⠚⠉⣝⣽⠿⣿⣾⣻⣿⣯⣷⣿⡷⣝⡧⣤⣀⠨⠑⢫⡛⢿⡄     ",
        "  ⠀⠀⠰⢴⠥⠄⠳⡀⠐⠐⠄⠐⣤⢿⣷⣿⣿⣙⣿⡷⠿⡟⣛⣻⣽⡿⣿⣾⣿⣿⣷⣯⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⠉⠙⠛⢾⣳⡽⣿⣿⣷⣇⣴⣻⣩⡋⠇⡿⣷⣦⢠⠡⡄⢹     ",
        "  ⣦⡄⠀⠀⠐⠠⡀⠂⠐⠀⠀⠂⠀⠣⣿⣿⣭⣶⣾⡿⣖⠟⣛⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠈⠻⣮⠃⠩⡐⠫⢫⠟⢕⢾⣿⣾⣾⣷⣶⠟⠁     ",
        "  ⢹⣿⣮⣆⡀⢰⡰⠘⠀⠀⠀⠀⠀⠉⠟⠛⢋⢬⣕⣾⣶⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠈⠳⣶⣄⠘⠢⣄⡈⠛⢿⣿⣿⣿⣝⡆⠀     ",
        "  ⠀⢻⡯⠟⡈⢻⠟⠄⠀⠀⠀⠀⠀⢀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣗⢧⢞⠛⠷⢦⣤⣭⣿⣿⣃⡼     ",
        "  ⠀⠀⠈⠉⠉⠐⠓⠒⠶⠤⠤⠒⣾⣿⣿⣿⣿⣿⡿⣿⣿⣿⡿⣿⣿⣯⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠺⣶⣀⣀⣌⣩⣍⡭⣷⡟⠁     ",
        "  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣻⢷⣭⣟⣯⣿⣿⡿⣛⣛⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀     ",
        "  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣷⣷⣾⣉⣟⣷⣟⠓⣤⣼⣿⣽⣿⣿⣿⣿⣷⣾⢟⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⢿⣿⣷⣿⣿⣿⣵⣿⣿⣿⣿⣿⣿⣿⣭⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "  ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀  ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀  ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀  ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀  ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "  ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "  ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "⠀  ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ",
        "                                                                        ",
        "                                                                        ",
        "                                                                        ",
        "                                                                        ")

    happy_face = (
        "        ",
        "  0  0  ",
        "        ",
        " 1    1 ",
        "  1111  ",
        "        ",
        "        ",
        "        "
        )
    '''
    the_drive = pygame.cursors.compile(THE_DRIVE,
                               black='⢸',
                               white= '⣿', xor='o')
    pygame.mouse.set_cursor(the_drive)
    '''
    happy = pygame.cursors.compile(happy_face, black='0', white='1', xor='o')
    pygame.mouse.set_cursor(happy)


def menu_choices(screen, s, event):
    # These are the values for the start button, which the rest will adjust accordingly
    width = 200
    height = 50
    x = 150
    y = 150
    start_button = pygame.draw.rect(screen, "yellow", (x, y, width, height))
    medium_button = pygame.draw.rect(screen, "white", (x, y + height * 2, width, height))  # Place it just under start
    hard_button = pygame.draw.rect(screen, "white", (x, y + height * 4, width, height))  # Place it just under med
    exit_button = pygame.draw.rect(screen, "white", (x, y + height * 6, width, height))  # Place it just under hard
    # Start Button Function
    if start_button.collidepoint(pygame.mouse.get_pos()):
        start_button = pygame.draw.rect(screen, "green", (x, y, width, height))
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("start_button pressed")
    # Medium Difficulty Function
    elif medium_button.collidepoint(pygame.mouse.get_pos()):
        medium_button = pygame.draw.rect(screen, "green", (x, y + height * 2, width, height))
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("medium_button pressed")
    # Hard Difficulty Function
    elif hard_button.collidepoint(pygame.mouse.get_pos()):
        hard_button = pygame.draw.rect(screen, "green", (x, y + height * 4, width, height))
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("start_button pressed")
    elif exit_button.collidepoint(pygame.mouse.get_pos()):
        exit_button = pygame.draw.rect(screen, "green", (x, y + height * 6, width, height))
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("exit_button pressed")
    else:
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("no button pressed")
    pygame.display.flip()


def endgame(screen, s):
    power = pygame.movie('THE_POWER.gif')
    x, y = screen.get_size()
    screen.blit(pygame.transform.scale(power.get_surface(), (x, y)), (0, 0))
    pygame.display.flip()

    duration = time.time()
    while time.time() - duration < 5:
        power.play()
        pygame.time.wait(10)
        screen.blit(pygame.transform.scale(power.get_surface(), (x, y)), (0,0))
        pygame.display.flip()

