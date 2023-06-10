from PIL import Image

frames = []

for num in range(1, 10):
    frame = Image.open(f'image/homer-{num}.jpg')
    frames.append(frame)

frames[0].save(
    'homer.gif',
    save_all=True,
    append_images=frames[1:],
    optimize=True,
    duration=100,
    loop=0
)