import pygame
import random
import psycopg2

# Connect to the PostgreSQL database
def connect_to_db():
    return psycopg2.connect(
        host='localhost',
        dbname='suppliers',
        user='postgres',
        password='motfootball23'
    )

# Function to create tables if they don't exist
def create_tables():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id SERIAL PRIMARY KEY,
                    username VARCHAR(255) UNIQUE
                )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS user_scores (
                    score_id SERIAL PRIMARY KEY,
                    user_id INT REFERENCES users(user_id),
                    score INT,
                    level INT
                )''')
    conn.commit()
    cur.close()
    conn.close()

# Function to check if a user exists
def user_exists(username):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT EXISTS(SELECT 1 FROM users WHERE username = %s)", (username,))
    exists = cur.fetchone()[0]
    cur.close()
    conn.close()
    return exists

# Function to insert a new user
def insert_user(username):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return user_id

# Function to get the current level of a user
def get_user_level(username):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT level FROM user_scores JOIN users ON user_scores.user_id = users.user_id WHERE username = %s ORDER BY score_id DESC LIMIT 1", (username,))
    level = cur.fetchone()
    cur.close()
    conn.close()
    return level

# Function to save user score
def save_user_score(username, score, level):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    user_id = cur.fetchone()[0]
    cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
    conn.commit()
    cur.close()
    conn.close()

# Function to run the snake game
def run_game(username):
    pygame.init()
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
    dis_width = 600
    dis_height = 400
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game by Edureka')
    clock = pygame.time.Clock()
    snake_block = 10
    initial_snake_speed = 15
    speed_increment = 2
    speed_level_increment = 4
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

    # Function to display message on screen
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])

    # Function to display user score and level
    def Your_score(score, level):
        value = score_font.render("Score: " + str(score) + "  Level: " + str(level), True, yellow)
        dis.blit(value, [0, 0])

    # Function to draw the snake
    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

    # Initialize game variables
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    level = 1
    score = 0
    snake_speed = initial_snake_speed

    # Main game loop
    while not game_over:

        # Game over screen
        while game_close:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        run_game(username)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if snake hits the wall
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(score, level)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 1

            # Check if level should be increased
            if score % speed_level_increment == 0:
                level += 1
                snake_speed += speed_increment

        clock.tick(snake_speed)

    # Save user score
    save_user_score(username, score, level)
    pygame.quit()
    quit()

# Main function
def main():
    # Create tables if they don't exist
    create_tables()

    # Prompt user to enter username
    username = input("Enter your username: ")

    # Check if user exists, if not insert user into the database
    if not user_exists(username):
        user_id = insert_user(username)
    else:
        user_id = get_user_level(username)

    # Run the snake game
    run_game(username)

# Run the main function
if __name__ == "__main__":
    main()
