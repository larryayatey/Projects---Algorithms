// Problem 1 
// function remove_spaces(space){
//     let result = space.replace(/\s/g, '');
//     return result;
// }

// let space = "Come find me";
// let result = remove_spaces(space);
// console.log(result);


// Problem 2
// function numbers_only(number){
//     let only_nums = number.replace(/\D/g, '');
//     let only_string = parseInt(only_nums, 10);
//     return only_string;
// }

// let number = "asdfg867asdf543";
// let result = numbers_only(number);
// console.log(result);


// Problem 3
// function acronym(uppercase) {
//     let words = uppercase.split(/\s+/); 

//     let acronym = "";

//     for (let i = 0; i < words.length; i++) {
//         if (words[i]) { 
//             acronym += words[i][0].toUpperCase(); 
//         }
//     }

//     return acronym;
// }

// let uppercase = "how did i get here";
// let result = acronym(uppercase);
// console.log(result); 

// Problem 4
// function countspaces(spaces) {
//     let count = 0;

//     for (let i = 0; i < spaces.length; i++) {
//         if (spaces[i] !== ' ') {
//             count++;
//         }
//     }

//     return count;
// }

// let spaces = "can you see the stars from where you are";
// let result = countspaces(spaces);
// console.log(result); 

// Problem 5 
// function removeshorterstrings(arr, shorter) {
//     let removeshorter = arr.filter(strings => strings.length >= shorter);
//     return removeshorter;
// }

// let strings = ["watermelon", "mango", "grapes", "guava", "lime"];
// let shorter = 6;
// let result = removeshorterstrings(strings, shorter);
// console.log(result); 