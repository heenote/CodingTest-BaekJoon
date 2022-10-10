const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

let max = Number(input[0])
let index = 0
for(let i = 1; i < input.length; i++){
    const cur = Number(input[i])
    if(max < cur){
      max = cur
      index = i
    }
}

console.log(max, index+1 )