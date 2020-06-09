import os
import torch
import torch.nn.functional as F
from transformers import BertTokenizer, cached_path
from training.transformer_utils.model import TransformerWithClfHeadAndAdapters


def transformer_score(texts):
    model_path = "models/transformer"
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    config = torch.load(cached_path(os.path.join(model_path, "model_training_args.bin")))
    model = TransformerWithClfHeadAndAdapters(config["config"],
                                              config["config_ft"]).to(device)
    state_dict = torch.load(cached_path(os.path.join(model_path, "model_weights.pth")),
                            map_location=device)

    model.load_state_dict(state_dict)  # Load model state dict
    tokenizer = BertTokenizer.from_pretrained('bert-base-cased', do_lower_case=False)  # Load tokenizer

    clf_token = tokenizer.vocab['[CLS]']  # classifier token
    pad_token = tokenizer.vocab['[PAD]']  # pad token

    max_length = config['config'].num_max_positions

    def encode(i):
        # Encode text as IDs using the BertTokenizer
        return list(tokenizer.convert_tokens_to_ids(o) for o in i)

    scores = []
    for text in texts:
        inputs = tokenizer.tokenize(text)
        if len(inputs) >= max_length:
            inputs = inputs[:max_length - 1]
        ids = encode(inputs) + [clf_token]

        model.eval()  # Disable dropout
        with torch.no_grad():  # Disable backprop
            tensor = torch.tensor(ids, dtype=torch.long).to(device)
            tensor_reshaped = tensor.reshape(1, -1)
            tensor_in = tensor_reshaped.transpose(0, 1).contiguous()  # to shape [seq length, 1]
            logits = model(tensor_in,
                           clf_tokens_mask=(tensor_in == clf_token),
                           padding_mask=(tensor_reshaped == pad_token))

        val, _ = torch.max(logits, 0)
        val = F.softmax(val, dim=0).detach().cpu().numpy()

        pred = int(val.argmax()) + 1
        if pred == 1:
            pred = "Very Negative"
        elif pred == 2:
            pred = "Slightly Negative"
        elif pred == 3:
            pred = "Neutral"
        elif pred == 4:
            pred = "Slightly Positive"
        elif pred == 5:
            pred = "Very Positive"
        scores.append(pred)
    return scores
