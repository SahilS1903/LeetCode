function checkPowersOfThree(n) {
    while (n > 0) {
        if (n % 3 === 0) {
            n /= 3;
        } else if (n % 3 === 1) {
            n -= 1;
        } else {
            return false;
        }
    }
    return true;
}