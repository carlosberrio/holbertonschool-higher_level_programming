#!/usr/bin/node

if (isNaN(process.argv[2])) {
    console.log('Not a number');
  } else {
    console.log('My number:', parseInt(process.argv[2]));
  }
