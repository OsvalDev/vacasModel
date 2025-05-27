# 🐄 Detector de Vacas con YOLO y OpenCV

Este proyecto utiliza un modelo entrenado de YOLOv8 (`bestGeneral.pt`) para detectar vacas en imágenes o directorios completos de imágenes.

## 📦 Requisitos

- Python 3.8 o superior
- Sistema operativo: Raspberry Pi OS, Ubuntu o similar
- Dependencias:
  - `ultralytics`
  - `opencv-python`
  - `torch` (instalación depende de la arquitectura)

## 🚀 Instalación

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
    git clone https://github.com/TU_USUARIO/detector-vacas-yolo.git
    cd detector-vacas-yolo


🧠 ¿Cómo funciona?
El script toma como entrada una imagen o un directorio con imágenes. Detecta vacas usando un modelo YOLOv8 personalizado y guarda un archivo con el conteo de vacas detectadas

📸 Uso
1. **Detectar una sola imagen**
   ```bash
   python3 main.py ruta/a/la/imagen.jpg

2. **Detectar en todas las imágenes de un directorio**
   ```bash
   python3 main.py ruta/a/directorio/

## Resultado
Se genera un archivo dentro de la carpeta outputs/ con el nombre resultados_<timestamp>.txt, por ejemplo:

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
