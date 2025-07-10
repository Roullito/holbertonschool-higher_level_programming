#!/usr/bin/node

process.argv;

if (process.argv.length - 2 === 0) {
    console.log('No argument');
} else { (process.argv.length - 2 >= 1)
    console.log('Argument found');
}
