from trivia import Question, Quiz

def run_quiz():
    print("*******************************************")
    print("Bienvenido al juego de TRIVIA")
    print("*******************************************")

    print("Responde las siguientes preguntas seleccionando el numero de la opccion correcta")
    quiz = Quiz()

    preguntas = [
        {
            "description": "¿cua es el record mundial del cubo de rubik de 3x3?",
            "options": ["5,11 segundos", "4,24 segundos", "4,01 segundos", "3,08 segundos"],
            "correct_answer": "3,08 segundos"
        },
        {
            "description": "¿cual es la capital del peru?",
            "options": ["Cusco", "Arequipa", "Lima", "Trujillo"],
            "correct_answer": "Lima"
        },
        {
            "description": "¿quien fue el ultimo inca?",
            "options": ["Tupac Amaru", "Atahualpa", "Manco Capac", "Pachacutec"],
            "correct_answer": "Atahualpa"
        },
        {
            "description": "¿en que lugar se encuentra el lago titicaca?",
            "options": ["Puno", "Cusco", "Loreto", "Ayacucho"],
            "correct_answer": "Puno"
        },
        {
            "description": "¿en que año se proclamo la independencia del Peru?",
            "options": ["1820", "1821", "1822", "1824"],
            "correct_answer": "1821"
        },
        {
            "description": "¿que animal aparece en el escudo nacional del Peru?",
            "options": ["Puma", "Condor", "Vicuña", "Llama"],
            "correct_answer": "Vicuña"
        },
        {
            "description": "cual es el oceano mas grande del planeta?",
            "options": ["Oceano Atlantico", "Oceano Pacifico", "Oceano Artico", "Oceano Antartico"],
            "correct_answer": "Oceano Pacifico"
        },
        {
            "description": "¿cuatos huesos tiene el cuerpo de un adulto?",
            "options": ["108", "296", "208", "206"],
            "correct_answer": "206"
        },
        {
            "description": "¿cuantas calorias aporta un gramo de proteina?",
            "options": ["2", "3", "4", "5"],
            "correct_answer": "4"
        },
        {
            "description": "¿cual es el quinto planeta del sistema solar?",
            "options": ["Marte", "Mercurio", "Jupiter", "Tierra"],
            "correct_answer": "Jupiter"
        },  
    ]

    for p in preguntas:
        quiz.add_question(Question(p["description"], p["options"], p["correct_answer"]))
    
    print("-------------------------------------------")
    cont = 0
    puntos = 0
    while True:
        pregunta = quiz.get_next_question()
    
        if pregunta is None:
            print("se acabaron las preguntas, GRACIAS POR JUGAR")
            break
        
        cont = cont + 1

        print(f"pregunta {cont}: {pregunta.description}")
        for i, opcion in enumerate(pregunta.options):
            print(f"{i + 1}. {opcion}")
        
        #respueta = int(input("eliga la clave correcta(1-4): "))
        while True:
            respuesta = input("\neliga una opccion (1-4): ")
            try:
                indice = int(respuesta)
                if 1 <= indice <= len(pregunta.options):
                    seleccion = pregunta.options[indice - 1]
                    break
            except ValueError:
                print("\nEntrada invalida")

        if pregunta.is_correct(seleccion):
            print("¡CORRECTO!")
            puntos += 1
        else:
            print("la clave es incorrecta")
        
        print("-------------------------------------------")
    
    print("\nJUEGO TERMINADO ")
    print("total de preguntas")
    print(f"respuestas correctas: {puntos}")
    print(f"respuestas incorrectas: {10-puntos}")

run_quiz()