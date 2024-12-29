import dearpygui.dearpygui as dpg

def country_pick():
    city_value = dpg.get_value("city_input")
    print(f"City entered: {city_value}")

dpg.create_context()
dpg.create_viewport(title='Tempest Sky', width=600, height=600)
dpg.setup_dearpygui()

with dpg.window():
    dpg.add_text("Pick Your Country")
    dpg.add_input_text(hint="e.g., London", tag="city_input")
    dpg.add_button(label="Search", callback=country_pick)

    
    

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()