import random
import pygame
import pygame.gfxdraw
import time
import player as play

'''
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
    
    the_drive = pygame.cursors.compile(THE_DRIVE,
                               black='⢸',
                               white= '⣿', xor='o')
    pygame.mouse.set_cursor(the_drive)
    
    happy = pygame.cursors.compile(happy_face, black='0', white='1', xor='o')
    pygame.mouse.set_cursor(happy)
'''


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
            easy_mode(screen, s)

    # Medium Difficulty Function
    elif medium_button.collidepoint(pygame.mouse.get_pos()):
        medium_button = pygame.draw.rect(screen, "green", (x, y + height * 2, width, height))
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("medium_button pressed")
            med_mode(screen, s)

    # Hard Difficulty Function
    elif hard_button.collidepoint(pygame.mouse.get_pos()):
        hard_button = pygame.draw.rect(screen, "green", (x, y + height * 4, width, height))
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("hard_button pressed")
            hard_mode(screen, s)

    # Exit Button Function
    elif exit_button.collidepoint(pygame.mouse.get_pos()):
        exit_button = pygame.draw.rect(screen, "green", (x, y + height * 6, width, height))
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("exit_button pressed")
    else:
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("no button pressed")
    pygame.display.flip()


def play_game(screen, s, p, hidden_circle):
    while True:
        event = pygame.event.wait(1)
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                p.set_player_accx(-0.5)
            elif event.key == pygame.K_RIGHT:
                p.set_player_accx(0.5)
            elif event.key == pygame.K_UP:
                p.set_player_accy(-0.5)
            elif event.key == pygame.K_DOWN:
                p.set_player_accy(0.5)
            elif event.key == pygame.K_ESCAPE or event.unicode == "q":
                break
        if event.type == pygame.QUIT:
            break
        p.move_player_circle()

        if hidden_circle.colliderect(p.get_player_circle()):
            hidden_circle = pygame.draw.circle(screen, "blue", (hidden_circle.x, hidden_circle.y), 10, 1)
            pygame.display.flip()
            endgame(screen, s)
            break
        pygame.display.flip()
        p.draw_player_circle(hidden_circle, screen, s)


def easy_mode(screen, s):
    print("easy")  # Placeholder

    # Player Circle
    p = play.player_circle(250, 250)
    p.set_player_width(200)
    p.set_player_height(175)
    # Hidden Circle
    x = random.random() * 250
    y = random.random() * 250
    hidden_circle = pygame.draw.circle(screen, "black", (x, y), 10, 1)
    while(hidden_circle.colliderect(p.get_player_circle())):
        x = random.random() * 250
        y = random.random() * 250
        hidden_circle = pygame.draw.circle(screen, "black", (x, y), 10, 1)
    play_game(screen, s, p, hidden_circle)


def med_mode(screen, s):
    print("mid")  # Placeholder
    p = play.player_circle(250, 250)
    p.set_player_width(100)
    p.set_player_height(87.5)

    # Hidden Circle
    x = random.random() * 250
    y = random.random() * 250
    hidden_circle = pygame.draw.circle(screen, "black", (x, y), 10, 1)
    while (hidden_circle.colliderect(p.get_player_circle())):
        x = random.random() * 250
        y = random.random() * 250
        hidden_circle = pygame.draw.circle(screen, "black", (x, y), 10, 1)
    play_game(screen, s, p, hidden_circle)


def hard_mode(screen, s):
    print("hard")  # Placeholder
    p = play.player_circle(250, 250)
    p.set_player_width(50)
    p.set_player_height(43.75)

    # Hidden Circle
    x = random.random() * 250
    y = random.random() * 250
    hidden_circle = pygame.draw.circle(screen, "black", (x, y), 10, 1)
    while (hidden_circle.colliderect(p.get_player_circle())):
        x = random.random() * 250
        y = random.random() * 250
        hidden_circle = pygame.draw.circle(screen, "black", (x, y), 10, 1)
    play_game(screen, s, p, hidden_circle)


def endgame(screen, s):
    '''
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
    '''
    print("You did it!")
    pygame.time.delay(5000)

