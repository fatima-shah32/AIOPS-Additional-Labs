function showMessage() {
    const messageDiv = document.getElementById('message');
    messageDiv.innerHTML = 'Hello! Your CI/CD pipeline is working!';
    messageDiv.className = 'success';
}

function addNumbers(a, b) {
    return a + b;
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = { addNumbers };
}
