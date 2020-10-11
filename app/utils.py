from transformers import BertTokenizer

def tokenize_plots(list_of_plots
				   max_length = 200,
				   padding = 'max_length',
				   truncation = True,
				   return_tensors = 'tf'):
	tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
	return tokenizer(list_of_plots, 
					 max_length = max_length, 
					 padding = padding,
					 truncation = truncation,
					 return_tensors = return_tensors, 
					 )


def genre_from_indices(indices, indices_genre_mapping):
	return [indices_genre_mapping[index] for index in indices]
