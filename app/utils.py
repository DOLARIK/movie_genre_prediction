from transformers import BertTokenizer
from cmu_movie_dataset.plot_summary_genre.utils import clean_plot_summary

def tokenize_plots(list_of_plots,
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

def pre_process_plot_summaries(plots,   
					  max_length = 200,
				      padding = 'max_length',
				      truncation = True,
				      return_tensors = 'tf'):

    cleaned_plot_summaries = [clean_plot_summary(plot) for plot in plots]
    tokenized_plots = tokenize_plots(cleaned_plot_summaries, 
    	                             max_length=max_length,
    	                             padding=padding,
    	                             truncation=truncation,
    	                             return_tensors=return_tensors)

    input_ids = tokenized_plots[0]
    attention_masks = tokenized_plots[1]
    token_type_ids = tokenized_plots[2]

    pre_processed_plot_summaries = {
			    "inputs" : input_ids.numpy().tolist(),
			    "attention_mask" : attention_masks.numpy().tolist(),
			    "token_type_ids" : token_type_ids.numpy().tolist()
    }

	return pre_processed_plot_summaries
