from tkinter import *

from tkinter.ttk import Combobox

from tkinter import messagebox
from tkinter import colorchooser

from tkinter.filedialog import askdirectory, askopenfilename

from PIL import ImageTk, Image

from pathlib import Path
import json


def read_file(path, f_name):
    fp = open(path + f_name, mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
    read_data = json.loads(fp.read())
    fp.close()
    return read_data


def write_data(path, f_name, w_data):
    w_data = json.dumps(w_data, ensure_ascii=False, indent=4)
    fp = open(path + f_name, mode='w', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)
    fp.write(w_data)
    fp.close()


def find_file(path, f_name):
    data = None
    for x in Path(path).iterdir():
        if x.name == f_name:
            data = read_file(path, f_name)
            break
    else:
        messagebox.showerror('Файловая ошибка!', 'Отсутствует ' + f_name)
    return data


def dir_list(path):
    dirs = []
    p = Path(path)

    for x in p.iterdir():
        if x.is_dir():
            dirs.append(str(x).split("\\")[-1])

    return dirs


def file_list(path, ext):
    files = []
    p = Path(path)

    for x in p.iterdir():
        if x.is_file():
            if ext is True:
                files.append(str(x).split('\\')[-1])
            else:
                files.append(str(x).split('\\')[-1].split('.')[0])

    return files


def find_dir(path, dir_name, message=True):
    direct = False
    for x in Path(path).iterdir():
        if x.is_dir():
            if x.name == dir_name:
                direct = True
                break
    else:
        if message is True:
            messagebox.showerror('Файловая ошибка!', 'Отсутствует папка ' + dir_name)
    return direct


def clear_mainframe():
    for w in main_frame.grid_slaves():
        w.grid_forget()


def default_settings(category):
    global settings
    settings = read_file(miex_path + '/data/profile/', 'settings_d.txt')
    write_data(miex_path + '/data/profile/', 'settings.txt', settings)
    cr_new_win(category)


def cr_new_win(category):
    clear_mainframe()
    global miex_path
    global settings
    global full_win
    global language
    cur_row = 0

    if full_win is True:
        for widget in root.winfo_children():
            if isinstance(widget, Toplevel):
                widget.destroy()
        full_win = False

    if category == 'basic':

        def choose_log_dir():
            log_path = askdirectory().replace('\\', '/')
            log_path_lb.config(text=str(log_path))
            settings['ed_log_folder'] = log_path
            file_list = []
            for x in Path(log_path).iterdir():
                if x.is_file():
                    if x.stem[0:8] == "Journal." and x.stem[-3] == ".":
                        file_list.append(x)

            settings['log_files_len'] = len(file_list)
            main_frame.update()

        def save_settings():

            settings['language'] = lang.get()
            settings['resolution'][0] = resolution_0.get()
            settings['resolution'][1] = resolution_1.get()
            settings['data_hook_time'] = data_hook_time.get()
            settings['ed_start_time'] = ed_start_time.get()
            settings['extra_sound'] = extra_sound_var.get()
            settings['voice_assist'] = voice_assist_var.get()

            write_data(miex_path + '/data/profile/', 'settings.txt', settings)

        Label(main_frame, text=language['basic']['lang']).grid(row=cur_row, column=0, padx=(10, 5), pady=5, sticky="nw")

        lang = Combobox(main_frame, width=8)
        lang['values'] = (file_list(miex_path + '/data/lang', False))
        lang.set(settings['language'])

        lang.grid(column=1, columnspan=3, sticky='nw', row=cur_row, padx=(5, 10))

        cur_row += 1
        Label(main_frame, text=language['basic']['resolution']).grid(row=cur_row, column=0, padx=(10, 5), pady=5, sticky="nw")

        resolution_0 = Entry(main_frame, width=8)
        resolution_0.grid(row=cur_row, column=1, padx=5, pady=5, sticky="nw")
        resolution_0.insert(0, settings['resolution'][0])

        Label(main_frame, text="x").grid(row=cur_row, column=2, pady=5, sticky="nw")

        resolution_1 = Entry(main_frame, width=8)
        resolution_1.grid(row=cur_row, column=3, padx=(5, 20), pady=5, sticky="nw")
        resolution_1.insert(0, settings['resolution'][1])

        cur_row += 1

        LabelFrame(main_frame, labelanchor="n", text=language['basic']['log_header']).grid(row=cur_row, rowspan=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        Label(main_frame, text=language['basic']['log_path']).grid(row=cur_row, column=0, columnspan=4, padx=(20, 20), pady=(20, 0), sticky="nsew")
        cur_row += 1

        log_path_lb = Label(main_frame, text=str(settings['ed_log_folder']))
        log_path_lb.grid(row=cur_row, column=0, columnspan=4, padx=(20, 20), pady=5, sticky="nsew")

        cur_row += 1
        log_path_but = Button(main_frame, text=language['basic']['log_path_btn'])
        log_path_but.grid(row=cur_row, column=0, columnspan=4, padx=20, pady=(5, 10), sticky="nsew")
        log_path_but.config(command=lambda: choose_log_dir())

        cur_row += 1
        Label(main_frame, text=language['basic']['data_hook_time']).grid(row=cur_row, column=0, columnspan=3, padx=(20, 5), pady=5, sticky="nw")
        data_hook_time = Entry(main_frame, width=4)
        data_hook_time.grid(row=cur_row, column=3, padx=(5, 20), pady=5, sticky="sew")
        data_hook_time.insert(0, float(settings['data_hook_time']))

        cur_row += 1
        Label(main_frame, text=language['basic']['ed_start_time']).grid(row=cur_row, column=0, columnspan=3, padx=(20, 5), pady=(5, 15), sticky="nw")
        ed_start_time = Entry(main_frame, width=4)
        ed_start_time.grid(row=cur_row, column=3, padx=(5, 20), pady=(5, 15), sticky="sew")
        ed_start_time.insert(0, float(settings['ed_start_time']))

        LabelFrame(main_frame, labelanchor="n", text=language['basic']['modules_header']).grid(row=cur_row, rowspan=2, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        extra_sound_var = BooleanVar(value=settings['extra_sound'])

        voice_assist_var = BooleanVar(value=settings['voice_assist'])

        Checkbutton(main_frame, text=language['basic']['extra_sound_mod'], variable=extra_sound_var, onvalue=True, offvalue=False).grid(row=cur_row, column=0, columnspan=4, padx=20, pady=(25, 0), sticky="nsew")
        cur_row += 1
        Checkbutton(main_frame, text=language['basic']['voice_assist_mod'], variable=voice_assist_var, onvalue=True, offvalue=False).grid(row=cur_row, column=0, columnspan=4, padx=20, pady=(0, 10), sticky="nsew")
        cur_row += 1

        cur_row += 1
        but_save = Button(main_frame, text=language['all_txt']['save'])
        but_save.grid(row=cur_row, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        but_save.config(command=lambda: save_settings())
        cur_row += 1

        but_def = Button(main_frame, text=language['all_txt']['default'])
        but_def.grid(row=cur_row, column=0, columnspan=4, padx=5, pady=(5, 10), sticky="nsew")
        but_def.config(command=lambda: default_settings('basic'))

    elif category == 'sound':

        def save_settings():

            settings['sound_levels']['ch_ui'] = round((ch_ui_val.get() / 100), 2)
            settings['sound_levels']['ch_notif'] = round((ch_notif_val.get() / 100), 2)
            settings['sound_levels']['ch_voice'] = round((ch_voice_val.get() / 100), 2)
            settings['sound_levels']['ch_sfx'] = round((ch_sfx_val.get() / 100), 2)
            settings['sound_levels']['ch_assistant'] = round((ch_assistant_val.get() / 100), 2)
            settings['sound_levels']['ch_extra'] = round((ch_extra_val.get() / 100), 2)
            settings['sound_levels']['ch_music'] = round((ch_music_val.get() / 100), 2)

            write_data(miex_path + '/data/profile/', 'settings.txt', settings)
        LabelFrame(main_frame, labelanchor="n", text=language['sound']['ch_ui']).grid(row=cur_row, rowspan=2, column=0, padx=5, pady=5, sticky="nsew")
        LabelFrame(main_frame, labelanchor="n", text=language['sound']['ch_notif']).grid(row=cur_row, rowspan=2, column=1, padx=5, pady=5, sticky="nsew")
        LabelFrame(main_frame, labelanchor="n", text=language['sound']['ch_voice']).grid(row=cur_row, rowspan=2, column=2, padx=5, pady=5, sticky="nsew")
        LabelFrame(main_frame, labelanchor="n", text=language['sound']['ch_sfx']).grid(row=cur_row, rowspan=2, column=3, padx=5, pady=5, sticky="nsew")
        LabelFrame(main_frame, labelanchor="n", text=language['sound']['ch_assistant']).grid(row=cur_row, rowspan=2, column=4, padx=5, pady=5, sticky="nsew")
        LabelFrame(main_frame, labelanchor="n", text=language['sound']['ch_extra']).grid(row=cur_row, rowspan=2, column=5, padx=5, pady=5, sticky="nsew")
        LabelFrame(main_frame, labelanchor="n", text=language['sound']['ch_music']).grid(row=cur_row, rowspan=2, column=6, padx=5, pady=5, sticky="nsew")

        cur_row += 1
        ch_ui_val = Scale(main_frame, from_=100, to=1, length=150)
        ch_ui_val.grid(row=cur_row, column=0, padx=10, pady=20, sticky="nsew")
        ch_ui_val.set(int(settings['sound_levels']['ch_ui']*100))

        ch_notif_val = Scale(main_frame, from_=100, to=1, length=150)
        ch_notif_val.grid(row=cur_row, column=1, padx=10, pady=20, sticky="nsew")
        ch_notif_val.set(int(settings['sound_levels']['ch_notif'] * 100))

        ch_voice_val = Scale(main_frame, from_=100, to=1, length=150)
        ch_voice_val.grid(row=cur_row, column=2, padx=10, pady=20, sticky="nsew")
        ch_voice_val.set(int(settings['sound_levels']['ch_voice'] * 100))

        ch_sfx_val = Scale(main_frame, from_=100, to=1, length=150)
        ch_sfx_val.grid(row=cur_row, column=3, padx=10, pady=20, sticky="nsew")
        ch_sfx_val.set(int(settings['sound_levels']['ch_sfx'] * 100))

        ch_assistant_val = Scale(main_frame, from_=100, to=1, length=150)
        ch_assistant_val.grid(row=cur_row, column=4, padx=10, pady=20, sticky="nsew")
        ch_assistant_val.set(int(settings['sound_levels']['ch_assistant'] * 100))

        ch_extra_val = Scale(main_frame, from_=100, to=1, length=150)
        ch_extra_val.grid(row=cur_row, column=5, padx=10, pady=20, sticky="nsew")
        ch_extra_val.set(int(settings['sound_levels']['ch_extra'] * 100))

        ch_music_val = Scale(main_frame, from_=100, to=1, length=150)
        ch_music_val.grid(row=cur_row, column=6, padx=10, pady=20, sticky="nsew")
        ch_music_val.set(int(settings['sound_levels']['ch_music'] * 100))



        #Label(main_frame, text=language['basic']['log_path']).grid(row=cur_row, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")


        cur_row += 1
        but_save = Button(main_frame, text=language['all_txt']['save'])
        but_save.grid(row=cur_row, column=0, columnspan=7, padx=5, pady=5, sticky="nsew")
        but_save.config(command=lambda: save_settings())
        cur_row += 1

        but_def = Button(main_frame, text=language['all_txt']['default'])
        but_def.grid(row=cur_row, column=0, columnspan=7, padx=5, pady=(5, 10), sticky="nsew")
        but_def.config(command=lambda: default_settings('basic'))

    elif category == 'keypad':

        def save_settings():

            write_data(miex_path + '/data/profile/', 'settings.txt', settings)

        def key_combo(name, wgt_list):

            def save_combo():

                keys = ''
                for k in wgt_list[:-1]:
                    if k.get() != '-':
                        keys = keys + k.get() + '+'
                keys = keys[:-1]
                settings[name] = keys

            combo = settings[name].split('+')

            wgt_list.append(Combobox(main_frame, state="normal", width=6))
            wgt_list[-1]['values'] = ['-', 'ctrl', 'shift', 'alt']
            wgt_list.append(Combobox(main_frame, state="normal", width=6))
            wgt_list[-1]['values'] = list('1234567890qwertyuiopasdfghjklzxcvbnm')

            if len(combo) == 2:
                wgt_list[0].current(wgt_list[0]['values'].index(combo[0]))
                wgt_list[1].current(wgt_list[1]['values'].index(combo[1]))

            else:
                wgt_list[0].current(0)
                wgt_list[1].current(wgt_list[1]['values'].index(combo[0]))

            wgt_list[0].grid(column=0, row=cur_row, sticky='nw', padx=(20, 5))
            wgt_list[1].grid(column=2, row=cur_row, sticky='nw', padx=5)

            Label(main_frame, text="+").grid(row=cur_row, column=1, sticky="nw")

            wgt_list.append(Button(main_frame, text=language['all_txt']['accept'], command=lambda: save_combo()))
            wgt_list[-1].grid(row=cur_row, column=3, padx=(5, 20), sticky="nsew")

        LabelFrame(main_frame, labelanchor="n", text=language['keypad']['base_header']).grid(row=cur_row, rowspan=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        Label(main_frame, text=language['keypad']['action_key']).grid(row=cur_row, column=0, columnspan=4, padx=20, pady=(25, 0), sticky="nsew")
        cur_row += 1

        action_key = []
        key_combo('action_key', action_key)

        cur_row += 1
        Label(main_frame, text=language['keypad']['task_key']).grid(row=cur_row, column=0, columnspan=4, padx=20, pady=(5, 0), sticky="nsew")
        cur_row += 1
        action_key = []
        key_combo('task_key', action_key)
        cur_row += 1
        Label(main_frame, text="").grid(row=cur_row, column=0, columnspan=4, padx=20, pady=(0, 10), sticky="nsew")
        cur_row += 1

        LabelFrame(main_frame, labelanchor="n", text=language['keypad']['test_header']).grid(row=cur_row, rowspan=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        Label(main_frame, text=language['keypad']['message_test_key']).grid(row=cur_row, column=0, columnspan=4, padx=20, pady=(25, 0), sticky="nsew")
        cur_row += 1
        action_key = []
        key_combo('message_test_key', action_key)

        cur_row += 1
        Label(main_frame, text=language['keypad']['minigame_test_key']).grid(row=cur_row, column=0, columnspan=4, padx=20, pady=(5, 0), sticky="nsew")
        cur_row += 1
        action_key = []
        key_combo('minigame_test_key', action_key)

        cur_row += 1
        Label(main_frame, text="").grid(row=cur_row, column=0, columnspan=4, padx=20, pady=(0, 10), sticky="nsew")
        cur_row += 1

        cur_row += 1
        but_save = Button(main_frame, text=language['all_txt']['save'])
        but_save.grid(row=cur_row, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        but_save.config(command=lambda: save_settings())
        cur_row += 1

        but_def = Button(main_frame, text=language['all_txt']['default'])
        but_def.grid(row=cur_row, column=0, columnspan=4, padx=5, pady=(5, 10), sticky="nsew")
        but_def.config(command=lambda: default_settings('keypad'))

    elif category == 'themes':

        def save_settings():
            settings['def_theme'] = theme_var.get()
            write_data(miex_path + '/data/profile/', 'settings.txt', settings)

        def ref_img():
            for w in img_frame.grid_slaves():
                w.grid_forget()
            img = Image.open(miex_path + '/data/icons/LOGOS/adder/original.png').convert('RGBA').split()[-1]
            img = img.resize((120, 120), 1)
            theme_layer = Image.new('RGBA', img.size, settings['icon_col'])
            theme_layer.putalpha(img)

            image = ImageTk.PhotoImage(theme_layer)

            panel = Label(img_frame, image=image)
            panel.image = image
            panel.grid(row=0, column=0)

            main_frame.update()

        def change_color(theme, variable):
            settings[theme][variable] = colorchooser.askcolor(settings[theme][variable])[1]
            label_dict[theme][variable].configure(background=settings[theme][variable])
            main_frame.update()

        def change_img_color():
            img_col = colorchooser.askcolor(settings['icon_col'])
            if img_col is not None:
                settings['icon_col'] = img_col[1]
                img_col_lbl.configure(background=settings['icon_col'])
                ref_img()
                rebuild_img_btn.configure(state='normal', command=lambda e='': rebuild_img())

        def rebuild_img():

            if messagebox.askquestion(language['themes']['messagebox_head_icons'], language['themes']['messagebox_icons'], icon='info') == 'yes':

                for i_cat in ['LOGOS', 'MISC', 'MISSIONS', 'NPC']:
                    print('start cat ' + i_cat)
                    for i_id in dir_list(miex_path + '/data/icons/' + i_cat + '/'):
                        if i_cat in ['LOGOS', 'MISC', 'MISSIONS']:
                            img = Image.open(miex_path + '/data/icons/' + i_cat + '/' + i_id + '/original.png').convert('RGBA', palette=Image.ADAPTIVE, colors=4).split()[-1]
                            img = img.resize((500, 500), 1)

                            theme_layer = Image.new('RGBA', img.size, settings['icon_col'])
                            theme_layer.putalpha(img)

                        else:
                            theme_layer = Image.open(miex_path + '/data/icons/' + i_cat + '/' + i_id + '/original.png').convert('RGB', palette=Image.ADAPTIVE)
                            theme_layer = theme_layer.resize((500, 500), 1)
                        for s in list(reversed(range(30)[5:])):
                            name = s + 1
                            save_img = theme_layer.copy()
                            save_img = save_img.resize((name * 10, name * 10), 1)
                            save_img = save_img.quantize(method=2)
                            save_img.save(miex_path + '/data/icons/' + i_cat + '/' + i_id + '/' + str(name) + '.png', optimize=True)

                messagebox.showinfo(language['themes']['messagebox_head_icons'], language['themes']['messagebox_icons_fin'])

        theme_var = BooleanVar()
        theme_var.set(settings['def_theme'])

        label_dict = {'theme_default': {}, 'theme_custom': {}}

        Label(main_frame, text=language['themes']['theme_choose']).grid(row=cur_row, column=0, columnspan=4, pady=5, sticky="nsew")
        cur_row += 1
        Checkbutton(main_frame, text=language['themes']['theme_custom_choose'], variable=theme_var, onvalue=False, offvalue=True).grid(row=cur_row, column=0, columnspan=4, pady=5, sticky="nsew")
        cur_row += 1

        LabelFrame(main_frame, labelanchor="n", text=language['themes']['theme_default_header']).grid(row=cur_row, rowspan=11, column=0, columnspan=2, padx=5, sticky="nsew")

        LabelFrame(main_frame, labelanchor="n", text=language['themes']['theme_custom_header']).grid(row=cur_row, rowspan=11, column=2, columnspan=2, padx=5, sticky="nsew")

        Label(main_frame, text="").grid(row=cur_row, column=0, columnspan=2, padx=20, pady=(15, 0), sticky="nsew")
        Label(main_frame, text="").grid(row=cur_row, column=2, columnspan=2, padx=20, pady=(15, 0), sticky="nsew")
        cur_row += 1

        for l_k in settings['theme_default'].keys():
            label_text = language['themes']['theme_label_text']

            label_dict['theme_default'][l_k] = Label(main_frame, background=settings['theme_default'][l_k], anchor='center', justify='center', width=6)
            label_dict['theme_default'][l_k].grid(row=cur_row, column=0, sticky='nsew', padx=(15, 5), pady=2)

            label_dict['theme_custom'][l_k] = Label(main_frame, background=settings['theme_custom'][l_k], anchor='center', justify='center', width=6)
            label_dict['theme_custom'][l_k].grid(row=cur_row, column=2, sticky='nsew', padx=(15, 5), pady=2)

            Button(main_frame, text=label_text[l_k], anchor='center', justify='center', command=lambda t='theme_default', v=l_k: change_color(t, v)).grid(row=cur_row, column=1, sticky='nsew', padx=(5, 15), pady=2)

            Button(main_frame, text=label_text[l_k], anchor='center', justify='center', command=lambda t='theme_custom', v=l_k: change_color(t, v)).grid(row=cur_row, column=3, sticky='nsew', padx=(5, 15), pady=2)

            cur_row += 1

        Label(main_frame, text="").grid(row=cur_row, column=0, columnspan=2, padx=20, pady=(5, 2), sticky="nsew")
        Label(main_frame, text="").grid(row=cur_row, column=2, columnspan=2, padx=20, pady=(5, 2), sticky="nsew")

        cur_row += 1

        LabelFrame(main_frame, labelanchor="n", text=language['themes']['icons_col']).grid(row=cur_row, rowspan=3, column=0, columnspan=4, padx=5, sticky="nsew")

        img_frame = Frame(main_frame, width="120", height="120")
        img_frame.grid(row=cur_row, rowspan=3, columnspan=2, column=0, pady=(20, 20))
        ref_img()

        img_col_lbl = Label(main_frame, text="", background=settings['icon_col'], anchor='center', justify='center', width=8)
        img_col_lbl.grid(row=cur_row, column=2, columnspan=2, sticky='nsew', padx=(0, 20), pady=(20, 5))

        cur_row += 1

        Button(main_frame, text=language['themes']['icons_choose_col'], command=lambda e='': change_img_color()).grid(row=cur_row, column=2, columnspan=2, sticky='nsew', padx=(0, 20))
        cur_row += 1

        rebuild_img_btn = Button(main_frame, text=language['themes']['rebuild_img_btn'], state='disabled')
        rebuild_img_btn.grid(row=cur_row, column=2, columnspan=2, sticky='nsew', padx=(0, 20), pady=(0, 20))

        cur_row += 1

        but_save = Button(main_frame, text=language['all_txt']['save'])
        but_save.grid(row=cur_row, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        but_save.config(command=lambda: save_settings())
        cur_row += 1

        but_def = Button(main_frame, text=language['all_txt']['default'])
        but_def.grid(row=cur_row, column=0, columnspan=4, padx=5, pady=(5, 10), sticky="nsew")
        but_def.config(command=lambda: default_settings('themes'))

    elif category == 'profile':

        def get_fr_journal():
            global last_journal
            log_path = ''
            if settings['ed_log_folder'] is None:
                log_path = askdirectory().replace('\\', '/')
                settings['ed_log_folder'] = log_path

            log_path = settings['ed_log_folder']
            file_list = []
            for x in Path(log_path).iterdir():
                if x.is_file():
                    if x.stem[0:8] == "Journal." and x.stem[-3] == ".":
                        file_list.append(x)

            settings['log_files_len'] = len(file_list)
            fp = open(str(file_list[-1]), mode='r', buffering=-1, encoding='utf-8', errors=None, newline=None, closefd=True, opener=None)

            last_journal = fp.readlines()
            fp.close()
            for line in enumerate(last_journal):
                last_journal[line[0]] = json.loads(line[1])

                if last_journal[line[0]]['event'] == 'Commander':
                    profile['Commander'] = last_journal[line[0]]['Name']
                    profile['FID'] = last_journal[line[0]]['FID']

                elif last_journal[line[0]]['event'] == 'Loadout':
                    cur_loadout = {}
                    cur_loadout['Ship_type'] = [last_journal[line[0]]['Ship']]
                    cur_loadout['Ship_ident'] = [last_journal[line[0]]['ShipIdent']]
                    cur_loadout['Ship_name'] = [last_journal[line[0]]['ShipName']]

                    for m in last_journal[line[0]]['Modules']:
                        if m['Slot'] not in ['PaintJob', 'Decal1', 'Decal2', 'Decal3', 'Decal4', 'Decal5', 'Decal6', 'WeaponColour', 'VesselVoice']:
                            cur_loadout[m['Slot']] = [m['Item'], m['Health'], m['Priority'], m['On']]
                            if 'Engineering' in m.keys():
                                cur_loadout[m['Slot']][0] = m['Item'] + "##" + m['Engineering']['BlueprintName'] + '_' + str(m['Engineering']['Level'])

                    profile['Ship'] = cur_loadout

                elif last_journal[line[0]]['event'] == 'Location':
                    profile['Docked'] = last_journal[line[0]]['Docked']
                    profile['Dock_data']['StationName'] = last_journal[line[0]]['StationName']
                    profile['Dock_data']['StationType'] = last_journal[line[0]]['StationType']
                    profile['Dock_data']['StationGovernment'] = last_journal[line[0]]['StationGovernment']
                    profile['Dock_data']['StationAllegiance'] = last_journal[line[0]]['StationAllegiance']
                    profile['Dock_data']['StationEconomy'] = last_journal[line[0]]['StationEconomy']

                    profile['System_data']['StarSystem'] = last_journal[line[0]]['StarSystem']
                    profile['System_data']['SystemSecurity'] = last_journal[line[0]]['SystemSecurity']
                    profile['System_data']['SystemGovernment'] = last_journal[line[0]]['SystemGovernment']
                    profile['System_data']['SystemAllegiance'] = last_journal[line[0]]['SystemAllegiance']
                    profile['System_data']['SystemEconomy'] = last_journal[line[0]]['SystemEconomy']

                elif last_journal[line[0]]['event'] == 'Materials':
                    materials_list = last_journal[line[0]]['Raw']
                    materials_list.extend(last_journal[line[0]]['Manufactured'])
                    materials_list.extend(last_journal[line[0]]['Encoded'])
                    for mat in materials_list:
                        profile['Ship_materials'][mat['Name']] = mat['Count']

                elif last_journal[line[0]]['event'] == 'Statistics':
                    profile['Credit_line'] = last_journal[line[0]]['Bank_Account']['Current_Wealth']
                    profile['Deposite_line'] = last_journal[line[0]]['Bank_Account']['Current_Wealth'] \
                                               + last_journal[line[0]]['Bank_Account']['Spent_On_Ships'] \
                                               + last_journal[line[0]]['Bank_Account']['Spent_On_Outfitting']

                    profile['Pays'] = last_journal[line[0]]['Bank_Account']['Spent_On_Repairs'] \
                                      + last_journal[line[0]]['Bank_Account']['Spent_On_Fuel'] \
                                      + last_journal[line[0]]['Bank_Account']['Spent_On_Ammo_Consumables'] \
                                      + last_journal[line[0]]['Bank_Account']['Spent_On_Insurance'] \
                                      + last_journal[line[0]]['Crime']['Total_Fines']

            cmdr_name.configure(text='Имя: ' + profile['Commander'])
            cmdr_id.configure(text='FID: ' + profile['FID'])
            depos.configure(text='Депозиты: ' + str(profile['Deposite_line']))
            credit.configure(text='Кредитная линия: ' + str(profile['Credit_line']))
            ship.configure(text='Корабль: ' + profile['Ship']['Ship_type'][0])
            ship_id.configure(text='ID корабля: ' + profile['Ship']['Ship_ident'][0])
            ship_name.configure(text='Имя корабля: ' + profile['Ship']['Ship_name'][0])
            main_frame.update()

        def ref_img():
            for w in img_frame.grid_slaves():
                w.grid_forget()
            img = Image.open(miex_path + '/data/icons/NPC/actor/original.png')
            img = img.resize((120, 120), 1)
            image = ImageTk.PhotoImage(img)

            panel = Label(img_frame, image=image)
            panel.image = image
            panel.grid(row=0, column=0)

            main_frame.update()

        def choose_new_avatar():
            new_img_file = askopenfilename(initialdir="/", title="Выберите изображение", filetypes=(("JPEG", "*.jpg"), ("PNG", "*.png"), ("GIF", "*.gif"), ("all files", "*.*")))
            if len(new_img_file) > 0:
                im = Image.open(new_img_file)
                im = im.resize((512, 512), 1)
                im.save(miex_path + '/data/icons/NPC/actor/original.png')
                for s in list(reversed(range(30)[5:])):
                    name = s + 1
                    im = im.resize((name * 10, name * 10), 1)
                    im.save(miex_path + '/data/icons/NPC/actor/' + str(name) + '.png', palette=Image.ADAPTIVE)
                ref_img()

        def save_profile():
            write_data(miex_path + '/data/profile/', 'settings.txt', settings)
            write_data(miex_path + '/data/profile/', 'profile.txt', profile)

        def restore_profile():
            profile = read_file(miex_path + '/data/profile/', 'profile_d.txt')
            write_data(miex_path + '/data/profile/', 'profile.txt', profile)

            cmdr_name.configure(text=language['profile']['commander'] + profile['Commander'])
            cmdr_id.configure(text=language['profile']['fid'] + profile['FID'])
            depos.configure(text=language['profile']['deposite_line'] + str(profile['Deposite_line']))
            credit.configure(text=language['profile']['credit_line'] + str(profile['Credit_line']))
            ship.configure(text=language['profile']['ship_type'] + profile['Ship']['Ship_type'][0])
            ship_id.configure(text=language['profile']['ship_ident'] + profile['Ship']['Ship_ident'][0])
            ship_name.configure(text=language['profile']['ship_name'] + profile['Ship']['Ship_name'][0])
            main_frame.update()

        profile = read_file(miex_path + '/data/profile/', 'profile.txt')

        img_frame = Frame(main_frame, width="120", height="120")
        img_frame.grid(row=cur_row, rowspan=5, columnspan=2, column=0, pady=5, padx=(5, 10))
        ref_img()

        cmdr_name = Label(main_frame, text=language['profile']['commander'] + profile['Commander'])
        cmdr_name.grid(row=cur_row, column=2, padx=(0, 10), sticky="nw")

        cur_row += 1

        cmdr_id = Label(main_frame, text=language['profile']['fid'] + profile['FID'])
        cmdr_id.grid(row=cur_row, column=2, padx=(0, 10), sticky="nw")

        cur_row += 1

        depos = Label(main_frame, text=language['profile']['deposite_line'] + str(profile['Deposite_line']))
        depos.grid(row=cur_row, column=2, padx=(0, 10), sticky="nw")

        cur_row += 1

        credit = Label(main_frame, text=language['profile']['credit_line'] + str(profile['Credit_line']))
        credit.grid(row=cur_row, column=2, padx=(0, 10), sticky="nw")

        cur_row += 1

        ship = Label(main_frame, text=language['profile']['ship_type'] + profile['Ship']['Ship_type'][0])
        ship.grid(row=cur_row, column=2, padx=(0, 10), sticky="nw")


        cur_row += 1

        ship_id = Label(main_frame, text=language['profile']['ship_ident'] + profile['Ship']['Ship_ident'][0])
        ship_id.grid(row=cur_row, column=2, padx=(0, 10), sticky="nw")


        Button(main_frame, text=language['profile']['choose_new_avatar'], command=lambda e='': choose_new_avatar()).grid(row=cur_row, column=0, columnspan=2, sticky='nsew', pady=(0, 5), padx=10)

        cur_row += 1

        Button(main_frame, text=language['profile']['get_fr_journal'], command=lambda e='': get_fr_journal()).grid(row=cur_row, column=0, columnspan=2, sticky='nsew', pady=(0, 5), padx=10)

        ship_name = Label(main_frame, text=language['profile']['ship_name'] + profile['Ship']['Ship_name'][0])
        ship_name.grid(row=cur_row, column=2, padx=(0, 10), sticky="nw")

        cur_row += 1

        Button(main_frame, text=language['profile']['save_profile'], command=lambda e='': save_profile()).grid(row=cur_row, column=0, columnspan=4, sticky='nsew', pady=(0, 5), padx=10)

        cur_row += 1
        Button(main_frame, text=language['profile']['restore_profile'], command=lambda e='': restore_profile()).grid(row=cur_row, column=0, columnspan=4, sticky='nsew', pady=(0, 15), padx=10)

    elif category == 'gui':

        def kill_top():
            win.destroy()
            root.update()

        def ch_olay_style(data):
            if col_names_sm[0][0:3] == data[0:3]:
                for n in olay_text_names_sm.keys():
                    if data == olay_text_names_sm[n][0]:
                        return n
            else:
                for n in olay_text_names_reg.keys():
                    if data == olay_text_names_reg[n][0]:
                        return n

        def save_settings():

            settings['gui_data']['task_frame_bor'] = task_frame_bor
            settings['gui_data']['cent_frame_bor'] = cent_frame_bor
            settings['gui_data']['bottom_frame_bor'] = bottom_frame_bor
            settings['gui_data']['left_frame_bor'] = left_frame_bor
            settings['gui_data']['right_frame_bor'] = right_frame_bor

            settings['gui_data']['state_style'] = ch_olay_style(state_style.get())
            settings['gui_data']['task_text'] = ch_olay_style(task_text.get())
            settings['gui_data']['task_extra'] = ch_olay_style(task_extra.get())
            settings['gui_data']['olay_text'] = ch_olay_style(olay_text.get())
            settings['gui_data']['olay_text_lt'] = ch_olay_style(olay_text_lt.get())
            settings['gui_data']['olay_text_sm'] = ch_olay_style(olay_text_sm.get())
            settings['gui_data']['olay_text_sm_lt'] = ch_olay_style(olay_text_sm_lt.get())

            write_data(miex_path + '/data/profile/', 'settings.txt', settings)




        def ch_frame_pos(var, dir):

            def act(var_list):
                if dir is True:
                    if var_list[0] > 0:
                        var_list[0] -=1
                        var_list[1] += 1
                else:
                    if var_list[1] > 0:
                        var_list[0] += 1
                        var_list[1] -= 1
                return var_list

            var = act(var)

            ch_win()

        def ch_win():
            for w in win.grid_slaves():
                w.grid_forget()

            task_frame = LabelFrame(win, labelanchor="n", text=language['gui']['header_task_frame'], height=bor * 14, width=(resolution[0] - (bor * 10)))
            task_frame.grid(row=1, column=1, columnspan=3, padx=bor * 5, pady=((tx_bor * task_frame_bor[0]), (tx_bor * task_frame_bor[1])), sticky="nsew")
            task_frame.grid_propagate(False)

            left_frame = LabelFrame(win, labelanchor="n", text=language['gui']['header_left_frame'], height=bor * 9, width=bor * 30)
            left_frame.grid(row=3, column=1, padx=bor, sticky="sw", pady=((tx_bor * left_frame_bor[0]), (tx_bor * left_frame_bor[1])))
            left_frame.grid_propagate(False)

            right_frame = LabelFrame(win, labelanchor="n", text=language['gui']['header_right_frame'], height=bor * 20, width=bor * 30)
            right_frame.grid(row=3, column=3, padx=bor, sticky="nsew", pady=((tx_bor * right_frame_bor[0]), (tx_bor * right_frame_bor[1])))
            right_frame.grid_propagate(False)

            bottom_frame = LabelFrame(win, labelanchor="n", text=language['gui']['header_bottom_frame'], height=bor * 6, width=bor * 93)
            bottom_frame.grid(row=3, column=2, padx=bor, sticky="sew", pady=((tx_bor * bottom_frame_bor[0]), (tx_bor * bottom_frame_bor[1])))
            bottom_frame.grid_propagate(False)

            cent_frame = LabelFrame(win, labelanchor="n", text=language['gui']['header_cent_frame'], height=bor * 36, width=bor * 20)
            cent_frame.grid(row=2, column=1, columnspan=3, sticky="nsew", pady=((tx_bor * cent_frame_bor[0]), (tx_bor * cent_frame_bor[1])))
            cent_frame.grid_propagate(False)
            root.update()
        if full_win is False:
            win = Toplevel(master=root, height=settings['resolution'][1], width=settings['resolution'][0])
            win.title('gui themer')

            win.resizable(False, False)
            win.overrideredirect(True)
            win.geometry('+0+0')

            full_win = True


        col_names_reg = language['gui']['col_names_reg']
        col_names_sm = language['gui']['col_names_sm']

        if settings['def_theme'] is True:
            olay_text_names_reg = {
                'Custom_olay.TLabel': (col_names_reg[0], settings['theme_default']['fg_col']),
                'Custom_d_olay.TLabel': (col_names_reg[1], settings['theme_default']['fg_col_d']),
                'Custom_2_olay.TLabel': (col_names_reg[2], settings['theme_default']['fg_col2']),
                'Custom_c_olay.TLabel': (col_names_reg[3], settings['theme_default']['fg_col_cont']),
                'Custom_lt_olay.TLabel': (col_names_reg[4], settings['theme_default']['fg_col']),
                'Custom_lt_d_olay.TLabel': (col_names_reg[5], settings['theme_default']['fg_col_d']),
                'Custom_lt_2_olay.TLabel': (col_names_reg[6], settings['theme_default']['fg_col2']),
                'Custom_lt_c_olay.TLabel': (col_names_reg[7], settings['theme_default']['fg_col_d'])}

            olay_text_names_sm = {
                'Custom_sm_olay.TLabel': (col_names_sm[0], settings['theme_default']['fg_col']),
                'Custom_sm_d_olay.TLabel': (col_names_sm[1], settings['theme_default']['fg_col_d']),
                'Custom_sm_2_olay.TLabel': (col_names_sm[2], settings['theme_default']['fg_col2']),
                'Custom_sm_c_olay.TLabel': (col_names_sm[3], settings['theme_default']['fg_col_cont']),
                'Custom_sm_lt_olay.TLabel': (col_names_sm[4], settings['theme_default']['fg_col']),
                'Custom_sm_lt_d_olay.TLabel': (col_names_sm[5], settings['theme_default']['fg_col_d']),
                'Custom_sm_lt_2_olay.TLabel': (col_names_sm[6], settings['theme_default']['fg_col2']),
                'Custom_sm_lt_c_olay.TLabel': (col_names_sm[7], settings['theme_default']['fg_col_d'])}

        else:
                olay_text_names_reg = {
                'Custom_olay.TLabel': (col_names_reg[0], settings['theme_custom']['fg_col']),
                'Custom_d_olay.TLabel': (col_names_reg[1], settings['theme_custom']['fg_col_d']),
                'Custom_2_olay.TLabel': (col_names_reg[2], settings['theme_custom']['fg_col2']),
                'Custom_c_olay.TLabel': (col_names_reg[3], settings['theme_custom']['fg_col_cont']),
                'Custom_lt_olay.TLabel': (col_names_reg[4], settings['theme_custom']['fg_col']),
                'Custom_lt_d_olay.TLabel': (col_names_reg[5], settings['theme_custom']['fg_col_d']),
                'Custom_lt_2_olay.TLabel': (col_names_reg[6], settings['theme_custom']['fg_col2']),
                'Custom_lt_c_olay.TLabel': (col_names_reg[7], settings['theme_custom']['fg_col_d'])}

                olay_text_names_sm = {
                'Custom_sm_olay.TLabel': (col_names_sm[0], settings['theme_custom']['fg_col']),
                'Custom_sm_d_olay.TLabel': (col_names_sm[1], settings['theme_custom']['fg_col_d']),
                'Custom_sm_2_olay.TLabel': (col_names_sm[2], settings['theme_custom']['fg_col2']),
                'Custom_sm_c_olay.TLabel': (col_names_sm[3], settings['theme_custom']['fg_col_cont']),
                'Custom_sm_lt_olay.TLabel': (col_names_sm[4], settings['theme_custom']['fg_col']),
                'Custom_sm_lt_d_olay.TLabel': (col_names_sm[5], settings['theme_custom']['fg_col_d']),
                'Custom_sm_lt_2_olay.TLabel': (col_names_sm[6], settings['theme_custom']['fg_col2']),
                'Custom_sm_lt_c_olay.TLabel': (col_names_sm[7], settings['theme_custom']['fg_col_d'])}


        resolution = [int(settings['resolution'][0]), int(settings['resolution'][1])]

        bor = ((resolution[0] // 12) * 8) // 100
        tx_bor = bor // 2

        task_frame_bor = settings['gui_data']['task_frame_bor']

        cent_frame_bor = settings['gui_data']['cent_frame_bor']

        bottom_frame_bor = settings['gui_data']['bottom_frame_bor']

        left_frame_bor = settings['gui_data']['left_frame_bor']

        right_frame_bor = settings['gui_data']['right_frame_bor']

        ch_win()

        LabelFrame(main_frame, labelanchor="n", text=language['gui']['olay_pos_head']).grid(row=cur_row, rowspan=4, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")
        cur_row += 1
        Label(main_frame, text=language['gui']['label_task_frame']).grid(row=cur_row, column=0, padx=(10, 5), pady=(20, 2), sticky="nsew")
        Label(main_frame, text=language['gui']['label_cent_frame']).grid(row=cur_row, column=1, padx=5, pady=(20, 2), sticky="nsew")
        Label(main_frame, text=language['gui']['label_left_frame']).grid(row=cur_row, column=2, padx=5, pady=(20, 2), sticky="nsew")
        Label(main_frame, text=language['gui']['label_right_frame']).grid(row=cur_row, column=3, padx=5, pady=(20, 2), sticky="nsew")
        Label(main_frame, text=language['gui']['label_bottom_frame']).grid(row=cur_row, column=4, padx=(5, 10), pady=(20, 2), sticky="nsew")
        cur_row += 1

        Button(main_frame, text=language['gui']['upper_act'], anchor='center', justify='center', command=lambda var=task_frame_bor, dir=True: ch_frame_pos(var, dir)).grid(row=cur_row, column=0, sticky='nsew', padx=(10, 5), pady=2)
        Button(main_frame, text=language['gui']['upper_act'], anchor='center', justify='center', command=lambda var=cent_frame_bor, dir=True: ch_frame_pos(var, dir)).grid(row=cur_row, column=1, sticky='nsew', padx=5, pady=2)
        Button(main_frame, text=language['gui']['upper_act'], anchor='center', justify='center', command=lambda var=left_frame_bor, dir=True: ch_frame_pos(var, dir)).grid(row=cur_row, column=2, sticky='nsew', padx=5, pady=2)
        Button(main_frame, text=language['gui']['upper_act'], anchor='center', justify='center', command=lambda var=right_frame_bor, dir=True: ch_frame_pos(var, dir)).grid(row=cur_row, column=3, sticky='nsew', padx=5, pady=2)
        Button(main_frame, text=language['gui']['upper_act'], anchor='center', justify='center', command=lambda var=bottom_frame_bor, dir=True: ch_frame_pos(var, dir)).grid(row=cur_row, column=4, sticky='nsew', padx=(5, 10), pady=2)

        cur_row += 1

        Button(main_frame, text=language['gui']['lower_act'], anchor='center', justify='center', command=lambda var=task_frame_bor, dir=False: ch_frame_pos(var, dir)).grid(row=cur_row, column=0, sticky='nsew', padx=(10, 5), pady=(2, 15))
        Button(main_frame, text=language['gui']['lower_act'], anchor='center', justify='center', command=lambda var=cent_frame_bor, dir=False: ch_frame_pos(var, dir)).grid(row=cur_row, column=1, sticky='nsew', padx=5, pady=(2, 15))
        Button(main_frame, text=language['gui']['lower_act'], anchor='center', justify='center', command=lambda var=left_frame_bor, dir=False: ch_frame_pos(var, dir)).grid(row=cur_row, column=2, sticky='nsew', padx=5, pady=(2, 15))
        Button(main_frame, text=language['gui']['lower_act'], anchor='center', justify='center', command=lambda var=right_frame_bor, dir=False: ch_frame_pos(var, dir)).grid(row=cur_row, column=3, sticky='nsew', padx=5, pady=(2, 15))
        Button(main_frame, text=language['gui']['lower_act'], anchor='center', justify='center', command=lambda var=bottom_frame_bor, dir=False: ch_frame_pos(var, dir)).grid(row=cur_row, column=4, sticky='nsew', padx=(5, 10), pady=(2, 15))

        cur_row += 1

        LabelFrame(main_frame, labelanchor="n", text=language['gui']['olay_col_header']).grid(row=cur_row, rowspan=6, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

        cur_row += 1

        Label(main_frame, text=col_names_reg[0], background=olay_text_names_reg['Custom_olay.TLabel'][1]).grid(row=cur_row, column=0, padx=(10, 5), pady=(25, 5), sticky="nsew")
        Label(main_frame, text=col_names_reg[1], background=olay_text_names_reg['Custom_d_olay.TLabel'][1]).grid(row=cur_row, column=1, padx=5, pady=(25, 5), sticky="nsew")
        Label(main_frame, text=col_names_reg[2], background=olay_text_names_reg['Custom_2_olay.TLabel'][1]).grid(row=cur_row, column=2, padx=5, pady=(25, 5), sticky="nsew")
        Label(main_frame, text=col_names_reg[3], background=olay_text_names_reg['Custom_c_olay.TLabel'][1]).grid(row=cur_row, column=3, padx=5, pady=(25, 5), sticky="nsew")

        cur_row += 1

        Label(main_frame, text=language['gui']['olay_col_task_text']).grid(row=cur_row, column=0, padx=(10, 5), pady=(5, 2), sticky="nsew")
        Label(main_frame, text=language['gui']['olay_col_task_extra']).grid(row=cur_row, column=1, padx=5, pady=(5, 2), sticky="nsew")
        Label(main_frame, text=language['gui']['olay_col_state_style']).grid(row=cur_row, column=2, padx=5, pady=(5, 2), sticky="nsew")
        Label(main_frame, text=language['gui']['olay_col_olay_text']).grid(row=cur_row, column=3, padx=5, pady=(5, 2), sticky="nsew")
        Label(main_frame, text=language['gui']['olay_col_text_lt']).grid(row=cur_row, column=4, padx=(5, 10), pady=(5, 2), sticky="nsew")
        cur_row += 1
        task_text = Combobox(main_frame, width=12)
        task_text['values'] = col_names_reg
        task_text.set(olay_text_names_reg[settings['gui_data']['task_text']][0])
        task_text.grid(column=0, sticky='nw', row=cur_row, padx=(10, 5))

        task_extra = Combobox(main_frame, width=12)
        task_extra['values'] = col_names_sm
        task_extra.set(olay_text_names_sm[settings['gui_data']['task_extra']][0])
        task_extra.grid(column=1, sticky='nw', row=cur_row, padx=5)

        state_style = Combobox(main_frame, width=12)
        state_style['values'] = col_names_sm
        state_style.set(olay_text_names_sm[settings['gui_data']['state_style']][0])
        state_style.grid(column=2, sticky='nw', row=cur_row, padx=5)

        olay_text = Combobox(main_frame, width=12)
        olay_text['values'] = col_names_reg
        olay_text.set(olay_text_names_reg[settings['gui_data']['olay_text']][0])
        olay_text.grid(column=3, sticky='nw', row=cur_row, padx=5)

        olay_text_lt = Combobox(main_frame, width=12)
        olay_text_lt['values'] = col_names_reg
        olay_text_lt.set(olay_text_names_reg[settings['gui_data']['olay_text_lt']][0])
        olay_text_lt.grid(column=4, sticky='nw', row=cur_row, padx=5)

        cur_row += 1
        Label(main_frame, text=language['gui']['olay_col_text_sm']).grid(row=cur_row, column=0, padx=(10, 5), pady=(2, 0), sticky="nsew")
        Label(main_frame, text=language['gui']['olay_col_text_sm_lt']).grid(row=cur_row, column=1, padx=5, pady=(2, 0), sticky="nsew")

        cur_row += 1

        olay_text_sm = Combobox(main_frame, width=12)
        olay_text_sm['values'] = col_names_sm
        olay_text_sm.set(olay_text_names_sm[settings['gui_data']['olay_text_sm']][0])
        olay_text_sm.grid(column=0, sticky='nw', row=cur_row, padx=(10, 5), pady=(0, 25))

        olay_text_sm_lt = Combobox(main_frame, width=12)
        olay_text_sm_lt['values'] = col_names_sm
        olay_text_sm_lt.set(olay_text_names_sm[settings['gui_data']['olay_text_sm_lt']][0])
        olay_text_sm_lt.grid(column=1, sticky='nw', row=cur_row, padx=5, pady=(0, 25))

        cur_row += 1
        but_save = Button(main_frame, text=language['all_txt']['save'])
        but_save.grid(row=cur_row, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")
        but_save.config(command=lambda: save_settings())
        cur_row += 1

        but_def = Button(main_frame, text=language['all_txt']['default'])
        but_def.grid(row=cur_row, column=0, columnspan=5, padx=5, pady=(5, 10), sticky="nsew")
        but_def.config(command=lambda: default_settings('gui'))


root = Tk()
root.title("MIEX Settings 0.0.5 Alpha")

mainmenu = Menu(root)
root.config(menu=mainmenu)
root.wm_attributes('-topmost', True)
root.geometry("+600+200")
root.resizable(False, False)
root.lift()
root.bind("<Escape>", lambda e: root.destroy())

miex_path = str(Path(__file__).absolute()).split('\\')
miex_path = '/'.join(miex_path[0:-3])


main_frame = Frame(root, width="300", height="600")
main_frame.grid(row=0, rowspan=10, column=0, columnspan=20)
settings = read_file(miex_path+'/data/profile/', 'settings.txt')


language = read_file(miex_path + '/data/lang/', settings['language'] + '.txt')
language = language['settings']

mainmenu.add_command(label=language['mainmenu'][0], command=lambda: cr_new_win('basic'))
mainmenu.add_command(label=language['mainmenu'][1], command=lambda: cr_new_win('keypad'))
mainmenu.add_command(label=language['mainmenu'][2], command=lambda: cr_new_win('sound'))
mainmenu.add_command(label=language['mainmenu'][3], command=lambda: cr_new_win('gui'))
mainmenu.add_command(label=language['mainmenu'][4], command=lambda: cr_new_win('themes'))
mainmenu.add_command(label=language['mainmenu'][5], command=lambda: cr_new_win('profile'))


last_journal = []

full_win = False

cr_new_win('basic')

root.mainloop()
