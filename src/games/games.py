class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        
        Args:
            jugador1 (str): Elección del jugador 1 ("piedra", "papel", "tijera")
            jugador2 (str): Elección del jugador 2 ("piedra", "papel", "tijera")
            
        Returns:
            str: "jugador1", "jugador2" o "empate"
            
        Reglas:
            - Piedra vence a tijera
            - Tijera vence a papel
            - Papel vence a piedra
        """
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()
        if (
            (jugador2 == "piedra" and jugador1 == "tijera") or
            (jugador2 == "tijera" and jugador1 == "papel") or
            (jugador2 == "papel" and jugador1 == "piedra")
        ):
            return "jugador2"
        elif (
            (jugador1 == "piedra" and jugador2 == "tijera") or
            (jugador1 == "tijera" and jugador2 == "papel") or
            (jugador1 == "papel" and jugador2 == "piedra")
        ):
            return "jugador1"
        elif jugador1 == jugador2:
            return "empate"
        else:
            return "invalid"
    
    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        
        Args:
            numero_secreto (int): El número que se debe adivinar
            intento (int): El número propuesto por el jugador
            
        Returns:
            str: "correcto", "muy alto" o "muy bajo"
        """
        if numero_secreto == intento:
            return "correcto"
        elif numero_secreto < intento:
            return "muy alto"
        elif numero_secreto > intento:
            return "muy bajo"
    
    def ta_te_ti_ganador(self, tablero):
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.
        
        Args:
            tablero (list): Matriz 3x3 con valores "X", "O" o " " (espacio vacío)
            
        Returns:
            str: "X", "O", "empate" o "continua"
            
        Ejemplo:
            [["X", "X", "X"],
             ["O", "O", " "],
             [" ", " ", " "]] -> "X"
        """
        def ganador(tabpo, val):
            return (
                (tabpo[0] == tabpo[1] == tabpo[2] == val) or
                (tabpo[0] == tabpo[4] == tabpo[8] == val) or
                (tabpo[0] == tabpo[3] == tabpo[6] == val) or
                (tabpo[1] == tabpo[4] == tabpo[7] == val) or
                (tabpo[2] == tabpo[5] == tabpo[8] == val) or
                (tabpo[2] == tabpo[4] == tabpo[6] == val) or
                (tabpo[3] == tabpo[4] == tabpo[5] == val) or
                (tabpo[6] == tabpo[7] == tabpo[8] == val)
            )
        tablero = [letra for fila in tablero for letra in fila]
        if ganador(tablero, "X"):
            return "X"
        elif ganador(tablero, "O"):
            return "O"
        elif " " in tablero:
            return "continua"
        elif (ganador(tablero, "O") == False and ganador(tablero, "X") == False):
            return "empate"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        import random
        combi = []
        lon = len(colores_disponibles)
        if longitud == 0:
            return combi
        else:
            if longitud < lon:
                combi.append(colores_disponibles[0])
            elif longitud >= lon:
                while longitud > 0:
                    ind = random.randint(0, lon)
                    combi.append(colores_disponibles[ind])
                    longitud -= 1
            return combi
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        pass