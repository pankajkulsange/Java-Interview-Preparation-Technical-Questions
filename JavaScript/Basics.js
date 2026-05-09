let str = "hello";
let rev = "";

for (let i = str.length - 1; i >= 0; i--) {
  rev += str.charAt(i);
}
console.log("Original String: " + str);
console.log("Reversed String: " + rev);

// using build in array methods
let reversed = str.split("").reverse().join("");
console.log("Original String: " + str);
console.log("Reversed String: " + reversed);
