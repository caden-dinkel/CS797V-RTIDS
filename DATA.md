# Data Preprocessing and Embedding

1. Transform non-numerical data to numberical (Checkout research article for options)
    a. Based on the procedure stated in the paper:

    "Unlike other machine learning models, our method aim to retain as many features as possible for the purpose of accuracy improvement, the self-attention mechanism in our model can select features automatically. We transform all the symbolic features contained in the datasets into numerical values."

    Check out conversions at: https://www.kaggle.com/code/filipekoriginal/cicids2017-preprocessing

2. Normalize Data to [0,1] using the method:

    x_norm = (x_actual - min_x_train) / (max_x_train - min_x_train)

    -- Min-Max Normalization Technique

3. Split into Training (70%), Testing (15%), Validation (15%)
