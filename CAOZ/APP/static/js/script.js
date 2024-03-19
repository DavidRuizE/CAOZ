document.addEventListener('DOMContentLoaded', function() {
    const quantityInput = document.getElementById('quantity');
    const incrementButton = document.getElementById('increment');
    const decrementButton = document.getElementById('decrement');

    incrementButton.addEventListener('click', function() {
        quantityInput.stepUp();
    });

    decrementButton.addEventListener('click', function() {
        quantityInput.stepDown();
    });
});

