#everything in mm

import math

matboard_length = 813
matboard_width = 1016
matboard_height = 1.27

def get_area_pi_beam(length, web_height, bent_length, support_length = 0, width = 100, top_layers = 2, web_layers = 2):
    return ((length * width * top_layers) + ((web_height + bent_length) * web_layers * length)) + support_length * width

def get_area_variable_pi_beam(length, angle_of_variation, center_beam_width, web_layers = 2):
    height_of_variation = ((length - center_beam_width) / 2) * math.tan(angle_of_variation) 
    return (((length - center_beam_width) / 2) * math.tan(angle_of_variation) + height_of_variation * center_beam_width) * web_layers

def get_area_i_beam(length, width, web_height, horizontal_layers = 2, web_layers = 2):
    return (length * width * horizontal_layers * 2) + (length * web_height * web_layers)

def get_i_I_beam(web_height, width, horizontal_layers, web_layers):
    y_bar = (web_height + horizontal_layers * 2 * matboard_height) / 2
    I = ((width * ((web_height + horizontal_layers * matboard_height * 2)**3)) / 12) - (((width - web_layers * matboard_height) * (web_height) ** 3) / 12)
    return I

def get_i_Pi_beam(web_height, width, horizontal_layers, web_layers):
    y_bar = 

print("I TEST:", get_i_I_beam(150, 100, 3, 4))

class beam:

    def __init__(self, beam_type, length, width, web_height, angle = 0, bent_length = None, support_length = 0, horizontal_layers = 2, web_layers = 1):
        if(beam_type == "pi"):
            self.area = get_area_pi_beam(length, web_height, bent_length, support_length, width, horizontal_layers, web_layers)
        elif(beam_type == "i"):
            self.area = get_area_i_beam(length, width, web_height, horizontal_layers, web_layers)
        elif(beam_type == 'variable'):
            self.area = get_area_variable_pi_beam(length, angle, center_beam_width, web_layers)



class bridge:
    
    def __init__ (self):
        self.beams = []
        self.total_area = 0
        pass

    def add_beam(self, beam):
        self.beams.append(beam)
        self.total_area += beam.area

bridge1 = bridge()

point_load_loc = 280

bridge_length = 950
bridge_width = 100
main_beam_height = 30
main_beam_h_layers = 2
main_beam_v_layers = 2
main_beam_angle = 45
center_beam_width = 150
center_beam_height = 600 - math.tan(main_beam_angle) * ((bridge_length / 2) - point_load_loc - center_beam_width / 2)
center_beam_h_layers = 3
center_beam_v_layers = 4

main_beam = beam('pi', bridge_length, bridge_width, main_beam_height, bent_length = 10, horizontal_layers = main_beam_h_layers, web_layers = main_beam_v_layers, support_length = 30)
variable_main_beam = beam('variable', bridge_length - point_load_loc * 2, bridge_width, 0, main_beam_angle, web_layers = main_beam_v_layers)
center_beam = beam('i', center_beam_height, bridge_width, center_beam_width, horizontal_layers = center_beam_h_layers, web_layers = center_beam_v_layers)

print("MAIN BEAM:", main_beam.area)
print("VARIABLE: ", variable_main_beam.area)
print("CENTER BEAM", center_beam.area)

bridge1.add_beam(main_beam)
bridge1.add_beam(variable_main_beam)
bridge1.add_beam(center_beam)

print("Total Area of Bridge 1:", bridge1.total_area)
print(matboard_length * matboard_width)