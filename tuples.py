
def get_coordinate(azara):
    return azara[1]



def convert_coordinate(cordenada):
    num=cordenada[:-1]
    letra=cordenada[-1]
    return num,letra



def create_record(azara, rui):
    azara_cord= azara[1]
    azara_cordf= convert_coordinate(azara_cord)
    rui_cord= rui[1]
    if azara_cordf==rui_cord:
        return (azara[0], azara_cord, rui[0], rui[1], rui[2])
    else:
        return "No coincide"
   
 
