from fastapi import FastAPI, File, UploadFile
import numpy as np
import tensorflow as tf
from PIL import Image
import io
from tensorflow.keras.preprocessing import image
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import AsyncSessionLocal, get_db
from crud import get_food_info

app = FastAPI()

# Initialize the database
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Load the model once at startup
print("Loading TensorFlow model...")
model = tf.keras.models.load_model("food_classifier_inceptionv3_fine_tuned.keras")
class_names = ['apple_gpie', 'baby_back_ribs', 'baklava', 'beef_carpaccio',
                 'beef_tartare', 'beet_salad', 'beignets', 'bibimbap', 
                 'bread_pudding', 'breakfast_burrito', 'bruschetta', 
                 'caesar_salad', 'cannoli', 'caprese_salad', 'carrot_cake', 
                 'ceviche', 'cheese_plate', 'cheesecake', 'chicken_curry', 
                 'chicken_quesadilla', 'chicken_wings', 'chocolate_cake', 
                 'chocolate_mousse', 'churros', 'clam_chowder', 'club_sandwich', 
                 'crab_cakes', 'creme_brulee', 'croque_madame', 'cup_cakes', 
                 'deviled_eggs', 'donuts', 'dumplings', 'edamame', 'eggs_benedict', 
                 'escargots', 'falafel', 'filet_mignon', 'fish_and_chips', 
                 'foie_gras', 'french_fries', 'french_onion_soup', 'french_toast', 
                 'fried_calamari', 'fried_rice', 'frozen_yogurt', 'garlic_bread', 
                 'gnocchi', 'greek_salad', 'grilled_cheese_sandwich', 'grilled_salmon', 
                 'guacamole', 'gyoza', 'hamburger', 'hot_and_sour_soup', 'hot_dog', 
                 'huevos_rancheros', 'hummus', 'ice_cream', 'lasagna', 'lobster_bisque', 
                 'lobster_roll_sandwich', 'macaroni_and_cheese', 'macarons', 'miso_soup', 
                 'mussels', 'nachos', 'omelette', 'onion_rings', 'oysters', 'pad_thai', 
                 'paella', 'pancakes', 'panna_cotta', 'peking_duck', 'pho', 'pizza', 
                 'pork_chop', 'poutine', 'prime_rib', 'pulled_pork_sandwich', 'ramen', 
                 'ravioli', 'red_velvet_cake', 'risotto', 'samosa', 'sashimi', 'scallops', 
                 'seaweed_salad', 'shrimp_and_grits', 'spaghetti_bolognese', 
                 'spaghetti_carbonara', 'spring_rolls', 'steak', 'strawberry_shortcake', 
                 'sushi', 'tacos', 'takoyaki', 'tiramisu', 'tuna_tartare', 'waffles']
print("Model loaded successfully.")


@app.post("/predict/")
async def predict(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    image = image.resize((299, 299))

    # Convert to array
    image_array = np.array(image).astype("float32")
    image_array = image_array / 127.5 - 1
    processed_image = np.expand_dims(image_array, axis=0)

    # Perform inference
    predictions = model.predict(processed_image)
    predicted_label = class_names[np.argmax(predictions, axis=-1)[0]]

    # Query the db
    food_info = await get_food_info(db, predicted_label)

    if not food_info:
        raise HTTPException(status_code=404, detail="Food label not found")

    # Return food information
    return {
        "label": food_info.label,
        "calories": food_info.calories,
        "protein": food_info.protein,
        "carbohydrates": food_info.carbohydrates,
        "fats": food_info.fats,
        "fiber": food_info.fiber,
        "sugars": food_info.sugars,
        "sodium": food_info.sodium
    }

