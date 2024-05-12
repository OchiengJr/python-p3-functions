/**
 * Greets a programmer with a default message.
 * @returns {string} The greeting message.
 */
function greetProgrammer() {
  return "Hello, programmer!";
}

/**
 * Greets a person by their name.
 * @param {string} name - The name of the person to greet.
 * @returns {string} The greeting message.
 */
function greet(name) {
  return `Hello, ${name}!`;
}

/**
 * Greets a person by their name or defaults to "programmer" if no name is provided.
 * @param {string} [name="programmer"] - The name of the person to greet.
 * @returns {string} The greeting message.
 */
function greetWithDefault(name = "programmer") {
  return `Hello, ${name}!`;
}

/**
 * Adds two numbers.
 * @param {number} num1 - The first number.
 * @param {number} num2 - The second number.
 * @returns {number} The sum of the two numbers.
 */
function add(num1, num2) {
  return num1 + num2;
}

/**
 * Halves a number.
 * @param {number} number - The number to halve.
 * @returns {number|null} The halved number, or null if the argument is not a number.
 */
function halve(number) {
  if (typeof number !== "number") return null;

  return number / 2;
}
