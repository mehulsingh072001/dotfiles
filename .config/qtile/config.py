# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401
from libqtile import qtile
from libqtile import extension

mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                             # My terminal of choice
myBrowser = "firefox"
myConfig = "/home/lucifer/.config/qtile/config.py"    # The Qtile config file location

keys = [
         ### The essentials
         
         Key([mod], "p",
             lazy.spawn("gnome-screenshot"),
             desc='Launches My Terminal'
             ),
         Key(["mod1"], "m",
             lazy.spawn("mongodb-compass"),
             desc='Launches My Terminal'
             ),
         Key(["mod1"], "p",
             lazy.spawn("postman"),
             desc='Launches My Terminal'
             ),
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod], "space",
             lazy.spawn("dmenu_run -p 'Run: ' -fn 'Ubuntu Mono-12'"),
             desc='Dmenu Run Launcher'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod], "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "mod1"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),

         ### Window controls
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
            lazy.screen.prev_group(),
            desc='move to left group'),

         Key([mod], "l",
            lazy.screen.next_group(),
            desc='move to right group'),

         Key([mod, "control"], "h",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod, "control"], "l",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod, "shift"], "m",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'

             ),
         ### Stack controls
         Key([mod, "shift"], "space",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
         Key([mod], "F8",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),

         Key([mod, "control"], "Return",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),

         ### Dmenu script launcher
          Key([mod, "mod1"], 'p',
              lazy.spawn('./.dmenu/dmenu-pdf.sh'),
              desc='Dmenu pdf launcer'
            ),
          Key([mod, "mod1"], 'e',
              lazy.spawn('./.dmenu/dmenu-edit-configs.sh'),
              desc='Dmenu pdf launcer'
            ),
          Key([mod, "mod1"], 'd',
              lazy.spawn('./.dmenu/dmenu-doc.sh'),
              desc='Dmenu pdf launcer'
            ),


         ### My application launcher 
         Key([mod], "F5",
             lazy.spawn("oblogout"),
             desc='Logout'
            ),
         Key(["mod1"], "i",
             lazy.spawn("inkscape"),
             desc='launch inkscape',
            ),
         Key([mod], "g",
             lazy.spawn("gimp"),
             desc='launch gimp',
            ),
         Key(["mod1"], "k",
             lazy.spawn("kdenlive"),
             desc='launch kdenlive',
            ),
         Key([mod], "i",
             lazy.spawn("brightnessctl s 5%+"),
             desc='Brightness'
            ),
         Key([mod], "d",
             lazy.spawn("brightnessctl s 5%-"),
             desc='Brightness'
            ),
         Key([mod], "c",
             lazy.spawn("code"),
             desc='Brightness'
            ),
         Key(["mod1"], "t",
             lazy.spawn(myBrowser + " --new-tab 'https://twitter.com/home'"),
             desc='lynx browser'
             ),
         Key(["mod1"], "f",
             lazy.spawn(myBrowser + " --new-tab 'www.google.com'"),
             desc='lynx browser'
             ),
         Key(["mod1"], "d",
             lazy.spawn(myBrowser + " --new-tab 'https://drive.google.com/drive/my-drive'"),
             desc='lynx browser'
             ),
         Key(["mod1"], "g",
             lazy.spawn(myBrowser + " --new-tab 'https://github.com/mehulsingh072001'"),
             desc='firefox browser github'
             ),
         Key(["mod1"], "y",
             lazy.spawn(myBrowser + " --new-tab 'https://www.youtube.com/'"),
             desc='firefox browser youtube'
             ),
         Key(["mod1"], "b",
             lazy.spawn(myBrowser),
             desc='firefox browser'
             ),
         Key([mod, "shift"], "f",
             lazy.spawn("nautilus"),
             desc='tig'
             ),
         Key(["mod1", "shift"], "f",
             lazy.spawn("urxvt -e ranger"),
             desc='vifm'
             ),
         Key([mod], "F4",
             lazy.spawn(myTerm+" -e ncmpcpp"),
             desc='ncpamixer'
             ),
         Key([mod], "F1",
             lazy.spawn("redshift-gtk"),
             desc='redshift'
            ),
         Key([mod], "F2",
             lazy.spawn("barrier"),
             desc='barrier'
            ),
         Key([mod], "F3",
             lazy.spawn("optimus-manager --no-confirm --switch nvidia"),
             desc='barrier'
            ),
]

group_names = [(" CODE ", {'layout': 'monadtall'}),
               (" WWW ", {'layout': 'monadtall'}),
               (" API ", {'layout': 'monadtall'}),
               (" SERVER ", {'layout': 'monadtall'}),
               (" DB ", {'layout': 'monadtall'}),
               (" CHAT ", {'layout': 'monadtall'}),
               (" PKG ", {'layout': 'monadtall'}),
               (" MUS ", {'layout': 'monadtall'}),
               (" REC ", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 1,
                "margin": 8,
                "border_focus": "adadff",
                "border_normal": "505050"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND"],
         section_fontsize = 11,
         bg_color = "141414",
         active_bg = "90C435",
         active_fg = "000000",
         inactive_bg = "384323",
         inactive_fg = "a0a0a0",
         padding_y = 5,
         section_top = 10,
         panel_width = 320
         ),
    layout.Floating(**layout_theme)
]

colors = [["#000000", "#000000"], # panel background
          ["#3475d1", "#3475d1"], # background for current screen tab
          ["#fefefe", "#fefefe"], # font color for group names
          ["#fefefe", "#fefefe"], # border line color for current tab
          ["#1d1d1d", "#1d1d1d"], # border line color for other tab and odd widgets
          ["#3475d1", "#3475d1"], # color for the even widgets
          ["#fefefe", "#fefefe"],
          ["#268bd2", "#268bd2"],
          ["#505050", "#505050"]] # window name

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    fontsize = 14,
    padding = 0,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()
def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 11,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[3],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[0],
                       other_screen_border = colors[0],
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Prompt(
                       prompt = prompt,
                       font = "Ubuntu Mono",
                       padding = 10,
                       foreground = colors[3],
                       background = colors[1]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 40,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " 🌡",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[5],
                       fontsize = 11
                       ),
              widget.ThermalSensor(
                       foreground = colors[2],
                       background = colors[5],
                       threshold = 90,
                       padding = 5
                       ),
              widget.TextBox(
                       text='',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " 🖬",
                       foreground = colors[2],
                       background = colors[4],
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Memory(
                       foreground = colors[2],
                       background = colors[4],
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e htop')},
                       padding = 5
                       ),
              widget.TextBox(
                       text='',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Net(
                       interface = "wlp2s0",
                       format = '{down} ↓↑ {up}',
                       foreground = colors[2],
                       background = colors[5],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                      text = " Vol:",
                       foreground = colors[2],
                       background = colors[4],
                       padding = 0
                       ),
              widget.Volume(
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[0],
                       background = colors[5],
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[5],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Clock(
                       foreground = colors[2],
                       background = colors[4],
                       format = "%A, %B %d  [ %H:%M ]"
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 10,
                       foreground = colors[0],
                       background = colors[4]
                       ),
              widget.Systray(
                       background = colors[0],
                       padding = 5
                       ),
              ]
    return widgets_list

 

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=23)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=40)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wmclass': 'oblogout'},  # ssh-askpass
    {'wmclass': 'feh'},  # ssh-askpass
    {'wmclass': 'gnome-screenshot'},  # ssh-askpass
    {'wmclass': 'blueman-manager'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

wmname = "LG3D"
