# DMOJ problem ecoo15r1p1, When You Eat Your Smarties

# I separate them into their color groups
# orange
# blue
# green
# yellow
# pink
# violet
# brown
# red

# my hand can hold a maximum of 7 Smarties: other colors not red * 13
# red one * 16

# The input will contain 10 test cases.
for dataset in range(10):
    colors = ''
    while True:
        smarties = input()
        if smarties == 'end of box':
            break
        colors = colors + ' ' + smarties

    num_orange  =   (colors.count('orange') + 6)    // 7
    num_blue    =   (colors.count('blue')   + 6)    // 7
    num_green   =   (colors.count('green')  + 6)    // 7
    num_yellow  =   (colors.count('yellow') + 6)    // 7
    num_pink    =   (colors.count('pink')   + 6)    // 7
    num_violet  =   (colors.count('violet') + 6)    // 7
    num_brown   =   (colors.count('brown')  + 6)    // 7
    num_red     =   (colors.count('red'))

    times_cost_orange   = num_orange    * 13
    times_cost_blue     = num_blue      * 13
    times_cost_green    = num_green     * 13
    times_cost_yellow   = num_yellow    * 13
    times_cost_pink     = num_pink      * 13
    times_cost_violet   = num_violet    * 13
    times_cost_brown    = num_brown     * 13
    times_cost_red      = num_red       * 16

    total_cost = 0
    total_cost = total_cost + times_cost_orange
    total_cost = total_cost + times_cost_blue
    total_cost = total_cost + times_cost_green
    total_cost = total_cost + times_cost_yellow
    total_cost = total_cost + times_cost_pink
    total_cost = total_cost + times_cost_violet
    total_cost = total_cost + times_cost_brown
    total_cost = total_cost + times_cost_red

    print(total_cost)