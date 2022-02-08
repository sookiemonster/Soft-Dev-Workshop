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

function gcd(a, b) {
    if (a == 0 || b == 0) {
        return 0;
    }
    else if (a == b) {
        return a;
    }
    else if (a < b) {
        return gcd_helper(a, b);
    }
    else {
        return gcd_helper(b, a);
    }
}

function gcd_helper(low, high) {
    result = 0;
    for (let i = 0; i <= low; i++) {
        if (low % i == 0 && high % i == 0) {
            result = i;
        }
    }
    return result;
}

// Shenanigans with Event Listeners

var fact_num = document.getElementById('fact-num');
var fact_result = document.getElementById('fact-result');

fact_num.addEventListener('change', function(event) {
    fact_result.innerHTML = fact(
        fact_num.value
    );
});

var fib_num = document.getElementById('fib-num');
var fib_result = document.getElementById('fib-result');

fib_num.addEventListener('change', function(event) {
    fib_result.innerHTML = fib(
        fib_num.value
    );
});

var gcd_nums = document.querySelectorAll('.gcd-num');
var gcd_result = document.getElementById('gcd-result');

for (let i = 0; i < gcd_nums.length; i++) {
    gcd_nums[i].addEventListener('change', function(event) {
        gcd_result.innerHTML = gcd(
            gcd_nums[0].value, gcd_nums[1].value
        )
    });
}