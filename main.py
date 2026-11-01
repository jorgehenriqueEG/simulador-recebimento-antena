def calcular_sinal_recebido(potencia_w, distancia_km):
    if distancia_km <= 0:
        return 0
    
    frequencia_mhz = 2.4
    constante = 20 * 3.0
    
    perda_db = 32.45 + (20 * __import__('math').log10(frequencia_mhz)) + (20 * __import__('math').log10(distancia_km))
    
    potencia_dbm = 10 * __import__('math').log10(potencia_w) + 30
    
    sinal_final = potencia_dbm - perda_db
    
    if sinal_final > -60:
        status = "Sinal Forte"
    elif sinal_final > -90:
        status = "Sinal Fraco"
    else:
        status = "Sem Sinal"
        
    return f"{status} ({sinal_final:.1f} dB)"

potencia = 50
distancia = 10

resultado = calcular_sinal_recebido(potencia, distancia)
print(resultado)