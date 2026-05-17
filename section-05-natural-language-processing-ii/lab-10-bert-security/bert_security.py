import pandas as pd
import torch
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from datasets import Dataset
from transformers import (
    BertTokenizer,
    BertForSequenceClassification,
    Trainer,
    TrainingArguments
)

# =========================
# Dataset
# =========================

data = {
    "malware_description": [
        "Trojan hides as legitimate software and infects system.",
        "Ransomware encrypts files and demands payment.",
        "Spyware steals user activity data silently.",
        "Adware shows unwanted advertisements on screen.",
        "Trojan spreads via phishing email attachments.",
        "Ransomware locks system until Bitcoin payment."
    ],
    "category": [0, 1, 2, 3, 0, 1]  # encoded labels
}

df = pd.DataFrame(data)

# =========================
# Tokenizer
# =========================

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

def tokenize(batch):
    return tokenizer(
        batch["malware_description"],
        padding="max_length",
        truncation=True,
        max_length=64
    )

dataset = Dataset.from_pandas(df)
dataset = dataset.map(tokenize, batched=True)
dataset = dataset.rename_column("category", "labels")
dataset.set_format("torch")

train_test = dataset.train_test_split(test_size=0.3)
train_dataset = train_test["train"]
test_dataset = train_test["test"]

# =========================
# Model
# =========================

model = BertForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=4
)

# =========================
# Training Args (lightweight for VM)
# =========================

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=1,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    logging_steps=2,
    evaluation_strategy="epoch",
    save_strategy="no"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset
)

# =========================
# Train Model
# =========================

trainer.train()

# =========================
# Evaluate Model
# =========================

results = trainer.evaluate()
print("\n===== MODEL RESULTS =====")
print(results)

# =========================
# Plot Loss (simple)
# =========================

log_history = trainer.state.log_history

train_loss = [x["loss"] for x in log_history if "loss" in x]
eval_loss = [x["eval_loss"] for x in log_history if "eval_loss" in x]

plt.plot(train_loss, label="Training Loss")
plt.plot(eval_loss, label="Validation Loss")
plt.title("BERT Training Performance")
plt.xlabel("Steps")
plt.ylabel("Loss")
plt.legend()

plt.savefig("bert_training_plot.png")

print("\nFiles Generated:")
print("- bert_training_plot.png")
