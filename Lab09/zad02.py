from PIL import Image, ImageEnhance
import multiprocessing

BRIGHTNESS_FACTOR = 1.5
NUM_PROCESSES = 4

def adjust_brightness(image_part_bytes):
    image_part = Image.frombytes('RGB', image_part_bytes['size'], image_part_bytes['data'])
    enhancer = ImageEnhance.Brightness(image_part)
    brighter_part = enhancer.enhance(BRIGHTNESS_FACTOR)
    return brighter_part.tobytes()

def main():
    input_path = 'input.jpg'
    output_path = 'output.jpg'

    image = Image.open(input_path).convert('RGB')
    width, height = image.size

    part_width = width // NUM_PROCESSES
    parts = []

    for i in range(NUM_PROCESSES):
        left = i * part_width
        right = (i + 1) * part_width if i != NUM_PROCESSES - 1 else width
        box = (left, 0, right, height)
        part = image.crop(box)
        parts.append({
            'data': part.tobytes(),
            'size': part.size
        })

    with multiprocessing.Pool(NUM_PROCESSES) as pool:
        results = pool.map(adjust_brightness, parts)

    new_image = Image.new('RGB', (width, height))
    x_offset = 0
    for i, part_bytes in enumerate(results):
        part_width, part_height = parts[i]['size']
        part_image = Image.frombytes('RGB', (part_width, part_height), part_bytes)
        new_image.paste(part_image, (x_offset, 0))
        x_offset += part_width

    new_image.save(output_path)
    print("Obraz został przetworzony i zapisany jako:", output_path)

if __name__ == '__main__':
    main()
