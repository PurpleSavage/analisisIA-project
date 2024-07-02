from serviceOpenIa import OpenIaInspector
from analysisData import Data
from generateUUID import generate_random_id

# instanciamos la clase data
data = Data()

#aquí obtenemos todo el historial, tambien hay una funcion llamada obtener_historial_por_empleado que solo sirve para obtener el hisotrial de una persona
# esta función hay que mejorarla
historial = data.get_historial()

list_porcentaje_asistencia= data.get_percentage_assist(historial)

#instanciamos la clase para comunicarnos con gpt
gpt=OpenIaInspector(list_porcentaje_asistencia)
text_gpt= gpt.get_gpt_response()
#creamos un word pasando la lista del hisotrial, el exto obtenido del gpt y el nombre del archivo


#es importante generar un id random para que los documentos nunca se repitan,se está 
# tomando la fecha, la hora y una porcion de un uuid para siempre tener el regit de los documentos por hora fecha y un id unico
myuuid=generate_random_id()
data.create_word(list_porcentaje_asistencia,text_gpt,f"{myuuid}-informacion")      
