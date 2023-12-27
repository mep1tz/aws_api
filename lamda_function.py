import json, base64
from PIL import Image
from io import BytesIO

def lambda_handler(event, context):
    # TODO implement
    content = event.get('queryStringParameters', {})
    
    width=int(content.get('width', 100))
    height=int(content.get('height', 100))
    color=content.get('color', 'RED')
    
    image = Image.new('RGB', (width, height), color=color)

    # Convert image to base64 string
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    base64_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # TODO: write code...
    return {
            'headers': { "Content-Type": "image/png" },
            'statusCode': 200,
            'body': base64_image,
            'isBase64Encoded': True
        }