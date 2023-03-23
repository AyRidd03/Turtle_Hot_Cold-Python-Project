import random
import pygame
import pygame.gfxdraw
import player as play


def set_background(screen):  # Sorry Debbie
    THE_DRIVE = (
        "What's the key to success? The key is, there is no key.",
        "Be humble, hungry, and the hardest worker in any room.",
        "With drive and a bit of talent you can move mountains.",
        "Don’t be afraid to be ambitious about your goals.",
        "Hard work never stops. Neither should your dreams.",
        "If something stands between you and your success,",
        "MOVE IT! Never be denied.",
        "The wall! Your success is on the other side.",
        "Can’t jump over it or go around it. You know what to do.",
        "Not only do I think being nice and kind is easy,",
        "but being kind, in my opinion is important.",
        "Failure's not an option. It's just a step.",
        "You don’t need directions, just point yourself to the top and go!",
        "When life puts you in tough situations,",
        "don’t say ‘Why me?’ just say ‘Try me’.",
        "Success isn’t overnight.",
        "It’s when every day you get a little better than the day before.",
        "It all adds up. There is no substitute for hard work.",
        "Always be humble and hungry. Blood, sweat and respect.",
        "First two you give, last one you earn.",
        "When you walk up to opportunities door, don’t knock it.",
        "Kick that b!tch in, smile and introduce yourself.",
        "In 1995 I had $7 bucks in my pocket and I knew two things:",
        "I’m broke as hell and one day I won’t be.",
        "The men I idolized built their bodies and became somebody",
        "– like Sylvester Stallone and Arnold Schwarzenegger –",
        "and I thought, ‘That can be me.’ So I started working out.",
        "The funny thing is I didn’t realize back then that I was having a defining moment.",
        "I like to use the hard times in the past to motivate me today.",
        "Success isn’t always about ‘greatness’, it’s about consistency.",
        "Consistent, hard work gains success.",
        "The first step to achieving your goal, is to take a moment to respect your goal.",
        "Know what it means to you to achieve it.",
        "All success begins with self-discipline. It starts with you.",
        "Success at anything will always come down to this: focus and effort.",
        "And we control both. I'll never, ever be full. I'll always be hungry.",
        "Obviously, I'm not talking about food.",
        "Growing up, I had nothing for such a long time.",
        "Someone told me a long time ago, and I've never forgotten it,",
        "Once you've ever been hungry, really, really hungry, then you'll never, ever be full.",
        "Think back five years ago. Think of where you’re at today.",
        "Think ahead five years and what you want to accomplish. Be unstoppable.",
        "There's no substitute for hard work and getting out there and busting your butt at whatever it is.",
        "Nothing comes easy. You can overcome so much just through hard, focused work.",
        "The single most powerful thing I can be is to be myself.",
        "I grew up where, when a door closed, a window didn't open.",
        "The only thing I had was cracks. I'd do everything to get through those cracks",
        "- scratch, claw, bite, push, bleed. Now the opportunity is here.",
        "The door is wide open, and it's as big as a garage.")

    font = pygame.font.Font(None, int(screen.get_width()/64))
    count = 0
    for i in THE_DRIVE:
        text = font.render(i, True, (255, 202, 0))
        textpos = text.get_rect(x=screen.get_width() / 64, y=int(count*screen.get_height()/48))
        screen.blit(text, textpos)
        count += 1


def menu_choices(screen, s, event, easy, med, hard):
    pygame.display.flip()
    screen.fill((131, 75, 196))
    set_background(screen)

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

    # Start Button Function
    if start_button.collidepoint(pygame.mouse.get_pos()):
        start_button = pygame.draw.rect(screen, "green", (x, y, width, height))
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("start_button pressed")
            easy_mode(screen, s, easy)

    # Medium Difficulty Function
    elif medium_button.collidepoint(pygame.mouse.get_pos()):
        medium_button = pygame.draw.rect(screen, "green", (x, y + height * 2, width, height))
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("medium_button pressed")
            med_mode(screen, s, med)

    # Hard Difficulty Function
    elif hard_button.collidepoint(pygame.mouse.get_pos()):
        hard_button = pygame.draw.rect(screen, "green", (x, y + height * 4, width, height))
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("hard_button pressed")
            hard_mode(screen, s, hard)
    else:
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("no button pressed")


def play_game(screen, s, color, p, hidden_circle, record):
    hot_cold_y = int(screen.get_height()/64*8)
    hot_cold_x = int(screen.get_width()/16)
    timer_x = int(screen.get_width()/32)
    timer_y = int(screen.get_height()/64*4)
    clock = pygame.time.Clock()
    time = 0
    while True:
        clock.tick(60000)  # 60 fps
        time += 0.01
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
        p.move_player_circle(screen)
        font = pygame.font.Font(None, 64)
        font_hue = p.get_player_distance(hidden_circle) * 255 / screen.get_width()
        font_color = (255 - font_hue, 0, font_hue)
        if p.get_player_distance(hidden_circle) > p.get_old_distance():
            text = font.render("Colder", True, font_color)
            textpos = text.get_rect(x=hot_cold_x, y=hot_cold_y)
            if p.get_player_distance(hidden_circle) > screen.get_width()/2:
                text = font.render("Ice Cold", True, font_color)
            screen.blit(text, textpos)
        elif p.get_player_distance(hidden_circle) < p.get_old_distance():
            text = font.render("Warmer", True, font_color)
            textpos = text.get_rect(x=hot_cold_x, y=hot_cold_y)
            if p.get_player_distance(hidden_circle) < screen.get_width()/8:
                text = font.render("Very Hot", True, font_color)
            screen.blit(text, textpos)
        if hidden_circle.colliderect(p.get_player_circle()):
            hidden_circle = pygame.draw.circle(screen, "blue", (hidden_circle.x, hidden_circle.y), 10, 1)
            pygame.display.flip()
            endgame(screen, time, record, p)
            break
        text = font.render(f"Time : {time:{4}.{10}}", True, (10, 10, 10))
        textpos = text.get_rect(x=timer_x, y=timer_y)
        screen.blit(text, textpos)
        pygame.display.flip()
        screen.fill(color)
        p.draw_player_circle(hidden_circle, screen, s)


def easy_mode(screen, s, record):
    print("easy")  # Placeholder
    # Player Circle
    p = play.PlayerCircle(screen.get_width() / 2, screen.get_height() / 2)
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
    color = (125, 181, 124)
    play_game(screen, s, color, p, hidden_circle, record)


def med_mode(screen, s, record):
    print("mid")  # Placeholder
    p = play.PlayerCircle(screen.get_width() / 2, screen.get_height() / 2)
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
    play_game(screen, s, color, p, hidden_circle, record)


def hard_mode(screen, s, record):
    print("hard")  # Placeholder
    p = play.PlayerCircle(screen.get_width() / 2, screen.get_height() / 2)
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
    play_game(screen, s, color, p, hidden_circle, record)


def endgame(screen, time, record, player):

    if time < record.get_record():
        record.set_record(time)

    while True:
        y = 200
        # Victory Statement
        font = pygame.font.Font(None, 64)
        text = font.render("You Did It!", True, (10, 10, 10))
        textpos = text.get_rect(centerx=screen.get_width() / 2, y=y)
        screen.blit(text, textpos)
        # Time
        if time == record.get_record():
            text = font.render(f"NEW RECORD!!! {record.get_record():{10}.{4}}", True, (10, 10, 10))
            y += 50
            textpos = text.get_rect(centerx=screen.get_width() / 2, y=y)
            screen.blit(text, textpos)

        else:
            text = font.render(f"Record is  {record.get_record():{10}.{4}}", True, (10, 10, 10))
            y += 50
            textpos = text.get_rect(centerx=screen.get_width() / 2, y=y)
            screen.blit(text, textpos)
            text = font.render(f"Your Time  {time:{10}.{4}}", True, (10, 10, 10))
            y += 50
            textpos = text.get_rect(centerx=screen.get_width() / 2, y=y)
            screen.blit(text, textpos)
        # Distance Traveled
        text = font.render(f"You Traveled  {player.get_travel_distance():.2f} Pixels :)", True, (10, 10, 10))
        y += 50
        textpos = text.get_rect(centerx=screen.get_width() / 2, y=y)
        screen.blit(text, textpos)
        # Instructions
        font = pygame.font.Font(None, 32)
        text = font.render("Click the Screen to Go Back to Menu", True, (10, 10, 10))
        y += 50
        textpos = text.get_rect(centerx=screen.get_width() / 2, y=y)
        screen.blit(text, textpos)
        pygame.display.flip()
        event = pygame.event.wait(1)
        if event.type == pygame.MOUSEBUTTONDOWN:
            break
        if event.type == pygame.QUIT:
            break


class Record:
    def __init__(self):
        self.record = 999.0

    def set_record(self, value):
        self.record = value

    def get_record(self):
        return self.record
