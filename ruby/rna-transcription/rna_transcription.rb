class Complement
  DNA_COMPLEMENTS = {
    'G' => 'C',
    'C' => 'G',
    'T' => 'A',
    'A' => 'U'
  }
  RNA_COMPLEMENTS = {
    'G' => 'C',
    'C' => 'G',
    'U' => 'A',
    'A' => 'T'
  }

  def self.of_dna(strand)
    strand.chars.map do |base|
      if not DNA_COMPLEMENTS[base]
        raise ArgumentError.new("#{base} is not a valid DNA base")
      end
      DNA_COMPLEMENTS[base]
    end.join('')
  end

  def self.of_rna(strand)
    strand.chars.map do |base|
      if not RNA_COMPLEMENTS[base]
        raise ArgumentError.new("#{base} is not a valid DNA base")
      end
      RNA_COMPLEMENTS[base]
    end.join('')
  end
end
