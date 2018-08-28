#!/usr/bin/node
/*
prints statements about c, python, and javascript */
const num = process.argv[2];
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
