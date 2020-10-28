textarea = document.querySelector("#plotSummary");
textarea.addEventListener('input', autoResize, false);

function autoResize() {
    this.style.height = 'auto';
    this.style.height = this.scrollHeight + 'px';
}

async function predictFunction() {

	var plotSummary = document.getElementById('plotSummary').value

	let data = {
		'plot_summary': plotSummary
	}
	
	const response = await fetch('http://192.168.1.12:5000/genre', {
		method: 'POST',
		mode: 'cors',
	    headers: {
	    	"Content-Type": "application/json"
	    }, 
		body: JSON.stringify(data),
	})
	.then(response => {return response.json()})

	var results = document.getElementById('genres')

	// list-group-item-dark
	var genreResults = `<li class="list-group-item list-group-item-primary">Genres</li>`

	if (response['genres'].length > 0){
	
		for (var genre of response['genres']){
				genreResults = genreResults + `<li class="list-group-item">${genre}</li>`
			}
	}
	else{
		genreResults = genreResults + `<li class="list-group-item">None</li>`
	}

	results.innerHTML = '<ul class="list-group list-group-horizontal-xl">' + genreResults + '</ul>'
}

const predict = document.getElementById('predict');
predict.addEventListener('click', predictFunction);