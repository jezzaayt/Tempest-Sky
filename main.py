import dearpygui.dearpygui as dpg
from api import *


width = 900
height = 450
dpg.create_context()
dpg.create_viewport(title='Tempest Sky', width=width, height=height)
dpg.set_viewport_small_icon("icon.ico")  # Small icon for the title bar
dpg.set_viewport_large_icon("icon.ico")  # Large icon for the taskbar
dpg.setup_dearpygui()

measurement_list=["metric","imperial", "kelvin"]

with dpg.window (width=width, height=height, no_move=True,  no_title_bar=True):
    dpg.add_text("Pick Your City")
    dpg.add_input_text(hint="e.g., London", tag="City Name")
    dpg.add_button(label="Search", callback=fetch_weather)
    dpg.add_listbox(items=measurement_list, tag="Measurement" )
    
    dpg.add_text("Weather Output:")
    dpg.add_text(tag="latlon", default_value="")

    dpg.add_listbox(tag="Weather_Conditions",  default_value="", width=900)


    
    

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()