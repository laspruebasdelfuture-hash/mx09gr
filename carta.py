from flask import Flask, render_template_string, request
import datetime

app = Flask(__name__)

# Plantilla con Pantalla de Seguridad + Carta de Amor
PLANTILLA_AMOR = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Para ti ❤️</title>
    <style>
        /* ===== ESTILOS DE LA TERMINAL DE SEGURIDAD ===== */
        #pantalla-entrada {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-color: #000000;
            color: #00ff00;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            transition: opacity 1.5s ease;
            font-family: monospace;
        }
        
        /* Diseño de la caja de contraseña tipo hacker */
        #input-pass {
            background-color: black;
            color: #00ff00;
            border: 1px solid #00ff00;
            padding: 10px;
            font-size: 18px;
            margin: 20px;
            text-align: center;
            font-family: monospace;
            outline: none;
        }

        #boton-verificar {
            background-color: #00ff00;
            color: black;
            border: none;
            padding: 10px 20px;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
            font-family: monospace;
        }

        #boton-verificar:hover {
            background-color: white;
        }

        .ocultar { opacity: 0; pointer-events: none; }
        
        /* ===== ESTILOS DE LA CARTA ===== */
        body {
            background-color: #ffe6ea;
            font-family: 'Arial', sans-serif;
            text-align: center;
            margin-top: 50px;
            overflow-x: hidden;
        }
        @keyframes aparecer {
            from { opacity: 0; transform: translateY(40px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes latido {
            0% { transform: scale(1); }
            50% { transform: scale(1.08); }
            100% { transform: scale(1); }
        }
        .tarjeta {
            background-color: white;
            border-radius: 20px;
            padding: 30px;
            width: 90%;
            max-width: 400px;
            margin: 0 auto;
            box-shadow: 0px 10px 20px rgba(0,0,0,0.1);
            animation: aparecer 1.5s ease-out; 
        }
        h1 { color: #d63031; animation: latido 2s infinite; }
        p { color: #2d3436; font-size: 18px; line-height: 1.6; }
        .foto-pareja { width: 100%; border-radius: 15px; margin-bottom: 15px; }
    </style>
</head>
<body>
    <!-- INTERFAZ DE ENTRADA CON CONTRASEÑA -->
    <div id="pantalla-entrada">
        <h2 id="texto-terminal">SISTEMA BLOQUEADO. Ingrese clave de acceso:</h2>
        <!-- Caja para escribir la contraseña -->
        <input type="password" id="input-pass" placeholder="Contraseña..." onkeypress="revisarEnter(event)">
        <button id="boton-verificar" onclick="verificarSeguridad()">Acceder</button>
    </div>

    <!-- LA CARTA REAL -->
    <div class="tarjeta">
        <h1>Sistema de Amor Iniciado</h1>
        <img class="foto-pareja" src="https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=500" alt="Nuestra foto">
        <p>Conectando con el corazón de <strong>[Su Nombre Aquí]</strong>...</p>
        <p>❤️ <strong>Carga completada al 300%</strong> ❤️</p>
        <p><strong>Estado del sistema:</strong> Completamente enamorado.</p>
        <p><strong>Motivo:</strong> Tienes la sonrisa más bonita de todo mi servidor.</p>
        <p><strong>Error 404:</strong> Tristeza no encontrada cuando estoy contigo.</p>
        <br>
        <p><em>Bucle: Prometo quererte en cada línea de código de mi vida.</em></p>
    </div>

    <!-- SCRIPT DE SEGURIDAD -->
    <script>
        // Permite presionar la tecla Enter en lugar de darle clic al botón
        function revisarEnter(event) {
            if (event.key === "Enter") {
                verificarSeguridad();
            }
        }

        function verificarSeguridad() {
            // Obtenemos lo que escribió y lo pasamos a minúsculas para que no importen las mayúsculas
            let claveIngresada = document.getElementById('input-pass').value.toLowerCase();
            let textoTerminal = document.getElementById('texto-terminal');
            
            // === AQUÍ CONFIGURAS TU CONTRASEÑA SECRETA ===
            // Puedes poner una fecha, su nombre o una frase (puedes usar palabras en inglés también si prefieres)
            if (claveIngresada === "te amo" || claveIngresada === "iloveyou" || claveIngresada === "1402") { 
                
                textoTerminal.innerText = "Contraseña correcta. Desencriptando archivos...";
                textoTerminal.style.color = "#00ff00"; // Verde
                
                // Ocultamos la caja de texto y el botón
                document.getElementById('input-pass').style.display = "none";
                document.getElementById('boton-verificar').style.display = "none";
                
                // Esperamos 2 segundos para dar el efecto de carga y revelamos la carta
                setTimeout(function() {
                    document.getElementById('pantalla-entrada').classList.add('ocultar');
                }, 2000);
                
            } else {
                // Si la contraseña es incorrecta
                textoTerminal.innerText = "[!] ALERTA: ACCESO DENEGADO [!]";
                textoTerminal.style.color = "red"; // Rojo
                
                // Vaciamos la caja de texto
                document.getElementById('input-pass').value = "";
                
                // Después de 1.5 segundos, vuelve al texto original
                setTimeout(function() {
                    textoTerminal.innerText = "SISTEMA BLOQUEADO. Ingrese clave de acceso:";
                    textoTerminal.style.color = "#00ff00"; // Vuelve a verde
                }, 1500);
            }
        }
    </script>
</body>
</html>
'''

@app.route('/')
def inicio():
    # Sistema de rastreo de IPs intacto
    ip_visitante = request.headers.get('X-Forwarded-For', request.remote_addr)
    hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    registro = f"[{hora_actual}] Visita detectada - IP: {ip_visitante}\n"
    
    with open("registro_ips.txt", "a") as archivo:
        archivo.write(registro)
        
    print(f"\n\033[91m[!] ALERTA HACKER: Nueva conexión detectada desde la IP {ip_visitante}\033[0m\n")

    return render_template_string(PLANTILLA_AMOR)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)