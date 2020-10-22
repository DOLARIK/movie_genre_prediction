async function predictFunction() {

	var plotSummary = document.getElementById('plotSummary').value

	let data = {
		'plot_summary': plotSummary
	}
	
	const response = await fetch('http://localhost:5000/genre', {
		method: 'POST',
	    headers: {
	    	"Content-Type": "application/json"
	    }, 
		body: JSON.stringify(data),
	})
	.then(response => {return response.json()})

	var results = document.getElementById('genres')

	results.innerHTML = response['genres']
}

const predict = document.getElementById('predict');
predict.addEventListener('click', predictFunction);