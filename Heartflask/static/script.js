// Object to hold existing accounts
let existingAccounts = {};

// Validate email format
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Toggle between login and signup forms
document.querySelector('.login-btn').addEventListener('click', function () {
    document.querySelector('.login-form').style.display = 'block';
});

// Handle user login
document.querySelector('#user-login-form').addEventListener('submit', function (e) {
    e.preventDefault();
    let email = document.querySelector('#user-email').value;
    let password = document.querySelector('#user-password').value;

    // Validate email format
    if (!validateEmail(email)) {
        alert('Please enter a valid email address.');
        return;
    }

    // Redirect to homepage
    window.location.href = '/homepage'; // Make sure the homepage route is correctly defined in app.py
});

// Admin login logic would be similar
