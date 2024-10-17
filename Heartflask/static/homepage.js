document.addEventListener('DOMContentLoaded', () => {
    const predictButton = document.querySelector('.predict-btn');

    // Adding a single event listener to the predict button
    predictButton.addEventListener('click', () => {
        // Optional: Show an alert (remove this line if not needed)
        alert("Predict button clicked! Redirecting to prediction functionality...");

        // Redirect to the prediction page
        window.location.href = '/predict';  // Change this to the correct path for your predict.html page
    });
});
