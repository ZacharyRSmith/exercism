module.exports = words;

function addCount (elt, obj) {
  if (isNaN(obj[elt])) { obj[elt] = 1; }
  else { obj[elt] += 1; }

  return obj;
}

function words (str) {
  var words = str.trim().split(/\s+/);
  var wordCounts = {};

  words.forEach(function (word) {
    wordCounts = addCount(word, wordCounts);
  });

  return wordCounts;
}

// Note: I added this test:
//   it("does not count whitespace between words", function() {
//     var expectedCounts = { Introductory: 1, Course: 1 };
//     expect(words("\t\tIntroductory\nCourse      ")).toEqual(expectedCounts);
//   });
