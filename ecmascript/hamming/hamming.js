class Hamming {
  constructor() {

  }

  compute (strand1, strand2) {
    if(strand1.length !== strand2.length) throw(new Error('DNA strands must be of equal length.'));

    return strand1.split('').reduce((counter, acid, i) => {
      return counter += ( acid !== strand2[i] ? 1 : 0 )
    }, 0);
  }
}

export default Hamming;

// export default class Hamming {
//   compute(a, b) {
//     if(a.length !== b.length) throw new Error('DNA strands must be of equal length.');

//     for(let e of String(a).entries()) {
//       console.log(e)
//     }

//     // return a.split('').reduce((memo, _, idx) => {
//     //   return (a[idx] === b[idx] ? memo : ++memo);
//     // }, 0)
//   }
// };
