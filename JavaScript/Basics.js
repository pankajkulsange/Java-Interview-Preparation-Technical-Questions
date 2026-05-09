let str = "hello";
let rev = "";

for (let i = str.length - 1; i >= 0; i--) {
  rev += str.charAt(i);
}
console.log("Original String: " + str);
console.log("Reversed String: " + rev);
