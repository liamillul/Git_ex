import pygame
import BubblesGrid
import Bubble
import consts
import Screen
import Stack

state = {
    "original_arrow": Screen.create_arrow(consts.ARROW_IMG),
    "rotated_arrow": None,
    "is_bubble_fired": False,
    "bubbles_popping": [],
    "turns_left_to_add_row": consts.NUM_OF_TURNS_TO_ADD_ROW,
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
    "bullet_bubble": None,
    "bubble_direction": None,
    "mouse_angle": None
}

state["rotated_arrow"] = state["original_arrow"]


def main():
    pygame.init()
    BubblesGrid.create()
    Stack.create(consts.STACK_SIZE)

    while state["is_window_open"]:

        handle_user_events()

        if state["is_bubble_fired"]:

            move_bubble()

            if Bubble.should_stop(BubblesGrid.bubbles_grid,
                                  state["bullet_bubble"]):
                state["is_bubble_fired"] = False

                new_bubble_location = BubblesGrid.find_bubble_location_in_grid(
                    state["bullet_bubble"])
                BubblesGrid.put_bubble_in_grid(state["bullet_bubble"],
                                               new_bubble_location)

                same_color_cluster = BubblesGrid.get_same_color_cluster(
                    new_bubble_location,
                    state["bullet_bubble"]["color"],
                    [])

                if BubblesGrid.should_bubbles_pop(same_color_cluster):
                    state["bubbles_popping"] = \
                        BubblesGrid.pop_bubbles(same_color_cluster)

                # The counter counts only if bubbles weren't popped
                else:
                    state["turns_left_to_add_row"] -= 1

                    if state["turns_left_to_add_row"] == 0:
                        BubblesGrid.add_new_line()

                        # Resetting the counter
                        state["turns_left_to_add_row"] = \
                            consts.NUM_OF_TURNS_TO_ADD_ROW

                remove_isolated_bubbles()
                BubblesGrid.set_one_empty_line()
                remove_extinct_colors(consts.bubble_colors)
                Stack.add_bubble(Stack.get_length())

                if is_lose():
                    state["state"] = consts.LOSE_STATE
                elif is_win():
                    state["state"] = consts.WIN_STATE

        Screen.draw_game(state)


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.MOUSEMOTION:
            rotate_arrow()

        elif event.type == pygame.MOUSEBUTTONDOWN and \
                not state["is_bubble_fired"] and \
                not state["bubbles_popping"]:
            fire_bubble()


def rotate_arrow():
    state["mouse_angle"] = Screen.calc_mouse_angle(pygame.mouse.get_pos())
    state["rotated_arrow"] = pygame.transform.rotate(state["original_arrow"],
                                                     state["mouse_angle"] - 90)


def fire_bubble():
    state["is_bubble_fired"] = True
    state["bubble_direction"] = \
        Bubble.calc_direction(state["mouse_angle"])
    state["bullet_bubble"] = Stack.remove_first()


def move_bubble():
    Bubble.move_in_direction(state["bullet_bubble"], state["bubble_direction"])

    if Bubble.is_colliding_with_wall(state["bullet_bubble"]):
        state["bubble_direction"] = (state["bubble_direction"][0] * (-1), state["bubble_direction"][1])


def remove_isolated_bubbles():
    isolated_bubbles_locations = BubblesGrid.find_isolated_bubbles()

    if len(isolated_bubbles_locations) > 0:
        state["bubbles_popping"] += \
            BubblesGrid.pop_bubbles(isolated_bubbles_locations)


# -----------------------------------------------------------------------------
# ---------------------------------your code-----------------------------------
# -----------------------------------------------------------------------------

def remove_extinct_colors(bubble_colors):  # the colors are in tuples, and numbers in the tuples
    colors_in_stack_list = Stack.colors_in_stack()
    colors_list_grid = BubblesGrid.colors_in_grid()
    for color in bubble_colors:
        if color not in colors_in_stack_list and color not in colors_list_grid:
            bubble_colors.remove(color)
    pass


def is_lose():
    rows_index_list = []
    for row_i in range(len(BubblesGrid.bubbles_grid)):  # find the last row index
        rows_index_list.append(row_i)  # make a list of all the indexes
    last_row_index = rows_index_list[-1]
    bubbles_rows_num = last_row_index
    if bubbles_rows_num >= consts.NUM_OF_LINES_LOSE:
        return True
    else:
        return False
    pass


def is_win():
    color_list = []
    for row in range(len(BubblesGrid.bubbles_grid) - 1):
        for col in range(len(BubblesGrid.bubbles_grid[row])):
            bubble = BubblesGrid.bubbles_grid[row][col]
            if bubble["color"] != "EMPTY":
                color_list.append(0)
            else:
                color_list.append("yes")
    if 0 in color_list:
        return False
    else:
        return True
    pass


# -----------------------------------------------------------------------------
# ------------------------------your code end----------------------------------
# -----------------------------------------------------------------------------

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
