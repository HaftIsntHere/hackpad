# You import all the IOs of your board
import board
import busio

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.oled import Oled, OledDisplayMode, OledReactionType, OledData

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Add encoder support
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Define your pins here!
PINS = [board.D7, board.D8, board.D9, board.D10]

# Configure the encoder
encoder_handler.pins = (
    (board.D2, board.D1, board.D4, False),  # (pin_a, pin_b, pin_button, is_inverted)
)

# Define encoder actions
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),),  # Volume up/down and mute
]

# Configure OLED display
i2c = busio.I2C(board.SCL, board.SDA)
oled_ext = Oled(
    OledData(
        corner_one={0: OledReactionType.STATIC, 1: ["HAFT"]},
        corner_two={0: OledReactionType.LAYER, 1: ["Layer: ", "Layer: ", "Layer: ", "Layer: "]},
        corner_three={0: OledReactionType.LAYER, 1: ["1", "2", "3", "4"]},
        corner_four={0: OledReactionType.STATIC, 1: ["SIGN"]},
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
)
keyboard.extensions.append(oled_ext)

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.F13, KC.F14, KC.F15, KC.F16]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()