import random
import pygame
import pygame.gfxdraw
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
    pygame.display.flip()
    screen.fill((131, 75, 196))

    # These are the values for the start button, which the rest will adjust accordingly
    width = screen.get_width()/2
    height = screen.get_height()/10
    x = screen.get_width()/2 - width/2
    y = screen.get_height()/4 + height/2
    font = pygame.font.Font(None, 64)

    text = font.render("Rock Finds a Circle", True, (10, 10, 10))
    textpos = text.get_rect(centerx=screen.get_width() / 2, y=10)
    screen.blit(text, textpos)

    # Start Button (Easy Mode)
    text = font.render("Easy", True, (10, 10, 10))
    start_button = pygame.draw.rect(screen, "white", (x, y, width, height))
    textpos = text.get_rect(centerx=screen.get_width() / 2, y=y)
    screen.blit(text, textpos)

    text = font.render("Medium", True, (10, 10, 10))
    medium_button = pygame.draw.rect(screen, "yellow", (x, y + height * 2, width, height))  # Place it just under start
    textpos = text.get_rect(centerx=screen.get_width() / 2, y=y + height * 2)
    screen.blit(text, textpos)

    text = font.render("Hard", True, (10, 10, 10))
    hard_button = pygame.draw.rect(screen, "red", (x, y + height * 4, width, height))  # Place it just under med
    textpos = text.get_rect(centerx=screen.get_width() / 2, y=y + height * 4)
    screen.blit(text, textpos)
    # exit_button = pygame.draw.rect(screen, "white", (x, y + height * 6, width, height))  # Place it just under hard

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
    # elif exit_button.collidepoint(pygame.mouse.get_pos()):
    #    exit_button = pygame.draw.rect(screen, "green", (x, y + height * 6, width, height))
    #    if event.type == pygame.MOUSEBUTTONDOWN:
    #        print("exit_button pressed")

    else:
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("no button pressed")


def play_game(screen, s, color, p, hidden_circle):
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
        font = pygame.font.Font(None, 64)
        font_hue = p.get_player_distance(hidden_circle) * 255 / screen.get_width()
        font_color = (255 - font_hue, 0, font_hue)
        if p.get_player_distance(hidden_circle) > p.get_old_distance():
            text = font.render("Colder", True, (font_color))
            textpos = text.get_rect(centerx=screen.get_width() / 8, y=10)
            if p.get_player_distance(hidden_circle) > screen.get_width()/2:
                text = font.render("Ice Cold", True, (font_color))
            screen.blit(text, textpos)
        elif p.get_player_distance(hidden_circle) < p.get_old_distance():
            text = font.render("Warmer", True, (font_color))
            textpos = text.get_rect(centerx=screen.get_width() / 8, y=10)
            if p.get_player_distance(hidden_circle) < screen.get_width()/8:
                text = font.render("Very Hot", True, (font_color))
            screen.blit(text, textpos)
        if hidden_circle.colliderect(p.get_player_circle()):
            hidden_circle = pygame.draw.circle(screen, "blue", (hidden_circle.x, hidden_circle.y), 10, 1)
            pygame.display.flip()
            endgame(screen)
            break
        pygame.display.flip()
        screen.fill(color)
        p.draw_player_circle(hidden_circle, screen, s)


def easy_mode(screen, s):
    print("easy")  # Placeholder

    # Player Circle
    p = play.player_circle(screen.get_width()/2, screen.get_height()/2)
    p.set_player_width(screen.get_width()/4)
    p.set_player_height(screen.get_height()/4)
    # Hidden Circle
    x = random.random() * screen.get_width()
    y = random.random() * screen.get_height()
    hidden_circle = pygame.draw.circle(screen, "black", (x, y), 10, 1)
    while hidden_circle.colliderect(p.get_player_circle()):
        x = random.random() * screen.get_width()
        y = random.random() * screen.get_height()
        hidden_circle = pygame.draw.circle(screen, "black", (x, y), 10, 1)
    color = (125,181,124)
    play_game(screen, s, color, p, hidden_circle)


def med_mode(screen, s):
    print("mid")  # Placeholder
    p = play.player_circle(screen.get_width() / 2, screen.get_height() / 2)
    p.set_player_width(screen.get_width() / 8)
    p.set_player_height(screen.get_height() / 8)

    # Hidden Circle
    x = random.random() * screen.get_width()
    y = random.random() * screen.get_height()
    hidden_circle = pygame.draw.circle(screen, "black", (x, y), 10, 1)
    while hidden_circle.colliderect(p.get_player_circle()):
        x = random.random() * screen.get_width()
        y = random.random() * screen.get_height()
        hidden_circle = pygame.draw.circle(screen, "black", (x, y), 10, 1)

    color = (235, 226, 119)
    play_game(screen, s, color, p, hidden_circle)


def hard_mode(screen, s):
    print("hard")  # Placeholder
    p = play.player_circle(screen.get_width() / 2, screen.get_height() / 2)
    p.set_player_width(screen.get_width() / 16)
    p.set_player_height(screen.get_height() / 16)

    # Hidden Circle
    x = random.random() * screen.get_width()
    y = random.random() * screen.get_height()
    hidden_circle = pygame.draw.circle(screen, "black", (x, y), 10, 1)
    while hidden_circle.colliderect(p.get_player_circle()):
        x = random.random() * screen.get_width()
        y = random.random() * screen.get_height()
        hidden_circle = pygame.draw.circle(screen, "black", (x, y), 10, 1)
    color = (235, 137, 119)
    play_game(screen, s, color, p, hidden_circle)


def endgame(screen):

    # power = pygame.movie('THE_POWER.gif')
    # x, y = screen.get_size()
    # screen.blit(pygame.transform.scale(power.get_surface(), (x, y)), (0, 0))
    # pygame.display.flip()

    # duration = time.time()
    # while time.time() - duration < 5:
    #     power.play()
    #     pygame.time.wait(10)
    #     screen.blit(pygame.transform.scale(power.get_surface(), (x, y)), (0,0))
    #     pygame.display.flip()

        while True:
            font = pygame.font.Font(None, 64)
            text = font.render("You Did It!", True, (10, 10, 10))
            textpos = text.get_rect(centerx=screen.get_width() / 2, y=200)
            screen.blit(text, textpos)

            font = pygame.font.Font(None, 32)
            text = font.render("Click the Screen to Go Back to Menu", True, (10, 10, 10))
            textpos = text.get_rect(centerx=screen.get_width() / 2, y=250)
            screen.blit(text, textpos)
            pygame.display.flip()
            event = pygame.event.wait(1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                break
            if event.type == pygame.QUIT:
                break

