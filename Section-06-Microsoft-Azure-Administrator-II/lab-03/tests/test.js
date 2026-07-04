function addNumbers(a, b) {
    return a + b;
}

function runTests() {
    console.log("Running tests...");

    if (addNumbers(2, 3) !== 5) {
        console.log("Test failed: addNumbers(2, 3)");
        process.exit(1);
    }

    if (addNumbers(-1, 1) !== 0) {
        console.log("Test failed: addNumbers(-1, 1)");
        process.exit(1);
    }

    console.log("All tests passed successfully!");
}

runTests();
