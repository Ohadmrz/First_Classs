####### colored value --X--> no Background #############################################################################

def get_black(variable):
    return f"\033[2;30m{variable}\033[00m"

def get_black_bolt(variable):
    return f"\033[1;30m{variable}\033[00m"

def get_black_bolt_and_line(variable):
    return f"\033[4;30;01m{variable}\033[00m"



def get_gray(variable):
    return f"\033[90m{variable}\033[00m"



def get_red(variable):
    return f"\033[91m{variable}\033[00m"

def get_red_bolt(variable):
    return f"\033[1;31m{variable}\033[00m"

def get_red_bolt_brighter(variable):
    return f"\033[1;91m{variable}\033[00m"



def get_green(variable):
    return f"\033[92m{variable}\033[00m"

def get_green_bolt(variable):
    return f"\033[1;32m{variable}\033[0m"

def get_green_line(variable):
    return f"\033[4;32m{variable}\033[0m"



def get_yellow(variable):
    return f"\033[93m{variable}\033[00m"

def get_yellow_bolt(variable):
    return f"\033[1;93m{variable}\033[00m"

def get_yellow_line(variable):
    return f"\033[4;93m{variable}\033[00m"

def get_yellow_bolt_and_line(variable):
    return f"\033[4;93;01m{variable}\033[00m"

def get_yelow(variable):
    return f"\033[33m{variable}\033[00m"

def get_yelow_bolt(variable):
    return f"\033[1;33m{variable}\033[00m"

def get_yelow_line(variable):
    return f"\033[4;34;33m{variable}\033[00m"

def get_yelow_bolt_and_line(variable):
    return f"\033[4;33;01m{variable}\033[00m"



def get_blue(variable):
    return f"\033[34m{variable}\033[00m"

def get_blue_brighter(variable):
    return f"\033[94m{variable}\033[00m"

def get_blue_bolt(variable):
    return f"\033[1;34m{variable}\033[00m"

def get_blue_bolt_brighter(variable):
    return f"\033[1;94m{variable}\033[00m"

def get_blue_line(variable):
    return f"\033[4;34m{variable}\033[00m"

def get_blue_line_brighter(variable):
    return f"\033[4;94m{variable}\033[00m"

def get_blue_bolt_and_line(variable):
    return f"\033[4;34;01m {variable} \033[00m"

def get_blue_bolt_and_line_brighter(variable):
    return f"\033[4;94;01m {variable} \033[00m"






def get_purple_bolt(variable):
    return f"\033[1;35m{variable}\033[0m"

def get_purple_line(variable):
    return f"\033[4;35m{variable}\033[0m"

def get_purple_bolt_and_line(variable):
    return f"\033[4;35;01m{variable}\033[00m"

def get_purple_bolt_and_line_brighter(variable):
    return f"\033[4;95;01m{variable}\033[00m"



def get_light_blue(variable):
    return f"\033[96m{variable}\033[00m"

def get_light_blue_bolt(variable):
    return f"\033[4;96m\033[1;96m{variable}\033[00m"

def get_better_light_blue_bolt(variable):
    return f"\033[1;36m{variable}\033[00m"

def get_light_blue_line(variable):
    return f"\033[4;96m{variable}\033[00m"



def get_white(variable):
    return f"\033[97m{variable}\033[00m"

def get_white_bolt(variable):
    return f"\033[1;97m{variable}\033[00m"

def get_white_line(variable):
    return f"\033[4;97m{variable}\033[00m"



###### colored values --&-->  with Background ##########################################################################

def get_white_inside_gray(variable):
    return f"\033[01;91;100m{variable}\033[00m"

def get_white_inside_red(variable):
    return f"\033[101m{variable}\033[00m"

def get_white_inside_green(variable):
    return f"\033[102m{variable}\033[00m"

def get_white_inside_yellow(variable):
    return f"\033[103m{variable}\033[00m"

def get_white_inside_blue(variable):
    return f"\033[104m{variable}\033[00m"

def get_white_inside_pink(variable):
    return f"\033[105m{variable}\033[00m"

def get_white_inside_light_blue(variable):
    return f"\033[106m{variable}\033[00m"

def get_gray_inside_white(variable):
    return f"\033[107m{variable}\033[00m"

def get_yelow_inside_black(variable):
    return f"\033[1;33;40m{variable}\033[00m"

def get_black_inside_gray(variable):
    return f"\033[1;30;47m{variable}\033[00m"

def get_blue_inside_gray(variable):
    return f"\033[1;94;47{variable}\033[00m"

def get_blue_inside_black(variable):
    return f"\033[4;94;01m {variable} \033[00m"

if __name__ == '__main__':
    print(get_purple_bolt_and_line('avatar'.title()))
    print(get_purple_bolt_and_line_brighter('avatar'.title()))

    print(f" \033[1;35m Bright Magenta \033[0m         \033[1;30;47m ||| Koteret ||| \033[0m          \033[30m Black         \033[0m")
    print(f" \033[1;94;40m Bright Magenta \033[0m         \033[31m  Magenta \033[0m           \033[0;97;46m white \033[0m")

    print("\033[1;35;01m  All options for genres:  \033[00m")
    print("\033[2;95;01m  All options for genres:  \033[00m")
    print("\033[1;95;01m  All options for genres:  \033[00m")

    print(get_white('hdfgdrg'))
    print(get_white_bolt('hdfgdrg'))

    print(get_black('hdfgdrg'))
    # print(get_green_line('hdfgdrg'))
    #
    # print(get_yellow('hdfgdrg'))
    # print(get_yelow('hdfgdrg'))
    #
    # print(get_yellow_bolt('hdfgdrg'))
    # print(get_yelow_bolt('hdfgdrg'))
    #
    # print(get_yellow_line('hdfgdrg'))
    # print(get_yelow_line('hdfgdrg'))
    #
    # print(get_gray('hdfgdrg'))
    # print(get_black('hdfgdrg'))