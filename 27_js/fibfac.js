// Cappuccino :: Daniel Sooknanan, Tami Takada
// SoftDev pd1
// K27 -- Basic functions in JavaScript
// 2022-02-04
// --------------------------------------------------

function fact(n) {
    if (n == 1) {
        return 1;
    }

    return n * fact(n - 1);
}

function fib(n) {
    if (n <= 1) {
        return n;
    }

    return fib(n-1) + fib(n-2);
}

var fact_num = document.getElementById('fact-num');
var fact_result = document.getElementById('fact-result');

fact_num.addEventListener('change', function(event) {
    fact_result.innerHTML = fact(
        fact_num.value
    );
});