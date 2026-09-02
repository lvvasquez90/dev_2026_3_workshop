class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        a = 0
        sec = []
        fibo = 1
        if n == 0 or n == 1:
            return n
        elif n < 0:
            return None
        else:
            while len(sec) < n:
                sec.append(a)
                a, fibo = fibo, a + fibo
            return a
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        a = 0
        sec = []
        fibo = 1
        while len(sec) < n:
            sec.append(a)
            a, fibo = fibo, a + fibo
        return sec
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n <= 1: 
            return False
        elif n % 2 == 0 and n != 2:
            return False
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        gen = []
        if n == 1:
            return gen
        else:
            for i in range(n):
                if self.es_primo(i) == True:
                    gen.append(i)
            return gen
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        div = 0
        if n == 0 or n == 1:
            return False
        for i in range(1, n):
            if n % i == 0:
                div += i
        if div == n:
            return True
        else:
            return False
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        psc = [[1]]
        for i in range(1, filas):
            pscan = psc[-1]
            nuepsc = [1]
            for j in range(len(pscan) - 1):
                nuepsc.append(pscan[j] + pscan[j + 1])
            nuepsc.append(1)
            psc.append(nuepsc)
        return psc
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        facto = 1
        if n == 0 or n == 1:
            return 1
        elif n < 0:
            return None
        else:
            for i in range(n, 0, -1):
                facto *= i
            return facto
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        def diviso(lista, n):
            for i in range(1, n + 1):
                if n % i == 0:
                    lista.append(i)
        
        def mayor(dv):
            mx = dv[0]
            for i in dv:
                if i > mx:
                    mx = i
            return mx
        divia = []
        divib = []
        if self.es_primo(a) == True and self.es_primo(b) == True:
            return 1
        else:
            if a == 0:
                diviso(divib, b)
                if len(divib) == 1:
                    return divib[-1]
                else:
                    maxi = mayor(divib)
                return maxi
            elif b == 0:
                diviso(divia, a)
                if len(divia) == 1:
                    return divia[-1]
                else:
                    maxi = mayor(divia)
                return maxi
            else:
                diviso(divia, a)
                diviso(divib, b)
                div = [num for num in divia if num in divib]
                maxi = 0
                if len(div) == 1:
                    return div[-1]
                else:
                    maxi = mayor(div)
                return maxi
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        if a == 0 or b == 0:
            return 0
        else:
            return (a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        numi = [int(dig) for dig in str(n)]
        sumi = 0
        if len(numi) == 1:
            return n
        else:
            for i in numi:
                sumi += i
            return sumi
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        pass
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        pass