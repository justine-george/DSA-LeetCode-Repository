/**
 * @return {Function}
 */
// var createHelloWorld = () => (...args) => "Hello World";

var createHelloWorld = function () {
    return function (...args) {
        return "Hello World"
    }
}

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */