#!/usr/bin/env python3

# Imports
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# KIVY config file
with open("main.kv") as kv:
    Builder.load_string(kv.read())

# Login menu screens class
class LoginMenuScreen(Screen):

    # Check login password
    def login(self, username, errorlable):
        if username == "admin":
            self.manager.current = 'MainMenu'
        else:
            errorlable.text = "[b][color=#FF0000][font=RobotoMono-Regular]Login Failed! Try Again[/font][/color][/b]"

# Main menu screen class
class MainMenuScreen(Screen):
    pass

# Profile screen class
class ProfileScreen(Screen):
    pass

# About menu screen class
class AboutMenuScreen(Screen):
    pass

# guest menu screen class
class GuestMenuScreen(Screen):
    pass

class unk(Screen):
    def funcuion():
        print("hi")

# Main class
class BarareApp(App):

    # Build function
    def build(self):

        # root screen manager
        self.root = ScreenManager()
        
        # Login menu screen
        self.LoginMenuScreen = LoginMenuScreen(name='LoginMenu')
        self.root.add_widget(self.LoginMenuScreen)

        # Main menu screen
        self.MainMenuScreen = MainMenuScreen(name='MainMenu')
        self.root.add_widget(self.MainMenuScreen)

        # About menu screen
        self.AboutMenuScreen = AboutMenuScreen(name='AboutMenu')
        self.root.add_widget(self.AboutMenuScreen)

        # Profile screen
        self.ProfileScreen = ProfileScreen(name='Profile')
        self.root.add_widget(self.ProfileScreen)

        # Guest menu screen
        self.GuestMenuScreen = GuestMenuScreen(name='GuestMenu')
        self.root.add_widget(self.GuestMenuScreen)

        # Set current screen to Login menu and return root   
        self.root.current = 'LoginMenu'
        return self.root

# run the class
BarareApp().run()
