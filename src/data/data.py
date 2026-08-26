class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        linver = []
        for i in lista:
            linver.insert(0, i)
        return linver
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        for i in range(len(lista)):
            if elemento == lista[i]:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        lisindup = []
        for elem in lista:
            exist = True
            for i in lisindup:    
                if elem == i and type(elem) == type(i):
                    exist = False
                    break
            if exist:
                lisindup.append(elem)
        return lisindup
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        listcord = lista1 + lista2
        long = len(listcord)
        for i in range(long):
            posact = listcord[i]
            ind = i - 1
            while ind >= 0 and listcord[ind] > posact:
                listcord[ind + 1] = listcord[ind]
                ind -= 1
            listcord[ind + 1] = posact
        return listcord
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        if k == 0 or not lista:
            return lista
        
        k = k % len(lista)
        listrot = lista[-k:] + lista[:-k]
        return listrot
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        long = len(lista) + 1
        if long != 1:
            suma = long * (long + 1) / 2
            real = sum(lista)
        else:
            suma = long
            real = 0
        return suma - real
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        long = len(conjunto1)
        veri = 0
        for i in conjunto2:
            for j in conjunto1:
                if i == j:
                    veri += 1
        if veri == long:
            return True
        return False
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        lista = []
        
        def is_empty():
            if len(lista) == 0:
                return True
            else:
                return False
        
        def push(a):
            lista.append(a)
        
        def peek():
            return lista[-1]
        
        def pop():
            eli = lista.pop()
            return eli
        
        pila = {
            'is_empty': is_empty,
            'push': push,
            'peek': peek,
            'pop': pop    
        }
        
        return pila
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        lista = []
        
        def is_empty():
            if len(lista) == 0:
                return True
            else:
                return False
        
        def enqueue(a):
            lista.append(a)
        
        def dequeue():
            eli = lista.popleft()
            return eli
        
        def peek():
            return lista[0]
        
        cola = {
            'is_empty': is_empty,
            'enqueue': enqueue,
            'dequeue': dequeue,
            'peek': peek
        }
        
        return cola
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass