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
			genreResults = genreResults + `<li>${genre}</li>`
		}
	results.innerHTML = genreResults
}

const predict = document.getElementById('predict');
predict.addEventListener('click', predictFunction);