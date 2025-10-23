from PIL import Image, ImageDraw, ImageFont
import tempfile


def create_output_image(output_text):
    """Create a temporary image with black background and white text for output.
    
    This is a general-purpose utility that works with any text content.
    
    Args:
        output_text (str): The text to display on black background
        
    Returns:
        str: Path to the temporary PNG image file
    """
    # Set up text properties
    font_size = 14
    padding = 20
    line_spacing = 5
    
    # Try to use a monospace font, fall back to default if not available
    try:
        font = ImageFont.truetype("consola.ttf", font_size)  # Consolas on Windows
    except:
        try:
            font = ImageFont.truetype("Courier New.ttf", font_size)
        except:
            try:
                font = ImageFont.truetype("cour.ttf", font_size)
            except:
                font = ImageFont.load_default()
    
    # Split text into lines
    lines = output_text.split('\n')
    if not lines or (len(lines) == 1 and not lines[0].strip()):
        lines = ["(No output)"]
    
    # Calculate image dimensions
    # Use a dummy image to measure text
    dummy_img = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(dummy_img)
    
    max_width = 0
    total_height = 0
    
    for line in lines:
        if not line:  # Empty line
            line = " "
        bbox = draw.textbbox((0, 0), line, font=font)
        line_width = bbox[2] - bbox[0]
        line_height = bbox[3] - bbox[1]
        max_width = max(max_width, line_width)
        total_height += line_height + line_spacing
    
    # Add padding
    img_width = max_width + (padding * 2)
    img_height = total_height + (padding * 2)
    
    # Ensure minimum size
    img_width = max(img_width, 400)
    img_height = max(img_height, 100)
    
    # Create the actual image with black background
    image = Image.new('RGB', (img_width, img_height), color='black')
    draw = ImageDraw.Draw(image)
    
    # Draw text in white
    y_position = padding
    for line in lines:
        if not line:
            line = " "
        draw.text((padding, y_position), line, fill='white', font=font)
        bbox = draw.textbbox((0, 0), line, font=font)
        line_height = bbox[3] - bbox[1]
        y_position += line_height + line_spacing
    
    # Save to temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    image.save(temp_file.name, 'PNG')
    temp_file.close()
    
    return temp_file.name