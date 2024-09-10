import numpy as np
import matplotlib.pyplot as plt
import control as c
import pandas as pd
from colorama import Fore, Style, Back, init


print(Fore.YELLOW + '-'*100 + Style.BRIGHT)
print(Fore.CYAN + 'Design de Filtros'.center(100) + Style.BRIGHT)
print(Fore.YELLOW  + '-'*100 + Style.RESET_ALL)
print('')

'''Amax = float(input('Insira o valor de Amax: ')) #2
Amin = float(input('Insira o valor de Amin: ')) #60
Fp = float(input('Insira o valor de Fp: ')) # 1000
Fs = float(input('Insira o valor de Fs: ')) # 10000
K = float(input('Insira o valor do Ganho: ')) # 1'''
Amax = 1
Amin = 60
Fp = 1000
Fs = 2000
K = 10

print(Fore.YELLOW + '-'*100 + Style.RESET_ALL)

# Cálculo de Wp e Ws
Wp = 2 * np.pi * Fp
Ws = 2 * np.pi * Fs

entrada1 = int(input('Escolha o seu tipo de filtro: (1) Butterworth --- (2) Chebyshev .....: '))
entrada2 = int(input('Escolha a sua topologia: (1) Sallen-Key ---- (2) MFB .....: '))
print(Fore.YELLOW + '-'*100 + Style.RESET_ALL)

if entrada1 == 1 and entrada2 == 1:
    e = np.sqrt(10**(Amax/10) - 1)
    N = int(np.ceil((np.log10((10**(Amin/10) - 1) / (e**2))) / (2 * np.log10(Ws/Wp))))
    W0 = Wp * ((1/e)**(1/N))

    tetac = []  # Variável exclusiva apenas para mostrar os valores de teta para o usuário
    teta = []   # Variável que armazena os valores de teta para o cálculo em rad
    polos = []  # Variável que armazena os valores dos polos
    
    # olhar o cálculo dos polos dps
    
    for i in range(1, N+1):
        if i == 1:
            tetac_i = 180 / (2 * N)
        else:
            tetac_i = 180 * (2 * i - 1) / (2 * N)
        
        teta_i = np.deg2rad(tetac_i)
        polo = W0 * (-np.sin(teta_i) + 1j * np.cos(teta_i))
        
        tetac.append(tetac_i)
        teta.append(tetac_i)
        polos.append(polo)
    
    
    print(Fore.YELLOW + '-'*100 + Style.BRIGHT)
    print(Fore.RED + 'Polos:'.center(100) + Style.RESET_ALL)
    
    i = 1
    for polo in polos:
        print(Fore.GREEN + f'Polo({i}):  {polo.real:.2e} + {polo.imag:.2e}j' + Style.RESET_ALL)
        i = i+1
    print(Fore.YELLOW + '-'*100 + Style.RESET_ALL)

    plt.scatter(np.real(polos), np.imag(polos), color='red', marker='x')
    
    for polo in polos:
        plt.plot([0, np.real(polo)], [0, np.imag(polo)], color='blue', linestyle='--', linewidth=0.5)
            
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginária')
    plt.title('Polos do Filtro Butterworth')
    plt.grid()
    plt.show()
    
    # Função de transferência
    Tnum = [K * (W0**N)]
    Tden = np.poly(polos)
    T = c.TransferFunction(Tnum, Tden)
    
    print('')
    print(Fore.YELLOW + '-'*100 + Style.BRIGHT)
    print(Fore.RED + 'Função de Transferência: '.center(100) + Style.RESET_ALL)
    print(str(T).center(100))
    print(' ')
    
    # Cálculo manual do diagrama de Bode
    x = np.logspace(np.log10(Wp/100), np.log10(100*Wp), 1000)
    H = np.abs(np.polyval(Tnum, 1j*x) / np.polyval(Tden, 1j*x))
    
    # Diagrama de Bode (Magnitude)
    Hdb = 20 * np.log10(H)
    plt.figure()
    plt.semilogx(x, Hdb)
    plt.xlabel('Frequência [rad/s]')
    plt.ylabel('Magnitude [dB]')
    plt.title('Magnitude')
    plt.grid(which='both', linestyle='--', linewidth=0.5)
    plt.show()
    
    # Diagrama de Bode (Fase)
    fase = np.zeros_like(x)
    for polo in polos:
        wp = np.abs(polo)
        fase -= np.arctan(x/wp)
        
    fase_deg = np.degrees(fase)
    
    plt.figure()
    plt.semilogx(x, fase_deg)
    plt.xlabel('Frequência [rad/s]')
    plt.ylabel('Fase [°]')
    plt.title('Fase')
    plt.grid(which='both', linestyle='--', linewidth=0.5)
    plt.show()
    
    # Cálculo dos componentes R e C
    R1 = []
    R2 = []
    C1 = []
    C2 = []
    
    k = len(polos)
    
    for i in range(0, k//2):
        polo1 = polos[i].real
        polo2 = polos[i].imag
        ksi = abs(polo2)/abs(polo1)
        Q = 1/(2*ksi)
        print('Valor de Q: ', Q)
        n = 1.1 * 4*(Q**2)
        m = (-(2 - (n / (Q**2))) + np.sqrt(((2 - (n / (Q**2)))**2) - 4)) / 2
        
        print('Valor de n: ', n)
        print('Valor de m: ', m)
        

        C1v = 10e-9
        C2v = n * C1v
        R2v = 1/(W0 * C1v * np.sqrt(m * n))
        R1v = m * R2v
        
        C1.append(C1v)
        R1.append(R1v)
        R2.append(R2v)
        C2.append(C2v)
    
    print('-'*50)  
    print('Valores dos Componentes para o Sallen-Key'.center(50))
    print('-'*50)   
    print('C1: ', C1)
    print('C2: ', C2)
    print('R1: ', R1)
    print('R2: ', R2)
    print('-'*50)  
    
if entrada1 == 2 and entrada2 == 1:
    
    e = np.sqrt(10**(Amax/10)-1)
    N = int(np.ceil((np.arccosh(np.sqrt((10**(Amin/10)-1)/e**2)))/np.arccosh(Ws/Wp)))
    
    polos = []  # Variável que armazena os valores dos polos
    
    for i in range(1, N+1):
        polo = -Wp*np.sin(((2*i - 1)/N)*(np.pi/2))*np.sinh(1/N * np.arcsinh(1/e)) + 1j*Wp*np.cos(((2*i - 1)/N)*(np.pi/2))*np.cosh(1/N * np.arcsinh(1/e))
        polos.append(polo)
       
    print('-'*50)
    print('Polos:')
    
    for polo in polos:
        print(f'    {polo.real:.2e} + {polo.imag:.2e}j')
    print('-'*50)

    plt.scatter(np.real(polos), np.imag(polos), color='red', marker='x')
    
    for polo in polos:
        plt.plot([0, np.real(polo)], [0, np.imag(polo)], color='blue', linestyle='--', linewidth=0.5)
            
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginária')
    plt.title('Polos do Filtro Butterworth')
    plt.grid()
    plt.show()

    Tnum = np.array([K*Wp**N])
    Tden = np.poly(polos)*(e*2**(N-1))
    
    T = c.TransferFunction(Tnum, Tden)
    print(T)
    
    # Cálculo manual do diagrama de Bode
    x = np.logspace(np.log10(Wp/100), np.log10(100*Wp), 1000)
    H = np.abs(np.polyval(Tnum, 1j*x)/np.polyval(Tden, 1j*x))
    
    # Diagrama de Bode (Magnitude)
    Hdb = 20*np.log10(H)
    plt.figure()
    plt.semilogx(x, Hdb)
    plt.xlabel('Frequência [rad/s]')
    plt.ylabel('Magnitude [dB]')
    plt.title('Magnitude')
    plt.grid(which='both', linestyle='--', linewidth=0.5)
    plt.show()
    
    # Diagrama de Bode (Fase)
    fase = np.zeros_like(x)
    for polo in polos:
        wp = np.abs(polo)
        fase -= np.arctan(x/wp)
        
    fase_deg = np.degrees(fase)
    
    plt.figure()
    plt.semilogx(x, fase_deg)
    plt.xlabel('Frequência [rad/s]')
    plt.ylabel('Fase [°]')
    plt.title('Fase')
    plt.grid(which='both', linestyle='--', linewidth=0.5)
    plt.show()
    
    # Cálculo dos componentes R e C
    R1 = []
    R2 = []
    C1 = []
    C2 = []
    
    k = len(polos)
    
    for i in range(0, k//2):
        polo1 = polos[i].real
        polo2 = polos[i].imag
        W0 = np.abs(polos[i])
        ksi = abs(polo2)/abs(polo1)
        Q = 1/(2*ksi)
        n = 1 + 4*(Q**2)
        m = (-(2 - (n / (Q**2))) + np.sqrt(((2 - (n / (Q**2)))**2) - 4)) / 2

        C1v = 10e-9
        C2v = n * C1v
        R2v = 1/(W0 * C1v * np.sqrt(m * n))
        R1v = m*R2v
        
        
        C1.append(C1v)
        R1.append(R1v)
        R2.append(R2v)
        C2.append(C2v)
    
    print('-'*50)  
    print('Valores dos Componentes para o Sallen-Key'.center(50))
    print('-'*50)   
    print('C1: ', C1)
    print('C2: ', C2)
    print('R1: ', R1)
    print('R2: ', R2)
    print('-'*50)
    
if entrada1 == 1 and entrada2 == 2:
    e = np.sqrt(10**(Amax/10) - 1)
    N = int(np.ceil((np.log10((10**(Amin/10) - 1) / (e**2))) / (2 * np.log10(Ws/Wp))))
    K_n = K**(1/np.floor(N/2))
    W0 = Wp * ((1/e)**(1/N))

    tetac = []  # Variável exclusiva apenas para mostrar os valores de teta para o usuário
    teta = []   # Variável que armazena os valores de teta para o cálculo em rad
    polos = []  # Variável que armazena os valores dos polos
    
    for i in range(1, N+1):
        if i == 1:
            tetac_i = 180 / (2 * N)
        else:
            tetac_i = 180 * (2 * i - 1) / (2 * N)
        
        teta_i = np.deg2rad(tetac_i)
        polo = W0 * (-np.sin(teta_i) + 1j * np.cos(teta_i))
        
        tetac.append(tetac_i)
        teta.append(teta_i)
        polos.append(polo)
    
    
    print('-'*50)
    print('Polos:')
    for polo in polos:
        print(f'    {polo.real:.2e} + {polo.imag:.2e}j')
    print('-'*50)

    plt.scatter(np.real(polos), np.imag(polos), color='red', marker='x')
    
    for polo in polos:
        plt.plot([0, np.real(polo)], [0, np.imag(polo)], color='blue', linestyle='--', linewidth=0.5)
            
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginária')
    plt.title('Polos do Filtro Butterworth')
    plt.grid()
    plt.show()
    
    # Função de transferência
    Tnum = [K * (W0**N)]
    Tden = np.poly(polos)
    T = c.TransferFunction(Tnum, Tden)
    
    print('')
    print('-'*50)
    print('Função de Transferência: ', T)
    print(' ')
    
    # Cálculo manual do diagrama de Bode
    x = np.logspace(np.log10(Wp/100), np.log10(100*Wp), 1000)
    H = np.abs(np.polyval(Tnum, 1j*x) / np.polyval(Tden, 1j*x))
    
    # Diagrama de Bode (Magnitude)
    Hdb = 20 * np.log10(H)
    plt.figure()
    plt.semilogx(x, Hdb)
    plt.xlabel('Frequência [rad/s]')
    plt.ylabel('Magnitude [dB]')
    plt.title('Magnitude')
    plt.grid(which='both', linestyle='--', linewidth=0.5)
    plt.show()
    
    # Diagrama de Bode (Fase)
    fase = np.zeros_like(x)
    for polo in polos:
        wp = np.abs(polo)
        fase -= np.arctan(x/wp)
        
    fase_deg = np.degrees(fase)
    
    plt.figure()
    plt.semilogx(x, fase_deg)
    plt.xlabel('Frequência [rad/s]')
    plt.ylabel('Fase [°]')
    plt.title('Fase')
    plt.grid(which='both', linestyle='--', linewidth=0.5)
    plt.show()
    
    # Cálculo dos componentes R e C
    R1 = []
    R2 = []
    R3 = []
    C1 = []
    C2 = []
    
    k = len(polos)
    
    for i in range(0, k//2):
        
        polo1 = polos[i].real
        polo2 = polos[i].imag
        g = 1 + K
        #ksi = abs(polo2)/abs(polo1)
        ksi = polo1/abs(polos[i])
        #Q = 1/(2*np.sin(teta[i]))
        Q = 1/(2*ksi)
        n = 1.1*g*4*(Q**2)
        a = (2/g) - (n/((g**2)*Q**2))
        m = - a + np.sqrt((a**2)-(4/(g**2)))

        C1v = 10e-9
        C2v = (n * C1v)
        R2v = (1/(W0 * C1v * np.sqrt(m * n)))
        R3v = (m * R2v)
        R1v = (R3v/K)
        
        C1.append(C1v)
        R1.append(R1v)
        R2.append(R2v)
        R3.append(R3v)
        C2.append(C2v)
    
    print(Fore.YELLOW + '-'*100 + Style.RESET_ALL)  
    print(Fore.CYAN + 'Valores dos Componentes para o Sallen-Key'.center(100) + Style.BRIGHT)
    print(Fore.YELLOW + '-'*100 + Style.RESET_ALL)
    print(Fore.GREEN + 'C1: ' + Style.RESET_ALL, C1)
    print(Fore.GREEN + 'C2: ' + Style.RESET_ALL, C2)
    print(Fore.GREEN + 'R1: ' + Style.RESET_ALL, R1)
    print(Fore.GREEN + 'R2: ' + Style.RESET_ALL, R2)
    print(Fore.GREEN + 'R3: ' + Style.RESET_ALL, R3)
    print(Fore.YELLOW + '-'*100 + Style.RESET_ALL)
    
if entrada1 == 2 and entrada2 == 2:
    e = np.sqrt(10**(Amax/10)-1)
    N = int(np.ceil((np.arccosh(np.sqrt((10**(Amin/10)-1)/e**2)))/np.arccosh(Ws/Wp)))
    
    polos = []  # Variável que armazena os valores dos polos
    
    for i in range(1, N+1):
        polo = -Wp*np.sin(((2*i - 1)/N)*(np.pi/2))*np.sinh(1/N * np.arcsinh(1/e)) + 1j*Wp*np.cos(((2*i - 1)/N)*(np.pi/2))*np.cosh(1/N * np.arcsinh(1/e))
        polos.append(polo)
       
    print('-'*50)
    print('Polos:')
    
    for polo in polos:
        print(f'    {polo.real:.2e} + {polo.imag:.2e}j')
    print('-'*50)

    plt.scatter(np.real(polos), np.imag(polos), color='red', marker='x')
    
    for polo in polos:
        plt.plot([0, np.real(polo)], [0, np.imag(polo)], color='blue', linestyle='--', linewidth=0.5)
            
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginária')
    plt.title('Polos do Filtro Butterworth')
    plt.grid()
    plt.show()

    Tnum = np.array([K*Wp**N])
    Tden = np.poly(polos)*(e*2**(N-1))
    
    T = c.TransferFunction(Tnum, Tden)
    print(T)
    
    # Cálculo manual do diagrama de Bode
    x = np.logspace(np.log10(Wp/100), np.log10(100*Wp), 1000)
    H = np.abs(np.polyval(Tnum, 1j*x)/np.polyval(Tden, 1j*x))
    
    # Diagrama de Bode (Magnitude)
    Hdb = 20*np.log10(H)
    plt.figure()
    plt.semilogx(x, Hdb)
    plt.xlabel('Frequência [rad/s]')
    plt.ylabel('Magnitude [dB]')
    plt.title('Magnitude')
    plt.grid(which='both', linestyle='--', linewidth=0.5)
    plt.show()
    
    # Diagrama de Bode (Fase)
    fase = np.zeros_like(x)
    for polo in polos:
        wp = np.abs(polo)
        fase -= np.arctan(x/wp)
        
    fase_deg = np.degrees(fase)
    
    plt.figure()
    plt.semilogx(x, fase_deg)
    plt.xlabel('Frequência [rad/s]')
    plt.ylabel('Fase [°]')
    plt.title('Fase')
    plt.grid(which='both', linestyle='--', linewidth=0.5)
    plt.show()
    
    # Cálculo dos componentes R e C
    R1 = []
    R2 = []
    R3 = []
    C1 = []
    C2 = []
    
    k = len(polos)
    
    for i in range(0, k//2):
        
        polo1 = polos[i].real
        polo2 = polos[i].imag
        ksi = abs(polo2)/abs(polo1)
        W0 = np.abs(polos[i])
        Q = 1/(2*ksi)
        g = 1 + K
        n = 1.1*g*4*(Q**2)
        a = (2/g) - (n/((g**2)*Q**2))
        m = - a + np.sqrt((a**2)-(4/(g**2)))

        C1v = 10e-9
        C2v = (n * C1v)
        R2v = (1/(W0 * C1v * np.sqrt(m * n)))
        R3v = (m * R2v)
        R1v = (R3v/K)
        
        C1.append(C1v)
        R1.append(R1v)
        R2.append(R2v)
        R3.append(R3v)
        C2.append(C2v)
    
    print(Fore.YELLOW + '-'*100 + Style.RESET_ALL)  
    print(Fore.CYAN + 'Valores dos Componentes para o Sallen-Key'.center(100) + Style.BRIGHT)
    print(Fore.YELLOW + '-'*100 + Style.RESET_ALL)
    print(Fore.GREEN + 'C1: ' + Style.RESET_ALL, C1)
    print(Fore.GREEN + 'C2: ' + Style.RESET_ALL, C2)
    print(Fore.GREEN + 'R1: ' + Style.RESET_ALL, R1)
    print(Fore.GREEN + 'R2: ' + Style.RESET_ALL, R2)
    print(Fore.GREEN + 'R3: ' + Style.RESET_ALL, R3)
    print(Fore.YELLOW + '-'*100 + Style.RESET_ALL)
    
    
    