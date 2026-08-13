# Computer Addon Texture Guide

## Texture Specifications

All textures should be 16x16 pixels (standard Minecraft block size).

### CPU Block Texture (cpu_block.png)
- **Base Color**: Dark Brown (#654321)
- **Details**: Gold/Yellow circuit patterns (#FFD700)
- **Pattern**: Grid-like circuits across the surface
- **Style**: Tech/computer aesthetic

### RAM Block Texture (ram_block.png)
- **Base Color**: Dark Gray (#2F4F4F)
- **Details**: Green LEDs (#00FF00) or blue accents (#0099FF)
- **Pattern**: Vertical lines representing memory chips
- **Style**: Circuit board look

### Storage Block Texture (storage_block.png)
- **Base Color**: Metallic Silver (#C0C0C0)
- **Details**: Black lines (#000000) for sections
- **Pattern**: Segmented/divided squares
- **Style**: Hard drive platter appearance

### GPU Block Texture (gpu_block.png)
- **Base Color**: Dark Blue (#001F3F)
- **Details**: Green circuit lines (#00FF00)
- **Pattern**: Complex circuit board with traces
- **Style**: Advanced technology look

### Motherboard Texture (motherboard.json)
- **Base Color**: Olive/Dark Green (#2D5016)
- **Details**: Gold traces (#FFD700) and copper (#B87333)
- **Pattern**: PCB trace patterns, various sized contacts
- **Style**: Real motherboard aesthetic

### Power Supply Texture (power_supply.png)
- **Base Color**: Black (#000000) or Dark Gray (#333333)
- **Details**: Orange vents (#FF8C00) or red warning stripes (#FF0000)
- **Pattern**: Cooling vents, warning labels
- **Style**: Industrial power supply

### Cooling System Texture (cooling_system.png)
- **Base Color**: Metallic Silver (#C0C0C0)
- **Details**: Blue liquid (#0099FF) or ice blue (#00CCFF)
- **Pattern**: Radiator fins, tubing
- **Style**: High-end cooling aesthetic

## How to Create These

### Option 1: Using Blockbench (Recommended)
1. Download Blockbench: https://blockbench.net/
2. Create a new Minecraft block model
3. Paint textures directly in the program
4. Export as Minecraft addon format

### Option 2: Using Online Pixel Art Tools
- Piskel.app - Free browser-based pixel art editor
- Aseprite - Professional pixel art tool
- Paint.NET - Free and easy

### Option 3: Using AI Image Generation
- DALL-E: "16x16 pixel art texture of a CPU chip in minecraft style"
- Midjourney: "/imagine minecraft cpu block texture"
- Stable Diffusion: Use similar prompts

### Option 4: Using Python (PIL/Pillow)
```python
from PIL import Image, ImageDraw

# Create a 16x16 image
img = Image.new('RGB', (16, 16), color='#654321')  # CPU brown color
draw = ImageDraw.Draw(img)

# Add circuit patterns
for i in range(0, 16, 4):
    draw.line([(i, 0), (i, 16)], fill='#FFD700')
    draw.line([(0, i), (16, i)], fill='#FFD700')

img.save('cpu_block.png')
```

## File Locations
All textures should go in: `resource_pack/textures/blocks/`

Make sure the filenames match exactly what's referenced in the block JSON files!
