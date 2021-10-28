from app.models.configuration import Configuration

class FormValidator:
    # def __init__(self,type):
    #     self._type = type
    

    @staticmethod
    def color_is_valid(bg_color):
        return ( bg_color in Configuration.get_valid_colors() )