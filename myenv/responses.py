from random import randint, choice
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Escribe algo para utilizar el bot.'
    elif 'hola' in lowered:
        return 'Bienvenido al bot administrador de tareas.'