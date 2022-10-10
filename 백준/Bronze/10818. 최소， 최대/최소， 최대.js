const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
let num = input[1].split(' ');
let max = Number(num[0]);
let min = Number(num[0]);

for(let i = 1; i < num.length; i++){
    const cur = Number(num[i])
   if(max < cur)
    max = cur;
    if(min > cur)
    min = cur;
}

console.log(min, max)
