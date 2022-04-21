## this file contains options that can be changed to customize your game.
##
## lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## basics ######################################################################

## a human-readable name of the game. this is used to set the default window
## title, and shows up in the interface and error reports.
##
## the _() surrounding the string marks it as eligible for translation.

define config.name = _("ren'py extension sample for visual studio code")


## determines if the title given above is shown on the main menu screen. set
## this to false to hide the title.

define gui.show_name = true


## the version of the game.

define config.version = "2.0"


## text that is placed on the game's about screen. place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
example project for the ren'py extension for visual studio code
""")


## a short name for the game used for executables and directories in the built
## distribution. this must be ascii-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "extension"


## sounds and music ############################################################

## these three variables control which mixers are shown to the player by
## default. setting one of these to false will hide the appropriate mixer.

define config.has_sound = true
define config.has_music = true
define config.has_voice = true


## to allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## uncomment the following line to set an audio file that will be played while
## the player is at the main menu. this file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## transitions #################################################################
##
## these variables set transitions that are used when certain events occur.
## each variable should be set to a transition, or none to indicate that no
## transition should be used.

## entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## between screens of the game menu.

define config.intra_transition = dissolve


## a transition that is used after a game has been loaded.

define config.after_load_transition = none


## used when entering the main menu after the game has ended.

define config.end_game_transition = none


## a variable to set the transition used when the game starts does not exist.
## instead, use a with statement after showing the initial scene.


## window management ###########################################################
##
## this controls when the dialogue window is displayed. if "show", it is always
## displayed. if "hide", it is only displayed when dialogue is present. if
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## after the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## transitions used to show and hide the dialogue window

define config.window_show_transition = dissolve(.2)
define config.window_hide_transition = dissolve(.2)


## preference defaults #########################################################

## controls the default text speed. the default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## the default auto-forward delay. larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## save directory ##############################################################
##
## controls the platform-specific place ren'py will place the save files for
## this game. the save files will be placed in:
##
## windows: %appdata\renpy\<config.save_directory>
##
## macintosh: $home/library/renpy/<config.save_directory>
##
## linux: $home/.renpy/<config.save_directory>
##
## this generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "extension-1630425934"


## icon ########################################################################
##
## the icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## build configuration #########################################################
##
## this section controls how ren'py turns your project into distribution files.

init python:

    ## the following functions take file patterns. file patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. if multiple patterns match, the first is
    ## used.
    ##
    ## in a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## for example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## classify files as none to exclude them from the built distributions.

    build.classify('**~', none)
    build.classify('**.bak', none)
    build.classify('**/.**', none)
    build.classify('**/#**', none)
    build.classify('**/thumbs.db', none)

    ## to archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## a google play license key is required to download expansion files and perform
## in-app purchases. it can be found on the "services & apis" page of the google
## play developer console.

# define build.google_play_key = "..."


## the username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
