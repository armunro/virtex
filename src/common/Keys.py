# encoding=utf-8
# US keyboard layout
import os
import time
from tqdm import tqdm

KEY_A = 0x4  # a A
KEY_B = 0x5  # b B
KEY_C = 0x6  # c C
KEY_D = 0x7  # d D
KEY_E = 0x8  # e E
KEY_F = 0x9  # f F
KEY_G = 0xa  # g G
KEY_H = 0xb  # h H
KEY_I = 0xc  # i I
KEY_J = 0xd  # j J
KEY_K = 0xe  # k K
KEY_L = 0xf  # l L
KEY_M = 0x10  # m M
KEY_N = 0x11  # n N
KEY_O = 0x12  # o O
KEY_P = 0x13  # p P
KEY_Q = 0x14  # q Q
KEY_R = 0x15  # r R
KEY_S = 0x16  # s S
KEY_T = 0x17  # t T
KEY_U = 0x18  # u U
KEY_V = 0x19  # v V
KEY_W = 0x1a  # w W
KEY_X = 0x1b  # x X
KEY_Y = 0x1c  # y Y
KEY_Z = 0x1d  # z Z
KEY_1 = 0x1e  # 1 !
KEY_2 = 0x1f  # 2 @
KEY_3 = 0x20  # 3 #
KEY_4 = 0x21  # 4 $
KEY_5 = 0x22  # 5 %
KEY_6 = 0x23  # 6 ^
KEY_7 = 0x24  # 7 &
KEY_8 = 0x25  # 8 *
KEY_9 = 0x26  # 9 (
KEY_0 = 0x27  # 0 )
ENTER = 0x28  # Enter / Return
ESC = 0x29  # Escape
BACKSPACE = 0x2a  # Backspace
TAB = 0x2b  # Tab
SPACE = 0x2c  # Space
KEY_MINUS = 0x2d  # - _
KEY_EQUAL = 0x2e  # = +
OPEN_SQUARE_BRACKET = 0x2f  # [ {
CLOSE_SQUARE_BRACKET = 0x30  # ] }
BACKSLASH = 0x31  # \ |
SEMICOLON = 0x33  # ; :
SINGLE_QUOTE = 0x34  # ' "
BACKTICK = 0x35  # ` ~
COMMA = 0x36  # , <
DOT = 0x37  # . >
SLASH = 0x38  # / ?
CAPSLOCK = 0x39
F1 = 0x3a
F2 = 0x3b
F3 = 0x3c
F4 = 0x3d
F5 = 0x3e
F6 = 0x3f
F7 = 0x40
F8 = 0x41
F9 = 0x42
F10 = 0x43
F11 = 0x44
F12 = 0x45
PRINT_SCREEN = 0x46
SCROLL_LOCK = 0x47
PAUSE = 0x48
DELETE = 0x4c
KEY_RIGHT = 0x4f
KEY_LEFT = 0x50
KEY_DOWN = 0x51
KEY_UP = 0x52

LEFT_CTRL = 0b00000001
LEFT_SHIFT = 0b00000010
LEFT_ALT = 0b00000100
LEFT_GUI = 0b00001000
RIGHT_CTRL = 0b00010000
RIGHT_SHIFT = 0b00100000
RIGHT_ALT = 0b01000000
RIGHT_GUI = 0b10000000

RELEASE = bytes([0] * 8)

CHARS = {
    'a': bytes([0, 0, KEY_A, *[0] * 5]), 'A': bytes([LEFT_SHIFT, 0, KEY_A, *[0] * 5]),
    'b': bytes([0, 0, KEY_B, *[0] * 5]), 'B': bytes([LEFT_SHIFT, 0, KEY_B, *[0] * 5]),
    'c': bytes([0, 0, KEY_C, *[0] * 5]), 'C': bytes([LEFT_SHIFT, 0, KEY_C, *[0] * 5]),
    'd': bytes([0, 0, KEY_D, *[0] * 5]), 'D': bytes([LEFT_SHIFT, 0, KEY_D, *[0] * 5]),
    'e': bytes([0, 0, KEY_E, *[0] * 5]), 'E': bytes([LEFT_SHIFT, 0, KEY_E, *[0] * 5]),
    'f': bytes([0, 0, KEY_F, *[0] * 5]), 'F': bytes([LEFT_SHIFT, 0, KEY_F, *[0] * 5]),
    'g': bytes([0, 0, KEY_G, *[0] * 5]), 'G': bytes([LEFT_SHIFT, 0, KEY_G, *[0] * 5]),
    'h': bytes([0, 0, KEY_H, *[0] * 5]), 'H': bytes([LEFT_SHIFT, 0, KEY_H, *[0] * 5]),
    'i': bytes([0, 0, KEY_I, *[0] * 5]), 'I': bytes([LEFT_SHIFT, 0, KEY_I, *[0] * 5]),
    'j': bytes([0, 0, KEY_J, *[0] * 5]), 'J': bytes([LEFT_SHIFT, 0, KEY_J, *[0] * 5]),
    'k': bytes([0, 0, KEY_K, *[0] * 5]), 'K': bytes([LEFT_SHIFT, 0, KEY_K, *[0] * 5]),
    'l': bytes([0, 0, KEY_L, *[0] * 5]), 'L': bytes([LEFT_SHIFT, 0, KEY_L, *[0] * 5]),
    'm': bytes([0, 0, KEY_M, *[0] * 5]), 'M': bytes([LEFT_SHIFT, 0, KEY_M, *[0] * 5]),
    'n': bytes([0, 0, KEY_N, *[0] * 5]), 'N': bytes([LEFT_SHIFT, 0, KEY_N, *[0] * 5]),
    'o': bytes([0, 0, KEY_O, *[0] * 5]), 'O': bytes([LEFT_SHIFT, 0, KEY_O, *[0] * 5]),
    'p': bytes([0, 0, KEY_P, *[0] * 5]), 'P': bytes([LEFT_SHIFT, 0, KEY_P, *[0] * 5]),
    'q': bytes([0, 0, KEY_Q, *[0] * 5]), 'Q': bytes([LEFT_SHIFT, 0, KEY_Q, *[0] * 5]),
    'r': bytes([0, 0, KEY_R, *[0] * 5]), 'R': bytes([LEFT_SHIFT, 0, KEY_R, *[0] * 5]),
    's': bytes([0, 0, KEY_S, *[0] * 5]), 'S': bytes([LEFT_SHIFT, 0, KEY_S, *[0] * 5]),
    't': bytes([0, 0, KEY_T, *[0] * 5]), 'T': bytes([LEFT_SHIFT, 0, KEY_T, *[0] * 5]),
    'u': bytes([0, 0, KEY_U, *[0] * 5]), 'U': bytes([LEFT_SHIFT, 0, KEY_U, *[0] * 5]),
    'v': bytes([0, 0, KEY_V, *[0] * 5]), 'V': bytes([LEFT_SHIFT, 0, KEY_V, *[0] * 5]),
    'w': bytes([0, 0, KEY_W, *[0] * 5]), 'W': bytes([LEFT_SHIFT, 0, KEY_W, *[0] * 5]),
    'x': bytes([0, 0, KEY_X, *[0] * 5]), 'X': bytes([LEFT_SHIFT, 0, KEY_X, *[0] * 5]),
    'y': bytes([0, 0, KEY_Y, *[0] * 5]), 'Y': bytes([LEFT_SHIFT, 0, KEY_Y, *[0] * 5]),
    'z': bytes([0, 0, KEY_Z, *[0] * 5]), 'Z': bytes([LEFT_SHIFT, 0, KEY_Z, *[0] * 5]),
    '1': bytes([0, 0, KEY_1, *[0] * 5]), '!': bytes([LEFT_SHIFT, 0, KEY_1, *[0] * 5]),
    '2': bytes([0, 0, KEY_2, *[0] * 5]), '@': bytes([LEFT_SHIFT, 0, KEY_2, *[0] * 5]),
    '3': bytes([0, 0, KEY_3, *[0] * 5]), '#': bytes([LEFT_SHIFT, 0, KEY_3, *[0] * 5]),
    '4': bytes([0, 0, KEY_4, *[0] * 5]), '$': bytes([LEFT_SHIFT, 0, KEY_4, *[0] * 5]),
    '5': bytes([0, 0, KEY_5, *[0] * 5]), '%': bytes([LEFT_SHIFT, 0, KEY_5, *[0] * 5]),
    '6': bytes([0, 0, KEY_6, *[0] * 5]), '^': bytes([LEFT_SHIFT, 0, KEY_6, *[0] * 5]),
    '7': bytes([0, 0, KEY_7, *[0] * 5]), '&': bytes([LEFT_SHIFT, 0, KEY_7, *[0] * 5]),
    '8': bytes([0, 0, KEY_8, *[0] * 5]), '*': bytes([LEFT_SHIFT, 0, KEY_8, *[0] * 5]),
    '9': bytes([0, 0, KEY_9, *[0] * 5]), '(': bytes([LEFT_SHIFT, 0, KEY_9, *[0] * 5]),
    '0': bytes([0, 0, KEY_0, *[0] * 5]), ')': bytes([LEFT_SHIFT, 0, KEY_0, *[0] * 5]),
    '\n': bytes([0, 0, ENTER, *[0] * 5]),
    'ESC': bytes([0, 0, ESC, *[0] * 5]),
    'BACKSPACE': bytes([0, 0, BACKSPACE, *[0] * 5]),
    '\t': bytes([0, 0, TAB, *[0] * 5]),
    ' ': bytes([0, 0, SPACE, *[0] * 5]),
    '-': bytes([0, 0, KEY_MINUS, *[0] * 5]), '_': bytes([LEFT_SHIFT, 0, KEY_MINUS, *[0] * 5]),
    '=': bytes([0, 0, KEY_EQUAL, *[0] * 5]), '+': bytes([LEFT_SHIFT, 0, KEY_EQUAL, *[0] * 5]),
    '[': bytes([0, 0, OPEN_SQUARE_BRACKET, *[0] * 5]), '{': bytes([LEFT_SHIFT, 0, OPEN_SQUARE_BRACKET, *[0] * 5]),
    ']': bytes([0, 0, CLOSE_SQUARE_BRACKET, *[0] * 5]), '}': bytes([LEFT_SHIFT, 0, CLOSE_SQUARE_BRACKET, *[0] * 5]),
    '\\': bytes([0, 0, BACKSLASH, *[0] * 5]), '|': bytes([LEFT_SHIFT, 0, BACKSLASH, *[0] * 5]),
    ';': bytes([0, 0, SEMICOLON, *[0] * 5]), ':': bytes([LEFT_SHIFT, 0, SEMICOLON, *[0] * 5]),
    '\'': bytes([0, 0, SINGLE_QUOTE, *[0] * 5]), '"': bytes([LEFT_SHIFT, 0, SINGLE_QUOTE, *[0] * 5]),
    '`': bytes([0, 0, BACKTICK, *[0] * 5]), '~': bytes([LEFT_SHIFT, 0, BACKTICK, *[0] * 5]),
    ',': bytes([0, 0, COMMA, *[0] * 5]), '<': bytes([LEFT_SHIFT, 0, COMMA, *[0] * 5]),
    '.': bytes([0, 0, DOT, *[0] * 5]), '>': bytes([LEFT_SHIFT, 0, DOT, *[0] * 5]),
    '/': bytes([0, 0, SLASH, *[0] * 5]), '?': bytes([LEFT_SHIFT, 0, SLASH, *[0] * 5]),

    'F1': bytes([0, 0, F1, *[0] * 5]),
    'F2': bytes([0, 0, F2, *[0] * 5]),
    'F3': bytes([0, 0, F3, *[0] * 5]),
    'F4': bytes([0, 0, F4, *[0] * 5]),
    'F5': bytes([0, 0, F5, *[0] * 5]),
    'F6': bytes([0, 0, F6, *[0] * 5]),
    'F7': bytes([0, 0, F7, *[0] * 5]),
    'F8': bytes([0, 0, F8, *[0] * 5]),
    'F9': bytes([0, 0, F9, *[0] * 5]),
    'F10': bytes([0, 0, F10, *[0] * 5]),
    'F11': bytes([0, 0, F11, *[0] * 5]),
    'F12': bytes([0, 0, F12, *[0] * 5]),
}
HID_FILENAME = '/dev/hidg0'


def type_string(s):
    out_file = open(HID_FILENAME, mode='rb+')
    for c in s:
        if c in CHARS.keys():
            out_file.write(CHARS[c])
            out_file.write(RELEASE)
    out_file.close()


def press(inp_rpt: bytes, release=True):
    with open(HID_FILENAME, mode='rb+') as out_file:
        out_file.write(inp_rpt)
        if release:
            out_file.write(RELEASE)


def open_run():
    press(bytes([LEFT_GUI, 0, KEY_R, *[0] * 5]))


def launch_app(path):
    open_run()
    time.sleep(0.2)
    type_string(f'{path}\n')


def open_start():
    press(bytes([LEFT_GUI, 0, *[0] * 5]))


def open_search(search, enter=False):
    open_start()
    time.sleep(0.25)
    type_string(search + ' ')


def save_file(filename: str, gui_wait=0.5):
    press(bytes([LEFT_CTRL, 0, KEY_S, *[0] * 5]))
    time.sleep(gui_wait)
    type_string(filename)
    press(bytes([0, 0, ENTER, *[0] * 5]))


def line_count(path):
    assert os.path.exists(path)

    num_lines = 0
    with open(path) as f:
        for line in f:
            num_lines += 1

    return num_lines


def type_file_to_notepad(filepath: str, filename=None, close=True, gui_wait=0.5):
    assert os.path.exists(filepath)
    # open notepad
    notepad()
    # wait
    time.sleep(gui_wait)
    # get line count for progress bar
    num_lines = line_count(filepath)
    # open file to read content
    with open(filepath, encoding='utf-8') as inp_file:
        # use generator with tqdm for progress visualization
        for line in tqdm(inp_file, total=num_lines):
            type_string(line)
    if filename is None:
        filename = os.path.basename(filepath)
    save_file(filename)
    if close:
        time.sleep(gui_wait)
        press(bytes([LEFT_ALT, 0, F4, *[0] * 5]))
