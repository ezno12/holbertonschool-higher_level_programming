#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');
const url = args[0];
const rDict = {};
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    for (const i in json) {
      const entry = json[i];
      const completed = entry.completed;
      const userID = entry.userId;
      if (completed === true) {
        if (userID in rDict) {
          rDict[userID] += 1;
        } else {
          rDict[userID] = 1;
        }
      }
    }
  }
  console.log(rDict);
});
