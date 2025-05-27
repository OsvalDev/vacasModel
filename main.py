from ultralytics import YOLO
import cv2
import sys
import os
from pathlib import Path
from datetime import datetime

def process_image(image_path, model, display_width=700, display_height=600):
    image = cv2.imread(image_path)
    if image is None:
        return None, 0
    
    results = model(image, conf=0.6)
    
    h, w = image.shape[:2]
    
    scale_factor = min(display_width/w, display_height/h)
    resized_w = int(w * scale_factor)
    resized_h = int(h * scale_factor)
    resized_image = cv2.resize(image, (resized_w, resized_h))
    
    boxes = results[0].boxes.xyxy.cpu().numpy()
    num_boxes = len(boxes)
    
    for box in boxes:
        x1, y1, x2, y2 = box
        x1 = int(x1 * scale_factor)
        y1 = int(y1 * scale_factor)
        x2 = int(x2 * scale_factor)
        y2 = int(y2 * scale_factor)
        cv2.rectangle(resized_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    if resized_w < display_width or resized_h < display_height:
        top = (display_height - resized_h) // 2
        bottom = display_height - resized_h - top
        left = (display_width - resized_w) // 2
        right = display_width - resized_w - left
        resized_image = cv2.copyMakeBorder(resized_image, 
                                         top, bottom, left, right, 
                                         cv2.BORDER_CONSTANT, 
                                         value=[0, 0, 0])
    
    cv2.putText(resized_image, f'Objetos: {num_boxes}', (10, 30), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    return resized_image, num_boxes

def handle_directory(directory_path, model):
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp')
    image_paths = [os.path.join(directory_path, f) 
                   for f in sorted(os.listdir(directory_path)) 
                   if f.lower().endswith(image_extensions)]

    if not image_paths:
        print("No se encontraron imágenes en el directorio")
        return

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_dir = os.path.join(os.path.dirname(__file__), "outputs")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"resultados_{timestamp}.txt")

    with open(output_path, "w") as f:
        for idx, image_path in enumerate(image_paths):
            _, num_boxes = process_image(image_path, model)
            image_name = os.path.basename(image_path)
            f.write(f"{image_name}: {num_boxes} cows\n")
            print(f"{image_name}: {num_boxes} cows")

    print(f"\n Resultados guardados en: {output_path}")


def handle_single_image(image_path, model):
    _, num_boxes = process_image(image_path, model)
    image_name = os.path.basename(image_path)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_dir = os.path.join(os.path.dirname(__file__), "outputs")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"resultados_{timestamp}.txt")

    with open(output_path, "w") as f:
        f.write(f"{image_name}: {num_boxes} cows\n")

    print(f"{image_name}: {num_boxes} cows")
    print(f"\n Resultados guardados en: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <ruta_imagen_o_directorio>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    model = YOLO('bestGeneral.pt')
    
    if os.path.isfile(input_path):
        handle_single_image(input_path, model)
    elif os.path.isdir(input_path):
        handle_directory(input_path, model)
    else:
        print("Ruta no válida")
        sys.exit(1)