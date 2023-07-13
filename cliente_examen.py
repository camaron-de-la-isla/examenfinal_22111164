import threading
import sys
import socket
import pickle
import os

class Cliente():
#El cliente se inicializa y pregunta al usuario por el puerto y la IP y su nombre de usuario
	def __init__(self, host=input("Intoduzca la IP del servidor ?  "), port=int(input("Intoduzca el PUERTO del servidor ?  ")), nick=input("Introduce un nombre de usuario: ")):
		self.s = socket.socket()
		self.s.connect((host, int(port)))
		print('\n\tProceso con PID = ',os.getpid(), '\n\tHilo PRINCIPAL con ID =',threading.currentThread().getName(), '\n\tHilo en modo DAEMON = ', threading.currentThread().isDaemon(),'\n\tTotal Hilos activos en este punto del programa =', threading.active_count())
		threading.Thread(target=self.recibir, daemon=True).start()
#Añade el nombre de usuario del cliente a la lista de usuarios
		file = open("lista_de_usuarios.txt", "a")
		file.write(nick + os.linesep)
		file.close()
#La interfaz para introducir comandos
		while True:
			msg = nick+": "+input('\nEscriba texto ?   ** Enviar = ENTER   ** Salir Chat = 1 \n')
			if msg != nick + ": 1" : self.enviar(msg)
			else:
				print(" **** Me piro vampiro; cierro socket y mato al CLIENTE con PID = ", os.getpid())
				self.eliminarUsuario(nick)
				self.s.close()
				sys.exit()
#Recibe los mensajes de otros clientes y los muestra por pantalla
	def recibir(self):
		print('\nHilo RECIBIR con ID =',threading.currentThread().getName(), '\n\tPertenece al PROCESO con PID', os.getpid(), "\n\tHilos activos TOTALES ", threading.active_count())
		while True:
			try:
				data = self.s.recv(128)
                
				if data: A[] = [pickle.loads(data)[0]][pickle.loads(data)[1]]
                         B[] = [pickle.loads(data)[2]][pickle.loads(data)[3]]
                    sec_mult(A, B)
                    par_mult(A, B)
                    
                
			except: pass
#Envia un mensaje al servidor
	def enviar(self, msg):
		self.s.send(pickle.dumps(msg))
#Elimina el usuario de la lista de usuarios
	def eliminarUsuario(self, nick):
		with open('lista_de_usuarios.txt', 'r') as fr:
			lines = fr.readlines()

			with open('lista_de_usuarios.txt', 'w') as fw:
				for line in lines:
					if line.strip('\n') != nick:
						fw.write(line)
					

def sec_mult(A, B):
    C = [[0] * n_col_B for i in range(n_fil_A)]
    for i in range(n_fil_A):
        for j in range(n_col_B):
            for k in range(n_col_A):
                C[i][j] += A[i][k] * B[k][j]
    return C
def par_mult(A, B):
    n_cores = multiprocessing.cpu_count ()
    size_col = math.ceil(n_col_B/n_cores)
    size_fil = math.ceil(n_fil_A/n_cores)
    MC = mp.RawArray ('i', n_fil_A * n_col_B)
    cores = []
    for core in range(n_cores):
        i_MC = min(core * size_fil, n_fil_A)
        f_MC = min((core + 1) * size_fil, n_fil_A)
        cores.append(mp.Process(target=par_core, args=(A, B, MC, i_MC, f_MC)))
    for core in cores:
        core.start()
    for core in cores:
        core.join()
    C_2D = [[0] * n_col_B for i in range(n_fil_A)]
    for i in range(n_fil_A):
        for j in range(n_col_B):
            C_2D[i][i] = MC[i*n_col_B + j]
    return C_2D

def par_core(A, B, MC, i_MC, f_MC):
    for i in range (i_MC, f_MC):
        for j in range(len (B[0])):
            for k in range(len (A[0])):
                MC[i*len(B[0])+ j] += A[i][k] * B[k][j]

arrancar = Cliente()