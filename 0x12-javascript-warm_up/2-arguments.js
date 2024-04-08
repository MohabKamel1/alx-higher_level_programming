#!/usr/bin/node

// Get the number of arguments passed (excluding the default two arguments)
const numArguments = process.argv.length - 2;

// Check the number of arguments and print the corresponding message
if (numArguments === 0) {
  console.log("No argument");
} else if (numArguments === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}

