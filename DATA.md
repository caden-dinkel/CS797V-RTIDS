# Data Preprocessing and Embedding

Based on the paper, my belief is that the paper authors legitimately converted every single non-numerical data point into numerical values, and then normalized them on [0,1].

This isn't great from an engineering standpoint, so I may try some additional processing.


1. Transform non-numerical data to numberical (Checkout research article for options)
    a. Based on the procedure stated in the paper:

    "Unlike other machine learning models, our method aim to retain as many features as possible for the purpose of accuracy improvement, the self-attention mechanism in our model can select features automatically. We transform all the symbolic features contained in the datasets into numerical values."

    Based on this statement, I assume a naive conversion directly to numbers using `pd.to_numeric(df['col'], errors='coerce').fillna(0)`

    This will result in a flat column of zeros after conversion. This is basically just wasting data.

    b. Attempt some other method of conversion:

    Could hash url strings into a fixed integer range, which will help keep them somewhat distinct from one another.

    IP Addrs can be decomposed into octets (I think that's what it's called)

2. Normalize Data to [0,1] using the method:

    x_norm = (x_actual - min_x_train) / (max_x_train - min_x_train)

    -- Min-Max Normalization Technique


3. Split into Training (70%), Testing (15%), Validation (15%)