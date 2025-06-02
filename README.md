# 🐄 Detector de Vacas con YOLO

Este proyecto utiliza un modelo entrenado de YOLOv8 (`bestGeneral.pt`) para detectar vacas en imágenes o directorios completos de imágenes.

## Guia de instalacion y uso de dashboard
El archivo de readme con la instalacion del dashboard

## 📦 Requisitos

- Python 3.8 o superior
- Raspberry Pi (se recomienda modelo 4 con al menos 4 GB de RAM)
- Sistema operativo: Raspberry Pi OS, Ubuntu o distribucion basada en Debian. Windows.
- Dependencias:
  - `ultralytics`
  - `opencv-python`
  - `torch` (instalación depende de la arquitectura)

## 🚀 Instalación (Linux)

1. **Actualizar el sistema**
   ```bash
   sudo apt update && sudo apt upgrade

2. **Instalar Python y pip (si no están instalados)**
    ```bash
    sudo apt install python3 python3-pip

3. **Instalar dependencias**
⚠️ En Raspberry Pi, es mejor instalar torch de forma específica. Sigue los pasos de https://pytorch.org/get-started/locally/
Luego instala el resto:
    ```bash
    pip install ultralytics opencv-python

4. **Descargar el repositorio**
    ```bash
    git clone https://github.com/OsvalDev/vacasModel.git
    cd vacasModel

## 🚀 Instalación (Windows)

1. **Verificar la instalacion de Python**
   ```bash
   python --version

Al ejercutar el comando anterior se espera que se muestre en la consola la version que se tiene instalado de Python. En caso de no ser asi y se muestre algun error; entrar al siguiente enlace para la descarga, realizar la instalacion usando el archivo descargado de la pagina: https://www.python.org/downloads/
Una vez instalado, reiniciar la consola y verficiar la instalación.


2. **Crear un entorno virtual**
    ```bash
    python -m venv vacas

3. **Activar el entorno virtual**
    ```bash
    .\vacas\Scripts\activate

3. **Instalar dependencias**
Luego instala el resto:
    ```bash
    pip install ultralytics opencv-python torch torchvision torchaudio

4. **Descargar el repositorio**
    ```bash
    git clone https://github.com/OsvalDev/vacasModel.git
    cd vacasModel


🧠 ¿Cómo funciona?
El script toma como entrada una imagen o un directorio con imágenes. Detecta vacas usando un modelo YOLOv8 personalizado y guarda un archivo con el conteo de vacas detectadas

📸 Uso
La palabra reservada para la ejecucion depende de como se realizo la instalacion, pero se puede sustituir la palabra python por alguna de las siguientes: python, python3, py
1. **Detectar una sola imagen**
   ```bash
   python main.py ruta/a/la/imagen.jpg

2. **Detectar en todas las imágenes de un directorio**
   ```bash
   python main.py ruta/a/directorio/

## Resultado

*¿Dónde ver los resultados?*

1. El programa crea automáticamente una carpeta llamada outputs.
2. En caso de ya tener una carpeta de "outputs", se genera un archivo dentro de la carpeta outputs/ con el nombre resultados_timestamp.txt, por ejemplo:
    ```bash
    imagen1.jpg: 3 cows
    imagen2.jpg: 1 cows
    imagen3.jpg: 0 cows

🗂 Estructura del proyecto

```bash
detector-vacas-yolo/
├── bestGeneral.pt          # Modelo YOLOv8 personalizado
├── main.py                 # Script principal
├── outputs/                # Carpeta donde se guardan los resultados
└── README.md               # Este archivo
```

⚠️ **Solución de Problemas Comunes**
| Problema                      | Solución                                                                                  |
|------------------------------|-------------------------------------------------------------------------------------------|
| "No se encontró la imagen"   | Verifica que: 1) La foto esté en la carpeta correcta, 2) Escribiste bien el nombre        |
| "Error de módulos"           | Ejecuta: `pip install ultralytics opencv-python --force-reinstall`                        |
| Programa muy lento           | Usa fotos más pequeñas (menos de 2000x2000 píxeles)                                       |

## 📎**Anexo: Comandos Útiles**

| Comando                              | Para qué sirve                                      |
|-------------------------------------|-----------------------------------------------------|
| `ls`                                | Ver archivos en la carpeta actual                   |
| `cd nombre_carpeta`                 | Entrar a una carpeta                                |
| `python3 --version`                 | Ver versión de Python instalada                     |
| `scp foto.jpg pi@192.168.1.X:/ruta` | Enviar fotos desde tu PC a la Raspberry             |

