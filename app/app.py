from flask import Flask, request, jsonify
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
model = T5ForConditionalGeneration.from_pretrained("fine_tuned_t5").to(device)
tokenizer = T5Tokenizer.from_pretrained("fine_tuned_t5")

#initializing the flask app
app = Flask(__name__)
@app.route("/", methods=["GET"])
def home():
    return "Recipe Generation App is Running!"

@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    data = request.json
    ingredients = data.get('ingredients')
    if not ingredients:
        return jsonify({'error' : 'No ingredients provided'})
    
    input_text = f"Ingredients: {', '.join(ingredients.split(','))}"
    input_ids = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True, max_length=512).input_ids.to(device)

    with torch.no_grad():
        outputs = model.generate(input_ids, max_length=512, num_beams=4, early_stopping=True)
    recipe = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({'recipe': recipe})
if __name__ == '__main__':
    app.run(debug=True)

    
