class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        textosi = texto.replace(" ", "").lower()
        rev = textosi[::-1]
        if rev == textosi:
            return True
        return False
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        inv = ""
        for i in texto:
            inv = i + inv
        return inv
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        voc = ["a", "e", "i", "o", "u"]
        vcm = [vo.upper() for vo in voc]
        sma = 0
        for i in texto:
            if i in voc or i in vcm:
                sma += 1
        return sma
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        voc = ["a", "e", "i", "o", "u"]
        vcm = [vo.upper() for vo in voc]
        sma = 0
        for i in texto:
            if i not in voc and i not in vcm:
                sma += 1
        return sma
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        textosi1 = texto1.replace(" ", "").lower()
        textosi2 = texto2.replace(" ", "").lower()
        cont = []
        if len(textosi1) != len(textosi2):
            return False
        for i in textosi1:
            ana = False
            for j in range(len(textosi2)):
                if i == textosi2[j] and j not in cont:
                    cont.append(j)
                    ana = True
                    break
            if ana == False:
                return False
        return True
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        if not texto:
            return 0
        texto = texto.strip()
        cant = len(texto.split())
        return cant
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        if not texto:
            return ""
        sep = ""
        pali = True
        
        for i in texto:
            if i != " " and pali:
                sep += i.upper()
                pali = False
            else:
                sep += i
                if i == " ":
                    pali = True
        return sep
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        if not texto:
            return ""
        while "  " in texto:
            texto = texto.replace("  ", " ")
        return texto
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        nume = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"]
        cont = True
        for i in texto:
            if i == "." or i not in nume:
                cont = False
        return cont
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        if not texto:
            return ""
        dic = ["a", "b", "c", "d", "e", "f", "g", "h", "i", 
               "j", "k", "l", "m", "n", "o", "p", "q", "r", 
               "s", "t", "u", "v", "w", "x", "y", "z"]
        dicm = [let.upper() for let in dic]
        cice = ""
        for i in texto:
            if i in dic:
                iac = dic.index(i)
                inu = (iac + desplazamiento) % len(dic)
                cice += dic[inu]
            if i in dicm:
                iac = dicm.index(i)
                inu = (iac + desplazamiento) % len(dicm)
                cice += dicm[inu]
        return cice
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        pass