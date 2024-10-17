// Function to get query parameters
function getQueryParams() {
    const params = {};
    window.location.search.substring(1).split('&').forEach(pair => {
        const [key, value] = pair.split('=');
        params[decodeURIComponent(key)] = decodeURIComponent(value);
    });
    return params;
}

// Display the prediction results
const params = getQueryParams();
document.getElementById('results').innerHTML = `
    <p>Heart Disease: ${params.heart_disease === '1' ? 'Yes' : 'No'}</p>
    <p>Probability: ${params.probability}%</p>
`;
