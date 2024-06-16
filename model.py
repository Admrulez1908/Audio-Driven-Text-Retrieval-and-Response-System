whisper_model = whisper.load_model("base.en")
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
llama_model_name = 'openlm-research/open_llama_3b'


import torch
llama_tokenizer = LlamaTokenizer.from_pretrained(llama_model_name)
llama_model = LlamaForCausalLM.from_pretrained(
    llama_model_name, torch_dtype=torch.float16, device_map='auto',
    offload_folder="offload"
)
