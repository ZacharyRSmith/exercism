// function transform (old) {
//   return Object.keys(old).reduce(function (rslt, score) {
//     old[score].forEach(function (ltr) {
//       rslt[ltr.toLowerCase()] = +score;
//     });

//     return rslt;
//   }, {});
// }

function transform (old) {
  var rslt = {};

  for (var score in old) {
    old[score].forEach(function (ltr) {
      rslt[ltr.toLowerCase()] = +score;
    });
  }

  return rslt;
}

module.exports = transform;
