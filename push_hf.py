from transformers import AutoModel
import sys

model = AutoModel.from_pretrained(sys.argv[1])

# Push the model to the Hugging Face Hub under the name "my-model".
model.push_to_hub(sys.argv[2], use_auth_token=True)