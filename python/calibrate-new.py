# This is adapted from Pedro Lopes' python calibration examples from his openEMSstim Toolkit
# You can find his original files here at https://github.com/PedroLopes/openEMSstim/tree/master/apps/python

# This program enables to send commands via USB to the openEMSstim board
# NOTE: To use it you will need to adjust the serial_port to whatever your operating system reported for the arduino connection (Windows will be something like COM3, check on Device Manager, while unix will be /dev/tty.usbsomething)

import sys
if len(sys.argv) >= 2:
    serial_port = sys.argv[1]
else:
    serial_port = "/dev/tty.usbserial-1410"
import os
from time import sleep
from pyEMS import openEMSstim
from pyEMS.EMSCommand import ems_command
from pyEMS.channel import Channel

if sys.version_info >= (3, 0):
    import configparser
else:
    import ConfigParser

# create a new openEMSstim board
my_ems_board = openEMSstim.openEMSstim(serial_port,19200) #adjust serial_port above, do not change baudrate if you don't know why

def ConfigSectionMap(config, section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

# starting default parameters
channels = []
channels.append(Channel(1,100,"right_hand_flexor"))
channels.append(Channel(2,100,"right_hand_extensor"))
command_history = []
last_duration = 1000

# settings for commands
not_ended = True
print_channel_config_next_time = False
command_list = sys.argv[0] + "choose of of the commands below:\n"
command_list += "\t[1|2] [0-100] [0-2000] e.g., 1 100 1000 (stimulates on channel 1, with 100% for 1000 ms)\n"
command_list += "\t[r] repeats the previous command\n"
command_list += "\t[d] to display current EMS parameters\n"
command_list += "\t[q] to quit\n"

def cli_clear():
    if not sys.platform.startswith('win'):
        print(chr(27) + "[2J")
    pass

def print_configuration(print_channel_config_next_time):
    for c in channels:
        print("-----------")
        print(c.name)
        print(c.intensity)
    print("-----------")
    if len(command_history) >= 1:
        print("Command history (last 4)")
        for i in range(1,5):
            if i <= len(command_history):
                print(command_history[len(command_history)-i])
    else:
        print("Note: command history empty")
    print_channel_config_next_time = False

def stimulate(ems_board, command, command_history, save_command_to_history, channel=None, intensity=None, duration=None):
    global channels
    if command:
        if save_command_to_history:
            command_history.append(command)
            channels[int(channel)-1].intensity = int(intensity)
            last_duration = duration
        else:
            command = command_history[-1]
        print("openEMSstim: stimulates now (raw command is:" + str(command) + ")")
        ems_board.send(command)
    else:
        print("Error: command invalid, hence not sent")


while (not_ended):
    cli_clear()
    if len(command_history) >= 1:
        print("Last command: " + str(command_history[-1]))
    if print_channel_config_next_time:
        print_configuration(print_channel_config_next_time)
    command = raw_input(command_list)
    command_tokens = command.split(" ")

    # direct command mode
    if len(command_tokens) == 3:
        command = ems_command(command_tokens[0],command_tokens[1],command_tokens[2])
        stimulate(my_ems_board, command, command_history, True, command_tokens[0], command_tokens[1], command_tokens[2])

    # repeat command mode or all single "string" commands
    elif len(command_tokens) == 1:

        # repeat last command mode
        if command_tokens[0] == "r":
            if len(command_history) >= 1:
                stimulate(my_ems_board, command, command_history, False)
            else:
                print("Warning: there is no last command to repeat (history empty)")

        # display channel configurations mode
        elif command_tokens[0] == "d":
            print_channel_config_next_time = True

        # quit program
        elif command_tokens[0] == "q":
            not_ended = False
