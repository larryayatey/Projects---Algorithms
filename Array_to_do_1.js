// Question 1
let arr = [1, 2, 3];
arr.unshift(5);
console.log(arr);

// Question 2
let arr2 = [6, 5, 4, 3, 2];
let script = arr2.indexOf(2); 
if (script !== -1) {
    arr2.splice(script, 1); 
}
console.log(arr2);

// Question 3
let arr3 = [1, 2, 3, 4];
let index = 3; 
let value = 5; 

arr3.splice(index, 0, value);

console.log(arr3); 
