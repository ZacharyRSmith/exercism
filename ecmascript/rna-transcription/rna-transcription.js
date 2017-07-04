'use strict';

function transcribe({ nucleotide, complements }) {
    if(!complements[nucleotide]) throw new Error(`Invalid nucleotide "${nucleotide}" given!`);
    return complements[nucleotide];
}

class DnaTranscriber {

    constructor () {
        this.complements = DnaTranscriber.complements;
    }

    toRna (dnaStrand) {
        const { complements } = this;

        return [...dnaStrand].reduce((val, nucleotide) => {
            return val + transcribe({ nucleotide, complements });
        }, '');
    }
}

DnaTranscriber.complements = {
    'A': 'U',
    'T': 'A',
    'C': 'G',
    'G': 'C'
};

export default DnaTranscriber;
