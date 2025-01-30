# Using-Fine-Tuned-LLMs-to-Generate-Recipes-from-Ingredients

As international students we face the daily challenge of deciding what to cook for dinner. The idea for this project stemmed from this very own challenge and the main objective is to output meaningful and practical recipes using the ingredients available. This project fine-tunes the T5 transformer model on recipe data for generating recipes from a list of ingredients. The trained model can be deployed via a Flask web application. This project is still in development stage and more features will be added.

---
## ✨ Features
- Fine-tune the T5 transformer model on recipe datasets.
- Generate recipes based on a list of ingredients.
- Deploy the model as a Flask web app for user interaction.

🎓 Training the Model
The model was fine-tuned on the RecipeNLG dataset.

Steps:
Prepare the Dataset

Tokenize the training and testing datasets.
Save the tokenized data in .csv files for reuse.
Fine-Tune T5 Use the following script to fine-tune the T5 model

🌐 Using the Flask Web App
Run the Flask App
Download the Fine-Tuned Model

Ensure your fine-tuned model is downloaded and placed in the project directory.
Start the Flask App Run the Flask server
Input Ingredients Enter a list of ingredients, and the app will generate a recipe using the fine-tuned model.

🌟 Future Improvements
Use a more advanced model like T5-3B for better recipe generation.
Improve the UI using a frontend framework like React.
Add support for multi-cuisine recipe generation.
Deploy the app using a cloud service (e.g., AWS, GCP, or Heroku).

🛠️ Tech Stack
Programming Language: Python
Libraries: PyTorch, Transformers, Flask
Dataset: RecipeNLG
