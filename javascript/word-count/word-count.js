module.exports = words;

function words (str) {
  var words = str.match(/\S+/g);
  var wordCounts = {};

  words.forEach(function (word) {
    if (wordCounts.hasOwnProperty(word)) {
      wordCounts[word] += 1;
    } else {
      wordCounts[word] = 1;
    }
  });

  return wordCounts;
}

// Note: I added this test:
//   it("does not count whitespace between words", function() {
//     var expectedCounts = { Introductory: 1, Course: 1 };
//     expect(words("\t\tIntroductory\nCourse      ")).toEqual(expectedCounts);
//   });
