#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function incr () {
  myObject.value = myObject.value + 1;
  return (myObject);
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
