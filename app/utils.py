import json
import requests
import numpy as np
from transformers import BertTokenizer
from cmu_movie_dataset.plot_summary_genre.utils import clean_plot_summary

API_URI = 'http://localhost:8501/v1/models/bert:predict'
INDICES_GENRE_MAPPING = load_genre_indices_mapping('./config/bert/2/indices_genre.json')
TOKENIZER = BertTokenizer.from_pretrained('bert-base-uncased')

MAX_LENGTH = 200
PADDING = 'max_length'
TRUNCATION = True

def load_genre_indices_mapping(path_to_mapping):
	with open(path_to_mapping) as f:
	  mapping = json.load(f)
	return mapping

def tokenize_plots(list_of_plots,
				   max_length = 200,
				   padding = 'max_length',
				   truncation = True,
				   return_tensors = 'tf'):
	tokenizer = TOKENIZER
	return tokenizer(list_of_plots, 
					 max_length = max_length, 
					 padding = padding,
					 truncation = truncation,
					 return_tensors = return_tensors, 
					 )

def pre_process_plot_summaries(plot,   
					  max_length = 200,
				      padding = 'max_length',
				      truncation = True,
				      return_tensors = 'tf'):

    cleaned_plot_summaries = [clean_plot_summary(plot)]
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

def make_api_call(pre_processed_plot_summaries):
	data = json.dumps({"signature_name": "serving_default", 
					   "inputs": pre_processed_plot_summaries})

	headers = {"content-type": "application/json"}
	json_response = requests.post(API_URI, data=data, headers=headers)

	return json.loads(json_response.text)

def post_process_api_predictions(prediction_dict,
								 threshold = 0.5):
	outputs = prediction_dict['outputs']
	outputs_boolean = np.asarray(outputs) > threshold

	indices_genre = INDICES_GENRE_MAPPING

	genres_list = []

	for output_id in range(len(output)):
		generes = [indices_genre[i] for i, x in enumerate(outputs[index]) if x]
		genres_list.append(genres)

	genres_dict = {
			'genres': genres_list
	}

	return genres_dict

def get_genre(plot_dict):
	plot_summary = plot_dict['plot_summary']
	pre_processed_plot_summary = pre_process_plot_summaries(plot_summary,
													max_length = MAX_LENGTH,
													padding = PADDING,
													truncation = TRUNCATION,
													return_tensors = RETURN_TENSORS)
	
	prediction_dict = make_api_call(pre_processed_plot_summary)
	genres_dict = post_process_api_predictions(prediction_dict)

	return genres_dict












	

