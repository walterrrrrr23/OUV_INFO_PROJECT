
import pygame

def load_spritesheet(path, frame_width, frame_height):
    sheet = pygame.image.load(path).convert_alpha()
    sheet_width, sheet_height = sheet.get_size()
    
    frames = []
    rows = sheet_height // frame_height
    cols = sheet_width // frame_width
    
    for y in range(rows):
        row = []
        for x in range(cols):
            rect = pygame.Rect(x*frame_width, y*frame_height, frame_width, frame_height)
            row.append(sheet.subsurface(rect))
        frames.append(row)
    return frames
