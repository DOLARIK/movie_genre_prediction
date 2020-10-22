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

	var genreResults = ""

	for (var genre of response['genres']){
			genreResults = genreResults + `<li class="list-group-item">${genre}</li>`
		}
	results.innerHTML = '<ul class="list-group list-group-horizontal">' + genreResults + '</ul>'
}

const predict = document.getElementById('predict');
predict.addEventListener('click', predictFunction);