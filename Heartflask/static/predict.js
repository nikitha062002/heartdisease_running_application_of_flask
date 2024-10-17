document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const data = {};

    formData.forEach((value, key) => {
        data[key] = value;
    });

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)  // Send the data as JSON
    })
    .then(response => response.json())
    .then(prediction => {
        const queryParams = new URLSearchParams({
            heart_disease: prediction.heart_disease,
            probability: prediction.probability
        }).toString();
        window.location.href = `predicted?${queryParams}`;
    })
    .catch(error => console.error('Error:', error));
});
