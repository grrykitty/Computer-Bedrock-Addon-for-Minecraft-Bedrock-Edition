#!/usr/bin/env python3
"""
Generate PNG textures for Computer Bedrock Addon
Run this script to create all 16x16 pixel textures for PC components
"""

from PIL import Image, ImageDraw
import os

# Create textures directory if it doesn't exist
os.makedirs('resource_pack/textures/blocks', exist_ok=True)

def create_cpu_block():
    """CPU Block - Dark brown with gold circuit patterns"""
    img = Image.new('RGB', (16, 16), color='#654321')
    draw = ImageDraw.Draw(img)
    
    # Circuit grid lines (gold)
    for i in range(0, 16, 4):
        draw.line([(i, 0), (i, 16)], fill='#FFD700', width=1)
        draw.line([(0, i), (16, i)], fill='#FFD700', width=1)
    
    # Add some dots for circuit nodes
    for x in range(2, 16, 4):
        for y in range(2, 16, 4):
            draw.rectangle([x-1, y-1, x+1, y+1], fill='#FFA500')
    
    img.save('resource_pack/textures/blocks/cpu_block.png')
    print("✓ Created cpu_block.png")

def create_ram_block():
    """RAM Block - Dark gray with blue accents and LED patterns"""
    img = Image.new('RGB', (16, 16), color='#2F4F4F')
    draw = ImageDraw.Draw(img)
    
    # Vertical memory chip lines
    for x in range(2, 16, 3):
        draw.line([(x, 0), (x, 16)], fill='#404040', width=1)
    
    # Blue LED indicators
    for y in range(3, 16, 4):
        draw.rectangle([1, y, 3, y+1], fill='#0099FF')
        draw.rectangle([13, y, 15, y+1], fill='#0099FF')
    
    # White highlight
    draw.line([(0, 0), (16, 0)], fill='#FFFFFF', width=1)
    
    img.save('resource_pack/textures/blocks/ram_block.png')
    print("✓ Created ram_block.png")

def create_storage_block():
    """Storage Block - Silver with segmented sections"""
    img = Image.new('RGB', (16, 16), color='#C0C0C0')
    draw = ImageDraw.Draw(img)
    
    # Black dividing lines
    draw.line([(0, 8), (16, 8)], fill='#000000', width=1)
    draw.line([(8, 0), (8, 16)], fill='#000000', width=1)
    
    # Internal grid pattern
    for i in range(4, 16, 4):
        draw.line([(i, 0), (i, 16)], fill='#808080', width=1)
        draw.line([(0, i), (16, i)], fill='#808080', width=1)
    
    # Highlight edge
    draw.line([(0, 0), (0, 16)], fill='#FFFFFF', width=1)
    
    img.save('resource_pack/textures/blocks/storage_block.png')
    print("✓ Created storage_block.png")

def create_gpu_block():
    """GPU Block - Dark blue with green circuit traces"""
    img = Image.new('RGB', (16, 16), color='#001F3F')
    draw = ImageDraw.Draw(img)
    
    # Complex circuit trace pattern
    draw.line([(2, 2), (14, 2)], fill='#00FF00', width=1)
    draw.line([(14, 2), (14, 14)], fill='#00FF00', width=1)
    draw.line([(14, 14), (2, 14)], fill='#00FF00', width=1)
    draw.line([(2, 14), (2, 2)], fill='#00FF00', width=1)
    
    # Internal traces
    draw.line([(2, 8), (14, 8)], fill='#00DD00', width=1)
    draw.line([(8, 2), (8, 14)], fill='#00DD00', width=1)
    
    # Contact points
    for x in range(4, 14, 3):
        for y in range(4, 14, 3):
            draw.rectangle([x-1, y-1, x+1, y+1], fill='#00FF00')
    
    img.save('resource_pack/textures/blocks/gpu_block.png')
    print("✓ Created gpu_block.png")

def create_motherboard():
    """Motherboard - Olive green with gold traces"""
    img = Image.new('RGB', (16, 16), color='#2D5016')
    draw = ImageDraw.Draw(img)
    
    # Gold PCB traces
    draw.line([(2, 2), (14, 2)], fill='#FFD700', width=1)
    draw.line([(2, 8), (14, 8)], fill='#FFD700', width=1)
    draw.line([(2, 14), (14, 14)], fill='#FFD700', width=1)
    draw.line([(2, 2), (2, 14)], fill='#FFD700', width=1)
    draw.line([(14, 2), (14, 14)], fill='#FFD700', width=1)
    draw.line([(8, 2), (8, 14)], fill='#FFD700', width=1)
    
    # Copper contacts
    for x in range(3, 15, 4):
        for y in range(3, 15, 4):
            draw.rectangle([x-1, y-1, x+1, y+1], fill='#B87333')
    
    img.save('resource_pack/textures/blocks/motherboard.png')
    print("✓ Created motherboard.png")

def create_power_supply():
    """Power Supply - Black with orange cooling vents"""
    img = Image.new('RGB', (16, 16), color='#1a1a1a')
    draw = ImageDraw.Draw(img)
    
    # Cooling vents
    for y in range(2, 16, 2):
        draw.line([(2, y), (14, y)], fill='#FF8C00', width=1)
    
    # Central highlight panel
    draw.rectangle([4, 4, 12, 12], outline='#FFD700', width=1)
    
    # Warning stripes (red)
    for i in range(5, 11, 2):
        draw.line([(i, 5), (i+1, 11)], fill='#FF0000', width=1)
    
    img.save('resource_pack/textures/blocks/power_supply.png')
    print("✓ Created power_supply.png")

def create_cooling_system():
    """Cooling System - Silver with blue liquid look"""
    img = Image.new('RGB', (16, 16), color='#C0C0C0')
    draw = ImageDraw.Draw(img)
    
    # Radiator fins
    for y in range(1, 16, 2):
        draw.line([(1, y), (15, y)], fill='#8B8B8B', width=1)
    
    # Tubing/liquid flow (blue)
    draw.line([(2, 4), (14, 4)], fill='#0099FF', width=2)
    draw.line([(2, 12), (14, 12)], fill='#0099FF', width=2)
    draw.line([(4, 4), (4, 12)], fill='#0099FF', width=1)
    draw.line([(12, 4), (12, 12)], fill='#0099FF', width=1)
    
    # Highlight
    draw.line([(0, 0), (16, 0)], fill='#FFFFFF', width=1)
    
    img.save('resource_pack/textures/blocks/cooling_system.png')
    print("✓ Created cooling_system.png")

if __name__ == '__main__':
    print("Generating Computer Addon textures...\n")
    
    create_cpu_block()
    create_ram_block()
    create_storage_block()
    create_gpu_block()
    create_motherboard()
    create_power_supply()
    create_cooling_system()
    
    print("\n✓ All textures generated successfully!")
    print("Location: resource_pack/textures/blocks/")
