import copy

import tkinter

import tkinter.ttk

from random import randrange, randint, shuffle

from threading import Thread

import json

from pathlib import Path

from time import sleep

import keyboard

from pygame import mixer


class Settings:
    def __init__(self):
        fp = open("data/profile/settings.txt", mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        sett = json.loads(fp.read())
        fp.close()

        self.extra_sound_module = sett['extra_sound']

        if sett['def_theme'] is True:
            self.bg_col = sett['theme_default']['bg_col']
            self.bg_col2 = sett['theme_default']['bg_col2']
            self.bg_col3 = sett['theme_default']['bg_col3']
            self.fg_col = sett['theme_default']['fg_col']
            self.fg_col_d = sett['theme_default']['fg_col_d']
            self.fg_col2 = sett['theme_default']['fg_col2']
            self.fg_col_cont = sett['theme_default']['fg_col_cont']
            self.fg_col_dang = sett['theme_default']['fg_col_dang']
            self.fg_col_good = sett['theme_default']['fg_col_good']
        else:
            self.bg_col = sett['theme_custom']['bg_col']
            self.bg_col2 = sett['theme_custom']['bg_col2']
            self.bg_col3 = sett['theme_custom']['bg_col3']
            self.fg_col = sett['theme_custom']['fg_col']
            self.fg_col_d = sett['theme_custom']['fg_col_d']
            self.fg_col2 = sett['theme_custom']['fg_col2']
            self.fg_col_cont = sett['theme_custom']['fg_col_cont']
            self.fg_col_dang = sett['theme_custom']['fg_col_dang']
            self.fg_col_good = sett['theme_custom']['fg_col_good']

        self.resolution = (int(sett['resolution'][0]), int(sett['resolution'][1]))

        self.gui_data = sett['gui_data']

        self.sound_levels = sett['sound_levels']

        self.ed_start_time = float(sett['ed_start_time'])
        self.ed_log_folder = sett['ed_log_folder']
        self.data_hook_time = float(sett['data_hook_time'])
        self.log_files_len = int(sett['log_files_len'])

        self.action_key = sett['action_key']
        self.task_key = sett['task_key']
        self.message_test_key = sett['message_test_key']
        self.minigame_test_key = sett['minigame_test_key']

        fp = open("data/lang/" + sett['language'] + ".txt", mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        self.lang = json.loads(fp.read())['miex']
        fp.close()

        del sett

    def save_settings(self):

        fp = open("data/profile/settings.txt", mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        sett = json.loads(fp.read())
        fp.close()
        sett['log_files_len'] = self.log_files_len

        w_data = json.dumps(sett, ensure_ascii=False, indent=4)
        fp = open("data/profile/settings.txt", mode='w', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        fp.write(w_data)
        fp.close()


sett = Settings()

bor = ((sett.resolution[0] // 12) * 8) // 100
tx_bor = bor // 2

print("overlay start")
root = tkinter.Tk()
root.config(cursor="none")
root.title("MIEX olay")
root.configure(background='black')
root.wm_attributes('-transparentcolor', 'black')
root.wm_attributes('-topmost', True)
root.geometry(str(sett.resolution[0]) + "x" + str(sett.resolution[1]))
root.resizable(False, False)
root.overrideredirect(True)
root.lift()

s = tkinter.ttk.Style()
s.theme_use('clam')

# стили элементов


s.configure('Custom_olay.TFrame', background="black", bordercolor="black", lightcolor="black", darkcolor="black", relief='groove')

s.configure('Custom_olay.TLabel', background="black", foreground=sett.fg_col, font=('EurostileExtBla', tx_bor * 3))
s.configure('Custom_2_olay.TLabel', background="black", foreground=sett.fg_col2, font=('EurostileExtBla', tx_bor * 3))
s.configure('Custom_c_olay.TLabel', background="black", foreground=sett.fg_col_cont, font=('EurostileExtBla', tx_bor * 3))
s.configure('Custom_d_olay.TLabel', background="black", foreground=sett.fg_col_d, font=('EurostileExtBla', tx_bor * 3))
s.configure('Custom_lt_olay.TLabel', background="black", foreground=sett.fg_col, font=('EurostileExtReg', tx_bor * 3))
s.configure('Custom_lt_2_olay.TLabel', background="black", foreground=sett.fg_col2, font=('EurostileExtReg', tx_bor * 3))
s.configure('Custom_lt_c_olay.TLabel', background="black", foreground=sett.fg_col_cont, font=('EurostileExtReg', tx_bor * 3))
s.configure('Custom_lt_d_olay.TLabel', background="black", foreground=sett.fg_col_d, font=('EurostileExtReg', tx_bor * 3))

s.configure('Custom_sm_olay.TLabel', background="black", foreground=sett.fg_col, font=('EurostileExtBla', tx_bor * 2))
s.configure('Custom_sm_2_olay.TLabel', background="black", foreground=sett.fg_col2, font=('EurostileExtBla', tx_bor * 2))
s.configure('Custom_sm_c_olay.TLabel', background="black", foreground=sett.fg_col_cont, font=('EurostileExtBla', tx_bor * 2))
s.configure('Custom_sm_d_olay.TLabel', background="black", foreground=sett.fg_col_d, font=('EurostileExtBla', tx_bor * 3))
s.configure('Custom_sm_lt_olay.TLabel', background="black", foreground=sett.fg_col, font=('EurostileExtReg', tx_bor * 2))
s.configure('Custom_sm_lt_2_olay.TLabel', background="black", foreground=sett.fg_col2, font=('EurostileExtReg', tx_bor * 2))
s.configure('Custom_sm_lt_c_olay.TLabel', background="black", foreground=sett.fg_col_cont, font=('EurostileExtReg', tx_bor * 2))
s.configure('Custom_sm_lt_d_olay.TLabel', background="black", foreground=sett.fg_col_d, font=('EurostileExtReg', tx_bor * 2))

s.configure('Custom.TFrame', background=sett.fg_col, bordercolor=sett.fg_col, lightcolor=sett.bg_col, darkcolor=sett.bg_col, relief='groove')
s.configure('Custom_b.TFrame', background=sett.bg_col, bordercolor=sett.bg_col, lightcolor=sett.fg_col, darkcolor=sett.fg_col, relief='groove')

s.configure('Custom_emp.TFrame', background=sett.fg_col, bordercolor=sett.fg_col, lightcolor=sett.fg_col, darkcolor=sett.fg_col, relief='groove')
s.configure('Custom_emp_b.TFrame', background=sett.bg_col, bordercolor=sett.bg_col, lightcolor=sett.bg_col, darkcolor=sett.bg_col, relief='groove')

s.configure('Custom.TLabel', background=sett.bg_col, foreground=sett.fg_col, font=('EurostileExtBla', tx_bor * 3))
s.configure('Custom_b.TLabel', background=sett.fg_col, foreground=sett.bg_col, font=('EurostileExtBla', tx_bor * 3))

s.configure('Custom_2.TLabel', background=sett.bg_col, foreground=sett.fg_col2, font=('EurostileExtBla', tx_bor * 3))
s.configure('Custom_2_b.TLabel', background=sett.fg_col2, foreground=sett.bg_col, font=('EurostileExtBla', tx_bor * 3))

s.configure('Custom_lt.TLabel', background=sett.bg_col, foreground=sett.fg_col, font=('EurostileExtReg', tx_bor * 3))
s.configure('Custom_b_lt.TLabel', background=sett.fg_col, foreground=sett.bg_col, font=('EurostileExtReg', tx_bor * 3))

s.configure('Custom_sm.TLabel', background=sett.bg_col, foreground=sett.fg_col, font=('EurostileExtMed', tx_bor * 2))
s.configure('Custom_sm_b.TLabel', background=sett.fg_col, foreground=sett.bg_col, font=('EurostileExtMed', tx_bor * 2))

s.configure('Custom_sm_2.TLabel', background=sett.bg_col, foreground=sett.fg_col2, font=('EurostileExtMed', tx_bor * 2))
s.configure('Custom_sm_2_b.TLabel', background=sett.fg_col2, foreground=sett.bg_col, font=('EurostileExtMed', tx_bor * 2))

s.configure('Custom_sm_lt.TLabel', background=sett.bg_col, foreground=sett.fg_col, font=('EurostileExtReg', tx_bor * 2))
s.configure('Custom_sm_b_lt.TLabel', background=sett.fg_col, foreground=sett.bg_col, font=('EurostileExtReg', tx_bor * 2))

s.configure('Custom_esm.TLabel', background=sett.bg_col, foreground=sett.fg_col, font=('EurostileExtMed', tx_bor + 3))
s.configure('Custom_esm_b.TLabel', background=sett.fg_col, foreground=sett.bg_col, font=('EurostileExtMed', tx_bor + 3))

s.configure('Custom_esm_lt.TLabel', background=sett.bg_col, foreground=sett.fg_col, font=('EurostileExtReg', tx_bor + 3))
s.configure('Custom_esm_b_lt.TLabel', background=sett.fg_col, foreground=sett.bg_col, font=('EurostileExtReg', tx_bor + 3))

s.configure('Custom_c.TLabel', background=sett.bg_col, foreground=sett.fg_col_cont, font=('EurostileExtBla', tx_bor * 3))
s.configure('Custom_b_c.TLabel', background=sett.fg_col_cont, foreground=sett.bg_col, font=('EurostileExtBla', tx_bor * 3))

s.configure('Custom_lt_c.TLabel', background=sett.bg_col, foreground=sett.fg_col_cont, font=('EurostileExtReg', tx_bor * 3))
s.configure('Custom_b_lt_c.TLabel', background=sett.fg_col_cont, foreground=sett.bg_col, font=('EurostileExtReg', tx_bor * 3))

s.configure('Custom_sm_c.TLabel', background=sett.bg_col, foreground=sett.fg_col_cont, font=('EurostileExtBla', tx_bor * 2))
s.configure('Custom_sm_b_c.TLabel', background=sett.fg_col_cont, foreground=sett.bg_col, font=('EurostileExtBla', tx_bor * 2))

s.configure('Custom_sm_lt_c.TLabel', background=sett.bg_col, foreground=sett.fg_col_cont, font=('EurostileExtReg', tx_bor * 2))
s.configure('Custom_sm_b_lt_c.TLabel', background=sett.fg_col_cont, foreground=sett.bg_col, font=('EurostileExtReg', tx_bor * 2))

s.configure('Custom_term.TLabel', background=sett.bg_col, foreground=sett.fg_col, font=('Consolas', (tx_bor * 2) + 3))
s.configure('Custom_term_b.TLabel', background=sett.fg_col, foreground=sett.bg_col, font=('Consolas', (tx_bor * 2) + 3))

s.configure('Custom.TButton',
            background=sett.bg_col,
            bordercolor=sett.bg_col,
            lightcolor=sett.fg_col,
            darkcolor=sett.fg_col,
            borderwidth=1,
            foreground=sett.fg_col,
            highlightthickness='10',
            font=('EurostileExtBla', tx_bor * 3))

s.map('Custom.TButton',
      lightcolor=[('disabled', sett.fg_col_d), ('pressed', sett.fg_col), ('active', sett.fg_col)],
      darkcolor=[('disabled', sett.fg_col_d), ('pressed', sett.fg_col), ('active', sett.fg_col)],
      foreground=[('disabled', sett.bg_col), ('pressed', sett.fg_col_cont), ('active', sett.bg_col)],
      background=[('disabled', sett.fg_col_d), ('pressed', '!focus', sett.fg_col_d), ('active', sett.fg_col)],
      highlightcolor=[('focus', 'green'), ('!focus', 'red')],
      relief=[('pressed', 'groove'), ('!pressed', 'groove')])

s.configure('Custom_big.TButton',
            background=sett.bg_col,
            bordercolor=sett.bg_col,
            lightcolor=sett.fg_col,
            darkcolor=sett.fg_col,
            borderwidth=1,
            foreground=sett.fg_col,
            highlightthickness='10',
            font=('EurostileExtReg', tx_bor * 5))

s.map('Custom_big.TButton',
      lightcolor=[('disabled', sett.fg_col_d), ('pressed', sett.fg_col), ('active', sett.fg_col)],
      darkcolor=[('disabled', sett.fg_col_d), ('pressed', sett.fg_col), ('active', sett.fg_col)],
      foreground=[('disabled', sett.bg_col), ('pressed', sett.fg_col_cont), ('active', sett.bg_col)],
      background=[('disabled', sett.fg_col_d), ('pressed', '!focus', sett.fg_col_d), ('active', sett.fg_col)],
      highlightcolor=[('focus', 'green'), ('!focus', 'red')],
      relief=[('pressed', 'groove'), ('!pressed', 'groove')])

s.configure('Custom_pic.TButton',
            background=sett.bg_col,
            bordercolor=sett.bg_col,
            lightcolor=sett.fg_col,
            darkcolor=sett.fg_col,
            borderwidth=1,
            foreground=sett.fg_col,
            highlightthickness='10',
            font=('EurostileExtMed', tx_bor * 2))

s.map('Custom_pic.TButton',
      lightcolor=[('disabled', sett.fg_col_d), ('pressed', sett.fg_col), ('active', sett.fg_col)],
      darkcolor=[('disabled', sett.fg_col_d), ('pressed', sett.fg_col), ('active', sett.fg_col)],
      foreground=[('disabled', sett.bg_col), ('pressed', sett.fg_col_cont), ('active', sett.bg_col)],
      background=[('disabled', sett.fg_col_d), ('pressed', '!focus', sett.fg_col_d), ('active', sett.fg_col)],
      highlightcolor=[('focus', 'green'), ('!focus', 'red')],
      relief=[('pressed', 'groove'), ('!pressed', 'groove')])

s.layout('Custom_pic.TButton', [('Button.border', {'sticky': 'nswe', 'border': '1', 'children': [
    ('Button.focus', {'sticky': 'nswe', 'children': [('Button.padding', {'sticky': 'nswe', 'children': [('Button.label', {'sticky': 'nw'})]})]})]})])

s.configure('Custom_lt.TButton',
            background=sett.bg_col,
            bordercolor=sett.bg_col,
            lightcolor=sett.fg_col,
            darkcolor=sett.fg_col,
            borderwidth=1,
            foreground=sett.fg_col,
            highlightthickness='10',
            font=('EurostileExtReg', tx_bor * 3))

s.map('Custom_lt.TButton',
      lightcolor=[('disabled', sett.fg_col_d), ('pressed', sett.fg_col), ('active', sett.fg_col)],
      darkcolor=[('disabled', sett.fg_col_d), ('pressed', sett.fg_col), ('active', sett.fg_col)],
      foreground=[('disabled', sett.bg_col), ('pressed', sett.fg_col_cont), ('active', sett.bg_col)],
      background=[('disabled', sett.fg_col_d), ('pressed', '!focus', sett.fg_col_d), ('active', sett.fg_col)],
      highlightcolor=[('focus', 'green'), ('!focus', 'red')],
      relief=[('pressed', 'groove'), ('!pressed', 'groove')])

s.configure('Custom_sm.TButton',
            background=sett.bg_col,
            bordercolor=sett.bg_col,
            lightcolor=sett.fg_col,
            darkcolor=sett.fg_col,
            borderwidth=1,
            foreground=sett.fg_col,
            highlightthickness='10',
            font=('EurostileExtMed', tx_bor * 2))

s.map('Custom_sm.TButton',
      lightcolor=[('disabled', sett.fg_col_d), ('pressed', sett.fg_col), ('active', sett.fg_col)],
      darkcolor=[('disabled', sett.fg_col_d), ('pressed', sett.fg_col), ('active', sett.fg_col)],
      foreground=[('disabled', sett.bg_col), ('pressed', sett.fg_col_cont), ('active', sett.bg_col)],
      background=[('disabled', sett.fg_col_d), ('pressed', '!focus', sett.fg_col_d), ('active', sett.fg_col)],
      highlightcolor=[('focus', 'green'), ('!focus', 'red')],
      relief=[('pressed', 'groove'), ('!pressed', 'groove')])

s.configure('Custom_s.TButton',
            background=sett.bg_col,  # White
            bordercolor=sett.fg_col,  # Green
            lightcolor=sett.bg_col,  # Red
            darkcolor=sett.bg_col,  # Blue
            borderwidth=1,
            foreground=sett.fg_col,  # Cyan
            highlightthickness=1,
            font=('Arial', tx_bor * 2))

s.map('Custom_s.TButton',
      lightcolor=[('disabled', sett.fg_col_d), ('pressed', sett.fg_col), ('active', sett.fg_col)],
      darkcolor=[('disabled', sett.fg_col_d), ('pressed', sett.fg_col), ('active', sett.fg_col)],
      foreground=[('disabled', sett.bg_col), ('pressed', sett.fg_col_cont), ('active', sett.bg_col)],
      background=[('disabled', sett.fg_col_d), ('pressed', '!focus', sett.fg_col), ('active', sett.fg_col)],
      highlightcolor=[('focus', 'green'), ('!focus', 'red')],
      relief=[('pressed', 'groove'), ('!pressed', 'groove')])

s.configure('Custom.TCombobox',
            arrowcolor=sett.fg_col_cont,
            background=sett.bg_col,
            bordercolor=sett.bg_col,
            lightcolor=sett.fg_col,
            darkcolor=sett.fg_col,
            borderwidth=1,
            focusfill='red',
            foreground=sett.fg_col,
            fieldbackground='red',
            highlightthickness=1,
            font=('EurostileExtReg', tx_bor * 2))

s.configure('Custom.TCombobox.font', font=('EurostileExtReg', tx_bor * 2))

s.map('Custom.TCombobox',
      arrowcolor=[('readonly', sett.fg_col_d), ('pressed', sett.bg_col), ('active', 'green')],
      darkcolor=[('disabled', sett.fg_col_d), ('pressed', sett.fg_col), ('active', sett.fg_col)],
      foreground=[('disabled', sett.bg_col), ('pressed', sett.fg_col_cont), ('active', sett.bg_col)],
      background=[('disabled', sett.fg_col_d), ('pressed', '!focus', sett.fg_col), ('active', sett.fg_col)],
      highlightcolor=[('focus', 'green'), ('!focus', 'red')],
      relief=[('pressed', 'groove'), ('!pressed', 'groove')])

s.configure('Custom.TRadiobutton',  # First argument is the name of style. Needs to end with: .TRadiobutton
            background=sett.bg_col,  # White
            indicatorbackground='gray',
            indicatorforeground='green',
            focuscolor='gray',
            indicatorsize=20,
            indicatormargin=10,
            upperbordercolor=sett.fg_col,  # Green
            lowerbordercolor=sett.fg_col,  # Red
            darkcolor=sett.fg_col,  # Blue
            foreground=sett.fg_col,  # Cyan
            highlightthickness='10',
            font=('EurostileExtBla', tx_bor * 3))

s.map('Custom.TRadiobutton',
      indicatorbackground=[('active', sett.fg_col), ('pressed', 'magenta')],
      foreground=[('disabled', sett.fg_col2), ('pressed', sett.fg_col)],
      background=[('disabled', 'magenta'), ('pressed', '!focus', sett.fg_col_cont)],
      highlightcolor=[('focus', sett.fg_col), ('!focus', 'red')],
      relief=[('pressed', 'flat'), ('!pressed', 'flat')])

s.configure('Custom.TCheckbutton',
            background=sett.bg_col,  # White
            foreground=sett.fg_col,  # Cyan
            indicatorbackground='gray',
            indicatorforeground=sett.fg_col,
            focuscolor='gray',
            indicatorsize=20,
            indicatormargin=10,
            upperbordercolor=sett.fg_col,  # Green
            lowerbordercolor=sett.fg_col,  # Red
            font=('EurostileExtBla', tx_bor * 3))

s.map('Custom.TCheckbutton',
      indicatorbackground=[('active', sett.fg_col), ('pressed', 'magenta')],
      foreground=[('disabled', sett.fg_col2), ('pressed', sett.fg_col)],
      background=[('disabled', 'magenta'), ('pressed', '!focus', sett.fg_col_cont)],
      highlightcolor=[('focus', sett.fg_col), ('!focus', 'red')],
      relief=[('pressed', 'flat'), ('!pressed', 'flat')])

s.configure('Custom.Horizontal.TScrollbar',
            orient="horizontal",
            background=sett.fg_col,  # White
            bordercolor=sett.fg_col,  # Cyan
            borderwidth=1,
            troughcolor=sett.bg_col,
            lightcolor=sett.bg_col,
            darkcolor=sett.bg_col,
            arrowcolor=sett.bg_col,
            arrowsize=20,
            gripcount=0,
            sliderlength=800)

s.map('Custom.Horizontal.TScrollbar',
      arrowcolor=[('pressed', sett.fg_col), ('pressed', 'magenta')],
      background=[('disabled', sett.fg_col2), ('pressed', sett.bg_col)],
      relief=[('pressed', 'flat'), ('!pressed', 'flat')])

s.configure('Custom.Vertical.TScrollbar',
            orient="horizontal",
            background=sett.fg_col,  # White
            bordercolor=sett.fg_col,  # Cyan
            borderwidth=1,
            troughcolor=sett.bg_col,
            lightcolor=sett.bg_col,
            darkcolor=sett.bg_col,
            arrowcolor=sett.bg_col,
            arrowsize=bor * 3,
            gripcount=0,
            sliderlength=800)

s.map('Custom.Vertical.TScrollbar',
      arrowcolor=[('pressed', sett.fg_col), ('pressed', 'magenta')],
      background=[('disabled', sett.fg_col_d), ('pressed', sett.bg_col)],
      relief=[('pressed', 'flat'), ('!pressed', 'flat')])

s.configure('Custom_sm.Vertical.TScrollbar',
            orient="horizontal",
            background=sett.fg_col,  # White
            bordercolor=sett.fg_col,  # Cyan
            borderwidth=1,
            troughcolor=sett.bg_col,
            lightcolor=sett.bg_col,
            darkcolor=sett.bg_col,
            arrowcolor=sett.bg_col,
            arrowsize=tx_bor * 3,
            gripcount=0,
            sliderlength=bor)

s.map('Custom_sm.Vertical.TScrollbar',
      arrowcolor=[('pressed', sett.fg_col), ('pressed', 'magenta')],
      background=[('disabled', sett.fg_col_d), ('pressed', sett.bg_col)],
      relief=[('pressed', 'flat'), ('!pressed', 'flat')])

s.configure('Custom.TScale',  # First argument is the name of style. Needs to end with: .TRadiobutton
            background='gray',  # White
            indicatorbackground='gray',
            indicatorforeground='green',
            focuscolor='gray',
            indicatorsize=20,
            indicatormargin=10,
            upperbordercolor=sett.fg_col,  # Green
            lowerbordercolor=sett.fg_col,  # Red
            darkcolor=sett.fg_col,  # Blue
            foreground=sett.fg_col,  # Cyan
            highlightthickness='10',
            font=('EurostileExtBla', tx_bor * 2))

s.configure('Custom.Horizontal.TScale',
            bordercolor=sett.fg_col,
            lightcolor=sett.bg_col,
            darkcolor=sett.bg_col,
            borderwidth=1,
            sliderlength=20,
            troughcolor=sett.bg_col,
            background=sett.fg_col,
            arrowcolor='red',
            gripcount=0,
            arrowsize=20)

s.map('Custom.Horizontal.TScale',
      indicatorbackground=[('active', sett.fg_col), ('pressed', 'magenta')],
      foreground=[('disabled', sett.fg_col2), ('pressed', sett.fg_col)],
      background=[('disabled', 'magenta'), ('pressed', '!focus', sett.fg_col_cont)],
      highlightcolor=[('focus', sett.fg_col), ('!focus', 'red')],
      relief=[('pressed', 'flat'), ('!pressed', 'flat')])

s.configure('Custom.Horizontal.TProgressbar',
            bordercolor=sett.fg_col,
            lightcolor=sett.fg_col,
            darkcolor=sett.fg_col,
            borderwidth=1,
            sliderlength=20,
            troughcolor=sett.bg_col,
            background=sett.fg_col)

s.configure('Custom.Vertical.TProgressbar',
            bordercolor=sett.fg_col,
            lightcolor=sett.fg_col,
            darkcolor=sett.fg_col,
            borderwidth=1,
            sliderlength=10,
            troughcolor=sett.bg_col,
            background=sett.fg_col)


# стили элементов

class ActionHandler:
    def __init__(self):
        print("AH")

    @staticmethod
    def do_action(data_dict):
        print(data_dict)

        if data_dict[2] == 'system':  # системный модуль
            if data_dict[3] == 'main_menu':
                if datahook.game_load is False:
                    action.do_action([1, False, 'olay', 'add_state_item', sett.lang['state_items']['system']['session_connected'], 'notific'])
                else:
                    datahook.game_load = False
                    user_profile.save_profile()
                    action.do_action([1, False, 'olay', 'add_state_item', sett.lang['state_items']['system']['session_ended'], 'notific'])
                    # сюда кинуть функцию сохранения игровой сессии и записи в профиль всякостей

            elif data_dict[3] == 'shutdown':
                datahook.game_load = False
                user_profile.save_profile()
                quit_miex()

            elif data_dict[3] == 'loadgame':
                datahook.game_load = True
                if data_dict[4][0] == user_profile.profile['Commander'] and data_dict[4][1] == user_profile.profile['FID']:
                    user_profile.sync[0] = True
                    guitimer.add_timer([1, False, 'olay', 'add_state_item', sett.lang['state_items']['system']['name_sync'], 'notific'])

            elif data_dict[3] == 'val_act':
                datahook.val_act(data_dict[4], data_dict[5], data_dict[6], data_dict[7])

        elif data_dict[2] == 'data_hook':  # модуль даты
            datahook.read_capt_log(datahook.cur_capt_log.stat().st_size)

        elif data_dict[2] == 'searching_all_files':  # модуль даты
            datahook.searching_all_files(data_dict[3])

        elif data_dict[2] == 'top_win':  # модуль окна доп.окон

            if data_dict[3] == 'add_dialogue_line':  # функция добавления строки в диалог
                topwin.add_dial_line()

            elif data_dict[3] == 'show_dialogue':
                topwin.show_dialogue(data_dict[4])

            elif data_dict[3] == 'kill_dialog_win':  # функция уничтожения окна диалога
                topwin.kill_win()
                audio.restore_vol('voice')

            elif data_dict[3] == 'kill_win':  # функция уничтожения окна диалога
                topwin.kill_win()

            elif data_dict[3] == 'kill_win2':  # функция уничтожения окна диалога
                topwin.kill_win2()

            elif data_dict[3] == 'progress_bar_step':  # функция шага окна прогресс бара
                topwin.progress_bar_step(data_dict[4], data_dict[5])

            elif data_dict[3] == 'show_password_breaker':
                #добавить кастомное время и название в зависимости от
                topwin.show_password_breaker(data_dict[4], data_dict[5], data_dict[6], data_dict[7], data_dict[8])

        elif data_dict[2] == 'olay':  # модуль оверлея

            if data_dict[3] == 'remove_state_item':  # функция проверки обновления уведомлений и удаления онных
                olay.remove_state_item()

            elif data_dict[3] == 'show_task':  # показ задания
                olay.show_task(data_dict[4])

            elif data_dict[3] == 'add_state_item':  # показ задания
                olay.add_state_item(data_dict[4], data_dict[5])

            elif data_dict[3] == 'clear_frame':  # зачистка фремов
                if data_dict[4] == 'task_frame':
                    olay.clear_frame(olay.task_frame)
                    olay.task_showed = False
                elif data_dict[4] == 'bottom_frame':
                    olay.clear_frame(olay.bottom_frame)

            elif data_dict[3] == 'change_call_action':
                olay.change_call_action(data_dict[4])

            elif data_dict[3] == 'show_bottom':
                olay.show_bottom(data_dict[4], data_dict[5], data_dict[6], data_dict[7])

        elif data_dict[2] == 'audio':  # модуль звука
            if data_dict[3] == 'play_sound':  # воспризведение звука
                if len(data_dict) > 6:
                    audio.play_sound(data_dict[4], data_dict[5], path=data_dict[6])
                else:
                    audio.play_sound(data_dict[4], data_dict[5])

            elif data_dict[3] == 'restore_vol':
                audio.restore_vol(data_dict[4])

            elif data_dict[3] == 'sfx_stop':
                audio.sfx.stop()
                audio.restore_vol('ui')

        elif data_dict[2] == 'mw1':  # модуль основого окна
            if data_dict[3] == 'show_win':  # показать скрытое оконце
                mw1.win.deiconify()

            elif data_dict[3] == 'main_menu':  # главное меню
                if data_dict[4] == 0:  # мисcии
                    audio.play_sound('ui', 'click')
                    print("npc.cr_npc_dialogue('sidor')")

                if data_dict[4] == 1:
                    audio.play_sound('ui', 'click')
                    print("npc.cr_npc_dialogue('sidor')")

                elif data_dict[4] == 2:
                    audio.play_sound('ui', 'click')

                elif data_dict[4] == 3:
                    audio.play_sound('ui', 'click')

                elif data_dict[4] == 4:  # контакты
                    audio.play_sound('ui', 'click')
                    npc.cr_npc_dialogue('sidor')

                elif data_dict[4] == 5:
                    audio.play_sound('ui', 'click')

                elif data_dict[4] == 6:
                    audio.play_sound('ui', 'click')

                elif data_dict[4] == 7:
                    audio.play_sound('ui', 'click')

                elif data_dict[4] == 'main_menu_options':
                    audio.play_sound('ui', 'click')

                elif data_dict[4] == 'main_menu_quit':
                    audio.play_sound('ui', 'click')
                    mw1.quit()
                    quit_miex()

                elif data_dict[4] == 'main_menu_exit':
                    audio.play_sound('ui', 'click')
                    mw1.quit()

            elif data_dict[3] == 'mission':  # модуль миссий

                if data_dict[4] == 'mis_tsk':  # показ текущей мисии
                    audio.play_sound('ui', 'click')
                    missions.cr_mis_tsk(data_dict[5])

                elif data_dict[4] == 'mis_jrn':  # показ журнала текущей мисии
                    audio.play_sound('ui', 'click')
                    missions.cr_mis_jrn(data_dict[5])

                elif data_dict[4] == 'mis_inv':  # показ инвентаря текущей мисии
                    audio.play_sound('ui', 'click')
                    missions.cr_mis_inv(data_dict[5])

                elif data_dict[4] == 'mis_inv_cr_det':  # показ инвентаря текущей мисии
                    audio.play_sound('ui', 'click')
                    inventory.cr_item_card(data_dict[5], data_dict[6][0], data_dict[6][1].split('-')[1], data_dict[7])

            elif data_dict[3] == 'inventory':  # модуль инвентаря
                if data_dict[4] == 'cr_item_card':  # отображение карточки итема
                    audio.play_sound('ui', 'click')
                    inventory.cr_item_card(data_dict[5], data_dict[6], data_dict[7], data_dict[8])

                elif data_dict[4] == 'item_card_analyze':  # запуск системы анализа файла
                    inventory.item_card_analyze(data_dict[5], data_dict[6], data_dict[7], data_dict[8])

        elif data_dict[2] == 'mission':
            if data_dict[3] == 'set_cur_mission':
                olay.add_state_item(sett.lang['state_items']['missions']['ch_cur_mission'], 'stage')
                missions.set_cur_mission(data_dict[4])
            elif data_dict[3] == 'next_stage':
                olay.add_state_item(sett.lang['state_items']['missions']['next_stage'], 'stage')
                missions.cur_mission_next_stage(data_dict[4])
            elif data_dict[3] == 'add_jrn_tip':
                print('add_jrn_tip')
                missions.cur_mis_jrn.append([data_dict[4], data_dict[5]])
                print(missions.cur_mis_jrn)
                olay.add_state_item(sett.lang['state_items']['missions']['add_jrn_tip'], 'notif')
            elif data_dict[3] == 'cur_mission_complete':
                missions.cur_mission_complete()
                olay.add_state_item(sett.lang['state_items']['missions']['mis_success'], 'stage')


        elif data_dict[2] == 'link':  # ссылки в тексте
            if data_dict[3] == 'show_dialogue':
                npc.next_dialogue(data_dict[4], data_dict[5])

            elif data_dict[3] == 'dialogue_return':
                npc.return_dialogue(data_dict[4])

            elif data_dict[3] == 'dialogue_exit':
                mw1.quit()
                mw1.showed = False

            elif data_dict[3] == 'start_dialogue':
                npc.start_dialogue()

        elif data_dict[2] == 'keys':  # кнопки
            if data_dict[3] == 'change_action':
                olay.call_action = data_dict[4]

        elif data_dict[2] == 'npc':
            if data_dict[3] == 'npc_message':
                npc.cr_npc_message(data_dict[4], data_dict[5], data_dict[6])

        elif data_dict[2] == 'profile':

            if data_dict[3] == 'loadout':
                if user_profile.sync[2] is False:
                    ship = user_profile.loadout(data_dict[4], data_dict[5], user_profile.ship)
                    if ship[0] is True:
                        user_profile.sync[2] = True
                        guitimer.add_timer([1, False, 'olay', 'add_state_item', sett.lang['state_items']['system']['ship_sync'], 'notific'])
                    else:
                        guitimer.add_timer([1, False, 'olay', 'add_state_item', sett.lang['state_items']['system']['ship_desync_1'], 'notific'])
                else:
                    guitimer.add_timer([1, False, 'olay', 'add_state_item', sett.lang['state_items']['system']['ship_desync_2'], 'notific'])

            elif data_dict[3] == 'location':
                if user_profile.sync[1] is False:
                    if data_dict[4][0] == user_profile.docked[0]:
                        if data_dict[4][0] is True:
                            if user_profile.dock_sync(data_dict[4][1:], user_profile.dock_data.values()) is True:
                                user_profile.sync[1] = True
                                guitimer.add_timer([1, False, 'olay', 'add_state_item', sett.lang['state_items']['system']['loc_sync'], 'notific'])

                                guitimer.add_timer([10, False, 'profile', 'add_docking'])
                            else:
                                guitimer.add_timer([1, False, 'olay', 'add_state_item', sett.lang['state_items']['system']['loc_desync_2'], 'notific'])
                        else:
                            if user_profile.system_sync(data_dict[4][1:], user_profile.system_data.values()) is True:
                                user_profile.sync[1] = True
                                guitimer.add_timer([1, False, 'olay', 'add_state_item', sett.lang['state_items']['system']['loc_sync'], 'notific'])

                                guitimer.add_timer([10, False, 'profile', 'add_docking'])

                            else:
                                guitimer.add_timer([1, False, 'olay', 'add_state_item', sett.lang['state_items']['system']['loc_desync_3'], 'notific'])
                    else:
                        guitimer.add_timer([1, False, 'olay', 'add_state_item', sett.lang['state_items']['system']['loc_desync_1'], 'notific'])

            elif data_dict[3] == 'ch_sys_loc':

                user_profile.last_system_data['StarSystem'] = user_profile.system_data['StarSystem']
                user_profile.last_system_data['SystemSecurity'] = user_profile.system_data['SystemSecurity']
                user_profile.last_system_data['SystemGovernment'] = user_profile.system_data['SystemGovernment']
                user_profile.last_system_data['SystemAllegiance'] = user_profile.system_data['SystemAllegiance']
                user_profile.last_system_data['SystemEconomy'] = user_profile.system_data['SystemEconomy']

                user_profile.system_data['StarSystem'] = data_dict[4][0]
                user_profile.system_data['SystemSecurity'] = data_dict[4][1]
                user_profile.system_data['SystemGovernment'] = data_dict[4][2]
                user_profile.system_data['SystemAllegiance'] = data_dict[4][3]
                user_profile.system_data['SystemEconomy'] = data_dict[4][4]

            elif data_dict[3] == 'add_docking':
                datahook.events_list['profile'].append('Docked')

                datahook.events['profile'].append({'StationName': ['pass_val', 'StationName'],
                                                   'StationType': ['pass_val', 'StationType'],
                                                   'StationGovernment': ['pass_val', 'StationGovernment'],
                                                   'StationAllegiance': ['pass_val', 'StationAllegiance'],
                                                   'StationEconomy': ['pass_val', 'StationEconomy'],
                                                   'action': [[0, False, 'system', 'val_act', 'set', 'dict', 'profile-dock_data',
                                                               [['StationName',
                                                                 'StationType',
                                                                 'StationGovernment',
                                                                 'StationAllegiance',
                                                                 'StationEconomy'
                                                                 ],
                                                                'StationName',
                                                                'StationType',
                                                                'StationGovernment',
                                                                'StationAllegiance',
                                                                'StationEconomy'
                                                                ]],
                                                              [0, False, 'system', 'val_act', 'set', 'static', 'profile-docked', True, 'no_pass']
                                                              ]})

            elif data_dict[3] == 'finance_sync':
                if user_profile.finance_sync(data_dict[4]) is True:
                    user_profile.sync[3] = True
                    guitimer.add_timer([1, False, 'olay', 'add_state_item', sett.lang['state_items']['system']['fin_sync'], 'notific'])
                else:
                    guitimer.add_timer([1, False, 'olay', 'add_state_item', sett.lang['state_items']['system']['fin_desync'], 'notific'])

                print(user_profile.sync)

        elif data_dict[2] == 'transm':
            if data_dict[3] == 'freq':
                mixer.music.stop()
                transm.cur_freq_play = False
                if data_dict[4] == '+':
                    transm.ferq_ch(True)
                    audio.play_sound('ui', 'click')
                elif data_dict[4] == '-':
                    transm.ferq_ch(False)
                    audio.play_sound('ui', 'click')
                elif data_dict[4] == 'next_fav':
                    transm.ferq_fav_ch(True)
                    audio.play_sound('ui', 'click')
                elif data_dict[4] == 'prew_fav':
                    transm.ferq_fav_ch(False)
                    audio.play_sound('ui', 'click')

                elif data_dict[4] == 'play':
                    transm.cur_freq_play = True
                    freq_data = transm.freq_dict[transm.cur_freq]
                    cur_time = guitimer.c_time // 10
                    freq_pos = cur_time-((cur_time//freq_data[2])*freq_data[2])
                    audio.play_sound('music_pos_rep', freq_data[1], path='data/radio/', pos=freq_pos)

                elif data_dict[4] == 'stop':
                    'print do stop'

                audio.play_sound('ui', 'click')
                transm.cr_radio_wiget(*data_dict[5])

        elif data_dict[2] == 'extra_sound':
            if data_dict[3] == 'play_file_dep_on_name':
                extra_sound.play_file_dep_on_name(*data_dict[4])
            elif data_dict[3] == 'remove_name_from_dict':
                extra_sound.remove_name_from_dict(data_dict[4], data_dict[5])


class GuiTimer(Thread):
    def __init__(self):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = 'gui_timer'
        self.daemon = True
        self.shedule = []
        self.c_time = 0

    def run(self):
        """Запуск потока"""
        print("giu timer start")
        while root.title() == 'MIEX olay':
            self.c_time += 1
            shedule_range = range(len(self.shedule))
            shedule_kill_list = []
            for t in shedule_range:  # пробежали по списку событий
                if self.shedule[t][0] == self.c_time:  # посмотрели подходит ли время
                    event = self.shedule[t]  # взяли в переменную
                    shedule_kill_list.append(t)
                    action.do_action(event)
                    if event[1] is not False:  # посмотрели в цикле ли событие
                        event[0] = self.c_time + event[1]  # добавили времени
                        self.shedule.append(event)  # добавили в список

            shedule_kill_list.reverse()  # развернули дабы удалить сначала крайний элемент по ид, потом снова крайний
            for k in shedule_kill_list:  # пробежали по списку удаления
                del self.shedule[k]  # удалили лишнее

            sleep(0.1)
            # print("cyc "+ str(self.c_time))
            # print(self.shedule)

    def add_timer(self, data_dict):  # data_dict[time in sec, cycle time, func, args...]
        data_dict[0] = int(data_dict[0] * 10)
        if data_dict[1] != False:
            data_dict[1] = int(data_dict[1] * 10)
        data_dict[0] = self.c_time + data_dict[0]
        self.shedule.append(data_dict)


def quit_miex():
    root.title("MIEX Shutdown")
    action.do_action([0, False, 'olay', 'add_state_item', sett.lang['state_items']['system']['session_ended'], 'notific'])
    root.after(3000, root.destroy)


def key_hook():
    def action_call():
        if olay.call_action == "mainwindow":
            if mw1.showed is False:
                mw1.create()
            else:
                mw1.quit()
        elif olay.call_action == "fastdialogue":
            if mw1.showed is False:
                mw1.create()
                npc.cr_npc_dialogue()
                olay.clear_frame(olay.bottom_frame)

            else:
                mw1.quit()
                mw1.create()
                npc.cr_npc_dialogue()
                olay.clear_frame(olay.bottom_frame)

    def show_overlay():
        if olay.task_showed is False:
            if 'task_extra' in missions.cur_save_data.keys():
                olay.show_task(" / / / " + missions.cur_save_data['task_name'] + " \ \ \ ", task_extra=missions.cur_save_data['task_extra'])
            else:
                olay.show_task(" / / / " + missions.cur_save_data['task_name'] + " \ \ \ ", task_extra="missions.cur_save_data['task_extra']")
        else:
            olay.clear_frame(olay.task_frame)
            olay.task_showed = False

    def guittest():
        action.do_action([0, False, "npc", "npc_message", "message", "hacker", "hacker01"])

    def keytest():
        keyboard.send('l', True, True)
        keyboard.call_later(keyboard.send, args=('l', True, True), delay=2.001)

    def guittest2():
        action.do_action([0, False, "top_win", "show_password_breaker", "decode_l", "testbreak", 1, "ELITE", [[1, False, 'olay', 'add_state_item', 'Mini game test true act', 'notific'], [1, False, 'olay', 'add_state_item', 'Mini game test false act', 'notific']]])

    keyboard.add_hotkey(sett.action_key, action_call, trigger_on_release=False)
    keyboard.add_hotkey(sett.task_key, show_overlay, trigger_on_release=False)
    keyboard.add_hotkey(sett.message_test_key, guittest, trigger_on_release=False)
    keyboard.add_hotkey(sett.minigame_test_key, guittest2, trigger_on_release=False)
    # keyboard.add_hotkey("n", keytest, trigger_on_release=False)


class DataHook:
    def __init__(self):
        self.hook_cycle = False
        self.cur_capt_log = None
        self.cur_capt_log_size = 0
        self.cur_capt_log_list = []
        self.game_load = False

        guitimer.add_timer([sett.ed_start_time, False, 'searching_all_files', sett.ed_log_folder])

        self.events_list = {}
        self.events = {}

        self.vals_result_list = []
        self.vals_pass_list = []

        self.events_list['system'] = ['Music', 'Shutdown', 'LoadGame']
        self.events['system'] = [
            {'MusicTrack': ['equal', 'MainMenu'], 'action': [0, False, 'system', 'main_menu']},
            {'event': ['equal', 'Shutdown'], 'action': [0, False, 'system', 'shutdown']},
            {'event': ['equal', 'LoadGame'], 'Commander': ['pass_val', 'Commander'], 'FID': ['pass_val', 'FID'], 'action': [0, False, 'system', 'loadgame', ['Commander', 'FID']]}
        ]

    def read_capt_log(self, bytes):
        if self.hook_cycle is False:
            if datahook.game_load is False:
                guitimer.add_timer([sett.ed_start_time//2, False, 'data_hook'])
            else:
                guitimer.add_timer([sett.data_hook_time, sett.data_hook_time, 'data_hook'])
                self.hook_cycle = True

        if bytes > self.cur_capt_log_size:
            fp = open(self.cur_capt_log, mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
            fp.seek(self.cur_capt_log_size, 0)
            read_data = fp.read()
            fp.close()
            read_data = read_data.replace('\n', '').split("{ \x22timestamp\x22:\x22")
            read_data.pop(0)
            for i in range(len(read_data)):
                line = json.loads("{ \x22timestamp\x22:\x22" + read_data[i])
                line.pop('timestamp')

                events_hook = []

                for cat in self.events_list.keys():

                    in_count = self.events_list[cat].count(line['event'])
                    in_ind = 0
                    in_end = len(self.events_list[cat])
                    if in_count > 0:
                        for e in range(in_count):
                            in_ind = self.events_list[cat].index(line['event'], in_ind, in_end)
                            events_hook.append(self.events[cat][in_ind])
                            in_ind += 1

                self.event_handler(line, events_hook)

                del events_hook

            self.cur_capt_log_size = bytes

    def event_handler(self, s_line, events_hook):
        print(s_line)

        line = copy.deepcopy(s_line)

        actions_list = []
        vals_list = []
        vals_names_list = []
        vals_types_list = []
        self.vals_result_list = []
        self.vals_pass_list = []

        for eh in enumerate(events_hook):
            event_hook = copy.deepcopy(eh[1])
            actions_list.append(event_hook['action'])
            del event_hook['action']

            cur_vals_types = []
            cur_vals = []

            for val in event_hook.values():
                cur_vals_types.append(val[0])
                cur_vals.append(val[1])

            vals_list.append([*cur_vals])
            vals_names_list.append([*event_hook.keys()])
            vals_types_list.append([*cur_vals_types])
            self.vals_result_list.append([])
            self.vals_pass_list.append({})

            del event_hook

        for ev_l in enumerate(vals_types_list):
            for ev in enumerate(ev_l[1]):
                self.log_func(ev[1], ev_l[0], line[vals_names_list[ev_l[0]][ev[0]]], vals_list[ev_l[0]][ev[0]])

        # print(self.vals_pass_list)
        # print(vals_names_list)
        # print(self.vals_result_list)
        # print(actions_list)

        for res in enumerate(self.vals_result_list):  # пробегаем по списку с результатами
            if res[1].count(True) == len(res[1]):  # если все результаты Правда
                if type(actions_list[res[0]][0]) is list:  # если первый элемент экшона - список, значит тут несколько действий
                    for a in actions_list[res[0]]:  # цикл списку действий
                        if len(self.vals_pass_list[res[0]].keys()) > 0:  # если в списке словарей переданных переменных что-то есть
                            print(self.vals_pass_list)
                            if a[-1] != 'no_pass':
                                for k in self.vals_pass_list[res[0]].keys():  # цикл по именам переменных, дабы заменить их в действии
                                    val_ind = a[-1].index(k)
                                    a[val_ind] = self.vals_pass_list[res[0]][k]
                            else:
                                del a[-1]
                        action.do_action(a)

                else:
                    if len(self.vals_pass_list[res[0]].keys()) > 0:
                        for k in self.vals_pass_list[res[0]].keys():
                            val_ind = actions_list[res[0]][-1].index(k)
                            actions_list[res[0]][-1][val_ind] = self.vals_pass_list[res[0]][k]
                    action.do_action(actions_list[res[0]])

        self.vals_result_list = []
        self.vals_pass_list = []

    def log_func(self, type, data_bank, line_val, event_val):

        if len(type.split('-')) > 1:
            type_sp = type.split('-')
            type = type_sp[0]
            extra = event_val.pop(-1)
            if extra[0] == 'pass_val':
                self.vals_result_list[data_bank].append(True)
                self.vals_pass_list[data_bank][extra[1]] = line_val


        if type == 'equal':
            if event_val == line_val:
                self.vals_result_list[data_bank].append(True)
            else:
                self.vals_result_list[data_bank].append(False)

        elif type == 'inlist':
            if line_val in event_val:
                self.vals_result_list[data_bank].append(True)
            else:
                self.vals_result_list[data_bank].append(False)

        elif type == 'isbig':
            if event_val > line_val:
                self.vals_result_list[data_bank].append(True)
            else:
                self.vals_result_list[data_bank].append(False)

        elif type == 'isless':
            if event_val < line_val:
                self.vals_result_list[data_bank].append(True)
            else:
                self.vals_result_list[data_bank].append(False)

        elif type == 'inbord':
            if event_val[0] < line_val < event_val[1]:
                self.vals_result_list[data_bank].append(True)
            else:
                self.vals_result_list[data_bank].append(False)

        elif type == 'outbord':
            if event_val[0] > line_val > event_val[1]:
                self.vals_result_list[data_bank].append(True)
            else:
                self.vals_result_list[data_bank].append(False)

        elif type == 'pass_val':
            self.vals_result_list[data_bank].append(True)
            self.vals_pass_list[data_bank][event_val] = line_val

    def searching_all_files(self, directory):
        dirpath = Path(directory)
        assert (dirpath.is_dir())
        file_list = []
        for x in dirpath.iterdir():
            if x.is_file():
                if x.stem[0:8] == "Journal." and x.stem[-3] == ".":
                    file_list.append(x)
        if sett.log_files_len == len(file_list):
            if self.cur_capt_log is None:
                print('wait load ED')
                guitimer.add_timer([sett.ed_start_time, False, 'searching_all_files', directory])

        else:
            self.cur_capt_log = file_list[-1]
            sett.log_files_len = len(file_list)
            sett.save_settings()
            guitimer.add_timer([sett.ed_start_time//2, False, 'data_hook'])
            print('hook engine start')

    @staticmethod
    def val_act(act_type, datas_type, vars, datas):

        fin_data = None
        fin_var = None
        variant = None

        fin_act = act_type

        def vars_setter(var):
            var = var.split('-')
            var_len = len(var)
            if var[0] == 'profile':
                if var[1] == 'dock_data':
                    if var_len < 3:
                        return user_profile.dock_data
                elif var[1] == 'last_dock_data':
                    if var_len < 3:
                        return user_profile.last_dock_data

                elif var[1] == 'docked':
                    return user_profile.docked

        def act_setter(action, var, data):
            if action == 'set':
                var = data
                return var

            elif action == '+':
                var += data
                return var

            elif action == '-':
                var -= data
                return var

        if datas_type == 'var':
            fin_data = vars_setter(datas)

        elif datas_type == 'static':
            fin_data = datas

        elif datas_type == 'list':
            fin_data = datas

        elif datas_type == 'dict':
            fin_data = {}
            for i in range(len(datas) - 1):
                fin_data[datas[0][i]] = datas[i + 1]

        if type(act_type) is str:
            variant = False
        else:
            variant = True

        fin_var = vars_setter(vars)
        var_type = type(fin_var)
        if var_type is dict:
            if variant is False:
                fin_act = {}
            for k in fin_var.keys():
                if variant is False:
                    fin_act[k] = act_type
                fin_var[k] = act_setter(fin_act[k], fin_var[k], fin_data[k])

        elif var_type is list:
            if len(fin_var) == 1:
                fin_var[0] = act_setter(act_type, fin_var[0], fin_data)
            else:
                if variant is False:
                    fin_act = list((act_type,) * len(fin_var))
                for i in range(len(fin_var)):
                    fin_var[i] = act_setter(fin_act[i], fin_var[i], fin_data[i])


class LogFunc:
    def __init__(self):
        pass

    @staticmethod
    def equal_val(data_log, data):
        if isinstance(data, list) is True:
            for i in enumerate(data):
                if data_log[i[0]] == i[1]:
                    return True
                else:
                    return False
        else:
            if data == data_log:
                return True
            else:
                return False

    @staticmethod
    def isbig_val(data_log, data):
        if isinstance(data, list) is True:
            for i in enumerate(data):
                if data_log[i[0]] > i[1]:
                    return True
                else:
                    return False
        else:
            if data < data_log:
                return True
            else:
                return False

    @staticmethod
    def isless_val(data_log, data):
        if isinstance(data, list) is True:
            for i in enumerate(data):
                if data_log[i[0]] < i[1]:
                    return True
                else:
                    return False
        else:
            if data > data_log:
                return True
            else:
                return False

    @staticmethod
    def inbord_val(data_log, data_min, data_max):
        if isinstance(data_min, list) is True:
            for i in enumerate(data_min):
                if i[1] < data_log[i[0]] < data_max[i[0]]:
                    return True
                else:
                    return False
        else:
            if data_max > data_log > data_min:
                return True
            else:
                return False

    @staticmethod
    def set_val(data_log, var):
        if var[0] == 'user_profile':
            if var[1] == 'profile':
                if len(var) == 3:
                    user_profile.profile[var[2]] = data_log


class Statistics:
    def __init__(self):
        fp = open("data/statistics.txt", mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        stat_file = json.loads(fp.read())

        self.custom_data = stat_file['Custom_data']

        datahook.events_list['statistics'] = [
        ]

        datahook.events['statistics'] = [

        ]


class ExtraSound:
    def __init__(self):

        self.fsd_ads = None
        self.dock_ads = None

        self.sound_names_dict = {}

        fp = open("data/extra_sound.txt", mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        extra_sound = json.loads(fp.read())
        fp.close()

        datahook.events_list['extra_sound'] = []

        datahook.events['extra_sound'] = []

        if extra_sound['FSDAds_settings'][0] is True:
            self.fsd_ads = [extra_sound['FSDAds_settings'][1], *extra_sound['FSDAds']]
            datahook.events_list['extra_sound'].append('StartJump')
            datahook.events['extra_sound'].append({'JumpType': ['equal', 'Hyperspace'], 'action': [0, False, 'extra_sound', 'start_fsd_ads']})

        del extra_sound['FSDAds_settings']
        del extra_sound['FSDAds']

        if extra_sound['DockAds_settings'][0] is True:

            datahook.events_list['extra_sound'].append('Docked')
            datahook.events['extra_sound'].append({'event': ['equal', 'Docked'], 'action': [0, False, 'extra_sound', 'start_dock_ads']})

            self.dock_ads = {'cycle_time': extra_sound['DockAds_settings'][1]}
            self.dock_ads_list = None
            del extra_sound['DockAds_settings']
            for a in extra_sound.keys():
                self.dock_ads[a] = extra_sound[a]

        for e in enumerate(extra_sound['Events_List']):
            datahook.events_list['extra_sound'].append(e[1])
            datahook.events['extra_sound'].append(extra_sound['Events'][e[0]])

        self.sound_names_events = extra_sound['Sound_names_events']

        del extra_sound

    def start_dock_ads(self):

        if user_profile.docked is True:
            if self.dock_ads_list is None:

                self.dock_ads_list = []
                self.dock_ads_list.extend(self.dock_ads['DockAds_def'])
                self.dock_ads_list.extend(self.dock_ads['GovermentAds_def'])
                self.dock_ads_list.extend(self.dock_ads['AllegianceAds_def'])

                dock_data = []
                dock_data.append(user_profile.dock_data['StationGovernment'].split('_')[1])
                dock_data.append(user_profile.dock_data['StationEconomy'].split('_')[1])
                dock_data.append(user_profile.dock_data['StationAllegiance'])

                for dd in dock_data:
                    for k in self.dock_ads.keys():
                        if k.count(dd) == 1:
                            self.dock_ads_list.extend(self.dock_ads[k])

                f_time = randint(10, self.dock_ads['cycle_time'])
                guitimer.add_timer([f_time, False, 'audio', 'play_extra', self.dock_ads_list[randint(1, len(self.dock_ads_list) - 1)]])
                guitimer.add_timer([f_time, False, 'extra_sound', 'start_dock_ads'])

            else:
                guitimer.add_timer([self.dock_ads['cycle_time'], False, 'audio', 'play_extra', self.dock_ads_list[randint(1, len(self.dock_ads_list) - 1)]])
                guitimer.add_timer([self.dock_ads['cycle_time'], False, 'extra_sound', 'start_dock_ads'])


        else:
            self.dock_ads_list = None

    def clear_dock_ads(self):
        self.dock_ads_list = None

    def start_fsd_ads(self):
        if randint(0, 100) <= self.fsd_ads[0]:
            print(self.fsd_ads[randint(1, len(self.fsd_ads) - 1)])
            print('time to play chosen one')

    def play_file_dep_on_name(self, dir_name, name):
        if name not in self.sound_names_dict.keys():
            self.sound_names_dict[name] = [dir_name, 'sound_' + str(randint(1, self.sound_names_events[dir_name])) + '.ogg']
            guitimer.add_timer([300, False, 'extra_sound', 'remove_name_from_dict', name, dir_name])
            s_path = 'data/audio/extra_sound/Events/' + self.sound_names_dict[name][0] + '/' + self.sound_names_dict[name][1]
            audio.play_sound('extra', self.sound_names_dict[name][1], path=s_path)
        else:
            self.sound_names_dict[name][0] = dir_name
            guitimer.add_timer([300, False, 'extra_sound', 'remove_name_from_dict', name, dir_name])
            s_path = 'data/audio/extra_sound/Events/' + self.sound_names_dict[name][0] + '/' + self.sound_names_dict[name][1]
            audio.play_sound('extra', self.sound_names_dict[name][1], path=s_path)

        print('start sound')

    def remove_name_from_dict(self, name, dir_name):
        if name in self.sound_names_dict.keys():
            if self.sound_names_dict[name][0] == dir_name:
                del self.sound_names_dict[name]
            else:

                guitimer.add_timer([300, False, 'extra_sound', 'remove_name_from_dict', name, dir_name])


class Profile:
    def __init__(self):
        fp = open("data/profile/profile.txt", mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        prof = json.loads(fp.read())
        fp.close()

        self.docked = [prof['Docked']]
        del prof['Docked']

        self.dock_data = prof['Dock_data']
        del prof['Dock_data']

        self.system_data = prof['System_data']
        del prof['System_data']

        self.last_dock_data = prof['Last_dock_data']
        del prof['Last_dock_data']

        self.last_system_data = prof['Last_system_data']
        del prof['Last_system_data']

        self.last_route = prof['Last_route']
        del prof['Last_route']

        self.cur_route = []

        self.ship = prof['Ship']
        del prof['Ship']

        self.onboard_mats = prof['Ship_materials']
        del prof['Ship_materials']

        self.stored_mats = prof['Stored_materials']
        del prof['Stored_materials']

        self.onboard_cargo = prof['Ship_cargo']
        del prof['Ship_cargo']

        self.stored_cargo = prof['Stored_cargo']
        del prof['Stored_cargo']

        self.stored_ships = prof['Stored_ships']
        del prof['Stored_ships']

        self.stored_modules = prof['Stored_modules']
        del prof['Stored_modules']

        self.profile = prof.copy()
        del prof
        # [Name, Location, Ship, Finances]
        self.sync = [False, False, False, False]
        datahook.events_list['profile'] = []
        datahook.events['profile'] = []

        if self.docked[0] is True:
            datahook.events_list['profile'].append('Location')
            datahook.events['profile'].append({'Docked': ['pass_val', 'Docked'],
                                               'StationName': ['pass_val', 'StationName'],
                                               'StationType': ['pass_val', 'StationType'],
                                               'StationGovernment': ['pass_val', 'StationGovernment'],
                                               'StationAllegiance': ['pass_val', 'StationAllegiance'],
                                               'StationEconomy': ['pass_val', 'StationEconomy'],
                                               'action': [0, False, 'profile', 'location',
                                                          ['Docked',
                                                           'StationName',
                                                           'StationType',
                                                           'StationGovernment',
                                                           'StationAllegiance',
                                                           'StationEconomy'
                                                           ]]})
        else:
            datahook.events_list['profile'].append('Location')
            datahook.events['profile'].append({'Docked': ['pass_val', 'Docked'],
                                               'StarSystem': ['pass_val', 'StarSystem'],
                                               'SystemSecurity': ['pass_val', 'SystemSecurity'],
                                               'SystemGovernment': ['pass_val', 'SystemGovernment'],
                                               'SystemAllegiance': ['pass_val', 'SystemAllegiance'],
                                               'SystemEconomy': ['pass_val', 'SystemEconomy'],
                                               'action': [0, False, 'profile', 'location',
                                                          ['Docked',
                                                           'StarSystem',
                                                           'SystemSecurity',
                                                           'SystemGovernment',
                                                           'SystemAllegiance',
                                                           'SystemEconomy'
                                                           ]]})

        datahook.events_list['profile'].append('FSDJump')
        datahook.events['profile'].append({'StarSystem': ['pass_val', 'StarSystem'],
                                           'SystemSecurity': ['pass_val', 'SystemSecurity'],
                                           'SystemGovernment': ['pass_val', 'SystemGovernment'],
                                           'SystemAllegiance': ['pass_val', 'SystemAllegiance'],
                                           'SystemEconomy': ['pass_val', 'SystemEconomy'],
                                           'action': [0, False, 'profile', 'ch_sys_loc',
                                                      ['StarSystem',
                                                       'SystemSecurity',
                                                       'SystemGovernment',
                                                       'SystemAllegiance',
                                                       'SystemEconomy'
                                                       ]]})

        datahook.events_list['profile'].append('Undocked')
        datahook.events['profile'].append(
            {'event': ['equal', 'Undocked'],
             'action': [[0, False, 'system', 'val_act', 'set', 'var', 'profile-last_dock_data', 'profile-dock_data'], [0, False, 'system', 'val_act', 'set', 'static', 'profile-docked', False]]}
        )

        datahook.events_list['profile'].append('Loadout')
        datahook.events['profile'].append(
            {'Ship': ['pass_val', 'Ship'], 'ShipName': ['pass_val', 'ShipName'], 'ShipIdent': ['pass_val', 'ShipIdent'], 'Modules': ['pass_val', 'Modules'],
             'action': [0, False, 'profile', 'loadout', 'sync', ['Ship', 'ShipName', 'ShipIdent', 'Modules']]}
        )

        '''datahook.events_list['profile'].append('Statistics')
        datahook.events['profile'].append(
            {'Bank_Account': ['pass_val', 'Bank_Account'], 'Crime': ['pass_val', 'Crime'],
             'action': [0, False, 'profile', 'finance_sync', ['Bank_Account', 'Crime']]}
        )

        datahook.events_list['profile'].append('RepairAll')
        datahook.events['profile'].append(
            {'Cost': ['pass_val', 'Cost'],
             'action': [[0, False, 'system', 'val_act', '-', 'var', 'profile-credit_line', 'Cost'],
                        [0, False, 'system', 'val_act', '+', 'var', 'profile-pays', 'Cost']]}
        )

        datahook.events_list['profile'].append('Repair')
        datahook.events['profile'].append(
            {'Cost': ['pass_val', 'Cost'],
             'action': [[0, False, 'system', 'val_act', '-', 'var', 'profile-credit_line', 'Cost'],
                        [0, False, 'system', 'val_act', '+', 'var', 'profile-pays', 'Cost']]}
        )

        datahook.events_list['profile'].append('RefuelPartial')
        datahook.events['profile'].append(
            {'Cost': ['pass_val', 'Cost'],
             'action': [[0, False, 'system', 'val_act', '-', 'var', 'profile-credit_line', 'Cost'],
                        [0, False, 'system', 'val_act', '+', 'var', 'profile-pays', 'Cost']]}
        )

        datahook.events_list['profile'].append('PayFines')
        datahook.events['profile'].append(
            {'Amount': ['pass_val', 'Amount'],
             'action': [[0, False, 'system', 'val_act', '-', 'var', 'profile-credit_line', 'Amount'],
                        [0, False, 'system', 'val_act', '+', 'var', 'profile-pays', 'Amount']]}
        )

        datahook.events_list['profile'].append('BuyTradeData')
        datahook.events['profile'].append(
            {'Cost': ['pass_val', 'Cost'],
             'action': [0, False, 'system', 'val_act', '-', 'var', 'profile-credit_line', 'Cost']}
        )

        datahook.events_list['profile'].append('BuyExplorationData')
        datahook.events['profile'].append(
            {'Cost': ['pass_val', 'Cost'],
             'action': [0, False, 'system', 'val_act', '-', 'var', 'profile-credit_line', 'Cost']}
        )

        datahook.events_list['profile'].append('MultiSellExplorationData')
        datahook.events['profile'].append(
            {'TotalEarnings': ['pass_val', 'TotalEarnings'],
             'action': [0, False, 'system', 'val_act', '+', 'var', 'profile-credit_line', 'TotalEarnings']}
        )

        datahook.events_list['profile'].append('SellExplorationData')
        datahook.events['profile'].append(
            {'TotalEarnings': ['pass_val', 'TotalEarnings'],
             'action': [0, False, 'system', 'val_act', '+', 'var', 'profile-credit_line', 'TotalEarnings']}
        )

        datahook.events_list['profile'].append('BuyAmmo')
        datahook.events['profile'].append(
            {'Cost': ['pass_val', 'Cost'],
             'action': [[0, False, 'system', 'val_act', '-', 'var', 'profile-credit_line', 'Cost'],
                        [0, False, 'system', 'val_act', '+', 'var', 'profile-pays', 'Cost']]}
        )

        datahook.events_list['profile'].append('BuyDrones')
        datahook.events['profile'].append(
            {'TotalCost': ['pass_val', 'TotalCost'],
             'action': [[0, False, 'system', 'val_act', '-', 'var', 'profile-credit_line', 'TotalCost'],
                        [0, False, 'system', 'val_act', '+', 'var', 'profile-pays', 'TotalCost']]}
        )

        datahook.events_list['profile'].append('SellDrones')
        datahook.events['profile'].append(
            {'TotalSale': ['pass_val', 'TotalSale'],
             'action': [[0, False, 'system', 'val_act', '+', 'var', 'profile-credit_line', 'TotalSale'],
                        [0, False, 'system', 'val_act', '-', 'var', 'profile-pays', 'TotalSale']]}
        )

        datahook.events_list['profile'].append('ModuleSell')
        datahook.events['profile'].append(
            {'SellPrice': ['pass_val', 'SellPrice'],
             'action': [[0, False, 'system', 'val_act', '+', 'var', 'profile-credit_line', 'SellPrice'],
                        [0, False, 'system', 'val_act', '-', 'var', 'profile-deposit_line', 'SellPrice']]}
        )

        datahook.events_list['profile'].append('ModuleSellRemote')
        datahook.events['profile'].append(
            {'SellPrice': ['pass_val', 'SellPrice'],
             'action': [[0, False, 'system', 'val_act', '+', 'var', 'profile-credit_line', 'SellPrice'],
                        [0, False, 'system', 'val_act', '-', 'var', 'profile-deposit_line', 'SellPrice']]}
        )

        datahook.events_list['profile'].append('FetchRemoteModule')
        datahook.events['profile'].append(
            {'TransferCost': ['pass_val', 'TransferCost'],
             'action': [0, False, 'system', 'val_act', '-', 'var', 'profile-credit_line', 'TransferCost']}
        )

        datahook.events_list['profile'].append('ModuleBuy')
        datahook.events['profile'].append(
            {'BuyPrice': ['pass_val', 'BuyPrice'],
             'action': [[0, False, 'system', 'val_act', '-', 'var', 'profile-credit_line', 'BuyPrice'],
                        [0, False, 'system', 'val_act', '+', 'var', 'profile-deposit_line', 'BuyPrice']]}
        )

        datahook.events_list['profile'].append('ModuleSell')
        datahook.events['profile'].append(
            {'SellPrice': ['pass_val', 'SellPrice'],
             'action': [[0, False, 'system', 'val_act', '+', 'var', 'profile-credit_line', 'SellPrice'],
                        [0, False, 'system', 'val_act', '-', 'var', 'profile-deposit_line', 'SellPrice']]}
        )

        datahook.events_list['profile'].append('ModuleRetrieve')
        datahook.events['profile'].append(
            {'Cost': ['pass_val', 'Cost'],
             'action': [0, False, 'system', 'val_act', '-', 'var', 'profile-credit_line', 'Cost']}
        )

        datahook.events_list['profile'].append('ShipyardTransfer')
        datahook.events['profile'].append(
            {'TransferPrice': ['pass_val', 'TransferPrice'],
             'action': [0, False, 'system', 'val_act', '-', 'var', 'profile-credit_line', 'TransferPrice']}
        )

        datahook.events_list['profile'].append('SellShipOnRebuy')
        datahook.events['profile'].append(
            {'ShipPrice': ['pass_val', 'ShipPrice'],
             'action': [[0, False, 'system', 'val_act', '+', 'var', 'profile-credit_line', 'ShipPrice'],
                        [0, False, 'system', 'val_act', '-', 'var', 'profile-deposit_line', 'ShipPrice']]}
        )

        datahook.events_list['profile'].append('ShipyardSell')
        datahook.events['profile'].append(
            {'ShipPrice': ['pass_val', 'ShipPrice'],
             'action': [[0, False, 'system', 'val_act', '+', 'var', 'profile-credit_line', 'ShipPrice'],
                        [0, False, 'system', 'val_act', '-', 'var', 'profile-deposit_line', 'ShipPrice']]}
        )

        datahook.events_list['profile'].append('MarketBuy')
        datahook.events['profile'].append(
            {'TotalCost': ['pass_val', 'TotalCost'],
             'action': [0, False, 'system', 'val_act', '-', 'var', 'profile-credit_line', 'TotalCost']}
        )
        datahook.events_list['profile'].append('MarketSell')
        datahook.events['profile'].append(
            {'TotalSale': ['pass_val', 'TotalSale'],
             'action': [0, False, 'system', 'val_act', '+', 'var', 'profile-credit_line', 'TotalSale']}
        )

        datahook.events_list['profile'].append('MissionCompleted')
        datahook.events['profile'].append(
            {'Reward': ['pass_val', 'Reward'],
             'action': [0, False, 'system', 'val_act', '+', 'var', 'profile-credit_line', 'Reward']}
        )

        datahook.events_list['profile'].append('SearchAndRescue')
        datahook.events['profile'].append(
            {'Reward': ['pass_val', 'Reward'],
             'action': [0, False, 'system', 'val_act', '+', 'var', 'profile-credit_line', 'Reward']}
        )

        datahook.events_list['profile'].append('PayBounties')
        datahook.events['profile'].append(
            {'Amount': ['pass_val', 'Amount'],
             'action': [[0, False, 'system', 'val_act', '-', 'var', 'profile-credit_line', 'Amount'],
                        [0, False, 'system', 'val_act', '+', 'var', 'profile-pays', 'Amount']]}
        )

        datahook.events_list['profile'].append('PayFines')
        datahook.events['profile'].append(
            {'Amount': ['pass_val', 'Amount'],
             'action': [[0, False, 'system', 'val_act', '-', 'var', 'profile-credit_line', 'Amount'],
                        [0, False, 'system', 'val_act', '+', 'var', 'profile-pays', 'Amount']]}
        )

        datahook.events_list['profile'].append('PayFines')
        datahook.events['profile'].append(
            {'Amount': ['pass_val', 'Amount'],
             'action': [[0, False, 'system', 'val_act', '-', 'var', 'profile-credit_line', 'Amount'],
                        [0, False, 'system', 'val_act', '+', 'var', 'profile-pays', 'Amount']]}
        )'''


    def save_profile(self):
        prof = {}

        prof['Docked'] = self.docked[0]

        prof['Dock_data'] = self.dock_data

        prof['System_data'] = self.system_data

        prof['Last_dock_data'] = self.last_dock_data

        prof['Last_system_data'] = self.last_system_data

        prof['Last_route'] = self.cur_route

        prof['Ship'] = self.ship

        prof['Ship_materials'] = self.onboard_mats

        prof['Stored_materials'] = self.stored_mats

        prof['Ship_cargo'] = self.onboard_cargo

        prof['Stored_cargo'] = self.stored_cargo

        prof['Stored_ships'] = self.stored_ships

        prof['Stored_modules'] = self.stored_modules

        for k in self.profile.keys():
            prof[k] = self.profile[k]

        print(prof)
        w_data = json.dumps(prof, ensure_ascii=False, indent=4)
        fp = open('data/profile/profile.txt', mode='w', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        fp.write(w_data)
        fp.close()

    def finance_sync(self, fin_data):

        res_list = []

        sync_data = {}
        sync_data['Credit_line'] = fin_data[0]['Current_Wealth']
        sync_data['Deposite_line'] = fin_data[0]['Current_Wealth'] + fin_data[0]['Spent_On_Ships'] + fin_data[0]['Spent_On_Outfitting']
        sync_data['Pays'] = fin_data[0]['Spent_On_Repairs'] + fin_data[0]['Spent_On_Fuel'] + fin_data[0]['Spent_On_Ammo_Consumables'] + fin_data[0]['Spent_On_Insurance'] + fin_data[1]['Total_Fines']

        for k in sync_data.keys():
            if sync_data[k] == self.profile[k]:
                res_list.append(True)
            else:
                res_list.append(False)

        print(res_list)

        if False in res_list:
            return False
        else:
            return True

    @staticmethod
    def loadout(type, data_list, ref_list):

        cur_loadout = {}

        sync_dict = {}

        sync = True

        cur_loadout['Ship_type'] = [data_list[0]]
        cur_loadout['Ship_name'] = [data_list[1]]
        cur_loadout['Ship_ident'] = [data_list[2]]

        for m in data_list[3]:
            if m['Slot'] not in ['PaintJob', 'Decal1', 'Decal2', 'Decal3', 'Decal4', 'Decal5', 'Decal6', 'WeaponColour', 'VesselVoice']:
                cur_loadout[m['Slot']] = [m['Item'], m['Health'], m['Priority'], m['On']]
                if 'Engineering' in m.keys():
                    cur_loadout[m['Slot']].append(m['Engineering']['BlueprintName'] + '_' + str(m['Engineering']['Level']))

        for m in cur_loadout.keys():
            eng = False
            if m in ref_list.keys():
                m_name = cur_loadout[m][0]
                pr_name = ref_list[m][0]
                sync_dict[m] = []

                if len(cur_loadout[m]) == 5:  # engeneered
                    if m_name == pr_name:
                        if len(ref_list[m]) < 5:
                            sync_dict[m].append('eng')
                            eng = True
                    m_name += '##' + cur_loadout[m][4]

                if len(ref_list[m]) == 5:  # engeneered
                    if m_name == pr_name:
                        if len(cur_loadout[m]) < 5:
                            sync_dict[m].append('deeng')
                            eng = True
                    pr_name += '##' + ref_list[m][4]

                if eng is False:
                    if m_name == pr_name:
                        sync_dict[m].append('pass')
                    else:
                        sync_dict[m].append('fail')
                sync_dict[m].append(m_name)
                sync_dict[m].append(pr_name)

            else:
                m_name = cur_loadout[m][0]
                if len(cur_loadout[m]) == 5:  # engeneered
                    m_name += '##' + cur_loadout[m][4]

                sync_dict[m] = ['new', m_name, 'no_ref']

        sync_types = {
            'sync': ((), ('pass',)),
            'sync+': ((), ('pass', 'new')),
            'eng': ((), ('pass', 'eng', 'deeng')),
            'eng+': ((), ('pass', 'eng', 'deeng', 'new')),
            'nn_sync': (('Ship_type', 'Ship_name', 'Ship_ident'), ('pass',)),
            'nn_sync+': (('Ship_type', 'Ship_name', 'Ship_ident'), ('pass', 'new')),
            'nn_eng': (('Ship_type', 'Ship_name', 'Ship_ident'), ('pass', 'eng', 'deeng')),
            'nn_eng+': (('Ship_type', 'Ship_name', 'Ship_ident'), ('pass', 'eng', 'deeng', 'new')),
        }

        for s in sync_dict.keys():
            if s not in sync_types[type][0]:
                if sync_dict[s][0] not in sync_types[type][1]:
                    sync = False

        return sync, cur_loadout

    @staticmethod
    def dock_sync(dock_data, ref_data):
        result = 0
        for di in dock_data:
            if di in ref_data:
                result += 1

        if result == len(ref_data):
            return True
        else:
            return False

    @staticmethod
    def system_sync(system_data, ref_data):
        result = 0
        for si in system_data:
            if si in ref_data:
                result += 1

        if result == len(ref_data):
            return True
        else:
            return False

    def cr_profile_wiget(self, frame, size, row, column, height):

        def cr_blocks(cur, cap):
            return "[" + "◼" * cur + "◻" * (cap - cur) + "]"

        if size == 'small':
            profile_wiget = CrItem()

            profile_wiget.s_row = row
            profile_wiget.s_collumn = column
            profile_wiget.h_bor = height
            profile_wiget.construct.append({"type": "line", "long": False, "show": True, "pady": (0, 0)})
            profile_wiget.construct.append({"type": "img+label", "img": "NPC-actor", "style": ["Custom_sm_lt.TLabel", "nw"], "long": False,
                                            "text": '[CMDR]: ' + self.profile['Commander'] + '\n\n[УР]: ' + str(self.profile['Level']) + '\n[EXP]: ' + str(self.profile['Exp']) + '\n[HP]: ' + cr_blocks(
                                                self.profile['Health'], 10) + '\n[ST]: ' + cr_blocks(self.profile['Distress'], 10)})
            profile_wiget.construct.append({"type": "label", "style": ["Custom_sm_lt.TLabel", "nw"], "long": False,
                                            "text": "Статусы: " + self.profile['Statuses'] + "\n\nБанковский счет:\nКредиты: " + str(self.profile['Wallet_cr']) + "\nЭвриалы: " + str(
                                                self.profile['Wallet_other']['eur']) + "\nКр. линия: " + str(self.profile['Credit_line'])})

            profile_wiget.construct.append({"type": "btn", "style": "Custom.TButton", "long": False, "btn_data": [{"state": "enabled", "text": "ЭКП", "columnspan": 1, "action": [0, False, "mw1", 'profile', 'inventory']},
                                                                                                                  {"state": "enabled", "text": "ИНВЕНТАРЬ", "columnspan": 2,
                                                                                                                   "action": [0, False, "mw1", 'profile', 'used_inv']}]})

            profile_wiget.construct.append({"type": "line", "long": False, "show": True, "pady": (0, tx_bor)})

            profile_wiget.construct.append({"type": "btn", "style": "Custom.TButton", "long": False, "btn_data": [{"state": "enabled", "text": "СПТ", "columnspan": 1, "action": [0, False, "mw1", 'profile', 'special']},
                                                                                                                  {"state": "enabled", "text": "НВК", "columnspan": 1,
                                                                                                                   "action": [0, False, "mw1", 'profile', 'percs']},
                                                                                                                  {"state": "enabled", "text": "ИМП", "columnspan": 1,
                                                                                                                   "action": [0, False, "mw1", 'profile', 'inplants']}]})

            profile_wiget.construct.append({"type": "btn", "style": "Custom.TButton", "long": False, "btn_data": [{"state": "enabled", "text": "ДНВ", "columnspan": 1, "action": [0, False, "mw1", 'profile', 'journal']},
                                                                                                                  {"state": "enabled", "text": "РЕП", "columnspan": 1,
                                                                                                                   "action": [0, False, "mw1", 'profile', 'reputation']},
                                                                                                                  {"state": "enabled", "text": "КМД", "columnspan": 1, "action": [0, False, "mw1", 'profile', 'crew']}]})
            profile_wiget.construct.append({"type": "line", "long": False, "show": True, "pady": (0, tx_bor)})

            profile_wiget.cr_fr_it(frame, height, (tx_bor, 0))
            profile_wiget.start_construct()
            return profile_wiget.s_row


class OverLay:
    def __init__(self):
        print("overlay start")
        self.task_showed = False
        self.call_action = "mainwindow"

        self.task_frame = tkinter.ttk.Frame(root, style="Custom_olay.TFrame", height=bor * 14, width=(sett.resolution[0] - (bor * 10)))
        self.task_frame.grid(row=1, column=1, columnspan=3, padx=bor * 5, pady=((tx_bor * sett.gui_data['task_frame_bor'][0]), (tx_bor * sett.gui_data['task_frame_bor'][1])), sticky="nsew")
        self.task_frame.grid_propagate(False)

        left_frame = tkinter.ttk.Frame(root, style="Custom_olay.TFrame", height=bor * 9, width=bor * 30)
        left_frame.grid(row=3, column=1, padx=bor, pady=((tx_bor * sett.gui_data['left_frame_bor'][0]), (tx_bor * sett.gui_data['left_frame_bor'][1])), sticky="sw")
        left_frame.grid_propagate(False)

        self.right_frame = tkinter.ttk.Frame(root, style="Custom_olay.TFrame", height=bor * 20, width=bor * 30)
        self.right_frame.grid(row=3, column=3, padx=bor, pady=((tx_bor * sett.gui_data['right_frame_bor'][0]), (tx_bor * sett.gui_data['right_frame_bor'][1])), sticky="nsew")
        self.right_frame.grid_propagate(False)

        self.bottom_frame = tkinter.ttk.Frame(root, style="Custom_olay.TFrame", height=bor * 6, width=bor * 93)
        self.bottom_frame.grid(row=3, column=2, padx=bor, pady=((tx_bor * sett.gui_data['bottom_frame_bor'][0]), (tx_bor * sett.gui_data['bottom_frame_bor'][1])), sticky="sew")
        self.bottom_frame.grid_propagate(False)

        self.cent_frame = tkinter.ttk.Frame(root, style="Custom_olay.TFrame", height=bor * 36, width=bor * 20)
        self.cent_frame.grid(row=2, column=1, columnspan=3, sticky="nsew", pady=((tx_bor * sett.gui_data['cent_frame_bor'][0]), (tx_bor * sett.gui_data['cent_frame_bor'][1])))
        self.cent_frame.grid_propagate(False)

        self.state_list = ['', '', '', '', '']
        self.state_text = tkinter.StringVar()
        self.state_text.set("\n".join(self.state_list))
        tkinter.ttk.Label(left_frame, textvariable=self.state_text, style=sett.gui_data["state_style"], anchor="center", justify="center").grid(row=1, column=1, columnspan=2, sticky="nsew")

        # tkinter.ttk.Label(self.cent_frame, text="Загрузка...", style="Custom_sm.TLabel", anchor="center", justify="center", width=40).grid(row=1, column=1, columnspan=2, sticky="nsew")

        # tkinter.ttk.Label(self.cent_frame, text="Загрузка...", style="Custom_sm.TLabel", anchor="center", justify="center", width=40).grid(row=1, column=1, columnspan=2, sticky="nsew")

    def add_state_item(self, text, sound_type):
        if self.state_list[0] == '':
            if audio.play_sound('notif', sound_type) is True:
                self.state_list.reverse()
                for i in range(5):
                    if self.state_list[i] == '':
                        self.state_list[i] = text
                        time = 5
                        guitimer.add_timer([time, False, 'olay', 'remove_state_item'])
                        self.state_list.reverse()
                        self.state_text.set("\n".join(self.state_list))
                        break

            else:
                guitimer.add_timer([10, False, 'olay', 'add_state_item', text, sound_type])

        else:
            guitimer.add_timer([5, False, 'olay', 'add_state_item', text, sound_type])

    def remove_state_item(self):
        del self.state_list[-1]
        self.state_list.insert(0, '')
        self.state_text.set("\n".join(self.state_list))

    def show_task(self, task_text, task_extra=""):
        tkinter.ttk.Label(self.task_frame, text=task_text, style=sett.gui_data["task_text"], anchor="center", justify="center", width=80).grid(row=1, column=1, columnspan=2, sticky="nsew")
        tkinter.ttk.Label(self.task_frame, text=task_extra, style=sett.gui_data["task_extra"], anchor="center", justify="center", width=80).grid(row=2, column=1, columnspan=2, sticky="nsew")
        self.task_showed = True
        time = 5
        guitimer.add_timer([time, False, 'olay', 'clear_frame', 'task_frame'])

    def show_bottom(self, text, act=None, time=5, ui=None):
        if act is not None:
            action.do_action([0, False, 'keys', 'change_action', act])

        if ui is not None:
            audio.play_sound('ui', ui)
            guitimer.add_timer([time, False, 'audio', 'restore_vol', 'ui'])

        tkinter.ttk.Label(self.bottom_frame, text=text, style=sett.gui_data["bottom_text"], anchor="center", justify="center", width=49).grid(row=1, column=1, sticky="nsew")

        guitimer.add_timer([time, False, 'olay', 'clear_frame', 'bottom_frame'])
        guitimer.add_timer([time + 1, False, 'keys', 'change_action', 'mainwindow'])

    @staticmethod
    def clear_frame(frame):
        for w in frame.grid_slaves():
            w.grid_forget()


class AudioDrive:
    def __init__(self):
        mixer.init(frequency=44100, size=-16, channels=4, buffer=4096)
        self.ui = mixer.Channel(0)
        self.voice = mixer.Channel(1)
        self.sfx = mixer.Channel(2)
        self.notif = mixer.Channel(3)
        self.assistant = mixer.Channel(4)
        self.extra = mixer.Channel(5)
        self.music = mixer.Channel(6)

        self.ui.set_volume(sett.sound_levels['ch_ui'])
        self.voice.set_volume(sett.sound_levels['ch_voice'])
        self.sfx.set_volume(sett.sound_levels['ch_sfx'])
        self.notif.set_volume(sett.sound_levels['ch_notif'])
        self.assistant.set_volume(sett.sound_levels['ch_assistant'])
        self.extra.set_volume(sett.sound_levels['ch_extra'])
        self.music.set_volume(sett.sound_levels['ch_music'])
        mixer.music.set_volume(sett.sound_levels['ch_music'])

    def play_sound(self, channel, sound_name, path=None, pos=None):

        if channel == 'ui':
            if sound_name in ['call', 'click', 'fail', 'failed', 'miss', 'complete']:
                u = mixer.Sound("data/audio/" + sound_name + ".ogg")
            else:
                u = mixer.Sound(path)
            sound_len = round(u.get_length(), 1) + 0.2
            if self.ui.get_busy() == 1:
                self.ui.stop()
            self.silence_mode('ui', sound_len)
            self.ui.play(u)

        elif channel == 'notif':
            if sound_name in ['message', 'stage', 'notif', 'notific', 'obj']:
                n = mixer.Sound("data/audio/" + sound_name + ".ogg")
            else:
                n = mixer.Sound(path)
            sound_len = round(n.get_length(), 1) + 0.2
            if self.voice.get_busy() == 1:
                print('notif False')
                return False

            if self.ui.get_busy() == 1:
                guitimer.add_timer([2, False, 'audio', 'play_sound', channel, sound_name, path])
            else:
                self.silence_mode('notif', sound_len)
                self.notif.play(n)
                return True

        elif channel == 'voice':
            self.voice.stop()
            v = mixer.Sound(path)
            sound_len = round(v.get_length(), 1) + 0.2
            self.silence_mode('voice', sound_len)
            self.voice.play(v)

        elif channel == 'sfx':
            self.sfx.stop()
            s = mixer.Sound(path)
            sound_len = round(s.get_length(), 1) + 0.2
            self.silence_mode('sfx', sound_len)
            self.sfx.play(s)

        elif channel == 'assistant':
            self.assistant.stop()
            a = mixer.Sound(path)
            sound_len = round(a.get_length(), 1) + 0.2
            self.silence_mode('assistant', sound_len)
            self.assistant.play(a)

        elif channel == 'extra':
            self.extra.stop()
            e = mixer.Sound(path)
            sound_len = round(e.get_length(), 1) + 0.2
            self.silence_mode('extra', sound_len)
            self.extra.play(e)

        elif channel == 'music':
            self.music.stop()
            m = mixer.Sound(path)
            sound_len = round(m.get_length(), 1) + 0.5
            self.silence_mode('music', sound_len)
            self.music.play(m)

        elif channel == 'music_rep':
            self.music.stop()
            mixer.music.load(path + sound_name + ".mp3")
            mixer.music.play(-1)

        elif channel == 'music_pos':
            self.music.stop()
            mixer.music.load(path + sound_name + ".mp3")
            mixer.music.play(1, int(guitimer.c_time // 10))

        elif channel == 'music_pos_rep':
            self.music.stop()
            mixer.music.load(path + sound_name + ".mp3")
            mixer.music.play(-1, pos)

    def silence_mode(self, channel, lenght, restore=False):
        if channel == 'ui':
            self.voice.set_volume(round((sett.sound_levels['ch_voice'] * 0.8), 2))
            if self.voice.get_busy() == 0:
                self.sfx.set_volume(round((sett.sound_levels['ch_sfx'] * 0.8), 2))
                if self.sfx.get_busy() == 0:
                    self.notif.set_volume(round((sett.sound_levels['ch_notif'] * 0.8), 2))
                    if self.notif.get_busy() == 0:
                        self.assistant.set_volume(round((sett.sound_levels['ch_assistant'] * 0.4), 2))
                        if self.assistant.get_busy() == 0:
                            self.extra.set_volume(round((sett.sound_levels['ch_extra'] * 0.4), 2))
                            if self.assistant.get_busy() == 0:
                                self.music.set_volume(round((sett.sound_levels['ch_music'] * 0.4), 2))
                                mixer.music.set_volume(round((sett.sound_levels['ch_music'] * 0.4), 2))

        elif channel == 'voice':
            self.sfx.set_volume(round((sett.sound_levels['ch_sfx'] * 0.4), 2))
            self.notif.set_volume(round((sett.sound_levels['ch_notif'] * 0.0), 2))
            self.assistant.set_volume(round((sett.sound_levels['ch_assistant'] * 0.0), 2))
            self.extra.set_volume(round((sett.sound_levels['ch_extra'] * 0.0), 2))
            self.music.set_volume(round((sett.sound_levels['ch_music'] * 0.0), 2))
            mixer.music.set_volume(round((sett.sound_levels['ch_music'] * 0.0), 2))

        elif channel == 'sfx':
            if self.voice.get_busy() == 0:
                self.notif.set_volume(round((sett.sound_levels['ch_notif'] * 0.8), 2))
                if self.notif.get_busy() == 0:
                    self.assistant.set_volume(round((sett.sound_levels['ch_assistant'] * 0.6), 2))
                    if self.assistant.get_busy() == 0:
                        self.extra.set_volume(round((sett.sound_levels['ch_extra'] * 0.4), 2))
                        if self.extra.get_busy() == 0:
                            self.music.set_volume(round((sett.sound_levels['ch_music'] * 0.4), 2))
                            mixer.music.set_volume(round((sett.sound_levels['ch_music'] * 0.4), 2))
                        else:
                            self.music.set_volume(round((sett.sound_levels['ch_music'] * 0.0), 2))
                            mixer.music.set_volume(round((sett.sound_levels['ch_music'] * 0.0), 2))
                    else:
                        self.extra.set_volume(round((sett.sound_levels['ch_extra'] * 0.0), 2))
                        self.music.set_volume(round((sett.sound_levels['ch_music'] * 0.0), 2))
                        mixer.music.set_volume(round((sett.sound_levels['ch_music'] * 0.0), 2))

                else:
                    self.assistant.set_volume(round((sett.sound_levels['ch_assistant'] * 0.6), 2))
                    self.extra.set_volume(round((sett.sound_levels['ch_extra'] * 0.0), 2))
                    self.music.set_volume(round((sett.sound_levels['ch_music'] * 0.0), 2))
                    mixer.music.set_volume(round((sett.sound_levels['ch_music'] * 0.0), 2))

        elif channel == 'notif':
            if self.voice.get_busy() == 0 and self.sfx.get_busy() == 0:
                self.assistant.set_volume(round((sett.sound_levels['ch_assistant'] * 0.6), 2))
                if self.assistant.get_busy() == 0:
                    self.extra.set_volume(round((sett.sound_levels['ch_extra'] * 0.6), 2))
                    if self.extra.get_busy() == 0:
                        self.music.set_volume(round((sett.sound_levels['ch_music'] * 0.6), 2))
                    else:
                        self.music.set_volume(round((sett.sound_levels['ch_music'] * 0.0), 2))
                        mixer.music.set_volume(round((sett.sound_levels['ch_music'] * 0.0), 2))
                else:
                    self.extra.set_volume(round((sett.sound_levels['ch_extra'] * 0.0), 2))
                    self.music.set_volume(round((sett.sound_levels['ch_music'] * 0.0), 2))
                    mixer.music.set_volume(round((sett.sound_levels['ch_music'] * 0.0), 2))

        elif channel == 'assistant':
            if self.voice.get_busy() == 0 and self.sfx.get_busy() == 0 and self.notif.get_busy() == 0:
                self.extra.set_volume(round((sett.sound_levels['ch_extra'] * 0.0), 2))
                self.music.set_volume(round((sett.sound_levels['ch_music'] * 0.0), 2))
                mixer.music.set_volume(round((sett.sound_levels['ch_music'] * 0.0), 2))

        elif channel == 'extra':
            if self.voice.get_busy() == 0 and self.sfx.get_busy() == 0 and self.notif.get_busy() == 0 and self.assistant.get_busy() == 0:
                self.music.set_volume(round((sett.sound_levels['ch_music'] * 0.0), 2))
                mixer.music.set_volume(round((sett.sound_levels['ch_music'] * 0.0), 2))

        if restore is False:
            guitimer.add_timer([lenght, False, 'audio', 'restore_vol', channel])

    def restore_vol(self, channel):
        if channel == 'ui':
            self.ui.stop()
            self.voice.set_volume(sett.sound_levels['ch_voice'])
            if self.voice.get_busy() == 0:
                self.sfx.set_volume(sett.sound_levels['ch_sfx'])
                if self.sfx.get_busy() == 0:
                    self.notif.set_volume(sett.sound_levels['ch_notif'])
                    if self.notif.get_busy() == 0:
                        self.assistant.set_volume(sett.sound_levels['ch_assistant'])
                        if self.assistant.get_busy() == 0:
                            self.extra.set_volume(sett.sound_levels['ch_extra'])
                            if self.assistant.get_busy() == 0:
                                self.music.set_volume(sett.sound_levels['ch_music'])
                                mixer.music.set_volume(sett.sound_levels['ch_music'])

        elif channel == 'voice':
            self.voice.stop()
            self.voice.set_volume(sett.sound_levels['ch_voice'])
            self.sfx.set_volume(sett.sound_levels['ch_sfx'])
            if self.sfx.get_busy() == 0:
                self.notif.set_volume(sett.sound_levels['ch_notif'])
                if self.notif.get_busy() == 0:
                    self.assistant.set_volume(sett.sound_levels['ch_assistant'])
                    if self.assistant.get_busy() == 0:
                        self.extra.set_volume(sett.sound_levels['ch_extra'])
                        if self.extra.get_busy() == 0:
                            self.music.set_volume(sett.sound_levels['ch_music'])
                            mixer.music.set_volume(sett.sound_levels['ch_music'])
                        else:
                            self.silence_mode('extra', 0, True)
                    else:
                        self.silence_mode('assistant', 0, True)
                else:
                    self.silence_mode('notif', 0, True)
            else:
                self.silence_mode('sfx', 0, True)

        elif channel == 'sfx':
            self.sfx.stop()
            self.sfx.set_volume(sett.sound_levels['ch_sfx'])
            if self.voice.get_busy() == 0:
                self.notif.set_volume(sett.sound_levels['ch_notif'])
                if self.notif.get_busy() == 0:
                    self.assistant.set_volume(sett.sound_levels['ch_assistant'])
                    if self.assistant.get_busy() == 0:
                        self.extra.set_volume(sett.sound_levels['ch_extra'])
                        if self.extra.get_busy() == 0:
                            self.music.set_volume(sett.sound_levels['ch_music'])
                            mixer.music.set_volume(sett.sound_levels['ch_music'])
                        else:
                            self.silence_mode('extra', 0, True)
                    else:
                        self.silence_mode('assistant', 0, True)
                else:
                    self.silence_mode('notif', 0, True)

        elif channel == 'notif':
            self.notif.stop()
            self.notif.set_volume(sett.sound_levels['ch_notif'])
            if self.voice.get_busy() == 0 and self.sfx.get_busy() == 0:
                self.assistant.set_volume(sett.sound_levels['ch_assistant'])
                if self.assistant.get_busy() == 0:
                    self.extra.set_volume(sett.sound_levels['ch_extra'])
                    if self.extra.get_busy() == 0:
                        self.music.set_volume(sett.sound_levels['ch_music'])
                        mixer.music.set_volume(sett.sound_levels['ch_music'])
                    else:
                        self.silence_mode('extra', 0, True)
                else:
                    self.silence_mode('assistant', 0, True)

        elif channel == 'assistant':
            self.assistant.stop()
            self.assistant.set_volume(sett.sound_levels['ch_assistant'])
            if self.voice.get_busy() == 0 and self.sfx.get_busy() == 0 and self.notif.get_busy() == 0:
                self.extra.set_volume(sett.sound_levels['ch_extra'])
                if self.extra.get_busy() == 0:
                    self.music.set_volume(sett.sound_levels['ch_music'])
                    mixer.music.set_volume(sett.sound_levels['ch_music'])
                else:
                    self.silence_mode('extra', 0, True)

        elif channel == 'extra':
            self.extra.stop()
            self.extra.set_volume(sett.sound_levels['ch_extra'])
            if self.voice.get_busy() == 0 and self.sfx.get_busy() == 0 and self.notif.get_busy() == 0 and self.assistant.get_busy() == 0:
                self.music.set_volume(sett.sound_levels['ch_music'])
                mixer.music.set_volume(sett.sound_levels['ch_music'])

# создать класс, топ вью в инит список параметров - время работы, количество шагов, заголовок, есть ли строка над, лист строки над, индикатор у строки над или в центре, возможность неудачи,  текст кнопки успеха, текст кнопки неудачи
# сначала рандомом если шанс фейла - рассчитываем и разбивается на лист время и шаги, посылается  в гуи таймер а он шлет некст степ, он обновляет бар, текущий текст и каунтер


class TopWin:
    def __init__(self, master=None):
        self.showed = False

        self.showed_2 = False

        self.tkintvar = tkinter.IntVar()
        self.tkintvar2 = tkinter.IntVar()
        self.tkintvar3 = tkinter.IntVar()
        self.tkintvar4 = tkinter.IntVar()
        self.tkstrvar1 = tkinter.StringVar()
        self.tkstrvar2 = tkinter.StringVar()
        self.tkstrvar3 = tkinter.StringVar()
        self.tkstrvar4 = tkinter.StringVar()
        self.header = None

        self.win = None
        self.win2 = None

    @staticmethod
    def read_file(path, f_name):
        fp = open(path + f_name, mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        read_data = json.loads(fp.read())
        fp.close()
        return read_data

    @staticmethod
    def write_data(path, f_name, w_data):
        w_data = json.dumps(w_data, ensure_ascii=False, indent=4)
        fp = open(path + f_name, mode='w', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        fp.write(w_data)
        fp.close()

    def create_win(self, title, height, width, pad_x, pad_y, curs="none"):

        if self.showed is False:
            self.win = tkinter.Toplevel(master=root, height=bor * height, width=bor * width, cursor=curs, background=sett.bg_col)

            self.win.title(title)

            self.win.wm_attributes('-topmost', True)
            self.win.resizable(False, False)
            self.win.overrideredirect(True)
            self.win.lift()
            self.win.geometry('+' + str(bor * pad_x) + '+' + str(bor * pad_y))
            self.showed = True
            self.win.event_generate('<Motion>', warp=True, x=bor * pad_x, y=bor * pad_y)
            return True
        else:
            return False

    def create_win2(self, title, height, width, pad_x, pad_y, curs="none"):

        if self.showed_2 is False:
            self.win2 = tkinter.Toplevel(master=root, height=bor * height, width=bor * width, cursor=curs, background=sett.bg_col)

            self.win2.title(title)

            self.win2.wm_attributes('-topmost', True)
            self.win2.resizable(False, False)
            self.win2.overrideredirect(True)
            self.win2.lift()
            self.win2.geometry('+' + str(bor * pad_x) + '+' + str(bor * pad_y))
            self.showed_2 = True
            self.win2.event_generate('<Motion>', warp=True, x=bor * pad_x, y=bor * pad_y)
            return True
        else:
            return False

    def show_text_tip(self, size, time, header, text, closable=True):

        if size == 's':
            sizes = (60, 30, 65, 20)

        elif size == 'm':
            sizes = (60, 42, 60, 20)

        elif size == 'l':
            sizes = (60, 60, 50, 20)

        elif size == 'xl':
            sizes = (60, 81, 39, 20)

        self.create_win2(header, sizes[0], sizes[1], sizes[2], sizes[3], curs='@cross_or.cur')
        self.win2.grab_set()
        main_frame = tkinter.ttk.Frame(self.win2, style="Custom_b.TFrame", height=bor * sizes[0], width=bor * sizes[1])
        main_frame.grid_configure(row=0, rowspan=6, column=0, columnspan=3, sticky="ns", ipadx=bor, ipady=bor)
        main_frame.grid_propagate(False)

        col_s = (sizes[1] // 3)

        main_frame.grid_columnconfigure(0, minsize=bor * col_s)
        main_frame.grid_columnconfigure(1, minsize=bor * col_s)
        main_frame.grid_columnconfigure(2, minsize=bor * col_s)



        text_tip = CrItem()

        text_tip.col_width = col_s
        text_tip.s_row = 0
        text_tip.s_collumn = 0
        text_tip.h_bor = sizes[0] + 1



        if time > 0:
            guitimer.add_timer([time, False, 'top_win', 'kill_win2'])


        text_tip.construct.append({"type": "label", "style": ["Custom_sm_lt_c.TLabel", "center"], "long": False, "text": header})
        text_tip.construct.append({"type": "line", "long": False, "show": True, "pady": (0, tx_bor)})
        text_tip.construct.append({"type": "text", "style": {}, "long": True, "slider": True, "glob": False, "text_list": text, 'padx': (0, bor)})

        text_tip.construct.append({"type": "btn", "style": "Custom.TButton", "long": False, "btn_data": [
            {"state": "enabled", "text": "✖", "columnspan": 3, "action": [0, False, 'top_win', 'kill_win2', '']}]})

        text_tip.cr_fr_it(main_frame, 1, (tx_bor, 0))
        text_tip.start_construct()

    def show_password_breaker(self, type, header, hardness, pswrd, actions_list):

        type = type.split('_')

        if len(type) > 1:

            topwin.show_progress_bar(2, 2, {'label_max': 100, 'label_max_val': '%', 'label_header': 'Загрузка' + ' [ pass_hack_0_0_1 ]',
                                                      'label_suc': 'Загрузка успешна',
                                                      'label_fail': 'Ошибка загрузки', 'final': True, 'label_step': 'Процесс загрузки' + '...',
                                                      'on_end': [[2, False, "top_win", "show_password_breaker", type[0], header, hardness, pswrd, actions_list]]})
        else:


            type = type[0]

            def calc_clicks():
                cli = clicks[0]
                cli_str = '['
                for cl in range(clicks[1]):
                    if cli > 0:
                        cli_str += '◼'
                        cli -= 1
                    else:
                        cli_str += '◻'
                cli_str += ']'
                return cli_str

            def hyperlink(tag, act):
                id = int(tag.split("_")[1])
                if act == "Leave":
                    txt.tag_config(tag, foreground=sett.fg_col, background=sett.bg_col)
                    self.tkstrvar1.set('> ')
                    txt.update()

                elif act == "Enter":
                    txt.tag_config(tag, foreground=sett.bg_col, background=sett.fg_col)
                    self.tkstrvar1.set('> ' + attractors_list[id])
                    txt.update()

                elif act == "ButtonPress":
                    txt.tag_config(tag, foreground=sett.fg_col_cont, background=sett.bg_col)
                    txt.tag_bind(tag, "<Enter>", lambda a="on", t=tag: hyperlink(t, str(a.type) + "_pr"))
                    txt.tag_bind(tag, "<Leave>", lambda a="on", t=tag: hyperlink(t, str(a.type) + "_pr"))
                    txt.tag_bind(tag, "<Button-1>", lambda a="Click", t=tag: hyperlink(t, str(a.type) + "_pr"))
                    txt.update()

                    if id == password[0]:
                        tkinter.ttk.Label(main_frame, text='/ / / ' + sett.lang['mini_games']['password_breaker']['label_success'][0] + '\ \ \ \n\n' + sett.lang['mini_games']['password_breaker']['label_success'][1],
                                          style='Custom.TLabel', anchor="center").grid(row=0, rowspan=4, column=0, columnspan=2, sticky="nsew", padx=bor, pady=bor)
                        audio.play_sound('ui', 'complete')
                        guitimer.add_timer([3, False, 'top_win', 'kill_win'])
                        guitimer.add_timer([4, False, 'olay', 'add_state_item', sett.lang['state_items']['mini_games']['pb_success'], 'obj'])
                        if actions_list[0][0] > 0:
                            guitimer.add_timer(actions_list[0])
                        else:
                            action.do_action(actions_list[0])
                    else:
                        audio.play_sound('ui', 'miss')
                        clicks[0] += 1
                        self.tkstrvar3.set(sett.lang['mini_games']['password_breaker']['count_try'] + calc_clicks())
                        if clicks[0] == clicks[1]:
                            tkinter.ttk.Label(main_frame, text='/ / / ' + sett.lang['mini_games']['password_breaker']['label_failed'][0] + '\ \ \ \n\n' + sett.lang['mini_games']['password_breaker']['label_failed'][1],
                                              style='Custom.TLabel', anchor="center").grid(row=0, rowspan=4, column=0, columnspan=2, sticky="nsew", padx=bor, pady=bor)
                            audio.play_sound('ui', 'failed')
                            guitimer.add_timer([3, False, 'top_win', 'kill_win'])
                            guitimer.add_timer([4, False, 'olay', 'add_state_item', sett.lang['state_items']['mini_games']['pb_failed'], 'obj'])
                            if actions_list[1][2] == 'show_password_breaker' and actions_list[1][3] == 'redo':
                                guitimer.add_timer([3, False, 'top_win', 'show_password_breaker', type, header, hardness, pswrd, actions_list])
                            else:
                                if actions_list[1][0] > 0:
                                    guitimer.add_timer(actions_list[1])
                                else:
                                    action.do_action(actions_list[1])

                        cr_ords = 0
                        for l in range(len(password[1])):
                            cr_ords += attractors_list[id].count(password[1][l].lower())
                        if cr_ords > 0:
                            if clicks[0] == 6:
                                old_str = '> ' + sett.lang['mini_games']['password_breaker']['clear_bufer']
                            else:
                                old_str = self.tkstrvar2.get()
                            self.tkstrvar2.set(old_str + '\n\n> ' + attractors_list[id] + '\n> [' + str(cr_ords) + '/' + str(len(attractors_list[id])) + ']')
                        else:
                            if clicks[0] == 6:
                                old_str = sett.lang['mini_games']['password_breaker']['clear_bufer']
                            else:
                                old_str = self.tkstrvar2.get()
                            self.tkstrvar2.set(old_str + '\n\n> ' + attractors_list[id] + '\n> [0/' + str(len(attractors_list[id])) + ']')

            attractors = 10

            clicks = [0, 6]

            password = (randint(0, attractors - 1), pswrd)

            hex_addr = randint(10000, 64000)

            attractors_list = []

            line_width = 69

            lines = 15

            line_lenght = lines * line_width

            line_lenght -= lines * 10  # hex data

            pass_line = ''
            symbols = ['..', '..', '..', '`~!@#№$%^&*()_-+=[]{}|/?><,...;:"', '`~!@#№$%^&*()_-+=[]{}|/?><,...;:"',
                       '`~!@#№$%^&*()_-+=[]{}|/?><,...;:"', '`~!@#№$%^&*()_-+=[]{}|/?><,...;:"',
                       'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM', '0123456789']

            for at in range(attractors):
                rand = randint(0, 99999)
                if rand in attractors_list:
                    rand = randint(0, 99999)
                attractors_list.append(rand)

            attractors_list = sorted(attractors_list)



            with open('data/mini_data/pass_list_' + str(randint(0, 9)) + '.txt') as fp:
                aend = attractors_list[-1]
                for i, line in enumerate(fp):
                    if i in attractors_list:
                        passw = line[:-1]
                        attractors_list[attractors_list.index(i)] = passw
                        line_lenght -= len(str(passw)) + 2
                    elif i > aend + 1:
                        break
            fp.close()

            line_lenght += len(attractors_list[password[0]]) - len(password[1])
            attractors_list[password[0]] = password[1]

            symb_seq = [False, False, False]
            for s in range(line_lenght):
                symb_type = randint(0, len(symbols) - 1)
                if symb_type > 6:
                    symb_seq.append(True)
                else:
                    symb_seq.append(False)
                if symb_seq[1] and symb_seq[2] and symb_seq[3] is True:
                    symb_type = randint(0, 1)
                    symb_seq[3] = symb_type

                del symb_seq[0]
                pass_line += symbols[symb_type][randint(0, len(symbols[symb_type]) - 1)]



            self.create_win('MIEX PassBreaker', 50, 80, 40, 15, curs='@cross_or.cur')

            main_frame = tkinter.ttk.Frame(self.win, style="Custom_b.TFrame", height=bor * 39, width=bor * 80)
            main_frame.grid_configure(row=0, rowspan=3, column=0, columnspan=2, sticky="ns")
            main_frame.grid_propagate(False)

            main_frame.grid_columnconfigure(0, minsize=bor * 60)
            main_frame.grid_columnconfigure(1, minsize=bor * 20)

            main_frame.grid_rowconfigure(0, minsize=bor * 2)
            main_frame.grid_rowconfigure(1, minsize=bor * 2)
            main_frame.grid_rowconfigure(2, minsize=bor * 30)
            main_frame.grid_rowconfigure(3, minsize=bor * 1)

            self.tkstrvar3.set(sett.lang['mini_games']['password_breaker']['count_try'] + calc_clicks())
            tkinter.ttk.Label(main_frame, textvariable=self.tkstrvar3, style='Custom_term.TLabel', anchor="nw").grid(row=1, column=0, columnspan=3, sticky="nw", padx=bor, pady=(tx_bor, 0))

            txt = tkinter.Text(main_frame, height=15, width=69, selectbackground=sett.bg_col, borderwidth=0, background=sett.bg_col, foreground=sett.fg_col, font='Consolas' + ' ' + str((tx_bor * 2) + 2),
                               cursor='@cross_or.cur')

            txt.tag_config("fg_col", foreground=sett.fg_col)
            txt.tag_config("fg_col_d", foreground=sett.fg_col_d)
            txt.tag_config("fg_col2", foreground=sett.fg_col2)
            txt.tag_config("fg_col_cont", foreground=sett.fg_col_cont)

            for tg in range(attractors):
                tag = "attr_" + str(tg)
                txt.tag_config(tag, foreground=sett.fg_col, background=sett.bg_col)
                txt.tag_bind(tag, "<Enter>", lambda a="on", t=tag: hyperlink(t, str(a.type)))
                txt.tag_bind(tag, "<Leave>", lambda a="off", t=tag: hyperlink(t, str(a.type)))
                txt.tag_bind(tag, "<Button-1>", lambda a="Click", t=tag: hyperlink(t, str(a.type)))

            block_len = len(pass_line) // attractors
            for att in range(attractors):
                block_pl = randint(1, block_len - 1)
                txt.insert("end", pass_line[:block_pl], "fg_col")
                txt.insert("end", ' ' + attractors_list[att] + ' ', "attr_" + str(att))
                txt.insert("end", pass_line[block_pl:block_len], "fg_col")
                pass_line = pass_line[block_len:]

            txt.insert("end", pass_line, "fg_col")

            for h in range(lines):
                txt.insert(format(1.0 + h, '.2f'), hex(hex_addr + (line_width * h)) + "    ", "fg_col2")
                txt.insert(format(1.69 + h, '.2f'), "\n", "fg_col")

            txt.grid(row=2, rowspan=2, column=0, sticky="nsew", padx=bor, pady=bor)

            #добавить иф на настройки

            software_data = self.read_file('data/computers/software/', 'e106a9c218fe40fa977516ebe3713613.txt')
            tkinter.ttk.Button(main_frame, style="Custom_sm.TButton", text='Инструкция', takefocus=False, width=0, padding=0, command=lambda h=software_data['manual_header'], t=software_data['manual_text']: topwin.show_text_tip('s', 0, h, [t,])).grid(row=3, column=0, columnspan=2, sticky="nw", padx=bor)
            del software_data

            tkinter.ttk.Label(main_frame, textvariable=self.tkstrvar1, style='Custom_term.TLabel', anchor="sw").grid(row=3, column=1, sticky="sw", padx=bor, pady=bor)
            self.tkstrvar1.set("> ")

            tkinter.ttk.Label(main_frame, textvariable=self.tkstrvar2, style='Custom_term.TLabel', anchor="sw").grid(row=0, rowspan=3, column=1, sticky="sw", padx=bor, pady=bor)
            self.tkstrvar2.set("")

            main_frame.update()

            # tkinter.ttk.Frame(main_frame, style="Custom_b.TFrame").grid(row=2, rowspan=3, column=1, sticky="nsew", pady=bor)
            # tkinter.ttk.Frame(main_frame, style="Custom_b.TFrame").grid(row=2, rowspan=3, column=2, sticky="nsew", padx=bor, pady=bor)

    def show_progress_bar(self, time, steps, header):

        self.header = header

        progress_list = []

        progress_total = 0

        time_total = 0

        for l in range(steps):
            extra_progress = randint(2, 100 // steps)
            extra_time = randint(steps // time, time // steps)
            progress_list.append([extra_time, extra_progress])
            progress_total += extra_progress
            time_total += extra_time

        while 100 - progress_total > 5 or time - time_total > 2:
            id = randint(0, len(progress_list) - 1)
            if 100 - progress_total > 5:
                extra_progress = randint(2, (100 - progress_total) // 2)
                progress_list[id][1] += extra_progress
                progress_total += extra_progress
            if time - time_total > 2:
                extra_time = randint(1, (time - time_total) // 2)
                progress_list[id][0] += extra_time
                time_total += extra_time
        else:
            id = randint(0, len(progress_list) - 1)
            progress_list[id][1] += (100 - progress_total)
            progress_list[id][0] += (time - time_total)
            progress_total += 100 - progress_total
            time_total += time - time_total

        for l in range(steps):

            if l > 0:
                progress_list[l][0] += progress_list[l - 1][0]
                progress_list[l][1] += progress_list[l - 1][1]

            if "label_steps" in self.header.keys():
                guitimer.add_timer([progress_list[l][0], False, 'top_win', 'progress_bar_step', progress_list[l][1], l + 1])
            else:
                guitimer.add_timer([progress_list[l][0], False, 'top_win', 'progress_bar_step', progress_list[l][1], None])

        self.create_win("MIEX progressbar window", 25, 50, 55, 30)

        main_frame = tkinter.ttk.Frame(self.win, style="Custom_b.TFrame", height=bor * 12, width=bor * 49)
        main_frame.grid_configure(row=0, rowspan=5, column=0, columnspan=2, sticky="ns")
        main_frame.grid_propagate(False)

        main_frame.grid_columnconfigure(0, minsize=bor * 9)
        main_frame.grid_columnconfigure(1, minsize=bor * 31)
        main_frame.grid_columnconfigure(2, minsize=bor * 9)

        main_frame.grid_rowconfigure(0, minsize=bor * 2)
        main_frame.grid_rowconfigure(1, minsize=bor * 2)
        main_frame.grid_rowconfigure(2, minsize=bor * 3)
        main_frame.grid_rowconfigure(3, minsize=bor * 4)

        tkinter.ttk.Label(main_frame, text=self.header['label_header'], style='Custom_sm.TLabel', anchor="sw").grid(row=0, column=0, columnspan=3, sticky="nw", padx=tx_bor, pady=(tx_bor, 0))

        tkinter.ttk.Frame(main_frame, style="Custom_b.TFrame").grid(row=1, rowspan=4, column=0, columnspan=3, sticky="nsew", padx=tx_bor)

        if "label_steps" in self.header.keys():
            self.tkstrvar1.set(self.header["label_steps"][0])
        else:
            self.tkstrvar1.set(self.header["label_step"])

        tkinter.ttk.Label(main_frame, textvariable=self.tkstrvar1, style='Custom_sm_lt.TLabel', anchor="sw").grid(row=1, column=0, columnspan=2, sticky="nw", padx=bor, pady=(tx_bor, 0))
        self.tkintvar.set(0)
        tkinter.ttk.Progressbar(main_frame, style="Custom.Horizontal.TProgressbar", orient="horizontal", length=100, mode="determinate", maximum=100, variable=self.tkintvar).grid(row=2, column=0,
                                                                                                                                                                                   columnspan=3,
                                                                                                                                                                                   sticky="nsew",
                                                                                                                                                                                   padx=tx_bor * 3)

        self.tkstrvar2.set("[0/" + str(self.header['label_max']) + " " + self.header['label_max_val'] + "]")

        tkinter.ttk.Label(main_frame, textvariable=self.tkstrvar2, style='Custom_sm_b.TLabel', anchor="center").grid(row=3, column=1, sticky="nsew", padx=tx_bor, pady=(tx_bor, bor))

    def progress_bar_step(self, barvar, text_id, fail=False):
        if text_id is not None:
            self.tkstrvar1.set(self.header["label_steps"][text_id])
        text2 = (self.tkstrvar2.get().split("/"))[1].split(" ")
        self.tkintvar.set(barvar)

        self.tkstrvar2.set("[" + str((barvar * int(text2[0])) // 100) + "/" + text2[0] + " " + text2[1])
        if barvar == 100:
            if self.header['final'] is True:
                self.tkstrvar2.set(self.header['label_suc'])
            else:
                self.tkstrvar2.set(self.header['label_fail'])
            self.tkstrvar1.set("")
            guitimer.add_timer([2, False, 'top_win', 'kill_win'])
            for e in self.header['on_end']:
                guitimer.add_timer(e)

    def show_dialogue(self, data):

        self.cur_line = 0

        self.text_lines = []

        timer_list = []
        self.text_lines.extend([data[0][4], data[0][5]])

        if len(data) > 1:  # Коли длинный текст и с таймером
            first = True
            for l in data[1:]:
                if first is True:
                    timer_list.append(l[0])
                    guitimer.add_timer([l[0], False, 'top_win', 'add_dialogue_line'])
                    first = False
                else:
                    time = l[0] + timer_list[-1]
                    guitimer.add_timer([time, False, 'top_win', 'add_dialogue_line'])
                    timer_list.append(time)

                self.text_lines.extend([l[1], l[2]])

        self.create_win("MIEX message window", 11, 58, 45, 78)

        pic_frame = tkinter.ttk.Frame(self.win, style="Custom_b.TFrame", height=bor * 10, width=bor * 9)
        pic_frame.grid_configure(row=0, rowspan=2, column=1, sticky="ns", padx=tx_bor, pady=tx_bor)
        pic_frame.grid_propagate(False)

        self.text_frame = tkinter.ttk.Frame(self.win, style="Custom_b.TFrame", height=bor * 7, width=bor * 55)
        self.text_frame.grid_configure(row=0, rowspan=2, column=2, sticky="ns", padx=tx_bor, pady=tx_bor)
        self.text_frame.grid_propagate(False)
        data[0][1] = data[0][1].split('-')
        img = tkinter.PhotoImage(file='data/icons/' + data[0][1][0] + '/' + data[0][1][1] + '/' + str(bor - 3) + '.png')
        pic = tkinter.Label(pic_frame, image=img, background=sett.bg_col)
        pic.image = img
        pic.grid(row=0, column=1, sticky="nsew", padx=tx_bor, pady=(tx_bor, 0))

        tkinter.ttk.Label(pic_frame, text=data[0][0], style='Custom_esm.TLabel', anchor="center").grid(row=1, column=1, columnspan=1, sticky="nsew", padx=tx_bor)

        self.txt = tkinter.Text(self.text_frame, height=6, width=43, wrap="word", selectbackground=sett.bg_col, borderwidth=0, background=sett.bg_col, foreground=sett.fg_col, font='EurostileExtReg ' + str(tx_bor * 2),
                                cursor='none')

        self.txt.tag_config("fg_col", foreground=sett.fg_col)
        self.txt.tag_config("fg_col_d", foreground=sett.fg_col_d)
        self.txt.tag_config("fg_col2", foreground=sett.fg_col2)
        self.txt.tag_config("fg_col_cont", foreground=sett.fg_col_cont)
        self.txt.insert("end", self.text_lines[0], self.text_lines[1])

        self.txt.grid(row=0, column=1, sticky="nsew", padx=tx_bor, pady=tx_bor)

        self.text_frame.update()
        print(data)
        audio.play_sound('voice', None, 'data/audio/' + data[0][1][1] + "/" + data[0][2] + '.ogg')
        guitimer.add_timer([data[0][3], False, 'top_win', 'kill_dialog_win'])

    def add_dial_line(self):
        self.cur_line += 2
        self.txt.insert("end", self.text_lines[self.cur_line], self.text_lines[self.cur_line + 1])
        self.txt.see("end")
        self.text_frame.update()

    def kill_win(self):
        if self.showed is True:
            self.win.destroy()
            self.showed = False

    def kill_win2(self):
        if self.showed_2 is True:
            self.win2.grab_release()
            self.win2.destroy()
            self.showed_2 = False


class MainWindow:
    def __init__(self, name_w):
        self.showed = False

    def create(self):
        self.win = tkinter.Toplevel(master=root, height=bor * 74, width=bor * 100, cursor='@cross_or.cur', background=sett.bg_col)

        print("MIEX main window")
        self.win.title("MIEX_main_window")

        self.win.wm_attributes('-topmost', True)
        self.win.resizable(False, False)
        self.win.overrideredirect(True)
        self.win.lift()
        self.win.geometry('+' + str(bor * 32) + '+' + str(bor * 6))
        self.win.event_generate('<Motion>', warp=True, x=bor * 40, y=bor * 20)
        self.showed = True

        self.s_row = 0
        self.n1_collumn = 0
        self.n2_collumn = 3
        self.n3_collumn = 6

        self.mnu_fr = tkinter.Frame(self.win, background=sett.bg_col, height=bor * 4, width=bor * 80)
        self.mnu_fr.grid(sticky="nw", row=self.s_row, columnspan=10, column=self.n1_collumn, padx=(bor, 0))
        self.mnu_fr.grid_propagate(False)

        self.s_row += 1
        self.n1_fr = tkinter.ttk.Frame(self.win, style="Custom_b.TFrame", height=bor * 69, width=bor * 32)
        self.n1_fr.grid(row=self.s_row, rowspan=9, column=self.n1_collumn, columnspan=3, padx=bor, pady=(bor))
        self.n1_fr.grid_propagate(False)

        self.n2_fr = tkinter.ttk.Frame(self.win, style="Custom_b.TFrame", height=bor * 69, width=bor * 32)
        self.n2_fr.grid(row=self.s_row, rowspan=9, column=self.n2_collumn, columnspan=3, pady=(bor))
        self.n2_fr.grid_propagate(False)

        self.n3_fr = tkinter.ttk.Frame(self.win, style="Custom_b.TFrame", height=bor * 69, width=bor * 32)
        self.n3_fr.grid(row=self.s_row, rowspan=9, column=self.n3_collumn, columnspan=3, padx=bor, pady=(bor))
        self.n3_fr.grid_propagate(False)

        menu_items = []
        for i in range(len(sett.lang['system']['menu_list'])):
            menu_items.append({'type': 'item', "state": "enabled", "text": sett.lang['system']['menu_list'][i], "action": [0, False, "mw1", "main_menu", i]})

        menu_list = CrItem()
        menu_list.h_bor = 64
        menu_list.s_row = 0
        menu_list.s_collumn = 0

        menu_list.construct.append(
            {"type": "button_list", "long": False, "style": "Custom.TButton", "page_style": "numbered", "items_on_page": len(sett.lang['system']['menu_list']), "items_spacer": sett.lang['system']['items_spacer'],
             "columnspan": 3,
             "item_list": menu_items})

        menu_list.cr_fr_it(self.n1_fr, 9, (tx_bor, 0))
        menu_list.cr_menu_up_btn()
        menu_list.start_construct()

        missions.cr_mis_item(self.n3_fr, "cur_mis", 0, self.n3_collumn, 64)

        user_profile.cr_profile_wiget(self.n2_fr, "small", 0, self.n2_collumn, 9)

        transm.cr_radio_wiget(self.n2_fr, "small", 9, self.n2_collumn, 9)




        # actor = PersData('mw1', self.n2_fr, 3, 1)
        # radio = Transmissions(actor.coords()[0], actor.coords()[1], self.n2_fr, 0)

    def wide_fr(self):
        self.clear_frame([self.n1_fr, self.n2_fr, self.n3_fr])
        self.n2_fr.config(height=bor * 46, width=bor * 65)
        self.n2_fr.grid_configure(row=1, rowspan=9, column=3, columnspan=6, sticky="n", padx=(0, bor))

        self.n3_fr.config(height=bor * 22, width=bor * 65)
        self.n3_fr.grid_configure(row=9, rowspan=4, column=3, columnspan=6, sticky="s", padx=(0, bor), pady=(0, bor))

    def restore_fr(self):
        self.clear_frame([self.n1_fr, self.n2_fr, self.n3_fr])
        self.n2_fr.config(height=bor * 69, width=bor * 32)
        self.n2_fr.grid_configure(row=self.s_row, rowspan=9, column=self.n2_collumn, columnspan=3, pady=(bor))

        self.n3_fr.config(height=bor * 69, width=bor * 32)
        self.n3_fr.grid_configure(row=self.s_row, rowspan=9, column=self.n3_collumn, columnspan=3, padx=bor, pady=(bor))

    def quit(self):
        self.win.destroy()
        self.showed = False
        missions.module_restore()

    def exit(self):
        self.win.destroy()
        self.showed = False
        missions.module_restore()

    @staticmethod
    def clear_frame(frame_list):
        for f in frame_list:
            for o in f.grid_slaves():
                o.destroy()


class Missions:
    def __init__(self):
        cur_data = self.cur_mis_data()

        self.cur_save_data = cur_data['mis_save']
        del cur_data
        self.cur_mis_jrn = self.cur_save_data['jrn_tips']
        del self.cur_save_data['jrn_tips']
        self.cur_mis_inv = self.cur_save_data['inv_obj']
        del self.cur_save_data['inv_obj']
        #self.cur_mis_req = self.cur_save_data['mis_requirement']
        datahook.events_list['missions'] = self.cur_save_data['Events_List']
        datahook.events['missions'] = self.cur_save_data['Events']

        # если требование или триггер миссии входит в статистические переменные, тогда в функцию статистики подключается пункт проверки этих переменных на изменения

        self.cur_mis_itm = None
        self.mis_id = None
        self.mis_itm = None
        self.cur_mis_menu_list = None
        self.mis_menu_list = None

    def module_restore(self):
        self.cur_mis_itm = None
        self.mis_id = None
        self.mis_itm = None
        self.cur_mis_menu_list = None
        self.mis_menu_list = None

    @staticmethod
    def read_file(f_name):
        fp = open("data/missions/" + f_name, mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        read_data = json.loads(fp.read())
        fp.close()
        return read_data

    @staticmethod
    def write_data(f_name, w_data):
        w_data = json.dumps(w_data, ensure_ascii=False, indent=4)
        fp = open("data/missions/" + f_name, mode='w', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        fp.write(w_data)
        fp.close()

    def mis_list_add(self, add_mis):
        mis_list = self.read_file("mis_list.txt")
        mis_id = add_mis.pop("ID")
        if mis_id in mis_list.keys():
            mis_list.pop(mis_id)
            mis_list[mis_id] = add_mis
            self.write_data("mis_list.txt", mis_list)
            return False
        else:
            mis_list[mis_id] = add_mis
            self.write_data("mis_list.txt", mis_list)
            return True

    def mis_list_del(self, del_mis_id):
        mis_list = self.read_file("mis_list.txt")
        if del_mis_id in mis_list.keys():
            mis_list.pop(del_mis_id)
            self.write_data("mis_list.txt", mis_list)
            return True
        else:
            return False

    def mission_get_unseen(self):
        # Показать менюшку по случайной мисии (принять/отменить/выполнять)
        pass

    def set_cur_mission(self, mis_id):
        mis_data = self.read_file("cur_mission.txt")
        self.write_data(mis_data['ID'] + ".txt", mis_data)  # save unpick

        cur_data = self.read_file(mis_id + ".txt")

        if len(cur_data['mis_save'].keys()) < 5:
            cur_data['mis_save'] = {**cur_data['mis_save'], **cur_data['mis_in_preview'], **cur_data['mis_stage_start'], 'cur_stage': 'mis_stage_start'}

        if 'on_stage' in cur_data['mis_save'].keys():
            if type(cur_data['mis_save']['on_stage'][0]) is list:
                for act in cur_data['mis_save']['on_stage']:
                    if act[0] > 0:
                        guitimer.add_timer(act)
                    else:
                        action.do_action(act)
            else:
                if cur_data['mis_save']['on_stage'][0] > 0:
                    guitimer.add_timer(cur_data['mis_save']['on_stage'])
                else:
                    action.do_action(cur_data['mis_save']['on_stage'])

            del cur_data['mis_save']['on_stage']

        cur_data['mis_save']['stage'] += cur_data['mis_save']['plus_stage']
        del cur_data['mis_save']['plus_stage']

        self.cur_save_data = cur_data['mis_save']

        self.write_data("cur_mission.txt", cur_data)

        cur_data = self.cur_mis_data()
        self.cur_save_data = cur_data['mis_save']
        del cur_data
        self.cur_mis_jrn = self.cur_save_data['jrn_tips']
        del self.cur_save_data['jrn_tips']
        self.cur_mis_inv = self.cur_save_data['inv_obj']
        del self.cur_save_data['inv_obj']
        self.cur_mis_req = self.cur_save_data['mis_requirement']

        datahook.events_list['missions'] = self.cur_save_data['Events_List']
        datahook.events['missions'] = self.cur_save_data['Events']

        self.module_restore()

    def cur_mission_next_stage(self, stage):
        cur_data = self.cur_mis_data()
        next_stage_data = cur_data[stage].copy()
        self.cur_save_data['cur_stage'] = stage
        self.cur_save_data['stage'] += next_stage_data['plus_stage']
        del next_stage_data['plus_stage']
        cur_data_act = next_stage_data['on_stage']
        del next_stage_data['on_stage']
        for k in next_stage_data.keys():
            self.cur_save_data[k] = next_stage_data[k]

        save_data = self.cur_save_data
        save_data['jrn_tips'] = self.cur_mis_jrn
        save_data['inv_obj'] = self.cur_mis_inv
        cur_data['mis_save'] = save_data

        self.write_data('cur_mission.txt', cur_data)


        if type(cur_data_act[0]) is list:
            for a in cur_data_act:
                if a[0] > 0:
                    guitimer.add_timer(a)
                else:
                    action.do_action(a)
        else:
            if cur_data_act[0] > 0:
                guitimer.add_timer(cur_data_act)
            else:
                action.do_action(cur_data_act)

        datahook.events_list['missions'] = self.cur_save_data['Events_List']
        datahook.events['missions'] = self.cur_save_data['Events']

        self.module_restore()

    def cur_mission_complete(self):
        cur_data = self.cur_mis_data()
        print('Mission complete')
        taken_missions = self.read_file('taken_mis_list.txt')
        if cur_data['ID'] in taken_missions:
            del taken_missions[taken_missions.index(cur_data['ID'])]
            self.write_data('taken_mis_list.txt', taken_missions)
            self.set_cur_mission(taken_missions[0])
        else:
            olay.add_state_item(sett.lang['state_items']['missions']['error_get_1'], 'stage')
        self.module_restore()

        '''if self.cur_save_data['stage'] < self.cur_save_data['stages']:
            next_save_data = {**cur_data['mis_save'], **cur_data['mis_stage_' + str(self.cur_save_data['stage'] + 1)]}
            next_save_data['stage'] += 1

            if 'add_jrn_tip' in next_save_data.keys():
                next_save_data['jrn_tips'].append(next_save_data['add_jrn_tip'])
                del next_save_data['add_jrn_tip']

            if 'add_inv_obj' in next_save_data.keys():
                next_save_data['inv_obj'].append(next_save_data['add_inv_obj'])
                del next_save_data['add_inv_obj']

            cur_data['mis_save'] = next_save_data
            del next_save_data
            self.write_data('cur_mission.txt', cur_data)

            if 'on_trigger' in self.cur_save_data.keys():
                action.do_action(self.cur_save_data['on_trigger'])

            cur_data = self.cur_mis_data()
            self.cur_save_data = cur_data['mis_save']
            del cur_data
            self.cur_mis_jrn = self.cur_save_data['jrn_tips']
            del self.cur_save_data['jrn_tips']
            self.cur_mis_inv = self.cur_save_data['inv_obj']
            del self.cur_save_data['inv_obj']
            self.cur_mis_req = self.cur_save_data['mis_requirement']

            self.cur_task_trigger = self.cur_save_data['task_trigger']

            self.module_restore()

        else:
            print('Mission complete')
            taken_missions = self.read_file('taken_mis_list.txt')
            if cur_data['ID'] in taken_missions:
                del taken_missions[taken_missions.index(cur_data['ID'])]
                self.write_data('taken_mis_list.txt', taken_missions)
                self.set_cur_mission(taken_missions[0])
            else:
                olay.add_state_item(sett.lang['state_items']['missions']['error_get_1'], 'stage')

            olay.add_state_item(sett.lang['state_items']['missions']['mis_success'], 'stage')'''

    def cur_mis_data(self):
        return self.read_file("cur_mission.txt")

    def mission_scripts(self):
        if len(self.mis_do_list) > 0:
            for do in range(len(self.mis_do_list)):
                print(do)

    def cr_mis_item(self, frame, id, row, column, height):
        if id == 'cur_mis':
            if self.cur_mis_itm is None:
                self.cur_mis_itm = CrItem()

                self.cur_mis_itm.s_row = row
                self.cur_mis_itm.s_collumn = column
                self.cur_mis_itm.h_bor = 65
                self.cur_mis_menu_list = [[sett.lang['missions']['menu_mis_sm'][0], "disabled", 'mis_tsk', 'cur_mis'], [sett.lang['missions']['menu_mis_sm'][1], "enabled", 'mis_jrn', 'cur_mis'],
                                          [sett.lang['missions']['menu_mis_sm'][2], "enabled", 'mis_inv', 'cur_mis'], "mission"]
                self.cur_mis_itm.cr_up_btn(self.cur_mis_menu_list, frame)
                self.cur_mis_itm.cr_fr_it(frame, rowspan=8)
                self.cr_mis_tsk('cur_mis')

    def cr_mis_inv(self, id):
        if id == 'cur_mis':
            self.cur_mis_menu_list[2].configure(state='disabled')
            self.cur_mis_menu_list[0].configure(state='enabled')
            self.cur_mis_menu_list[1].configure(state='enabled')
            self.cur_mis_itm.clear_frame()
            self.cur_mis_itm.h_bor = 65
            item_list = []

            for i in range(len(missions.cur_mis_inv)):
                item_list.append({'type': 'item', "state": "enabled", "text": missions.cur_mis_inv[i]['title'],
                                  "action": [0, False, "mw1", 'mission', 'mis_inv_cr_det', 'cur_mis', missions.cur_mis_inv[i]['type'], missions.cur_mis_inv[i]['ID']]})

            self.cur_mis_itm.construct.append(
                {"type": "button_list", "long": False, "style": "Custom_sm.TButton", "page_style": "numbered", "items_on_page": 12, "items_spacer": "-", "columnspan": 3, "item_list": item_list})
            self.cur_mis_itm.start_construct()

    def cr_mis_jrn(self, id):
        if id == 'cur_mis':
            self.cur_mis_menu_list[1].configure(state='disabled')
            self.cur_mis_menu_list[0].configure(state='enabled')
            self.cur_mis_menu_list[2].configure(state='enabled')
            self.cur_mis_itm.clear_frame()
            self.cur_mis_itm.h_bor = 64

            text_list = []
            for j in missions.cur_mis_jrn:
                text_list.append([j[0], 'fg_col_cont', 'header'])
                text_list.append(["\n\n" + j[1] + "\n\n\n\n", 'fg_col2', 'text'])

            self.cur_mis_itm.construct.append({"type": "label", "style": ["Custom_sm.TLabel", "center"], "long": False, "text": self.cur_save_data["mission_name"]})
            self.cur_mis_itm.construct.append({"type": "text", "style": {}, "long": True, "slider": True, "glob": False, "text_list": text_list, 'padx': (0, bor)})
            self.cur_mis_itm.start_construct()

    def cr_mis_tsk(self, id):
        def cr_pers(cur, cap):

            pres = (cur * 100) // cap
            pres_list = list(str(pres))
            dig_list = ['⠀', '⠁', '⠃', '⠇', '⡅', '⡇', '⡏', '⡏', '⡟', '⡿']
            label_text = ''

            if len(pres_list) < 3:
                if len(pres_list) < 2:
                    label_text += dig_list[int(pres_list[0])]
                else:
                    label_text += '⣿' * int(pres_list[0])
                    label_text += dig_list[int(pres_list[1])]

            else:
                label_text += '⣿' * 10

            label_text += ' ' + str(pres) + '%'


            return "[" + label_text + "]"

        def cr_blocks(cur, cap):
            return "[" + "◼" * cur + "◻" * (cap - cur) + "]"

        def make_req_text(data):
            req_text = sett.lang['missions']['mis_task_win']['progress'] + '\n' + cr_pers(data["stage"], data["stages"]) + '\n\n'

            if len(data["mis_requirement_text"]) > 0:
                print("Есть требования")
            else:
                print("нет требований")
                # req_text += "Требования: Нет\n\n"

            if len(req_text.split("\n")) < 5:
                req_text += sett.lang['missions']['mis_task_win']['mis_reward']
                for r in data['reward_text']:
                    req_text += r

            '''req_text += "Требования: \n"
            req_text += "[✔]    " + data["mis_requirement_text"][0] + "\n"
            req_text += "[✔]    " + data["mis_requirement_text"][2] + "\n"
            req_text += "[✔]    " + data["mis_requirement_text"][2] + "\n"
            req_text += "[✔]    " + data["mis_requirement_text"][2]'''
            return req_text

        if id == 'cur_mis':
            self.cur_mis_menu_list[0].configure(state='disabled')
            self.cur_mis_menu_list[1].configure(state='enabled')
            self.cur_mis_menu_list[2].configure(state='enabled')

            self.cur_mis_itm.clear_frame()

            self.cur_mis_itm.h_bor = 64
            self.cur_mis_itm.construct.append({"type": "label", "style": ["Custom_sm.TLabel", "center"], "long": False, "text": self.cur_save_data["mission_name"]})
            self.cur_mis_itm.construct.append({"type": "img+label", "img": self.cur_save_data["mis_pic"], "style": ["Custom_sm_lt.TLabel", "n"], "long": False, "text": make_req_text(self.cur_save_data)})
            self.cur_mis_itm.construct.append({"type": "line", "long": False, "show": True})
            self.cur_mis_itm.construct.append({"type": "label", "style": ["Custom_sm.TLabel", "center"], "long": False, "text": sett.lang['missions']['mis_task_win']['cur_task']})
            self.cur_mis_itm.construct.append({"type": "img+label", "img": self.cur_save_data["task_pic"], "style": ["Custom_sm_lt.TLabel", "n"], "long": False, "text": self.cur_save_data["mis_task_name"]})
            self.cur_mis_itm.construct.append({"type": "text", "style": {}, "long": True, "slider": False, "glob": False, "text_list": [[self.cur_save_data["task_discr"], 'fg_col', 'text']]})

            self.cur_mis_itm.start_construct()

    @staticmethod
    def clear_frame(obj, final=False):
        for w in obj.fr_it.grid_slaves():
            w.grid_forget()

        if final is True:
            obj.fr_it.grid_forget()


class Inventory:
    def __init__(self):
        pass

    @staticmethod
    def read_file(f_name):
        fp = open("data/inventory/" + f_name, mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        read_data = json.loads(fp.read())
        fp.close()
        return read_data

    @staticmethod
    def write_data(f_name, w_data):
        w_data = json.dumps(w_data, ensure_ascii=False, indent=4)
        fp = open("data/inventory/" + f_name, mode='w', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        fp.write(w_data)
        fp.close()

    def get_item_storage(self, itm_uid):
        item_list = self.read_file('item_lists.txt')
        if itm_uid in item_list["onboard"]:
            return True
        else:
            return False

    def get_inv_item(self, storage_file, itm_uid):
        storage_list = self.read_file(storage_file)
        id_data = dict()
        for i in storage_list:
            id_data = i
            if i['ID'] == itm_uid:
                break
        return id_data


    @staticmethod
    def add_to_inv(data_list):
        print(data_list)

    @staticmethod
    def transfer(id_list, tostorage=True):
        print(id)

    def write_item(self, itm_data, storage):
        storage_data = self.read_file(storage)
        for f in range(len(storage_data)):
            if itm_data['ID'] == storage_data[f]['ID']:
                storage_data[f] = itm_data
                break

        self.write_data(storage, storage_data)

    def cr_item_list(self):
        pass

    def cr_item_card(self, frame_id, itm_type, itm_cat, itm_uid):

        def make_param_text():
            param_text = sett.lang['inventory']['inv_item']['type']['type'] + ': ' + sett.lang['inventory']['inv_item']['type'][item_data['param']['type']] + "\n"  # Тип предмета

            param_text += sett.lang['inventory']['inv_item']['integrity'] + ': ' + cr_blocks(item_data['param']['integrity'], 10) + "\n"  # Целостность

            param_text += sett.lang['inventory']['inv_item']['cost'] + ': '
            if item_data['param']['cost'] is False:
                param_text += "N/A" + "\n"
            else:
                param_text += str(item_data['param']['cost']) + " " + sett.lang['system']['main_currency'] + "\n"  # Стоимость

            if item_data['type'][0] == "file":  # Если предмет - файл
                param_text += sett.lang['inventory']['inv_item']['size'] + ': ' + str(item_data['param']['size']) + " " + sett.lang['system']['file_vol'] + "\n\n"  # Размер файла
                param_text += sett.lang['inventory']['inv_item']['access'] + ': ' + sett.lang['system']['main_bool'][int(item_data['param']['access'])] + "\n"  # Доступ
                param_text += sett.lang['inventory']['inv_item']['copyed'] + ': ' + str(item_data['param']['copyed'])  # Количество копий
            return param_text

        def make_file_extra():  # Доп параметры файла
            file_extra = ""
            if item_data['file_extra']['analyzed'] is True:  # Если проанализирован
                file_extra += "\n" + sett.lang['inventory']['inv_item']['analyzed'] + ': ' + sett.lang['system']['main_bool'][1] + "\n"

                if item_data['file_extra']['decrypted'] is False:  # Если не расшифрован
                    file_extra += sett.lang['inventory']['inv_item']['encrypted'] + ': ' + item_data['file_extra']['encrypted'][0] + " " + str(item_data['file_extra']['encrypted'][1]) + "\n"
                    file_extra += sett.lang['computer']['decrypter'] + ': ' + computer.comp_data['software']['decrypter']['name']
                    if item_data['file_extra']['encrypted'][0] in computer.comp_data['software']['decrypter']['types'].keys():  # Если для расшифровки достаточно

                        file_extra += " [" + item_data['file_extra']['encrypted'][0] + " " + str(
                            computer.comp_data['software']['decrypter']['types'][item_data['file_extra']['encrypted'][0]]['version']) + "]" + "\n"
                    else:  # Если для расшифровки недостаточно
                        file_extra += " [" + sett.lang['unavailable'] + "]" + "\n"

                    file_extra += sett.lang['inventory']['inv_item']['decrypted'] + ': ' + sett.lang['system']['main_bool'][0]
                else:  # Если расшифрован
                    file_extra += sett.lang['inventory']['inv_item']['decrypted'] + ': ' + sett.lang['system']['main_bool'][1]


            else:  # Если не проанализирован
                file_extra += sett.lang['inventory']['inv_item']['analyzed'] + ': ' + sett.lang['system']['main_bool'][0] + " [" + item_data['file_extra']['file'][0] + " " + str(
                    item_data['file_extra']['file'][1]) + "]" + "\n"
                file_extra += sett.lang['computer']['analyzer'] + ': ' + computer.comp_data['software']['analyzer']['name']

                if item_data['file_extra']['file'][0] in computer.comp_data['software']['analyzer']['types'].keys():
                    file_extra += " [" + item_data['file_extra']['file'][0] + " " + str(computer.comp_data['software']['analyzer']['types'][item_data['file_extra']['file'][0]]['version']) + "]" + "\n"
                else:
                    file_extra += " [" + sett.lang['system']['unavailable'] + "]" + "\n"

                if item_data['file_extra']['decrypted'] is False:
                    file_extra += sett.lang['inventory']['inv_item']['encrypted'] + ': ' + sett.lang['system']['unknown'] + "\n"
                    file_extra += sett.lang['computer']['decrypter'] + ': ' + computer.comp_data['software']['decrypter']['name'] + "\n"
                    file_extra += sett.lang['inventory']['inv_item']['decrypted'] + ': ' + sett.lang['system']['main_bool'][0]
                else:
                    file_extra += sett.lang['inventory']['inv_item']['decrypted'] + ': ' + sett.lang['system']['main_bool'][1]

            return file_extra

        def cr_blocks(cur, cap):
            return "[" + "◼" * cur + "◻" * (cap - cur) + "]"

        def btn_bool(rev, bool):
            if rev is True:
                if bool is True:
                    return 'enabled'
                else:
                    return 'disabled'
            else:
                if bool is False:
                    return 'enabled'
                else:
                    return 'disabled'

        if frame_id == 'cur_mis':
            print("cur mis frame")
            item = CrItem()
            missions.cur_mis_itm.get_orig_point()
            item.s_row = 0
            item.s_collumn = missions.cur_mis_itm.s_collumn
            item.h_bor = 65
            item.cr_fr_it(missions.cur_mis_itm.fr_it, padx=0)
        else:
            print("new mis frame")

        if self.get_item_storage(itm_uid) is True:
            onboarded = True
            item_data = self.get_inv_item(itm_type[0] + '_' + itm_cat[0] + '_onboard.txt', itm_uid)

        else:
            item_data = self.get_inv_item(itm_type[0] + '_' + itm_cat[0] + '_stored.txt', itm_uid)

        item.construct.append({"type": "label", "style": ["Custom_sm.TLabel", "center"], "long": False, "text": item_data["title"]})
        item.construct.append({"type": "img+label", "img": item_data["image"], "style": ["Custom_sm_lt.TLabel", "n"], "long": False, "text": make_param_text()})

        if item_data['param']['access'] is True:  # если файл доступен
            if onboarded is True:  # если файл на диске
                item.construct.append({"type": "btn", "style": "Custom.TButton", "long": False, "btn_data": [
                    {"state": "enabled", "text": "►", "columnspan": 1, "action": [0, False, "mw1", 'audio', 'item_card_play', itm_uid]},
                    {"state": "enabled", "text": "■", "columnspan": 1, "action": [0, False, "mw1", 'audio', 'stop_rec', "rec"]},
                    {"state": "enabled", "text": "❯❯❯", "columnspan": 1, "action": [0, False, "mw1", 'inventory', 'item_to_storage', frame_id, itm_type, itm_cat, itm_uid]}]})
            else:
                item.construct.append({"type": "btn", "style": "Custom.TButton", "long": False, "btn_data": [
                    {"state": "enabled", "text": "►", "columnspan": 1, "action": [0, False, "mw1", 'audio', 'item_card_play_storage', itm_uid]},
                    {"state": "enabled", "text": "■", "columnspan": 1, "action": [0, False, "mw1", 'audio', 'stop_rec', "rec"]},
                    {"state": "enabled", "text": "❮❮❮", "columnspan": 1, "action": [0, False, "mw1", 'inventory', 'item_from_storage', frame_id, itm_type, itm_cat, itm_uid]}]})

        else:  # если файл не доступен
            if onboarded is True:
                item.construct.append({"type": "btn", "style": "Custom.TButton", "long": False, "btn_data": [
                    {"state": "disabled", "text": "►", "columnspan": 1, "action": [0, False, "mw1", 'audio', 'item_card_play_storage', itm_uid]},
                    {"state": "disabled", "text": "◼", "columnspan": 1, "action": [0, False, "mw1", 'audio', 'stop_rec', "rec"]},
                    {"state": "enabled", "text": "❯❯❯", "columnspan": 1, "action": [0, False, "mw1", 'inventory', 'item_to_storage', frame_id, itm_type, itm_cat, itm_uid]}]})
            else:
                item.construct.append({"type": "btn", "style": "Custom.TButton", "long": False, "btn_data": [
                    {"state": "disabled", "text": "►", "columnspan": 1, "action": [0, False, "mw1", 'audio', 'item_card_play_storage', itm_uid]},
                    {"state": "disabled", "text": "◼", "columnspan": 1, "action": [0, False, "mw1", 'audio', 'stop_rec', "rec"]},
                    {"state": "enabled", "text": "❮❮❮", "columnspan": 1, "action": [0, False, "mw1", 'inventory', 'item_from_storage', frame_id, itm_type, itm_cat, itm_uid]}]})

        item.construct.append({"type": "label", "style": ["Custom_sm_lt.TLabel", "center"], "long": False, "text": make_file_extra()})

        if item_data['file_extra']['analyzed'] is False:  # Если файл не анализировали
            anal_btn = True
            decr_btn = False
            heal_btn = False
        else:
            anal_btn = False
            if item_data['file_extra']['decrypted'] is False:  # Если файл не расшифрован
                decr_btn = True
                heal_btn = False
            else:
                decr_btn = False
                if item_data['file_extra']['healed'] is False:  # Если файл не лечили
                    heal_btn = True
                else:
                    heal_btn = False

        item.construct.append({"type": "btn", "style": "Custom.TButton", "long": False, "btn_data": [
            {"state": btn_bool(True, anal_btn), "text": sett.lang['inventory']['inv_item']['analyzed_btn'], "columnspan": 1,
             "action": [0, False, "mw1", 'inventory', 'refresh', 'item_card_analyze', frame_id, itm_type, itm_cat, itm_uid]},
            {"state": btn_bool(True, decr_btn), "text": sett.lang['inventory']['inv_item']['dеcr_btn'], "columnspan": 1,
             "action": [0, False, "mw1", 'inventory', 'refresh', 'item_card_decrypt', frame_id, itm_type, itm_cat, itm_uid]},
            {"state": btn_bool(True, heal_btn), "text": sett.lang['inventory']['inv_item']['heal_btn'], "columnspan": 1,
             "action": [0, False, "mw1", 'inventory', 'refresh', 'item_card_heal', frame_id, itm_type, itm_cat, itm_uid]}]})

        item.construct.append({"type": "text", "style": {}, "long": True, "slider": False, "glob": False,
                               "text_list": item_data['obj_descr']})

        item.construct.append(
            {"type": "btn", "style": "Custom.TButton", "long": False, "btn_data": [{"state": "enabled", "text": "✖", "columnspan": 3, "action": [0, False, "mw1", 'inventory', 'item_close']}]})

        item.start_construct()

    def item_card_analyze(self, frame_id, itm_type, itm_cat, itm_uid):
        print("start analyze")
        if self.get_item_storage(itm_uid) is True:
            item_data = self.get_inv_item(itm_type[0] + '_' + itm_cat[0] + '_onboard.txt', itm_uid)

        else:
            print("error file in web storage")
        analyze = computer.use_soft('analyzer', item_data['file_extra']['file'][0], item_data['file_extra']['file'][1], item_data['param']['size'])
        if analyze[0] == 'alarm no ram':
            print('alarm no ram')
        elif analyze[0] == 'alarm no ram no type':
            print('alarm no ram no type')
        elif analyze[0] == 'alarm no type':
            print('alarm no type')
        else:
            topwin.show_progress_bar(analyze[1], (analyze[1] // 4) + 1,
                                     {'label_max': item_data['param']['size'], 'label_max_val': sett.lang['system']["file_vol"], 'label_header': sett.lang['computer']['analyzer'] + ' [ ' + analyze[2] + ' ]',
                                      'label_suc': sett.lang['computer']['soft_fin_true'],
                                      'label_fail': sett.lang['computer']['soft_fin_false'], 'final': analyze[0], 'label_step': sett.lang['computer']['analyze'] + '...',
                                      'on_end': [[1, False, 'olay', 'add_state_item', sett.lang['computer']['analyze_notif'], "obj"]]})
            if analyze[0] is True:
                item_data['file_extra']['analyzed'] = True
                self.write_item(item_data, itm_type[0] + '_' + itm_cat[0] + '_onboard.txt')
            else:
                item_data['param']['copyed'] -= 1
                if item_data['param']['copyed'] == 0:
                    print('rebuild card to find copy')
            mw1.win.withdraw()
            guitimer.add_timer([analyze[1] + 1, False, 'mw1', 'show_win'])
            guitimer.add_timer([analyze[1], False, 'mw1', 'inventory', 'cr_item_card', frame_id, itm_type, itm_cat, itm_uid])


class NPC:
    def __init__(self):
        self.cur_npc = None
        self.npc_dialogue = None
        self.cur_npc_data = None
        self.txt_dialogue = None

    def read_file(self, f_name):
        fp = open("data/npc/" + self.cur_npc + "/" + f_name, mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        read_data = json.loads(fp.read())
        fp.close()
        return read_data

    def write_data(self, f_name, w_data):
        w_data = json.dumps(w_data, ensure_ascii=False, indent=4)
        fp = open("data/npc/" + self.cur_npc + "/" + f_name, mode='w', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        fp.write(w_data)
        fp.close()

    def cr_npc_message(self, type, npc, message_id):
        self.cur_npc = npc
        message = self.read_file('messages.txt')
        data = message[message_id]
        data[0].insert(0, message['image'])
        data[0].insert(0, message['name'])
        if type == 'message':
            topwin.show_dialogue(data)
        elif type == 'call_primary':
            call_time = 2
            olay.show_bottom(text=sett.lang['npc']['call_primary'] + message['name'] + "]", time=call_time, ui='call')
            guitimer.add_timer([call_time, False, 'top_win', 'show_dialogue', data])
            guitimer.add_timer([call_time + data[0][3], False, 'olay', 'show_bottom', sett.lang['npc']['action_fastdialogue'][0] + sett.action_key + sett.lang['npc']['action_fastdialogue'][1], 'fastdialogue', 5, None])

    def cr_npc_dialogue(self, npc=None):
        if npc is not None:
            self.cur_npc = npc
        self.cur_npc_data = self.read_file("state.txt")
        self.npc_dialogue = self.read_file("dialogue.txt")

        mw1.wide_fr()
        self.cr_npc_info(mw1.n1_fr, npc)
        self.cr_dialogue_win("start_" + str(self.cur_npc_data["cur_data"]["rep_level"]))

    def add_to_dialogue(self, text, type):

        cur_dialogue = self.read_file("cur_dialogue.txt")

        if type == "npc":
            self.txt_dialogue.insert("end", "\n" + text + "\n\n", "npc_fg_col2")
            self.txt_dialogue.yview('end')
            text = ["\n" + text + "\n\n", "fg_col2", "npc"]
            cur_dialogue.append(text)


        elif type == "actor":
            self.txt_dialogue.insert("end", text + "\n", "actor_fg_col_d")
            self.txt_dialogue.yview('end')
            text = [text + "\n", "fg_col_d", "actor"]
            cur_dialogue.append(text)

        self.write_data("cur_dialogue.txt", cur_dialogue)

    def next_dialogue(self, dialogue_id, answer):
        dialogue_random = False
        if answer != "no_answer":
            audio.play_sound('ui', 'click')
            self.add_to_dialogue(answer[:-1], "actor")
        if isinstance(self.npc_dialogue[dialogue_id]['dialogue']['text'], list):  # коли есть случайные варианты у диалога
            text_id = randint(0, len(self.npc_dialogue[dialogue_id]['dialogue']['text']) - 1)
            dialogue_random = True
        if "sound" in self.npc_dialogue[dialogue_id]['dialogue'].keys():  # коли у диалога есть озвучка
            if dialogue_random is True:
                self.add_to_dialogue(self.npc_dialogue[dialogue_id]['dialogue']['text'][text_id], "npc")
                audio.play_sound('voice', None, 'data/audio/' + self.cur_npc + "/" + self.npc_dialogue[dialogue_id]['dialogue']["sound"][text_id][0] + '.ogg')

            else:
                self.add_to_dialogue(self.npc_dialogue[dialogue_id]['dialogue']['text'], "npc")
                audio.play_sound('voice', None, 'data/audio/' + self.cur_npc + "/" + self.npc_dialogue[dialogue_id]['dialogue']["sound"][0] + '.ogg')

        else:
            audio.restore_vol('voice')
            if dialogue_random is True:
                self.add_to_dialogue(self.npc_dialogue[dialogue_id]['dialogue'][text_id], "npc")
            else:
                self.add_to_dialogue(self.npc_dialogue[dialogue_id]['dialogue']['text'], "npc")
        self.cr_answers(dialogue_id)

        if 'action' in self.npc_dialogue[dialogue_id].keys():  # коли у диалога есть есть действие при появлении
            action.do_action(self.npc_dialogue[dialogue_id]['action'])

        if 'dialogues_capacity' in self.npc_dialogue[dialogue_id].keys():  # проверяем не статичный ли диалог (если он первый)
            if self.npc_dialogue[dialogue_id]['dialogue_capacity'] == 0:
                self.cur_npc_data['cur_data']['excluded_dialogues'].append(dialogue_id)
                cur_dialogue_id = dialogue_id
                zero = True
                while zero is True:  # пока нулевые диалоги бежим по родителям до первого с вариантом
                    cur_dialogue_id = self.npc_dialogue[cur_dialogue_id]['parent']  # берем родителя диалога
                    if 'dialogue_capacity' in self.npc_dialogue[cur_dialogue_id].keys():  # проверяем не статичный ли диалог (для переброса в начало)
                        if cur_dialogue_id in self.cur_npc_data['cur_data']['dialogues_capacity'].keys():  # проверяем есть ли диалог в покусаных
                            if self.cur_npc_data['cur_data']['dialogues_capacity'][cur_dialogue_id] < 2:  # проверяем есть ли ещё варианты
                                self.cur_npc_data['cur_data']['excluded_dialogues'].append(cur_dialogue_id)  # коли выбора нет
                                del self.cur_npc_data['cur_data']['dialogues_capacity'][cur_dialogue_id]
                                zero = True
                            else:
                                self.cur_npc_data['cur_data']['dialogues_capacity'][cur_dialogue_id] -= 1  # коли выбор есть
                                zero = False
                        else:
                            if self.npc_dialogue[cur_dialogue_id]['dialogue_capacity'] > 1:  # проверяем есть ли ещё варианты
                                self.cur_npc_data['cur_data']['dialogues_capacity'][cur_dialogue_id] = self.npc_dialogue[cur_dialogue_id]['dialogue_capacity'] - 1  # коли выбор есть
                                zero = False
                            else:
                                self.cur_npc_data['cur_data']['excluded_dialogues'].append(cur_dialogue_id)  # коли выбора нет
                                zero = True
                    else:
                        print("статичный")
                        zero = False

    def return_dialogue(self, dialogue_id):
        self.cr_answers(self.npc_dialogue[dialogue_id]['parent'])

    def start_dialogue(self):
        self.cr_answers("start_" + str(self.cur_npc_data["cur_data"]["rep_level"]))

    def cr_dialogue_win(self, dialogue_id):

        dialogue = CrItem()

        dialogue.s_row = 0
        dialogue.col_width = 20
        dialogue.width_corr = 2
        dialogue.s_collumn = 3
        dialogue.h_bor = 45
        dialogue.cr_fr_it(mw1.n2_fr, rowspan=3, pady=(tx_bor, 0))

        dialogue.construct.append({"type": "label", "style": ["Custom_sm.TLabel", "center"], "long": False, "text": self.cur_npc_data["main_data"]["name"]})
        dialogue.construct.append({"type": "line", "long": False, "show": True})
        dialogue.construct.append({"type": "text", "style": {}, "long": True, "slider": True, "glob": True,
                                   "text_list": self.read_file("cur_dialogue.txt")})

        dialogue.start_construct()

        self.txt_dialogue = dialogue.txt_wgt

        self.next_dialogue(dialogue_id, 'no_answer')

        self.cr_answers(dialogue_id)

    def cr_answers(self, dialogue_id):

        answers_list = self.npc_dialogue[dialogue_id]['answer']

        answers = CrItem()
        answers.s_row = 5
        answers.col_width = 20
        answers.width_corr = 2
        answers.s_collumn = 3
        answers.h_bor = 20

        mw1.clear_frame([mw1.n3_fr])
        answers.cr_fr_it(mw1.n3_fr, rowspan=3, pady=(0, 0))
        answers.construct.append({"type": "line", "long": False, "show": False})
        text_list = []
        for i in answers_list:
            if i[1][1] not in self.cur_npc_data['cur_data']['excluded_dialogues']:
                text_list.append([i[0] + "\n", 'link', 'answer', i[1]])
            else:
                if 'dialogue_capacity' not in self.npc_dialogue[dialogue_id].keys():
                    text_list.append([i[0] + "\n", 'link', 'answer', [i[1][0], "rep_" + i[1][1]]])
        if len(text_list) > 0:
            answers.construct.append({"type": "text", "style": {'font': ('EurostileExtMed', 2)}, "long": True, "slider": True, "glob": False, "text_list": text_list})
            answers.start_construct()
        else:
            self.cr_answers(self.npc_dialogue[dialogue_id]['parent'])

    @staticmethod
    def cr_npc_info(frame, npc):

        def cr_npc_label(npc_data):
            print(npc_data)

        npc_info = CrItem()

        npc_info.s_row = 1
        npc_info.s_collumn = 0
        npc_info.h_bor = 40

        npc_info.menu_list = [['ИЗБР', "disabled", 'cont_fav', 'npc_info'], ['КОНТ', "enabled", 'cont_adr', 'npc_info'],
                              ['МЕСТ', "enabled", 'cont_near', 'npc_info'], "npc"]
        npc_info.cr_up_btn(npc_info.menu_list, frame)
        npc_info.cr_fr_it(frame, rowspan=9, pady=(tx_bor, 0))

        npc_info.construct.append(
            {"type": "pic_button_list", "long": False, "style": "Custom_pic.TButton", "page_style": "numbered", "items_on_page": 7, "items_spacer": "            -", "columnspan": 3, "item_list": [
                {'img': 'NPC-sidor', 'type': 'item', "state": "disabled", "text": "Сидорович\n\n[торговец]\nреп: [◼◼◻◻◻◻]\n[online]", "action": [0, False, "mw1", "main_menu", 1]}
            ]})
        # npc_info.construct.append({"type": "label", "style": ["Custom_sm.TLabel", "center"], "long": False, "text": 'Сидорович'})
        # npc_info.construct.append({"type": "img+label", "img": 'sidor', "style": ["Custom_sm_lt.TLabel", "n"], "long": False, "text": '[торговец]\nреп: [◼◼◻◻◻◻]\n[online]'})
        # npc_info.construct.append({"type": "line", "long": False})

        npc_info.start_construct()


class Computer:
    def __init__(self, computer):
        print("create computer" + computer)
        self.comp_data = self.power_on(computer)
        self.start = self.comp_data['start']
        del self.comp_data['start']

    @staticmethod
    def power_on(computer_name):
        fp = open("data/computers/" + computer_name + ".txt", mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        comp_data = json.loads(fp.read())
        fp.close()

        term_load = 0
        cpu_usage = 0
        ram_usage = 0
        disk_usage = 0

        cpu = comp_data["hardware"]['processor']['cur_freq'] * comp_data["hardware"]['processor']['core_performance']
        ram = comp_data["hardware"]['ram']['size']
        disk = comp_data["hardware"]['disk']['size']

        plis = comp_data["hardware"]['plis']['matrix_size'] * comp_data["hardware"]['plis']['cur_freq']

        for u in comp_data["software"].keys():
            if 'cpu_usage' in comp_data["software"][u].keys():
                cpu_usage += comp_data["software"][u]['cpu_usage']
        cpu -= cpu_usage

        for u in comp_data["software"].keys():
            ram_usage += comp_data["software"][u]['ram_usage']
        ram -= ram_usage

        for u in comp_data["software"].keys():
            disk_usage += comp_data["software"][u]['size']
        disk -= disk_usage

        for t in comp_data["hardware"].keys():
            term_load += comp_data["hardware"][t]['term_load']

        comp_data["start"] = {'cpu': cpu, 'plis': plis, 'ram': ram, 'disk': disk, 'term_load': term_load}
        return comp_data

    def power_off(self, computer_name):
        w_data = json.dumps(self.comp_data, ensure_ascii=False, indent=4)
        fp = open("data/missions/" + computer_name + ".txt", mode='w', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
        fp.write(w_data)
        fp.close()

    def use_soft(self, soft_name, file_type, type_version, file_size):
        programm = self.comp_data["software"][soft_name]
        if file_type in programm['types']:  # расширение есть в программе
            if programm['types'][file_type]['version'] >= type_version:  # версия программы подходит к файлу
                timer = (file_size * programm['types'][file_type]['unpack_rate']) // programm['types'][file_type]['speed']
                if timer > self.start['ram']:  # свободна ли память для действия
                    return ('alarm no ram', programm['name'])
                else:  # свободна
                    if programm['types'][file_type]['plis'] is True:  # оптимизированно ли под ПЛИС
                        timer = timer // (self.start['cpu'] + self.start['plis'])
                        return (True, timer, programm['name'])
                    else:
                        timer = timer // self.start['cpu']
                        return (True, timer, programm['name'])


            else:  # версия программы не подходит к файлу
                if (file_size * programm['types'][file_type]['unpack_rate']) // programm['types'][file_type]['speed'] > self.start['ram']:  # свободна ли память для действия
                    return ('alarm no ram no type', programm['name'])
                else:
                    timer = ((self.start['ram'] // file_size))
                    fail = 0
                    for t in range(timer):  # расчет вероятности подбора
                        fail += (randint(0, 10) * programm['ai_rate'])

                    timer = (timer * (file_size * (programm['types'][file_type]['unpack_rate'] // programm['types'][file_type]['speed']))) // (self.start['cpu'] + self.start['plis'] // 2)

                    if fail >= 100:
                        return (True, timer, programm['name'])
                    else:
                        return (False, timer, programm['name'])

        else:  # расширения нет в программе
            return ('alarm no type', programm['name'])  # расширения нет в программе - оповещение


class CrItem:
    def __init__(self):
        self.fr_it = None

        self.txt_wgt = None

        self.tkintvar = tkinter.IntVar()
        self.tkintvar2 = tkinter.IntVar()
        self.tkstrvar1 = tkinter.StringVar()
        self.tkstrvar2 = tkinter.StringVar()

        self.s_row = 0
        self.s_collumn = 0
        self.h_bor = 64
        self.col_width = 10
        self.width_corr = 0
        self.construct = []

    def set_orig_point(self):
        self.s_row_orig = self.s_row
        self.s_collumn_orig = self.s_collumn

    def get_orig_point(self):
        self.s_row = self.s_row_orig
        self.s_collumn = self.s_collumn_orig

    def cr_menu_up_btn(self):
        self.fr_it.grid_columnconfigure(self.s_collumn, minsize=bor * 13)
        self.fr_it.grid_columnconfigure(self.s_collumn + 1, minsize=bor * 13)
        self.fr_it.grid_columnconfigure(self.s_collumn + 2, minsize=bor * 2)
        self.fr_it.grid_rowconfigure(self.s_row, minsize=bor * 2)

        tkinter.ttk.Button(self.fr_it, style="Custom.TButton", text=sett.lang['system']['menu_exit'], takefocus=False, width=0, padding=0,
                           command=lambda e=0: action.do_action([0, False, 'mw1', 'main_menu', 'main_menu_quit'])).grid(row=self.s_row, column=self.s_collumn, sticky="w", padx=(0, bor),
                                                                                                                        pady=(0, tx_bor))
        tkinter.ttk.Button(self.fr_it, style="Custom.TButton", text=sett.lang['system']['menu_options'], takefocus=False, width=0, padding=0,
                           command=lambda e=0: action.do_action([0, False, 'mw1', 'main_menu', 'main_menu_options'])).grid(row=self.s_row, column=self.s_collumn + 1, sticky="w", padx=(0, bor),
                                                                                                                           pady=(0, tx_bor))

        tkinter.ttk.Button(self.fr_it, style="Custom.TButton", text="✖", takefocus=False, width=0, padding=0,
                           command=lambda e=0: action.do_action([0, False, 'mw1', 'main_menu', 'main_menu_exit'])).grid(row=self.s_row, column=self.s_collumn + 2, sticky="e", padx=(0, bor),
                                                                                                                        pady=(0, tx_bor))

        self.s_row += 1

    def cr_up_btn(self, menu_list, frame):
        frame.grid_columnconfigure(self.s_collumn, minsize=bor * 11)
        frame.grid_columnconfigure(self.s_collumn + 1, minsize=bor * 11)
        frame.grid_columnconfigure(self.s_collumn + 2, minsize=bor * 10)
        frame.grid_rowconfigure(self.s_row, minsize=bor * 2)
        module = menu_list.pop(3)
        state_list = []
        for i in range(3):
            state_list.append(menu_list[i].pop(1))
            menu_list[i] = tkinter.ttk.Button(frame, style="Custom.TButton", text=menu_list[i][0], takefocus=False, width=0, padding=0,
                                              command=lambda m=module, f=menu_list[i][1], i=menu_list[i][2]: action.do_action([0, False, 'mw1', m, f, i]))
            menu_list[i].grid(row=self.s_row, column=self.s_collumn + i, sticky="nsew", pady=(0, tx_bor))
            menu_list[i].configure(state=state_list[i])
        self.s_row += 1

    def cr_fr_it(self, frame, rowspan=None, pady=(0, 0), padx=bor):
        if rowspan is None:
            self.fr_it = tkinter.Frame(frame, background=sett.bg_col)
            self.fr_it.grid(row=self.s_row, column=self.s_collumn, rowspan=frame.grid_size()[1], columnspan=3, sticky="nw", padx=padx, pady=pady)
            self.set_orig_point()
        else:
            self.fr_it = tkinter.Frame(frame, background=sett.bg_col)
            self.fr_it.grid(row=self.s_row, column=self.s_collumn, rowspan=rowspan, columnspan=3, sticky="nw", padx=padx, pady=pady)
            self.set_orig_point()

    def start_construct(self):

        def add_btnlist(data):

            def change_page(dir):
                if dir is True:
                    self.clear_frame(False)
                    header["cur_page"] -= 1
                    btnlist_construct()
                else:
                    self.clear_frame(False)
                    header["cur_page"] += 1
                    btnlist_construct()

            def btnlist_construct():
                for e in items_list[(header["cur_page"] - 1) * header["items_on_page"]:header["cur_page"] * header["items_on_page"]]:
                    if e['type'] == 'item':
                        tkinter.Frame(self.fr_it, background=sett.bg_col, width=bor * ((self.col_width * header["columnspan"]) + self.width_corr), height=header['btn_size']).grid(row=self.s_row,
                                                                                                                                                                                   column=self.s_collumn,
                                                                                                                                                                                   sticky="new",
                                                                                                                                                                                   columnspan=header[
                                                                                                                                                                                       "columnspan"])
                        tkinter.ttk.Button(self.fr_it, style=header['style'], text=e["text"], state=e["state"], takefocus=False, width=0, padding=0,
                                           command=lambda a=e["action"]: action.do_action(a)).grid(row=self.s_row, column=self.s_collumn, columnspan=header["columnspan"], sticky="nsew")
                        self.s_row += 1

                    elif e['type'] == 'spacer':
                        tkinter.Frame(self.fr_it, background=sett.bg_col, width=bor * ((self.col_width * header["columnspan"]) + self.width_corr), height=header['btn_size']).grid(row=self.s_row,
                                                                                                                                                                                   column=self.s_collumn,
                                                                                                                                                                                   sticky="new",
                                                                                                                                                                                   columnspan=header[
                                                                                                                                                                                       "columnspan"])
                        tkinter.ttk.Button(self.fr_it, style=header['style'], text=e["text"], takefocus=False, width=0, padding=0, ).grid(row=self.s_row, column=self.s_collumn,
                                                                                                                                          columnspan=header["columnspan"], sticky="nsew")
                        self.s_row += 1
                if header["pages_count"] > 1:
                    # add pages
                    tkinter.Frame(self.fr_it, background=sett.bg_col, height=bor * 3, width=bor * 3).grid(row=self.s_row, column=self.s_collumn, sticky="nsew")
                    tkinter.Frame(self.fr_it, background=sett.bg_col, height=bor * 3, width=bor * 23).grid(row=self.s_row, column=self.s_collumn + 1, sticky="nsew")
                    tkinter.Frame(self.fr_it, background=sett.bg_col, height=bor * 3, width=bor * 3).grid(row=self.s_row, column=self.s_collumn + 2, sticky="nsew")

                    if header["cur_page"] == 1:
                        tkinter.ttk.Button(self.fr_it, style="Custom.TButton", text=" < ", takefocus=False, width=0, padding=0, state='disabled').grid(row=self.s_row, column=self.s_collumn,
                                                                                                                                                       sticky="nsew")
                        tkinter.ttk.Label(self.fr_it, text=str(header["cur_page"]) + "/" + str(header["pages_count"]), style="Custom.TLabel", anchor="center").grid(row=self.s_row,
                                                                                                                                                                    column=self.s_collumn + 1,
                                                                                                                                                                    sticky="nsew")
                        tkinter.ttk.Button(self.fr_it, style="Custom.TButton", text=" > ", takefocus=False, width=0, padding=0, command=lambda: change_page(False)).grid(row=self.s_row,
                                                                                                                                                                         column=self.s_collumn + 2,
                                                                                                                                                                         sticky="nsew")

                    elif 1 < header["cur_page"] < header["pages_count"]:
                        tkinter.ttk.Button(self.fr_it, style="Custom.TButton", text=" < ", takefocus=False, width=0, padding=0, command=lambda: change_page(True)).grid(row=self.s_row,
                                                                                                                                                                        column=self.s_collumn,
                                                                                                                                                                        sticky="nsew")
                        tkinter.ttk.Label(self.fr_it, text=str(header["cur_page"]) + "/" + str(header["pages_count"]), style="Custom.TLabel", anchor="center").grid(row=self.s_row,
                                                                                                                                                                    column=self.s_collumn + 1,
                                                                                                                                                                    sticky="nsew")
                        tkinter.ttk.Button(self.fr_it, style="Custom.TButton", text=" > ", takefocus=False, width=0, padding=0, command=lambda: change_page(False)).grid(row=self.s_row,
                                                                                                                                                                         column=self.s_collumn + 2,
                                                                                                                                                                         sticky="nsew")
                    else:
                        tkinter.ttk.Button(self.fr_it, style="Custom.TButton", text=" < ", takefocus=False, width=0, padding=0, command=lambda: change_page(True)).grid(row=self.s_row,
                                                                                                                                                                        column=self.s_collumn,
                                                                                                                                                                        sticky="nsew")
                        tkinter.ttk.Label(self.fr_it, text=str(header["cur_page"]) + "/" + str(header["pages_count"]), style="Custom.TLabel", anchor="center").grid(row=self.s_row,
                                                                                                                                                                    column=self.s_collumn + 1,
                                                                                                                                                                    sticky="nsew")
                        tkinter.ttk.Button(self.fr_it, style="Custom.TButton", text=" > ", takefocus=False, width=0, padding=0, state='disabled').grid(row=self.s_row, column=self.s_collumn + 2,
                                                                                                                                                       sticky="nsew")

            items_list = data['item_list']
            del data['item_list']

            header = data
            data = None

            header['items_count'] = len(items_list)

            if header["items_count"] > header["items_on_page"]:
                # paged
                header["btn_size"] = int((self.h_bor - 3) / header["items_on_page"] * bor)
                if header["items_count"] % header["items_on_page"] > 0:
                    header["pages_count"] = (header["items_count"] // header["items_on_page"]) + 1
                    for n in range(header["items_on_page"] - (header["items_count"] % header["items_on_page"])):
                        items_list.append({"type": "spacer", "text": header["items_spacer"]})

                else:
                    header["pages_count"] = (header["items_count"] // header["items_on_page"])
            else:
                # not paged
                if header["items_count"] < header["items_on_page"]:
                    for n in range(header["items_on_page"] - header["items_count"]):
                        items_list.append({"type": "spacer", "text": header["items_spacer"]})
                header["btn_size"] = int((self.h_bor) / header["items_on_page"] * bor)
                header["pages_count"] = 1

            header["cur_page"] = 1

            btnlist_construct()

        def add_picbtnlist(data):

            def change_page(dir):
                if dir is True:
                    self.clear_frame(False)
                    header["cur_page"] -= 1
                    btnlist_construct()
                else:
                    self.clear_frame(False)
                    header["cur_page"] += 1
                    btnlist_construct()

            def btnlist_construct():
                for e in items_list[(header["cur_page"] - 1) * header["items_on_page"]:header["cur_page"] * header["items_on_page"]]:
                    if e['type'] == 'item':
                        tkinter.Frame(self.fr_it, background=sett.bg_col, width=bor * ((self.col_width * header['columnspan']) + self.width_corr), height=header['btn_size']).grid(row=self.s_row, column=self.s_collumn,
                                                                                                                                                                                   sticky='new',
                                                                                                                                                                                   columnspan=header['columnspan'])
                        e['img'] = e['img'].split('-')
                        cur_pic = tkinter.PhotoImage(file='data/icons/' + e['img'][0] + '/' + e['img'][1] + '/' + str(self.col_width) + '.png')
                        btn = tkinter.ttk.Button(self.fr_it, style=header['style'], text=e['text'], state=e['state'], takefocus=False, width=0, padding=0, image=cur_pic, compound="left",
                                                 command=lambda a=e['action']: action.do_action(a))

                        btn.image = cur_pic
                        btn.grid(row=self.s_row, column=self.s_collumn, columnspan=header['columnspan'], sticky="nsew")
                        self.s_row += 1

                    elif e['type'] == 'spacer':
                        tkinter.Frame(self.fr_it, background=sett.bg_col, width=bor * ((self.col_width * header["columnspan"]) + self.width_corr), height=header['btn_size']).grid(row=self.s_row,
                                                                                                                                                                                   column=self.s_collumn,
                                                                                                                                                                                   sticky="new",
                                                                                                                                                                                   columnspan=header[
                                                                                                                                                                                       "columnspan"])

                        cur_pic = tkinter.PhotoImage(file='data/icons/MISC/empty/' + str(self.col_width) + '.png')
                        btn = tkinter.ttk.Button(self.fr_it, style=header['style'], text=e["text"], takefocus=False, width=0, padding=0, image=cur_pic, compound="left")

                        btn.image = cur_pic
                        btn.grid(row=self.s_row, column=self.s_collumn, columnspan=header["columnspan"], sticky="nsew")

                        self.s_row += 1
                if header["pages_count"] > 1:
                    # add pages
                    tkinter.Frame(self.fr_it, background=sett.bg_col, height=bor * 3, width=bor * 3).grid(row=self.s_row, column=self.s_collumn, sticky="nsew")
                    tkinter.Frame(self.fr_it, background=sett.bg_col, height=bor * 3, width=bor * 23).grid(row=self.s_row, column=self.s_collumn + 1, sticky="nsew")
                    tkinter.Frame(self.fr_it, background=sett.bg_col, height=bor * 3, width=bor * 3).grid(row=self.s_row, column=self.s_collumn + 2, sticky="nsew")

                    if header["cur_page"] == 1:
                        tkinter.ttk.Button(self.fr_it, style="Custom.TButton", text=" < ", takefocus=False, width=0, padding=0, state='disabled').grid(row=self.s_row, column=self.s_collumn,
                                                                                                                                                       sticky="nsew")
                        tkinter.ttk.Label(self.fr_it, text=str(header["cur_page"]) + "/" + str(header["pages_count"]), style="Custom.TLabel", anchor="center").grid(row=self.s_row,
                                                                                                                                                                    column=self.s_collumn + 1,
                                                                                                                                                                    sticky="nsew")
                        tkinter.ttk.Button(self.fr_it, style="Custom.TButton", text=" > ", takefocus=False, width=0, padding=0, command=lambda: change_page(False)).grid(row=self.s_row,
                                                                                                                                                                         column=self.s_collumn + 2,
                                                                                                                                                                         sticky="nsew")

                    elif 1 < header["cur_page"] < header["pages_count"]:
                        tkinter.ttk.Button(self.fr_it, style="Custom.TButton", text=" < ", takefocus=False, width=0, padding=0, command=lambda: change_page(True)).grid(row=self.s_row,
                                                                                                                                                                        column=self.s_collumn,
                                                                                                                                                                        sticky="nsew")
                        tkinter.ttk.Label(self.fr_it, text=str(header["cur_page"]) + "/" + str(header["pages_count"]), style="Custom.TLabel", anchor="center").grid(row=self.s_row,
                                                                                                                                                                    column=self.s_collumn + 1,
                                                                                                                                                                    sticky="nsew")
                        tkinter.ttk.Button(self.fr_it, style="Custom.TButton", text=" > ", takefocus=False, width=0, padding=0, command=lambda: change_page(False)).grid(row=self.s_row,
                                                                                                                                                                         column=self.s_collumn + 2,
                                                                                                                                                                         sticky="nsew")
                    else:
                        tkinter.ttk.Button(self.fr_it, style="Custom.TButton", text=" < ", takefocus=False, width=0, padding=0, command=lambda: change_page(True)).grid(row=self.s_row,
                                                                                                                                                                        column=self.s_collumn,
                                                                                                                                                                        sticky="nsew")
                        tkinter.ttk.Label(self.fr_it, text=str(header["cur_page"]) + "/" + str(header["pages_count"]), style="Custom.TLabel", anchor="center").grid(row=self.s_row,
                                                                                                                                                                    column=self.s_collumn + 1,
                                                                                                                                                                    sticky="nsew")
                        tkinter.ttk.Button(self.fr_it, style="Custom.TButton", text=" > ", takefocus=False, width=0, padding=0, state='disabled').grid(row=self.s_row, column=self.s_collumn + 2,
                                                                                                                                                       sticky="nsew")

            items_list = data['item_list']
            del data['item_list']

            header = data
            data = None

            header['items_count'] = len(items_list)

            if header["items_count"] > header["items_on_page"]:
                # paged
                header["btn_size"] = int((self.h_bor - 3) / header["items_on_page"] * bor)
                if header["items_count"] % header["items_on_page"] > 0:
                    header["pages_count"] = (header["items_count"] // header["items_on_page"]) + 1
                    for n in range(header["items_on_page"] - (header["items_count"] % header["items_on_page"])):
                        items_list.append({"type": "spacer", "text": header["items_spacer"]})

                else:
                    header["pages_count"] = (header["items_count"] // header["items_on_page"])
            else:
                # not paged
                if header["items_count"] < header["items_on_page"]:
                    for n in range(header["items_on_page"] - header["items_count"]):
                        items_list.append({"type": "spacer", "text": header["items_spacer"]})
                header["btn_size"] = int((self.h_bor) / header["items_on_page"] * bor)
                header["pages_count"] = 1

            header["cur_page"] = 1

            btnlist_construct()

        def add_label(style, text, column, h_bor=bor * 2, columnspan=3, rowspan=1, pady=(0, tx_bor), padx=(0, 0)):
            tkinter.Frame(self.fr_it, background=sett.bg_col, width=bor * ((self.col_width * columnspan) + self.width_corr), height=h_bor).grid(row=self.s_row, column=column, columnspan=columnspan,
                                                                                                                                                rowspan=rowspan, sticky="new", pady=pady, padx=padx)
            tkinter.ttk.Label(self.fr_it, text=text, style=style[0], anchor=style[1]).grid(row=self.s_row, column=column, columnspan=columnspan, sticky="new", pady=pady, padx=padx)

        def add_image(image, pad=(0, 0), size=0, rowspan=1):
            image = image.split('-')
            cur_pic = tkinter.PhotoImage(file='data/icons/' + image[0] + '/' + image[1] + '/' + str(self.col_width + 1) + '.png')

            pic_label = tkinter.ttk.Label(self.fr_it, image=cur_pic, style="Custom_sm.TLabel")
            pic_label.image = cur_pic
            pic_label.grid(row=self.s_row, column=self.s_collumn, rowspan=rowspan, sticky="nw", pady=pad, padx=pad)

        def add_buttons(data_btn, style, rowspan=1, horizontal=True, pady=(0, tx_bor), padx=(0)):
            if horizontal is True:
                btn_len = len(data_btn)
                for b in range(btn_len):
                    tkinter.Frame(self.fr_it, background=sett.bg_col, width=bor * ((self.col_width * data_btn[b]["columnspan"]) + self.width_corr)).grid(row=self.s_row, column=self.s_collumn + b,
                                                                                                                                                         sticky="new", rowspan=rowspan,
                                                                                                                                                         columnspan=data_btn[b]["columnspan"],
                                                                                                                                                         pady=pady, padx=padx)

                for b in range(btn_len):
                    if data_btn[b]["action"][4] == "item_close":
                        tkinter.ttk.Button(self.fr_it, style=style, text=data_btn[b]["text"], state=data_btn[b]["state"], takefocus=False, width=0, padding=0,
                                           command=lambda: self.clear_frame(True)).grid(row=self.s_row, column=self.s_collumn + b, columnspan=data_btn[b]["columnspan"], sticky="nsew", pady=pady,
                                                                                        padx=padx)

                    elif data_btn[b]["action"][4] == "refresh":
                        del data_btn[b]["action"][4]
                        tkinter.ttk.Button(self.fr_it, style=style, text=data_btn[b]["text"], state=data_btn[b]["state"], takefocus=False, width=0, padding=0,
                                           command=lambda a=data_btn[b]["action"]: self.refresh(a)).grid(row=self.s_row,
                                                                                                         column=self.s_collumn + b,
                                                                                                         columnspan=data_btn[b]["columnspan"],
                                                                                                         sticky="nsew", pady=pady, padx=padx)

                    else:
                        tkinter.ttk.Button(self.fr_it, style=style, text=data_btn[b]["text"], state=data_btn[b]["state"], takefocus=False, width=0, padding=0,
                                           command=lambda a=data_btn[b]["action"]: action.do_action(a)).grid(row=self.s_row, column=self.s_collumn + b, columnspan=data_btn[b]["columnspan"],
                                                                                                             sticky="nsew", pady=pady, padx=padx)

        def add_text(h_bor, text_list, style, slider, glob, padx=(0, 0), columnspan=3, rowspan=1, pady=(0, tx_bor)):

            def hyperlink(tag, act, type, func=None):
                if act == "Leave":
                    txt.tag_config(tag, foreground=col_list[0])
                    txt.update()
                elif act == "Enter":
                    txt.tag_config(tag, foreground=col_list[2])
                    txt.update()
                elif act == "ButtonPress":
                    txt.tag_config(tag, foreground=col_list[3])
                    txt.update()
                    do = [0, False, "link"]
                    for f in func:
                        do.append(f)
                    action.do_action(do)

            s_keys = style.keys()
            if "col_list" in s_keys:
                col_list = [style["col_list"]["fg_col"], style["col_list"]["fg_col_d"], style["col_list"]["fg_col2"], style["col_list"]["fg_col_cont"]]
            else:
                col_list = [sett.fg_col, sett.fg_col_d, sett.fg_col2, sett.fg_col_cont]

            if "font" in s_keys:
                font = (style["font"][0], tx_bor * style["font"][1])
            else:
                font = ('EurostileExtReg', tx_bor * 2)

            tkinter.Frame(self.fr_it, background=sett.bg_col, height=bor * h_bor).grid(row=self.s_row, column=self.s_collumn, columnspan=3, sticky="nsew", pady=pady, padx=padx)
            txt = tkinter.Text(self.fr_it, height=0, width=0, wrap="word", selectbackground=sett.bg_col, borderwidth=0, background=sett.bg_col, foreground=sett.fg_col, font=font,
                               cursor='@cross_or.cur')

            # header_tags
            txt.tag_config("header_fg_col", foreground=col_list[0], lmargin1=bor)
            txt.tag_config("header_fg_col_d", foreground=col_list[1], lmargin1=bor)
            txt.tag_config("header_fg_col2", foreground=col_list[2], lmargin1=bor)
            txt.tag_config("header_fg_col_cont", foreground=col_list[3], lmargin1=bor)

            # actor_tags
            txt.tag_config("actor_fg_col", foreground=col_list[0], lmargin1=bor * 12, lmargin2=bor * 12, background=sett.bg_col2, justify="right")
            txt.tag_config("actor_fg_col_d", foreground=col_list[1], lmargin1=bor * 12, lmargin2=bor * 12, background=sett.bg_col2, justify="right")
            txt.tag_config("actor_fg_col2", foreground=col_list[2], lmargin1=bor * 12, lmargin2=bor * 12, background=sett.bg_col2, justify="right")
            txt.tag_config("actor_fg_col_cont", foreground=col_list[3], lmargin1=bor * 12, lmargin2=bor * 12, background=sett.bg_col2, justify="right")

            # npc_tags
            txt.tag_config("npc_fg_col", foreground=col_list[0], rmargin=bor * 10, justify="left")
            txt.tag_config("npc_fg_col_d", foreground=col_list[1], rmargin=bor * 10, justify="left")
            txt.tag_config("npc_fg_col2", foreground=col_list[2], rmargin=bor * 10, justify="left")
            txt.tag_config("npc_fg_col_cont", foreground=col_list[3], rmargin=bor * 10, justify="left")

            # else_tags
            txt.tag_config("fg_col", foreground=col_list[0], justify="left")
            txt.tag_config("fg_col_d", foreground=col_list[1], justify="left")
            txt.tag_config("fg_col2", foreground=col_list[2], justify="left")
            txt.tag_config("fg_col_cont", foreground=col_list[3], justify="left")

            if text_list[0][1] == 'link':
                i = 1
                for t in enumerate(text_list):
                    t[1][1] = t[1][1] + str(i)
                    tag = "link" + str(i)
                    txt.tag_config(tag, foreground=col_list[0])
                    txt.tag_bind(tag, "<Enter>", lambda a="on", t=tag, g=t[1][2]: hyperlink(t, str(a.type), g))
                    txt.tag_bind(tag, "<Leave>", lambda a="off", t=tag, g=t[1][2]: hyperlink(t, str(a.type), g))
                    txt.tag_bind(tag, "<Button-1>", lambda a="Click", t=tag, g=t[1][2], f=(t[1][3][0], t[1][3][1], t[1][0]): hyperlink(t, str(a.type), g, func=f))
                    i += 1

            for i in text_list:

                if i[2] == "header":
                    txt.insert("end", '[' + i[0] + ']', i[2] + '_' + i[1])
                elif i[2] in ("actor", "npc"):
                    txt.insert("end", i[0], i[2] + '_' + i[1])
                else:
                    txt.insert("end", i[0], i[1])

            if slider is True:
                scroll = tkinter.ttk.Scrollbar(self.fr_it, style="Custom_sm.Vertical.TScrollbar", command=txt.yview)
                scroll.grid(row=self.s_row, column=self.s_collumn + 2, sticky="nes", pady=pady, padx=padx)
                txt.config(yscrollcommand=scroll.set)

            txt.grid(row=self.s_row, columnspan=columnspan, rowspan=rowspan, column=self.s_collumn, sticky="nsew", pady=pady, padx=(padx[0], bor * 2))

            if glob is True:
                self.txt_wgt = txt

        def add_line(show, columnspan, pady, padx):
            if show is True:
                tkinter.Frame(self.fr_it, background=sett.fg_col, height=1, width=bor * (((self.col_width * columnspan) - 2) + self.width_corr)).grid(row=self.s_row, column=self.s_collumn, columnspan=columnspan,
                                                                                                                                                      sticky="nsew", padx=padx, pady=pady)
            else:
                tkinter.Frame(self.fr_it, background=sett.bg_col, height=1, width=bor * (((self.col_width * columnspan) - 2) + self.width_corr)).grid(row=self.s_row, column=self.s_collumn, columnspan=columnspan,
                                                                                                                                                      sticky="nsew", padx=padx, pady=pady)

        def add_frame(style, h_bor, columnspan, rowspan, pady, padx):
            if style == 'Custom_b':
                tkinter.ttk.Frame(self.fr_it, style='Custom_b.TFrame', height=bor * h_bor, width=bor * (((self.col_width * columnspan) - 2) + self.width_corr)).grid(row=self.s_row, rowspan=rowspan, column=self.s_collumn,
                                                                                                                                                                     columnspan=columnspan, sticky="nsew", padx=padx,
                                                                                                                                                                     pady=pady)

        long_data = []
        #s_row_save = None
        default_param = {'frame': {'columnspan': 3, 'rowspan': 1, 'pady': (0, tx_bor), 'padx': (0, 0)}, 'line': {'show': False, 'columnspan': 3, 'pady': (0, 0), 'padx': (bor, bor)}}

        for i in self.construct:
            if i['long'] is False:
                if i['type'] == 'label':
                    add_label(i['style'], i['text'], self.s_collumn)
                    self.s_row += 1

                elif i["type"] == 'img+label':
                    add_image(i['img'])
                    add_label(i['style'], i['text'], self.s_collumn + 1, columnspan=2)
                    self.s_row += 1

                elif i['type'] == 'btn':
                    add_buttons(i['btn_data'], i['style'])
                    self.s_row += 1

                elif i['type'] == 'button_list':
                    add_btnlist(i)
                    self.s_row += 1
                elif i['type'] == 'pic_button_list':
                    add_picbtnlist(i)
                    self.s_row += 1

                elif i["type"] == 'line':
                    paramlist = []
                    item_keys = i.keys()

                    for par in default_param[i["type"]].keys():
                        if par in item_keys:

                            paramlist.append(i[par])
                        else:
                            paramlist.append(default_param[i["type"]][par])
                    add_line(paramlist[0], paramlist[1], paramlist[2], paramlist[3])
                    self.s_row += 1

                elif i["type"] == 'frame':
                    paramlist = []
                    item_keys = i.keys()
                    paramlist.append(i["style"])
                    paramlist.append(i["h_bor"])

                    for par in ['columnspan', 'rowspan', 'pady', 'padx']:
                        if par in item_keys:
                            paramlist.append(i["par"])
                        else:
                            paramlist.append(default_param[i["type"]][i["par"]])

                    add_frame(paramlist)

            else:

                long_data.append([i, self.s_row])
                self.s_row += 1

        if len(long_data) > 0:
            s_row_save = self.s_row
            self.h_bor = ((self.h_bor - self.calc_long()) // len(long_data)) - 1
            for l in long_data:

                self.s_row = l[1]
                if l[0]["type"] == 'label':
                    self.add_label(style=l[0]["style"], text=l[0]["text"])
                elif l[0]["type"] == 'text':
                    add_text(self.h_bor, l[0]["text_list"], l[0]["style"], l[0]["slider"], l[0]["glob"])

    def clear_frame(self, final=False):
        for w in self.fr_it.grid_slaves():
            w.grid_forget()
            self.construct = []
            self.get_orig_point()

        if final is True:
            self.fr_it.grid_forget()
            self.get_orig_point()

    def refresh(self, act):
        print("ref_act")
        print(act)
        action.do_action(act)
        for w in self.fr_it.grid_slaves():
            w.grid_forget()
            self.fr_it.grid_forget()

    @staticmethod
    def update():
        print("update")

    def calc_long(self):
        self.fr_it.update()
        return self.fr_it.winfo_height() // bor


class Transmissions:
    def __init__(self):
        # таймер//10 копирнуть, поделить на длину радио, полученное умножить на длинну радио, если больше длинны радио , то удалить длинну радио, и в итоге получится сремя старта
        self.freq_dict = {79.9: None, 102.2: ['Espantoso', 'Espantoso', 3698], 103.0: ['Wave 103', 'Wave_103', 3033], 103.5: ['Flash FM', 'Flash_FM', 3792], 105.0: ['Fever 105', 'Fever_105', 3794], 200.0: None}
        self.cur_freq = 102.2
        self.freq_list = [*self.freq_dict.keys()]
        self.freq_fav_list = [103.0, 102.2]
        print('music_pos_rep')

        self.cur_freq_play = False

    def ret_ferq_data(self):
        if self.cur_freq in self.freq_list[1:-1]:
            return self.freq_dict[self.cur_freq]
        else:
            return ['N/A', 'emp_freq', 300]

    def ferq_ch(self, direct):
        if direct is True:
            if self.cur_freq + 0.1 == self.freq_list[-1]:
                self.cur_freq = self.freq_list[0] + 0.1
            else:
                self.cur_freq = round(self.cur_freq + 0.1, 1)
        else:
            if self.cur_freq - 0.1 == self.freq_list[0]:
                self.cur_freq = self.freq_list[-1] - 0.1
            else:
                self.cur_freq = round(self.cur_freq - 0.1, 1)

    def ferq_fav_ch(self, direct):

        list_enders = (0, len(self.freq_list) - 1)
        st_fav = 0

        if direct is True:
            for i in self.freq_list:
                if (round(abs(i - self.cur_freq), 1) + round(i - self.cur_freq, 1)) > 0:
                    st_fav = self.freq_list.index(i)
                    break
        else:
            for i in self.freq_list:
                if (round(abs(i - self.cur_freq), 1) + round(i - self.cur_freq, 1)) > 0:
                    st_fav = (self.freq_list.index(i) - 2)
                    if st_fav < 0:
                        st_fav = 0
                    break

        if st_fav in list_enders:
            print('in enders')
            if st_fav == list_enders[0]:
                self.cur_freq = self.freq_list[-2]
            else:
                self.cur_freq = self.freq_list[1]
        else:
            print(self.cur_freq)
            self.cur_freq = self.freq_list[st_fav]
            print(self.cur_freq)

    def cr_radio_wiget(self, frame, size, row, column, height):

        if size == 'small':
            profile_wiget = CrItem()

            profile_wiget.s_row = row
            profile_wiget.s_collumn = column
            profile_wiget.h_bor = height
            profile_wiget.construct.append({"type": "line", "long": False, "show": True, "pady": (0, tx_bor)})
            profile_wiget.construct.append({"type": "label", "style": ["Custom_sm_lt.TLabel", "nw"], "long": False, "text": "Частота: "+str(self.cur_freq)+"\n"+"Имя станции:"+self.ret_ferq_data()[0]+"\n"+"Избранное: Да"})
            if transm.cur_freq_play is True:
                profile_wiget.construct.append(
                    {"type": "btn", "style": "Custom.TButton", "long": False, "btn_data": [{"state": "disabled", "text": " ▲ ", "columnspan": 1, "action": [0, False, 'transm', 'freq',  'refresh', '+', [frame, size, row, column, height]]},
                                                                                           {"state": "enabled", "text": " ■ ", "columnspan": 1, "action": [0, False, 'transm', 'freq',  'refresh', 'stop', [frame, size, row, column, height]]},
                                                                                           {"state": "disabled", "text": " ▼ ", "columnspan": 1, "action": [0, False, 'transm', 'freq',  'refresh', '-', [frame, size, row, column, height]]}]})
            else:
                profile_wiget.construct.append(
                    {"type": "btn", "style": "Custom.TButton", "long": False, "btn_data": [{"state": "disabled", "text": " ▲ ", "columnspan": 1, "action": [0, False, 'transm', 'freq',  'refresh', '+', [frame, size, row, column, height]]},
                                                                                           {"state": "enabled", "text": " ► ", "columnspan": 1, "action": [0, False, 'transm', 'freq',  'refresh', 'play', [frame, size, row, column, height]]},
                                                                                           {"state": "disabled", "text": " ▼ ", "columnspan": 1, "action": [0, False, 'transm', 'freq',  'refresh', '-', [frame, size, row, column, height]]}]})

            if self.cur_freq in self.freq_fav_list:
                profile_wiget.construct.append(
                    {"type": "btn", "style": "Custom.TButton", "long": False, "btn_data": [{"state": "enabled", "text": " ◄ ", "columnspan": 1, "action": [0, False, 'transm', 'freq',  'refresh', 'prew_fav', [frame, size, row, column, height]]},
                                                                                           {"state": "disabled", "text": " ★ ", "columnspan": 1, "action": [0, False, 'transm', 'freq',  'refresh', 'unfav', [frame, size, row, column, height]]},
                                                                                           {"state": "enabled", "text": " ► ", "columnspan": 1, "action": [0, False, 'transm', 'freq',  'refresh', 'next_fav', [frame, size, row, column, height]]}]})
            else:
                profile_wiget.construct.append(
                    {"type": "btn", "style": "Custom.TButton", "long": False, "btn_data": [{"state": "enabled", "text": " ◄ ", "columnspan": 1, "action": [0, False, 'transm', 'freq',  'refresh', 'prew_fav', [frame, size, row, column, height]]},
                                                                                           {"state": "disabled", "text": " ☆ ", "columnspan": 1, "action": [0, False, 'transm', 'freq',  'refresh', 'fav', [frame, size, row, column, height]]},
                                                                                           {"state": "enabled", "text": " ► ", "columnspan": 1, "action": [0, False, 'transm', 'freq',  'refresh', 'next_fav', [frame, size, row, column, height]]}]})



            profile_wiget.construct.append({"type": "line", "long": False, "show": True, "pady": (0, tx_bor)})

            profile_wiget.cr_fr_it(frame, height, (tx_bor, 0))
            profile_wiget.start_construct()


class LittleMenu:
    def __init__(self, name_w, frame, cur_dir):
        tkinter.Frame(frame, background=sett.bg_col).grid(row=0, columnspan=8, column=0, sticky="nsew", ipadx=bor * 30)
        for i in range(8):
            if i == cur_dir:
                tkinter.ttk.Button(frame, style="Custom.TButton", text=sett.lang['system']['menu_list_sm'][i], takefocus=False, width=4, padding=0, state='disabled').grid(row=0, column=i, sticky="sew",
                                                                                                                                                                           pady=(bor, 0))
            else:
                tkinter.ttk.Button(frame, style="Custom.TButton", text=sett.lang['system']['menu_list_sm'][i], takefocus=False, width=4, padding=0).grid(row=0, column=i, sticky="sew", pady=(bor, 0))
        tkinter.ttk.Button(frame, style="Custom.TButton", text="✖", takefocus=False, width=4, padding=0, command=lambda e=8: self.btn_press(name_w, e)).grid(row=0, column=8, sticky="se",
                                                                                                                                                             pady=(bor, 0), padx=(bor * 6, 0))

    @staticmethod
    def btn_press(name_w, num):
        if name_w == "mw1":
            if num == 8:
                mw1.exit()


guitimer = GuiTimer()

guitimer.start()

action = ActionHandler()

datahook = DataHook()

audio = AudioDrive()

user_profile = Profile()

computer = Computer("computer")

keyh = Thread(target=key_hook)
keyh.daemon = True
keyh.start()



mw1 = MainWindow("mw1")

olay = OverLay()

topwin = TopWin()

missions = Missions()

inventory = Inventory()

npc = NPC()

statistics = Statistics()

transm = Transmissions()

if sett.extra_sound_module is True:
    extra_sound = ExtraSound()

guitimer.add_timer([1, False, 'olay', 'add_state_item', sett.lang['state_items']['system']['system_start'], "notific"])



root.mainloop()
