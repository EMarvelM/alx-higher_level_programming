#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.filter((l) => l === searchElement).length;
};
