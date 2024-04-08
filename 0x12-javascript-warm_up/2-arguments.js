#!/usr/bin/node

// Get the number of arguments passed (excluding the default two arguments)
const numArguments = process.argv.length - 2;

// Check the number of arguments and print the corresponding message
if (numArguments === 2) {
  console.log("No argument");
} else if (numArguments === 3) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}

