from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
import board

keyboard = KMKKeyboard()

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.row_pins=(
    board.GP5,  # R0
    board.GP4,  # R1
    board.GP3,  # R2
    board.GP2,  # R3
    board.GP1,  # R4
    board.GP0,  # R5
)
keyboard.col_pins = (
    board.GP27, # C0
    board.GP26, # C1
    board.GP22, # C2
    board.GP28, # C3
    board.GP6, # C4
    board.GP7, # C5
    board.GP8, # C6
    board.GP9, # C7
    board.GP10, # C8
    board.GP11, # C9
    board.GP12, # C10
    board.GP13, # C11
    board.GP20, # C12
    board.GP19, # C13
    board.GP18, # C14
    board.GP14,  # C15
    board.GP15,  # C16
    board.GP17,  # C17
    board.GP16,  # C18
)

keyboard.keymap = [[

    # ---------------- Row 0 ----------------
    KC.ESC, 
    KC.F1, 
    KC.F2, 
    KC.F3, 
    KC.F4,
    KC.F5, 
    KC.F6, 
    KC.F7, 
    KC.F8, 
    KC.F9,
    KC.F10, 
    KC.F11, 
    KC.F12, 
    KC.INS, 
    KC.DEL,

    KC.PSCR, 
    KC.END, 
    KC.PGUP, 
    KC.PGDN,

    # ---------------- Row 1 ----------------
    KC.GRV, 
    KC.N1, 
    KC.N2, 
    KC.N3, 
    KC.N4,
    KC.N5, 
    KC.N6, 
    KC.N7, 
    KC.N8, 
    KC.N9, 
    KC.N0, 
    KC.MINS, 
    KC.EQL,
    KC.NO, 
    KC.BSPC, 

    KC.NUMLOCK, 
    KC.PSLS, 
    KC.PAST, 
    KC.PMNS,

    # ---------------- Row 2 ----------------
    KC.TAB,
    KC.NO,
    KC.Q,
    KC.W, 
    KC.E,
    KC.R,
    KC.T,
    KC.Y,
    KC.U,
    KC.I,
    KC.O,
    KC.P,
    KC.LBRC,
    KC.RBRC,
    KC.BSLS,

    KC.P7,
    KC.P8,
    KC.P9,
    KC.NO,

    # ---------------- Row 3 ----------------
    KC.CAPS,
    KC.NO,
    KC.A,
    KC.S,
    KC.D,
    KC.F,
    KC.G,
    KC.H,
    KC.J,
    KC.K,
    KC.L,
    KC.SCLN,
    KC.QUOT,
    KC.ENT,
    KC.NO,

    KC.P4,
    KC.P5,
    KC.P6,
    KC.PPLS,

    # ---------------- Row 4 ----------------
    KC.NO,
    KC.LSFT,
    KC.Z,
    KC.X,
    KC.C,
    KC.V,
    KC.B,
    KC.N,
    KC.M,
    KC.COMM,
    KC.DOT,
    KC.SLSH,
    KC.NO,
    KC.RSFT,
    KC.UP,

    KC.P1,
    KC.P2,
    KC.P3,
    KC.NO,

    # ---------------- Row 5 ----------------
    KC.LCTL,
    KC.LGUI,
    KC.NO,
    KC.LALT,
    KC.NO,
    KC.NO,
    KC.SPC,
    KC.NO,
    KC.NO,
    KC.NO,
    KC.RALT,
    KC.APP,
    KC.RCTL,

    KC.LEFT,
    KC.DOWN,
    KC.RIGHT,

    KC.P0,
    KC.PDOT,
    KC.PENT,
]]


if __name__ == '__main__':
    keyboard.go()